- [Uniswap Contract V3](https://docs.uniswap.org/contracts/v3/reference/deployments)
- Swap Buy/Sell
- Create & Initialize Pool Pair
- Add/Remove Liquidity
- Calculating Price Pool/Pair Token/WETH
```
Calculate price per 1 token formula = sqrtPriceX96^2 / 2^192 * 10^token0_decimal / 10^token1_decimal
Ex token0 = your_token //decimal 18
Ex token1 = weth // decimal 18
Ex sqrtPriceX96 = 1000000000000000000000000000
1000000000000000000000000000^2 / 2^192 * 10^18 / 10^18 = 0.00015930919
1 your_token will be 0.00015930919 eth
your will be mint liquidity 1 your_token & 0.00015930919 eth
```
