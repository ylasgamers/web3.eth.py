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

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'BNB')

UpdateBalance()

inputamount1 = float(input("Enter Amount Of You Want Send To Recipient : "))
inputamount = web3.toWei(float(inputamount1), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

def RepeatMint():

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

#10x
def Repeat10x():
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)
    RepeatMint()
    time.sleep(2)

#10x10=100    
Repeat10x()
Repeat10x()
Repeat10x()
Repeat10x()
Repeat10x()
Repeat10x()
Repeat10x()
Repeat10x()
Repeat10x()
Repeat10x()