// SPDX-License-Identifier: None
pragma solidity =0.8.26;

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

interface IHyper {
    function mine(bytes calldata extraData) external;
}

interface IBlast {
    function configureClaimableGas() external;
    function configureGovernor(address governor) external;
    function claimMaxGas(address contractAddress, address recipient) external returns (uint256);
    function claimAllGas(address contractAddress, address recipient) external returns (uint256);
}

contract Miner {
    address private _owner;
    IBlast private constant BLAST = IBlast(0x4300000000000000000000000000000000000002);
    constructor(){
        _owner = msg.sender;
        BLAST.configureClaimableGas();
        BLAST.configureGovernor(address(this));
    }
    function MinerCustom(uint custom) external {
        require(msg.sender == _owner, "Caller is not the owner");
        for (uint256 i = 0; i < custom; i++) {
        IHyper(0x7E82481423B09c78e4fd65D9C1473a36E5aEd405).mine("");
    }}
    function withdrawToken(address token, address recipient) external {
        require(msg.sender == _owner, "Caller is not the owner");
        uint amount = IERC20(token).balanceOf(address(this));
        IERC20(token).transfer(recipient, amount);
    }
    function claimGas(bool isAll, bool isMax) external {
        require(msg.sender == _owner, "Caller is not the owner");
        if(isAll){
            BLAST.claimAllGas(address(this), address(this));
        }
        if(isMax){
            BLAST.claimMaxGas(address(this), address(this));
        }
        payable(msg.sender).transfer(address(this).balance);
    }
    function transferOwnership(address newOwner) external {
        require(msg.sender == _owner, "Caller is not the owner");
        _owner = newOwner;
    }
    fallback() external payable {}
	receive() external payable {}
}
