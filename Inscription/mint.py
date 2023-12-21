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
import config

web3 = Web3(Web3.HTTPProvider(config.rpcurl))
chainId = int(config.chain_id)

print('')
print('Mint AIO Inscription Blockchain Network')
print('This Support Mainnet Ethereum, Binance Smart Chain, Polygon')
print('Polygon zkEVM, Arbitrum, Optimism, Avalanche, Base, Other Chain Like Ethereum')
print('')

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

walletSender = web3.toChecksumAddress(config.youraddress)
walletSenderKey = config.pvkey
walletRecipient = web3.toChecksumAddress(config.youraddress)

InputMessage = str(config.code_mint)
Message = bytes(InputMessage, 'utf-8')
#gasPrice = 3 #enable this if you use manual/custom gas price
#gasLimit = 23000 #enable this if you use manual/custom gas limit

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(walletSender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    
UpdateBalance()

amountToSendBNB = web3.toWei(float(str("0")), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

#estimate gas limit
def CallMint():
    #disabled this if you want using custom/manual gas limit
    gasAmount = web3.eth.estimate_gas({ #estimate auto gas limit
        'chainId': chainId,
        'nonce': web3.eth.getTransactionCount(walletSender),
        'to': walletRecipient,
        'value': amountToSendBNB,
        'data': web3.toHex(Message)
        })

    #build a transaction in a dictionary
    tx = {
        'chainId': chainId,
        'nonce': web3.eth.getTransactionCount(walletSender),
        'to': walletRecipient,
        'value': amountToSendBNB,
        'data': web3.toHex(Message),
        'gas': gasAmount, #automatic gas limit
        'gasPrice': web3.eth.gas_price #use this if gas price auto
        #'gasPrice': web3.toWei(gasPrice, 'gwei') #use this if gas price manual
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
    time.sleep(5)

#looping
num = config.totalmint
for _ in range(num):
    CallMint()