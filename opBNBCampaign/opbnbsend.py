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

print('Auto Send opBNB Testnet 100x To Other Address')
sender = web3.toChecksumAddress(input("Enter Your Address Sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey Sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
recipient = web3.toChecksumAddress(input("Enter Your Address Recipient 0x...: "))
contract_nft = web3.toChecksumAddress("0x5aee67f8dc2d9a5537d4b64057b52da31d37516b")
gasAmount = 21000 #gas limit // change if transaction fail
gasPrice = 1 #gas price
numDetected = 0

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'BNB')
    print('Total Transaction :', str(numDetected))

UpdateBalance()

inputamount1 = float(input("Enter Amount Of You Want Send To Recipient : "))
inputamount = web3.toWei(float(inputamount1), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

def RepeatMint():
    try:
        token_tx = {
            'chainId': chainId,
            'nonce': web3.eth.getTransactionCount(sender),
            'to': recipient,
            'value': inputamount,
            'gas': gasAmount,
            'gasPrice': web3.toWei(gasPrice,'gwei')
        }
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
        
def listenForFinalized():
    #event_filter = contracttoken.events.Transfer.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                #finalizedLoop(event_filter, 0)))
                RepeatMint()))
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
