from web3 import Web3
import datetime 
import threading
import json
import asyncio
import requests
import time
import os
import sys
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Friend.tech Sniper Buy & Sell | Loading...")
os.system("mode con: lines=32766")
os.system("") #allows different colour text to be used
print('')
print('Friend.tech Sniper Buy Shares & Sell Shares With Custom Time')
print('You Need Active Account & Export Your Wallet From Friend.tech')
print('To Get Your Address & Privatekey From Friend.tech')
print('')

baserpc = "https://gateway.tenderly.co/public/base"
web3 = Web3(Web3.HTTPProvider(baserpc))
chainId = 8453

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

sender = web3.toChecksumAddress(input("Enter Your Address 0x...: "))
senderkey = input("Enter Your Privatekey abcde12345...: ")
custime = input("Enter Time In Second To Set Automatic Sell Shared After Buy Shares...: ")
friendtech_contract = web3.toChecksumAddress('0xcf205808ed36593aa40a44f10c7f7c2f67d4a4d4')
friendtechv1_abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"trader","type":"address"},{"indexed":false,"internalType":"address","name":"subject","type":"address"},{"indexed":false,"internalType":"bool","name":"isBuy","type":"bool"},{"indexed":false,"internalType":"uint256","name":"shareAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"protocolEthAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"subjectEthAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"supply","type":"uint256"}],"name":"Trade","type":"event"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"buyShares","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getBuyPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getBuyPriceAfterFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"supply","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getSellPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getSellPriceAfterFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFeeDestination","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFeePercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"sellShares","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeDestination","type":"address"}],"name":"setFeeDestination","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feePercent","type":"uint256"}],"name":"setProtocolFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feePercent","type":"uint256"}],"name":"setSubjectFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"sharesBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"sharesSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"subjectFeePercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=friendtech_contract, abi=friendtechv1_abi)

print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_eth = web3.fromWei(balance,'ether')
    print('Your Balance : ' ,balance_eth, 'ETH')
    print('')
    
UpdateBalance()

#BUY SHARES THREAD
def BuyShares(subjectAddr):
    if(subjectAddr != None):
        getbuypricefee = contract.functions.getBuyPriceAfterFee(subjectAddr, 1).call()
        #estimate gas limit contract
        gas_tx = contract.functions.buyShares(subjectAddr, 1).buildTransaction({
            'chainId': chainId,
            'from': sender,
            'value': web3.toWei(getbuypricefee, 'ether'),
            'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
            'nonce': web3.eth.getTransactionCount(sender)
        })
        gasAmount = web3.eth.estimateGas(gas_tx)
        
        buy_tx = contract.functions.buyShares(subjectAddr, 1).buildTransaction({
            'chainId': chainId,
            'from': sender,
            'value': web3.toWei(getbuypricefee, 'ether'),
            'gas': gasAmount,
            'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
            'nonce': web3.eth.getTransactionCount(sender)
        })
        
        #sign the transaction
        signed_tx = web3.eth.account.sign_transaction(buy_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        txid = str(web3.toHex(tx_hash))
        print('Transaction Buy Shares Success TX-ID : ',txid)
        UpdateBalance()
        
BuySharesThread = threading.Thread(target=BuyShares(None))
BuySharesThread.start()

#SELL SHARES THREAD
def SellShares(subjectAddr):
    if(subjectAddr != None):
        getsellpricefee = contract.functions.getSellPriceAfterFee(subjectAddr, 1).call()
        #estimate gas limit contract
        gas_tx = contract.functions.sellShares(subjectAddr, 1).buildTransaction({
            'chainId': chainId,
            'from': sender,
            'value': web3.toWei(getsellpricefee, 'ether'),
            'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
            'nonce': web3.eth.getTransactionCount(sender)
        })
        gasAmount = web3.eth.estimateGas(gas_tx)
        
        sell_tx = contract.functions.sellShares(subjectAddr, 1).buildTransaction({
            'chainId': chainId,
            'from': sender,
            'value': web3.toWei(getsellpricefee, 'ether'),
            'gas': gasAmount,
            'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
            'nonce': web3.eth.getTransactionCount(sender)
        })
        
        #sign the transaction
        signed_tx = web3.eth.account.sign_transaction(sell_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        txid = str(web3.toHex(tx_hash))
        print('Transaction Sell Shares Success TX-ID : ',txid)
        UpdateBalance()
        
SellSharesThread = threading.Thread(target=SellShares(None))
SellSharesThread.start()
        
print("Scanning For New Trader...")
print("") #line break

def foundTrader(event):
    try:
        ethAmounts = int(0)
        jsonEventContents = json.loads(Web3.toJSON(event));

        if ((jsonEventContents['args']['ethAmount'] == ethAmounts) or (jsonEventContents['args']['subject'] == ethAmounts)):
        
            if (jsonEventContents['args']['ethAmount'] == ethAmounts):
               subjectAddr = jsonEventContents['args']['subject']
            else:
                subjectAddr = jsonEventContents['args']['ethAmount']
         
        print("New Trader Found :",subjectAddr)
        print("Processing Buy Shares...")
        #BUY SHARES
        BuyShares(subjectAddr)
        
        #SELL SHARES
        print("Processing Sell Shares In "+custime+" Second...")
        time.sleep(custime)
        print("Execute Sell Shares...")
        SellShares(subjectAddr)
        
        print("") # line break: move onto scanning for next trader
        
    except:
        pass
        
async def tradeLoop(event_filter, poll_interval):
    while True:
        try:
            for Trade in event_filter.get_new_entries():
                foundTrader(Trade)
            await asyncio.sleep(poll_interval)
        except:
            pass
            
def listenForTrader():
    event_filter = contract.events.Trade.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                tradeLoop(event_filter, 0)))       
                # log_loop(block_filter, 2),
                # log_loop(tx_filter, 2)))
                 
    finally:
        # close loop to free up system resources
        #loop.close()
        #print("loop close")
        listenForTrader()

        #beware of valueerror code -32000 which is a glitch. make it ignore it and go bakc to listening

listenForTrader()

input("")