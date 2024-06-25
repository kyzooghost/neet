// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/proxy/Clones.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC20Vault
// Weigh voting power based on balance / totalSupply
// Delegate voting power
interface IVotes is IERC20 { 
    /** * @dev Delegates all voting power from the msg.sender to `delegatee`. */ 
    function delegate(address delegatee) external;
}

// Lesson 1 - delegatecall can never change the state of the 2nd contract
    // EOA -> C1 -delegatecall -> C2 -call -> C3
    // msg.sender is EOA in C1 and C2
    // msg.sender is C1 in C3
    // Can essentially remove C2 from the chain for state/context purposes - EOA -> C1 -call -> C3

// Lesson 2 - Don't shadow the 'delegate' call - you will just confuse yourself

// Lesson 3 - Someone else transfer tokens directly to either contract -> have ERC20 recovery functions, that cannot 

// Lesson 4 - Completely missed using Minimal Clones - Urgh delegatecall hole cost me

// Lesson 5 - Completely missed using Owner library

// Just sad with this question
    // 1. Boolean error with require(user_wallet == address(0))
    // 2. Delegate call hole
    // 3. Didn't want to go in ContractFactory direction, because gas cost of contract deployment. But this is not an issue with Minimal Proxy Standard
    // 4. Just lots of small issues pointed out on screen zzzzzzz

    // Tbh there are two weird restrictions here i.) The contract is already deployed, ii.) I wouldn't think of seeing this sort of delegate function in the wild, I would expect partial delegations to be supported by the already deployed contract.
    // It is hard to practice Solidity interview Qs like this - there's no standard resource for it. I have implemented this pattern before, but it's not something if I haven't touched it for ages.abi
    // Really didn't think OZ contracts would be in the scope of the Q, thought it would be more Solidity without libraries.

contract CounterFactory { 
    IVotes immutable voteToken;
    address immutable counterImplementation;
    mapping(address => address) user_to_wallet;
    mapping(address => uint256) user_balance;

    constructor(address _voteToken, address _counterImplementation) { 
        voteToken = IVotes(_voteToken); 
        counterImplementation = _counterImplementation;
    }
    
    /// @dev Approval for CounterFactory as spender 
    function partialDelegate(address delegatee, uint256 amountToDelegate) external { 
        address user_wallet = user_to_wallet[msg.sender]; 
        if (user_wallet == address(0)) {
            address new_wallet_address = Clones.clone(counterImplementation);
            user_to_wallet[msg.sender] = new_wallet_address; 
            user_wallet = new_wallet_address; 
        } 
        user_balance[msg.sender] += amountToDelegate; 
        voteToken.transferFrom(msg.sender, user_wallet, amountToDelegate); 
        Counter(user_wallet).fullDelegate(delegatee);
        // Emit event 
    }

    function withdraw(uint256 amountToWithdraw) external { 
        address user_wallet = user_to_wallet[msg.sender]; 
        require(user_wallet != address(0)); 
        uint256 cur_balance = user_balance[msg.sender]; 
        require(amountToWithdraw <= cur_balance); 
        user_balance[msg.sender] -= amountToWithdraw; 
        voteToken.transferFrom(user_wallet, msg.sender, amountToWithdraw); 
        // Emit event 
    }
}

// What if user transfers token outside of delegate function? Well we then need a recovery function that cannot cause valid withdraws to fail
contract Counter is Ownable { 
    IVotes immutable voteToken; 
    
    constructor(address _voteToken) Ownable(msg.sender) { 
        voteToken = IVotes(_voteToken); 
        voteToken.approve(msg.sender, type(uint256).max); 
    }
    
    function fullDelegate(address delegatee) external onlyOwner { 
        voteToken.delegate(delegatee); // Emit event 
    }
}