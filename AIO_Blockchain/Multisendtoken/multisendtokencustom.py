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

ctypes.windll.kernel32.SetConsoleTitleW("Multisend Token AIO Blockchain Network")
print('')
print('Multisend Token AIO Blockchain Network With Custom Amount To Multiple Address')
print('This Support Tesnet & Mainnet Ethereum, Binance Smart Chain, Polygon')
print('Polygon zkEVM, Arbitrum, Optimism, Avalanche, zkSync Era, & Base')
print('This Example Multisend To 10 Address With Custom Amount')
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
#ex send to 10 address, if want more send to a lot address, you need modif it
recipient1 = web3.toChecksumAddress(input("Enter Your Address Recipient1 0x...: "))
recipient2 = web3.toChecksumAddress(input("Enter Your Address Recipient2 0x...: "))
recipient3 = web3.toChecksumAddress(input("Enter Your Address Recipient3 0x...: "))
recipient4 = web3.toChecksumAddress(input("Enter Your Address Recipient4 0x...: "))
recipient5 = web3.toChecksumAddress(input("Enter Your Address Recipient5 0x...: "))
recipient6 = web3.toChecksumAddress(input("Enter Your Address Recipient6 0x...: "))
recipient7 = web3.toChecksumAddress(input("Enter Your Address Recipient7 0x...: "))
recipient8 = web3.toChecksumAddress(input("Enter Your Address Recipient8 0x...: "))
recipient9 = web3.toChecksumAddress(input("Enter Your Address Recipient9 0x...: "))
recipient10 = web3.toChecksumAddress(input("Enter Your Address Recipient10 0x...: "))
#recipient1 = web3.toChecksumAddress('0x0') #to this address
#recipient2 = web3.toChecksumAddress('0x0') #to this address
all_recipient = [recipient1,recipient2,recipient3,recipient4,recipient5,recipient6,recipient7,recipient8,recipient9,recipient10] #ex send to 10 address, if want more send to a lot address, you need modif it
tokenaddr = web3.toChecksumAddress(input('Enter Token Address 0x...: '))
contract_address = web3.toChecksumAddress(input("Enter Contract Address Disperse.app : ")) #Disperse.app
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price
#chainId = 56 

abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
tokenabi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=contract_address, abi=abi)
token_contract = web3.eth.contract(address=tokenaddr, abi=tokenabi)
tokenName = token_contract.functions.name().call()
tokenSymbol = token_contract.functions.symbol().call()

#Get balance account
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    #Get token balance account
    token_balance = token_contract.functions.balanceOf(sender).call()
    balance_token = web3.fromWei(token_balance, 'ether')
    print('Token Balance' ,balance_token, tokenSymbol)
    
UpdateBalance()

nonce = web3.eth.getTransactionCount(sender)

token_approve = token_contract.functions.balanceOf(sender).call()

#estimate gas limit approve
gas_approve = token_contract.functions.approve(contract_address, token_approve).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gasPrice': web3.eth.gas_price,
    'nonce': nonce
})
gasApprove = web3.eth.estimateGas(gas_approve)

#calculate transaction fee
print('')
print('Processing Approve Spender Token...')
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasApprove, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')

#Approve
Approve = token_contract.functions.approve(contract_address, token_approve).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gas': gasApprove,
    'gasPrice': web3.eth.gas_price,
    'nonce': nonce
})

sign_approve = web3.eth.account.sign_transaction(Approve, senderkey)
web3.eth.send_raw_transaction(sign_approve.rawTransaction)
print('Approved Spender Token Wait 10 Second...')
time.sleep(10)
print('')
inputamount1 = float(input("Enter Amount Of You Want Send To Recipient1 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount2 = float(input("Enter Amount Of You Want Send To Recipient2 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount3 = float(input("Enter Amount Of You Want Send To Recipient3 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount4 = float(input("Enter Amount Of You Want Send To Recipient4 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount5 = float(input("Enter Amount Of You Want Send To Recipient5 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount6 = float(input("Enter Amount Of You Want Send To Recipient6 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount7 = float(input("Enter Amount Of You Want Send To Recipient7 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount8 = float(input("Enter Amount Of You Want Send To Recipient8 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount9 = float(input("Enter Amount Of You Want Send To Recipient9 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
inputamount10 = float(input("Enter Amount Of You Want Send To Recipient10 : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount1 = web3.toWei(float(inputamount1), 'ether')
amount2 = web3.toWei(float(inputamount2), 'ether')
amount3 = web3.toWei(float(inputamount3), 'ether')
amount4 = web3.toWei(float(inputamount4), 'ether')
amount5 = web3.toWei(float(inputamount5), 'ether')
amount6 = web3.toWei(float(inputamount6), 'ether')
amount7 = web3.toWei(float(inputamount7), 'ether')
amount8 = web3.toWei(float(inputamount8), 'ether')
amount9 = web3.toWei(float(inputamount9), 'ether')
amount10 = web3.toWei(float(inputamount10), 'ether')
amountall = [amount1,amount2,amount3,amount4,amount5,amount6,amount7,amount8,amount9,amount10] #10 address, if want more send to a lot address, you need modif it
totaltoken = web3.toWei(float(inputamount*10), 'ether') #calc total token send ex inputamount*10 [10 = 10 address]

#estimate gas limit contract
nonce2 = web3.eth.getTransactionCount(sender)
gas_tx = contract.functions.disperseToken(tokenaddr, all_recipient, amountall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': nonce2
})
gasAmount = web3.eth.estimateGas(gas_tx)

#calculate transaction fee
print('')
amountFromWei = web3.fromWei(totaltoken, 'ether')
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')
print('Processing Send :' ,amountFromWei, tokenSymbol, 'To Recepient :', all_recipient)

token_tx = contract.functions.disperseToken(tokenaddr, all_recipient, amountall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gas': gasAmount,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': nonce2
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
