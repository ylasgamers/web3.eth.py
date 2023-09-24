- [PancakeSwap Contract V3](https://docs.pancakeswap.finance/developers/smart-contracts/pancakeswap-exchange/v3-contracts)
- Swap Buy/Sell
- Create & Initialize Pool Pair [ create_instalpoolv3.py for token/wbnb pool/pair ] [ create_instalpoolv3x.py for wbnb/token pool/pair ]
- Add/Remove Liquidity [ addliquidityv3.py for token/wbnb pool/pair ] [ addliquidityv3x.py for wbnb/token pool/pair ]

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

- Calculating Price Pool/Pair WBNB/Token
```
Calculate price per 1 wbnb formula = sqrtPriceX96^2 / 2^192 * 10^token0_decimal / 10^token1_decimal
Ex token0 = wbnb //decimal 18
Ex token1 = your_token // decimal 18
Ex sqrtPriceX96 = 10000000000000000000000000000000
10000000000000000000000000000000^2 / 2^192 * 10^18 / 10^18 = 15930.9191113
1 bnb will be 15930.9191113 your_token
your will be mint liquidity 15930.9191113 your_token & 1 bnb
```
