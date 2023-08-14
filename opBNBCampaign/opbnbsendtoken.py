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

print('Auto Send Token opBNB Testnet 100x To Other Address')
sender = web3.toChecksumAddress(input("Enter Your Address Sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey Sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
recipient = web3.toChecksumAddress(input("Enter Your Address Recipient 0x...: "))
contract_token = web3.toChecksumAddress(input("Enter Token Address 0x...: ")) #btcb
#gasAmount = 50000 #gas limit // change if transaction fail
gasPrice = 1 #gas price

tokenabi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
contracttoken = web3.eth.contract(address=contract_token, abi=tokenabi)
tokenSymbol = contracttoken.functions.symbol().call()

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'BNB')
    balancetoken = contracttoken.functions.balanceOf(sender).call()
    balance_btcb = web3.fromWei(balancetoken,'ether')
    print('Your Token : ' ,balance_btcb, tokenSymbol)
UpdateBalance()

inputamount1 = float(input("Enter Amount Of Token You Want Send To Recipient : "))
inputamount = web3.toWei(float(inputamount1), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

def RepeatMint():
    #estimate gas limit contract
    gas_tx = contracttoken.functions.transfer(recipient, inputamount).buildTransaction({
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
    #print('Transaction Fee :' ,Caclfee, 'tcBNB')

    token_tx = contracttoken.functions.transfer(recipient, inputamount).buildTransaction({
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

#10x
def Repeat10x():
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)
    RepeatMint()
    time.sleep(1)

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