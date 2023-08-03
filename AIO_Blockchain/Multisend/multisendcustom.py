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

ctypes.windll.kernel32.SetConsoleTitleW("Multisend AIO Blockchain Network")
print('')
print('Multisend AIO Blockchain Network With Custom Amount To Multiple Address')
print('This Support Tesnet & Mainnet Ethereum, Binance Smart Chain, Polygon')
print('Polygon zkEVM, Arbitrum, Optimism, Avalanche, zkSync Era, & Base')
print('This Example Multisend To 4 Address With Custom Amount')
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
recipient1 = web3.toChecksumAddress(input("Enter Your Address Recipient1 0x...: "))
recipient2 = web3.toChecksumAddress(input("Enter Your Address Recipient2 0x...: "))
recipient3 = web3.toChecksumAddress(input("Enter Your Address Recipient3 0x...: "))
recipient4 = web3.toChecksumAddress(input("Enter Your Address Recipient4 0x...: "))
#recipient1 = web3.toChecksumAddress('0x0') #to this address
#recipient2 = web3.toChecksumAddress('0x0') #to this address
all_recipient = [recipient1,recipient2,recipient3,recipient4] #ex send to 4 address, if want more send to a lot address, you need modif it
contract_address = web3.toChecksumAddress(input("Enter Contract Address Disperse.app : ")) #Disperse.app
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price
#chainId = 56 

abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
contract = web3.eth.contract(address=contract_address, abi=abi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    
UpdateBalance()

inputamount1 = float(input("Enter Amount Of You Want Send To Recipient1 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount2 = float(input("Enter Amount Of You Want Send To Recipient2 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount3 = float(input("Enter Amount Of You Want Send To Recipient3 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount4 = float(input("Enter Amount Of You Want Send To Recipient4 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount1 = web3.toWei(float(inputamount1), 'ether')
amount2 = web3.toWei(float(inputamount2), 'ether')
amount3 = web3.toWei(float(inputamount3), 'ether')
amount4 = web3.toWei(float(inputamount4), 'ether')
amountall = [amount1,amount2,amount3,amount4] #4 address, if want more send to a lot address, you need modif it
total_pay = web3.toWei(float(inputamount1+inputamount2+inputamount3+inputamount4), 'ether') #ex amount1+amount2+amount3+amount4 = totalpay [ if want more send to a lot address, you need modif it ]

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

#calculate transaction fee
print('')
amountFromWei = web3.fromWei(total_pay, 'ether')
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')
print('Processing Send :' ,amountFromWei, 'ETH/BNB/MATIC/OTHER To Recepient :', all_recipient)

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