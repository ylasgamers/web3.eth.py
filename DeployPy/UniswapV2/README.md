- You Need Deploy UniswapV2Factory First
- After Deploy UniswapV2Factory, You Need INIT_CODE_PAIR_HASH To Put On UniswapV2Router02
- You Can Use INIT_CODE_PAIR_HASH.py To Get INIT_CODE_PAIR_HASH
```
Here You Need Find This Function On UniswapV2Router02.sol :
function pairFor(address factory, address tokenA, address tokenB) internal pure returns (address pair) {
    (address token0, address token1) = sortTokens(tokenA, tokenB);
    pair = address(uint(keccak256(abi.encodePacked(
            hex'ff',
            factory,
            keccak256(abi.encodePacked(token0, token1)),
            hex'96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f' // you need change this without 0x
    ))));
}
```
- After Change INIT_CODE_PAIR_HASH, You Can Deploy UniswapV2Router02
