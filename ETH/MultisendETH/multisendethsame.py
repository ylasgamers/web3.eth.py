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

weth = "https://eth-rpc.gateway.pokt.network" #rpc eth custom
web3 = Web3(Web3.HTTPProvider(weth))

ctypes.windll.kernel32.SetConsoleTitleW("Multisender ETH")
print('multisender eth with same amount')
print('you can custom to send to a lot address')
print('this example send to 2 address')

#connecting web3
if  web3.isConnected() == True:
    print("web3 connected...\n")
else :
    print("error connecting please try again...")

sender = web3.toChecksumAddress(input("Enter your address sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter your privatekey sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
recipient1 = web3.toChecksumAddress(input("Enter your address recipient1 0x...: "))
recipient2 = web3.toChecksumAddress(input("Enter your address recipient2 0x...: "))
#recipient1 = web3.toChecksumAddress('0x0') #to this address
#recipient2 = web3.toChecksumAddress('0x0') #to this address
all_recipient = [recipient1, recipient2] #ex send to 2 address, if want more send to a lot address, you need modif it
contract_address = web3.toChecksumAddress('0xd152f549545093347a162dce210e7293f1452150') #Disperse.app
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price
chainId = 1 

abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
contract = web3.eth.contract(address=contract_address, abi=abi)

#Get balance account
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_eth = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_eth, 'ETH')
    
UpdateBalance()

inputamount = float(input("Enter amount of eth you want to send: ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount = web3.toWei(float(inputamount), 'ether')
amountall = [amount, amount] #2 address, if want more send to a lot address, you need modif it
total_pay = web3.toWei(float(inputamount*2), 'ether') #input amount*2 = totalpay [ 2 = 2 address, if want more send to a lot address, you need modif it ]

nonce = web3.eth.getTransactionCount(sender)

#estimate gas limit contract
gas_tx = contract.functions.disperseEther(all_recipient, amountall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'value': total_pay,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': nonce
})
gasAmount = web3.eth.estimateGas(gas_tx)

token_tx = contract.functions.disperseEther(all_recipient, amountall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'value': total_pay,
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
print('https://etherscan.io/tx/'+txid)
pc.copy('https://etherscan.io/tx/'+txid)
print('update current balance in 30 second...')
time.sleep(30)
UpdateBalance() #get latest balance
print('will close automatically in 30 second...')
time.sleep(30)
