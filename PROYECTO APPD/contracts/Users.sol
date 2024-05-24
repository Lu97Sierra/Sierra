// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Users is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _userIds;

    struct User {
        uint256 userId;
        string email;
        bytes32 passwordHash;
    }

    mapping(uint256 => User) public users;

    function createUser(string memory email, string memory password) public onlyOwner returns (uint256) {
        _userIds.increment();
        uint256 newUserId = _userIds.current();
        bytes32 passwordHash = keccak256(abi.encodePacked(password));
        User memory newUser = User(newUserId, email, passwordHash);
        users[newUserId] = newUser;
        return newUserId;
    }

    function modPassword(uint256 userId, string memory newPassword) public onlyOwner {
        require(userId <= _userIds.current() && userId > 0, "User does not exist");
        users[userId].passwordHash = keccak256(abi.encodePacked(newPassword));
    }

    function getUsers() public view returns (User[] memory) {
        User[] memory usersArray = new User[](_userIds.current());
        for (uint256 i = 1; i <= _userIds.current(); i++) {
            usersArray[i - 1] = users[i];
        }
        return usersArray;
    }
}