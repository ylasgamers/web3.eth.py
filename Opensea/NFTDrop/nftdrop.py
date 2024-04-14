from web3 import Web3, HTTPProvider
import json
import time
import config

web3 = Web3(Web3.HTTPProvider(config.rpcurl))
chainId = int(config.chainid)

print("Auto Mint NFT Drop Opensea Public")

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

# sender = config.sender
# senderkey = config.pvkey
nftaddr = config.nftaddr
feerecipient = config.feerecipient
nftdropaddr = config.nftdropaddr
#============================================================================
contractnft = web3.eth.contract(address=nftaddr, abi=config.nft_abi)
contractnftdrop = web3.eth.contract(address=nftdropaddr, abi=config.nftdrop_abi)
nftName = contractnft.functions.name().call()
nftSymbol = contractnft.functions.symbol().call()

def MultiMintPublic(sender, senderkey, totalmint):
    #estimate gas limit contract
    gas_tx = contractnftdrop.functions.mintPublic(nftaddr, feerecipient, config.nulladdr, totalmint).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'value': web3.toWei(float(0), 'ether'),
        'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.getTransactionCount(sender)
    })
    gasAmount = web3.eth.estimate_gas(gas_tx)
    #print(gasAmount)

    #calculate transaction fee
    print('')
    gasPrice = web3.fromWei(web3.eth.gasPrice, 'gwei')
    Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH')
    print('Processing Mint :' ,totalmint, nftName, 'NFT')

    token_tx = contractnftdrop.functions.mintPublic(nftaddr, feerecipient, config.nulladdr, totalmint).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'value': web3.toWei(float(0), 'ether'),
        'gas': gasAmount,
        'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.getTransactionCount(sender)
    })

    #sign the transaction
    sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
    #send transaction
    tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    #get transaction hash
    txid = str(web3.toHex(tx_hash))
    print('')
    print('Transaction Success TX-ID Result...')
    print(txid)

#set your address & privatekey & total mint
totalmint = int(1)   
MultiMintPublic(web3.toChecksumAddress("0xyour_addr1"), "yourpvkey1", totalmint)
MultiMintPublic(web3.toChecksumAddress("0xyour_addr2"), "yourpvkey2", totalmint)