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
bsc = "https://bsc-testnet.publicnode.com" #rpc bsctesnet custom
web3 = Web3(Web3.HTTPProvider(bsc))

ctypes.windll.kernel32.SetConsoleTitleW("BNB Tesnet Sender")
print('send bnb to other address')

#connecting web3
if  web3.isConnected() == True:
    print("web3 connected...\n")
else :
    print("error connecting please try again...")

walletSender = web3.toChecksumAddress(input("Enter your address sender 0x...: "))
#walletSender = '0x0' #sender
walletSenderKey = input("Enter your privatekey sender abcde12345...: ")
#walletSenderKey = 'abcde12345' #privatekey sender
walletRecipient = web3.toChecksumAddress(input("Enter your address recipient 0x...: "))
#walletRecipient = '0x0' #recipient 
#gasAmount = 21000 #gas limit
#gasPrice = 1 #gas price
chainId = 97

#Get balance account
balance = web3.eth.get_balance(walletSender)
balance_bnb = web3.fromWei(balance,'ether')
print('Your Balance' ,balance_bnb, 'BNB')
amountToSendBNB = web3.toWei(float(input("Enter amount of bnb you want to send: ")), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(walletSender)

#estimate gas price
# estgasPrice = int(web3.eth.gas_price)
# gasPrice = web3.fromWei(float(estgasPrice), 'ether')

#estimate gas limit
gasAmount = web3.eth.estimate_gas({
    'chainId': chainId,
    'nonce': nonce,
    'to': walletRecipient,
    'value': amountToSendBNB
    })

#build a transaction in a dictionary
tx = {
    'chainId': chainId,
    'nonce': nonce,
    'to': walletRecipient,
    'value': amountToSendBNB, #web3.toWei(float(amountToSendBNB), 'ether'),
    'gas': gasAmount,
    'gasPrice': web3.eth.gas_price #web3.toWei(gasPrice, 'gwei')
    }

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, walletSenderKey)
#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
txid = str(web3.toHex(tx_hash))
print('Transaction Success TX-ID Copied To Clipboard')
print('https://testnet.bscscan.com/tx/'+txid)
pc.copy('https://testnet.bscscan.com/tx/'+txid)
print('update current balance in 30 second...')
time.sleep(30)
print('Current Balance' ,balance_bnb, 'BNB')
print('will close automatically in 30 second...')
time.sleep(30)