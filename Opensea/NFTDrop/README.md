# Mint NFTDrop On Opensea
- Only Public NFTDrop
- You Can Mint Multiple Address/Wallet
- You Need Changed Url RPC, ChainID, NFT Address, Fee Recipient Address, & NFTDrop Contract Address On config.py
- You Need Edit Address/Wallet, Privatekey, & Total Mint
```
#set your address & privatekey & total mint , this example 2 address/wallet
#if you want more you can add more, or you can remove if you want mint not a lot
totalmint = int(1)  
MultiMintPublic(web3.toChecksumAddress("0xyour_addr1"), "yourpvkey1", totalmint)
MultiMintPublic(web3.toChecksumAddress("0xyour_addr2"), "yourpvkey2", totalmint)
```
