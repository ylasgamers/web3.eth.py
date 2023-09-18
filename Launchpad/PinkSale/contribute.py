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

#bsc = "https://bsc-testnet.publicnode.com" #rpc bsctesnet custom #you can find rpc on chainlist.org
inputrpc = str(input("Input Url RPC/Node Blockchain Network : "))
web3 = Web3(Web3.HTTPProvider(inputrpc))
#chain_id = 97 #you can find chainid on chainlist.org
chainId = int(input("Input Chain ID Blockchain Network : "))

ctypes.windll.kernel32.SetConsoleTitleW("Contribute Presale On Launchpad AIO Blockchain Network")
print('')
print('Contribute Presale On Launchpad Pinksale AIO Blockchain Network')
print('This Support Only Blockchain Network Available On Launchpad Pinksale')
print('')

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

sender = web3.toChecksumAddress(input("Enter Your Address 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
print("If Presale Have Affiliate Program Enter Referrer Address")
print("If Presale Not Have Affiliate Program Enter Address 0x0000000000000000000000000000000000000000")
reffaddr = web3.toChecksumAddress(input("Enter Referrer Address 0x...: "))
contract_presale = web3.toChecksumAddress(input("Enter Contract Address Presale : "))
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price
#chainId = 56 

presaleabi = json.loads('[{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"token","type":"address"}],"name":"contribute","outputs":[],"stateMutability":"payable","type":"function"}]')
contractpresale = web3.eth.contract(address=contract_presale, abi=presaleabi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    
UpdateBalance()

inputamount = float(input("Enter Amount Of You Want Contribute : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount = web3.toWei(float(inputamount), 'ether')

#estimate gas limit contract
gas_tx = contractpresale.functions.contribute(0, reffaddr).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'value': amount,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': web3.eth.getTransactionCount(sender)
})
gasAmount = web3.eth.estimateGas(gas_tx)

#calculate transaction fee
print('')
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')

token_tx = contractpresale.functions.contribute(0, reffaddr).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'value': amount,
    'gas': gasAmount,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': web3.eth.getTransactionCount(sender)
})

#sign the transaction
sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
#send transaction
tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

#get transaction hash
txid = str(web3.toHex(tx_hash))
print('')
print('Contribute Success TX-ID Copied To Clipboard')
print(txid)
pc.copy(txid)
print('Update Current Balance In 30 Second...')
time.sleep(30)
print('')
UpdateBalance() #get latest balance
print('Will Close Automatically In 30 Second...')
time.sleep(30)