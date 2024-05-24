// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Librarys is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _LibraryIds;

    struct Library {
        uint256 LibraryId;
        string name;
        uint256[] mangas;
    }

    mapping(uint256 => Library) public librarys;

    function createLibrary(string memory name, uint256[] memory mangas) public onlyOwner returns (uint256) {
        _LibraryIds.increment();
        uint256 newLibraryId = _LibraryIds.current();
        Library memory newLibrary = Library(newLibraryId, name, mangas);
        librarys[newLibraryId] = newLibrary;
        return newLibraryId;
    }

    function modName(uint256 LibraryId, string memory newName) public onlyOwner {
        require(LibraryId <= _LibraryIds.current(), "Library no existe");
        librarys[LibraryId].name = newName;
    }

    function getLibrarys() public view returns (Library[] memory) {
        Library[] memory librarysArray = new Library[](_LibraryIds.current());
        for (uint256 i = 1; i <= _LibraryIds.current(); i++) {
            librarysArray[i - 1] = librarys[i];
        }
        return librarysArray;
    }
}