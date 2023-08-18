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

bsc = "https://bsc-rpc.gateway.pokt.network" #rpc bsctesnet custom
web3 = Web3(Web3.HTTPProvider(bsc))
chainId = 56

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

ctypes.windll.kernel32.SetConsoleTitleW("Bridge BNB Mainnet To opBNB Mainnet")
print('')
print('Bridge BNB Mainnet To opBNB Mainnet Official')
print('')

sender = web3.toChecksumAddress(input("Enter Your Address 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
contract_bridge = web3.toChecksumAddress("0xF05F0e4362859c3331Cb9395CBC201E3Fa6757Ea") #contract bridge to opbnb
InputMessage = str("")
Message = bytes(InputMessage, 'utf-8')
#gasAmount = 20000000 #gas limit // change if transaction fail
#gasPrice = 5 #gas price
l2Gas = 200000
#numDetected = 0

bridgeabi = json.loads('[{"inputs":[{"internalType":"address payable","name":"_messenger","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"localToken","type":"address"},{"indexed":true,"internalType":"address","name":"remoteToken","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20BridgeFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"localToken","type":"address"},{"indexed":true,"internalType":"address","name":"remoteToken","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20BridgeInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"l1Token","type":"address"},{"indexed":true,"internalType":"address","name":"l2Token","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20DepositInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"l1Token","type":"address"},{"indexed":true,"internalType":"address","name":"l2Token","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20WithdrawalFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHBridgeFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHBridgeInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHDepositInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHWithdrawalFinalized","type":"event"},{"inputs":[],"name":"MESSENGER","outputs":[{"internalType":"contract CrossDomainMessenger","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OTHER_BRIDGE","outputs":[{"internalType":"contract StandardBridge","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeERC20To","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeETHTo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositERC20To","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositETHTo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"deposits","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeBridgeERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeBridgeETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeERC20Withdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeETHWithdrawal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"l2TokenBridge","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"messenger","outputs":[{"internalType":"contract CrossDomainMessenger","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')
contractbridge = web3.eth.contract(address=contract_bridge, abi=bridgeabi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'BNB')
    
UpdateBalance()

inputamount = web3.toWei(float(input("Enter Amount Of BNB You Want To Bridge : ")), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

#estimate gas limit contract
gas_tx = contractbridge.functions.depositETH(l2Gas, Message).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'value': inputamount,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.getTransactionCount(sender),
        })
        gasAmount = web3.eth.estimateGas(gas_tx)

#calculate transaction fee
print('')
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'BNB')

token_tx = contractbridge.functions.depositETH(l2Gas, Message).buildTransaction({
        'chainId': chainId,
        'nonce': web3.eth.getTransactionCount(sender),
        'from': sender,
        'value': inputamount,
        'gas': gasAmount,
        'gasPrice': web3.eth.gas_price #web3.toWei(gasPrice,'gwei'),
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