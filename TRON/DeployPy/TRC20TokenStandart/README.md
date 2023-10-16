- You Need Edit Name, Symbol, Total Supply On TRC20TOKEN.sol
```
    string constant public name = "FORATEST"; //add name here
    string constant public symbol = "FOTEST"; //add symbol here
    uint8 constant public decimals = 18;
    uint256 private _totalSupply;

    constructor() payable {
        _totalSupply = 1000000 * 1**18; //add totalSupply here
        _balances[owner()] = _balances[owner()].add(_totalSupply);
        emit Transfer(address(0), owner(), _totalSupply);
    }
```
