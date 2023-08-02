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

ctypes.windll.kernel32.SetConsoleTitleW("Send Token AIO Blockchain Network")
print('Send Token AIO Blockchain Network To Other Address')
print('This Support Tesnet & Mainnet Ethereum, Binance Smart Chain, Polygon')
print('Polygon zkEVM, Arbitrum, Optimism, Avalanche, zkSync Era, & Base')
print('You Need Gas Fee Depends On Your Choose Blockchain Network Like ETH/BNB/MATIC/OTHER')

#connecting web3
if  web3.isConnected() == True:
    print("web3 connected...\n")
else :
    print("error connecting please try again...")

sender = web3.toChecksumAddress(input("Enter your address sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter your privatekey sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
recipient = web3.toChecksumAddress(input("Enter your address recipient 0x...: "))
#recipient = web3.toChecksumAddress('0x0') #to this address
contract_address = web3.toChecksumAddress(input('Enter token address 0x...: '))
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=contract_address, abi=abi)
tokenName = contract.functions.name().call()
tokenSymbol = contract.functions.symbol().call()

#Get balance account
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    #Get token balance account
    token_balance = contract.functions.balanceOf(sender).call()
    balance_token = web3.fromWei(token_balance, 'ether')
    print('Token Balance' ,balance_token, tokenSymbol)
    
UpdateBalance()

inputamount = web3.toWei(float(input("Enter amount of token you want to send: ")), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

nonce = web3.eth.getTransactionCount(sender)

#estimate gas limit contract
gas_tx = contract.functions.transfer(recipient, inputamount).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': nonce
})
gasAmount = web3.eth.estimateGas(gas_tx)

#calculate transaction fee
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')

token_tx = contract.functions.transfer(recipient, inputamount).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gas': gasAmount,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': nonce
})

#sign the transaction
sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
#send transaction
tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

#get transaction hash
txid = str(web3.toHex(tx_hash))
print('Transaction Success TX-ID Copied To Clipboard')
print(txid)
pc.copy(txid)
print('update current balance in 30 second...')
time.sleep(30)
UpdateBalance() #get latest balance
print('will close automatically in 30 second...')
time.sleep(30)