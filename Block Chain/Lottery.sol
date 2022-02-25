// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Lottery
{

    address public manager;
    address payable[] private players;

    // Assign the Manager the one who Deployed the contract
    constructor(){
        manager = msg.sender;
    }

// check if there Exists the player in the array
    function isPresent() view private returns(bool){
        for(uint i=0;i<players.length;i++){
            if(players[i] == msg.sender) return true;
        }
        return false;
    }
// returns a random number : to check the Winner
    function rand() view private returns(uint){
        return uint(sha256(abi.encodePacked(block.difficulty,block.number,players)));
    }

    function enter()payable public{
        require(msg.sender != manager,"Manager Cannot Enter");
        require(isPresent() == false,"Player Already Entered");
        require(msg.value >=1 ether,"Minimum of 1 Ether is to be paid" );
        players.push(payable(msg.sender));
    }

    function pickPlayer() public  returns(address){
        require(manager == msg.sender,"Only Manager Can Pick the Winner");
        uint winnerIndex = rand() % players.length;
        address contractAddress = address(this);
        address winner = players[winnerIndex];
        players[winnerIndex].transfer(contractAddress.balance);
        players = new address payable[](0); // reset the Lottery

        return winner;
    }

}
/* 

Players
 1. One player can Enter Only Once
 2. Winner gets Ether of all the Entered Users
 3. Randomly Selection of Winner is to be done

Manager 
 1. Manager cannot enter the Lottery
 2. Manager can only announce the winner
 3. Manager will reset the Lottery Once the Lottery Winner is Picked


 */
