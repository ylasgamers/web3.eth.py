from web3 import Web3, HTTPProvider
import time
import datetime 
import threading
import json
import logging
import asyncio
import requests
import time
import os
import sys
import ctypes
import pyperclip as pc

#bsc = "https://bsc-testnet.publicnode.com" #rpc bsctesnet custom #you can find rpc on chainlist.org
inputrpc = str(input("Input Url RPC/Node Blockchain Network : "))
web3 = Web3(Web3.HTTPProvider(inputrpc))
#chain_id = 97 #you can find chainid on chainlist.org
chainId = int(input("Input Chain ID Blockchain Network : "))

ctypes.windll.kernel32.SetConsoleTitleW("Send AIO Blockchain Network")
print('')
print('Send AIO Blockchain Network To Other Address With Custom Message')
print('This Support Tesnet & Mainnet Ethereum, Binance Smart Chain, Polygon')
print('Polygon zkEVM, Arbitrum, Optimism, Avalanche, zkSync Era, & Base')
print('')

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

walletSender = web3.toChecksumAddress(input("Enter Your Address Sender 0x...: "))
#walletSender = '0x0' #sender
walletSenderKey = input("Enter Your Privatekey Sender abcde12345...: ")
#walletSenderKey = 'abcde12345' #privatekey sender
walletRecipient = web3.toChecksumAddress(input("Enter Your Address Recipient 0x...: "))
InputMessage = str(input("Enter Your Custom Message To Recipient : "))
Message = bytes(InputMessage, 'utf-8')#web3.to_bytes(text=InputMessage)
#walletRecipient = '0x0' #recipient 
#gasAmount = 21000 #gas limit
#gasPrice = 1 #gas price

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(walletSender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    
UpdateBalance()

amountToSendBNB = web3.toWei(float(input("Enter Amount Of You Want To Send : ")), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(walletSender)

#estimate gas limit
gasAmount = web3.eth.estimate_gas({
    'chainId': chainId,
    'nonce': nonce,
    'to': walletRecipient,
    'value': amountToSendBNB,
    'data': web3.toHex(Message)
    })
    
#calculate transaction fee
print('')
amountFromWei = web3.fromWei(amountToSendBNB, 'ether')
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')
print('Processing Send :' ,amountFromWei, 'ETH/BNB/MATIC/OTHER To Recepient :', walletRecipient)

#build a transaction in a dictionary
tx = {
    'chainId': chainId,
    'nonce': nonce,
    'to': walletRecipient,
    'value': amountToSendBNB, #web3.toWei(float(amountToSendBNB), 'ether'),
    'data': web3.toHex(Message),
    'gas': gasAmount,
    'gasPrice': web3.eth.gas_price #web3.toWei(gasPrice, 'gwei')
    }

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, walletSenderKey)
#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
txid = str(web3.toHex(tx_hash))
print('')
print('Transaction Success TX-ID Copied To Clipboard')
print(txid)
pc.copy(txid)
print('Update Current Balance In 30 Second...')
time.sleep(30)
print('')
UpdateBalance() #get latest balance
print('Will Close Automatically In 30 Second...')
time.sleep(30)