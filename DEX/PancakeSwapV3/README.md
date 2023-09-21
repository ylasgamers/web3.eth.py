- [PancakeSwap Contract V3](https://docs.pancakeswap.finance/developers/smart-contracts/pancakeswap-exchange/v3-contracts)
- Swap Buy/Sell
- Create & Initialize Pool Pair
- Add/Remove Liquidity

- Calculating Price Pool/Pair Token/WBNB
```
Calculate price per 1 token formula = sqrtPriceX96^2 / 2^192 * 10^token0_decimal / 10^token1_decimal
Ex token0 = your_token //decimal 18
Ex token1 = wbnb // decimal 18
Ex sqrtPriceX96 = 1000000000000000000000000000
1000000000000000000000000000^2 / 2^192 * 10^18 / 10^18 = 0.00015930919
1 your_token will be 0.00015930919 bnb
your will be mint liquidity 1 your_token & 0.00015930919 bnb
```
