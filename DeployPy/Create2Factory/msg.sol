// SPDX-License-Identifier: MIT
pragma solidity =0.8.0;

contract MessageContract {
    string private message;

    function writeMessage(string calldata newMessage) public {
        message = newMessage;
    }

    function readMessage() public view returns (string memory) {
        return message;
    }
}
