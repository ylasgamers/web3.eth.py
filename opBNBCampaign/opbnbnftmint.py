from web3 import Web3, HTTPProvider
import json
import logging
import datetime 
import threading
import asyncio
import requests
import time
import os
import sys
import ctypes
import pyperclip as pc

bsc = "https://opbnb-testnet-rpc.bnbchain.org" #rpc bsctesnet custom
web3 = Web3(Web3.HTTPProvider(bsc))
chainId = 5611

#connecting web3
# if  web3.isConnected() == True:
    # print("Web3 Connected...\n")
# else :
    # print("Error Connecting Please Try Again...")

print('Auto Mint opBNB Genesis NFT Testnet 100x')
sender = web3.toChecksumAddress(input("Enter Your Address Sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey Sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
contract_nft = web3.toChecksumAddress("0x5aee67f8dc2d9a5537d4b64057b52da31d37516b")
#gasAmount = 50000 #gas limit // change if transaction fail
gasPrice = 1 #gas price
numDetected = 0

nftabi = json.loads('[{"type":"constructor","inputs":[{"name":"name_","type":"string","internalType":"string"},{"name":"symbol_","type":"string","internalType":"string"}],"stateMutability":"nonpayable"},{"name":"Approval","type":"event","inputs":[{"name":"owner","type":"address","indexed":true,"internalType":"address"},{"name":"approved","type":"address","indexed":true,"internalType":"address"},{"name":"tokenId","type":"uint256","indexed":true,"internalType":"uint256"}],"anonymous":false,"signature":"0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925"},{"name":"ApprovalForAll","type":"event","inputs":[{"name":"owner","type":"address","indexed":true,"internalType":"address"},{"name":"operator","type":"address","indexed":true,"internalType":"address"},{"name":"approved","type":"bool","indexed":false,"internalType":"bool"}],"anonymous":false,"signature":"0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31"},{"name":"Transfer","type":"event","inputs":[{"name":"from","type":"address","indexed":true,"internalType":"address"},{"name":"to","type":"address","indexed":true,"internalType":"address"},{"name":"tokenId","type":"uint256","indexed":true,"internalType":"uint256"}],"anonymous":false,"signature":"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"},{"name":"approve","type":"function","inputs":[{"name":"to","type":"address","internalType":"address"},{"name":"tokenId","type":"uint256","internalType":"uint256"}],"outputs":[],"signature":"0x095ea7b3","stateMutability":"nonpayable"},{"name":"balanceOf","type":"function","inputs":[{"name":"owner","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"constant":true,"signature":"0x70a08231","stateMutability":"view"},{"name":"getApproved","type":"function","inputs":[{"name":"tokenId","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"address","internalType":"address"}],"constant":true,"signature":"0x081812fc","stateMutability":"view"},{"name":"isApprovedForAll","type":"function","inputs":[{"name":"owner","type":"address","internalType":"address"},{"name":"operator","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"constant":true,"signature":"0xe985e9c5","stateMutability":"view"},{"name":"mint","type":"function","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"signature":"0x1249c58b","stateMutability":"nonpayable"},{"name":"name","type":"function","inputs":[],"outputs":[{"name":"","type":"string","value":"opBNB Genesis NFT (testnet)","internalType":"string"}],"constant":true,"signature":"0x06fdde03","stateMutability":"view"},{"name":"ownerOf","type":"function","inputs":[{"name":"tokenId","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"address","internalType":"address"}],"constant":true,"signature":"0x6352211e","stateMutability":"view"},{"name":"safeTransferFrom","type":"function","inputs":[{"name":"from","type":"address","internalType":"address"},{"name":"to","type":"address","internalType":"address"},{"name":"tokenId","type":"uint256","internalType":"uint256"}],"outputs":[],"signature":"0x42842e0e","stateMutability":"nonpayable"},{"name":"safeTransferFrom","type":"function","inputs":[{"name":"from","type":"address","internalType":"address"},{"name":"to","type":"address","internalType":"address"},{"name":"tokenId","type":"uint256","internalType":"uint256"},{"name":"data","type":"bytes","internalType":"bytes"}],"outputs":[],"signature":"0xb88d4fde","stateMutability":"nonpayable"},{"name":"setApprovalForAll","type":"function","inputs":[{"name":"operator","type":"address","internalType":"address"},{"name":"approved","type":"bool","internalType":"bool"}],"outputs":[],"signature":"0xa22cb465","stateMutability":"nonpayable"},{"name":"supportsInterface","type":"function","inputs":[{"name":"interfaceId","type":"bytes4","internalType":"bytes4"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"constant":true,"signature":"0x01ffc9a7","stateMutability":"view"},{"name":"symbol","type":"function","inputs":[],"outputs":[{"name":"","type":"string","value":"OG","internalType":"string"}],"constant":true,"signature":"0x95d89b41","stateMutability":"view"},{"name":"tokenURI","type":"function","inputs":[{"name":"tokenId","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"string","internalType":"string"}],"constant":true,"signature":"0xc87b56dd","stateMutability":"view"},{"name":"transferFrom","type":"function","inputs":[{"name":"from","type":"address","internalType":"address"},{"name":"to","type":"address","internalType":"address"},{"name":"tokenId","type":"uint256","internalType":"uint256"}],"outputs":[],"signature":"0x23b872dd","stateMutability":"nonpayable"}]')
contractnft = web3.eth.contract(address=contract_nft, abi=nftabi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'BNB')
    balancenft = contractnft.functions.balanceOf(sender).call()
    print('Your NFT : ' ,balancenft)
    print('Total Transaction :', str(numDetected))
    
UpdateBalance()

def RepeatMint(event):
    try:
        #estimate gas limit contract
        gas_tx = contractnft.functions.mint().buildTransaction({
            'chainId': chainId,
            'from': sender,
            'gasPrice': web3.toWei(gasPrice,'gwei'),
            'nonce': web3.eth.getTransactionCount(sender)
        })
        gasAmount = web3.eth.estimateGas(gas_tx)
    
        #calculate transaction fee
        #print('')
        #gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
        #Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
        #print('Transaction Fee :' ,Caclfee, 'BNB')
    
        token_tx = contractnft.functions.mint().buildTransaction({
            'chainId': chainId,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': web3.toWei(gasPrice,'gwei'),
            'nonce': web3.eth.getTransactionCount(sender)
        })
        #sign the transaction
        sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        txid = str(web3.toHex(tx_hash))
        print(txid)
        UpdateBalance() #get latest balance
        global numDetected
        numDetected = numDetected + 1
    
    except:
        pass

async def finalizedLoop(event_filter, poll_interval):
    while True:
        try:
            for Transfer in event_filter.get_new_entries():
                RepeatMint(Transfer)
            await asyncio.sleep(poll_interval)
        except:
            pass
        
def listenForFinalized():
    event_filter = contractnft.events.Transfer.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                finalizedLoop(event_filter, 0)))       
                # log_loop(block_filter, 2),
                # log_loop(tx_filter, 2)))
                 
    finally:
        # close loop to free up system resources
        #loop.close()
        #print("loop close")
        listenForFinalized()

        #beware of valueerror code -32000 which is a glitch. make it ignore it and go bakc to listening

listenForFinalized()

input("")
