// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Mangas is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _MangaIds;

    struct Manga {
        uint256 MangaId;
        string name;
        uint256 price;
    }

    mapping(uint256 => Manga) public mangas;

    function createManga(string memory name, uint256 price) public onlyOwner returns (uint256) {
        _MangaIds.increment();
        uint256 newMangaId = _MangaIds.current();
        Manga memory newManga = Manga(newMangaId, name, price);
        mangas[newMangaId] = newManga;
        return newMangaId;
    }

    function modPrice(uint256 MangaId, uint256 newPrice) public onlyOwner {
        require(MangaId <= _MangaIds.current(), "Mangae no existe");
        mangas[MangaId].price = newPrice;
    }

    function getMangas() public view returns (Manga[] memory) {
        Manga[] memory mangasArray = new Manga[](_MangaIds.current());
        for (uint256 i = 1; i <= _MangaIds.current(); i++) {
            mangasArray[i - 1] = mangas[i];
        }
        return mangasArray;
    }
}