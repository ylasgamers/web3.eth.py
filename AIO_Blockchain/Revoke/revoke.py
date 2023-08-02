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

ctypes.windll.kernel32.SetConsoleTitleW("Revoke Contract Address")
print('')
print('Revoke Contract Address')
print('This Support Tesnet & Mainnet Ethereum, Binance Smart Chain, Polygon')
print('Polygon zkEVM, Arbitrum, Optimism, Avalanche, zkSync Era, & Base')
print('You Need Gas Fee Depends On Your Choose Blockchain Network Like ETH/BNB/MATIC/OTHER')
print('')

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

sender = web3.toChecksumAddress(input("Enter Your Address Sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey Sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
token_address = web3.toChecksumAddress(input('Enter Token Address You Want To Revoke 0x...: '))
contract_address = web3.toChecksumAddress(input('Enter Contract Address You Want To Revoke 0x...: '))
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price
#chainId = 56 

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=token_address, abi=abi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    
UpdateBalance()

nonce = web3.eth.getTransactionCount(sender)

#estimate gas limit approve
gas_revoke = contract.functions.approve(contract_address, 0).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gasPrice': web3.eth.gas_price,
    'nonce': nonce
})
gasRevoke = web3.eth.estimateGas(gas_revoke)

#calculate transaction fee
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasRevoke, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')

#Revoke
Revoke = contract.functions.approve(contract_address, 0).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gas': gasRevoke,
    'gasPrice': web3.eth.gas_price,
    'nonce': nonce
})

sign_revoke = web3.eth.account.sign_transaction(Revoke, senderkey)
txrevoke = web3.eth.send_raw_transaction(sign_revoke.rawTransaction)

#get transaction hash
txid = str(web3.toHex(txrevoke))
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