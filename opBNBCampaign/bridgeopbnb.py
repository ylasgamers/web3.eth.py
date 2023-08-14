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
chainId = 97

#connecting web3
# if  web3.isConnected() == True:
    # print("Web3 Connected...\n")
# else :
    # print("Error Connecting Please Try Again...")

sender = web3.toChecksumAddress(input("Enter Your Address Sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey Sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
contract_bridge = web3.toChecksumAddress("0x677311fd2ccc511bbc0f581e8d9a07b033d5e840")
InputMessage = str("")
Message = bytes(InputMessage, 'utf-8')
gasAmount = 20000000 #gas limit // change if transaction fail
gasPrice = 5 #gas price
l2Gas = 200000

bridgeabi = json.loads('[{"inputs":[{"internalType":"address payable","name":"_messenger","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"localToken","type":"address"},{"indexed":true,"internalType":"address","name":"remoteToken","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20BridgeFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"localToken","type":"address"},{"indexed":true,"internalType":"address","name":"remoteToken","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20BridgeInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"l1Token","type":"address"},{"indexed":true,"internalType":"address","name":"l2Token","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20DepositInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"l1Token","type":"address"},{"indexed":true,"internalType":"address","name":"l2Token","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20WithdrawalFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHBridgeFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHBridgeInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHDepositInitiated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHWithdrawalFinalized","type":"event"},{"inputs":[],"name":"MESSENGER","outputs":[{"internalType":"contract CrossDomainMessenger","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OTHER_BRIDGE","outputs":[{"internalType":"contract StandardBridge","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeERC20To","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeETHTo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositERC20To","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositETHTo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"deposits","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeBridgeERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeBridgeETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeERC20Withdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeETHWithdrawal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"l2TokenBridge","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"messenger","outputs":[{"internalType":"contract CrossDomainMessenger","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')
contractbridge = web3.eth.contract(address=contract_bridge, abi=bridgeabi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_bnb, 'BNB')
UpdateBalance()

inputamount1 = float(input("Enter Amount Of You Want To Bridge : "))
inputamount = web3.toWei(float(inputamount1), 'ether') #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001

def RepeatMint(event):
    try:
        #estimate gas limit contract
        # gas_tx = contractbridge.functions.depositETH(l2Gas, Message).buildTransaction({
            # 'chainId': chainId,
            # 'from': sender,
            # 'value': web3.toWei(float(0.000042), 'ether'),
            # 'gasPrice': web3.toWei(gasPrice,'gwei'),
            # 'nonce': web3.eth.getTransactionCount(sender)
        # })
        # gasAmount = web3.eth.estimateGas(gas_tx)

        # #calculate transaction fee
        # print('')
        # #gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
        # Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
        # print('Transaction Fee :' ,Caclfee, 'BNB')

        token_tx = contractbridge.functions.depositETH(l2Gas, Message).buildTransaction({
            'chainId': chainId,
            'from': sender,
            'value': web3.toWei(float(0.000042), 'ether'),
            'gas': gasAmount,
            'gasPrice': web3.toWei(gasPrice,'gwei'),
            'nonce': web3.eth.getTransactionCount(sender)
        })
        #sign the transaction
        sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        txid = str(web3.toHex(tx_hash))
        print(txid)
        UpdateBalance() #get latest balance
    
    except:
        pass
    
async def finalizedLoop(event_filter, poll_interval):
    while True:
        try:
            for ETHDepositInitiated in event_filter.get_new_entries():
                RepeatMint(ETHDepositInitiated)
            await asyncio.sleep(poll_interval)
        except:
            pass

def listenForFinalized():
    event_filter = contractbridge.events.ETHDepositInitiated.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                finalizedLoop(event_filter, 0)))       
                # log_loop(block_filter, 2),
                # log_loop(tx_filter, 2)))
                 
    finally:
        # close loop to free up system resources
        #loop.close()
        #print("loop close")
        listenForFinalized()

        #beware of valueerror code -32000 which is a glitch. make it ignore it and go bakc to listening

listenForFinalized()

input("")

# #10x
# def Repeat10x():
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)
    # RepeatMint()
    # time.sleep(3)

# #10x10=100    
# Repeat10x()
# Repeat10x()
# Repeat10x()
# Repeat10x()
# Repeat10x()
# Repeat10x()
# Repeat10x()
# Repeat10x()
# Repeat10x()
# Repeat10x()