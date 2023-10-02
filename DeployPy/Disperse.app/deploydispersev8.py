from solcx import compile_standard, install_solc
import datetime 
import threading
import asyncio
import requests
import time
import os
import sys
import ctypes
import pyperclip as pc
install_solc('0.8.0')

with open("Dispersev8.sol", "r") as file:
    disperse_file = file.read()

import json
...

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Dispersev8.sol": {"content": disperse_file}},
        "settings": {
             "optimizer": {
             "enabled": bool(True),
             "runs": 200
            },
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] # output needed to interact with and deploy contract 
                }
            }
        },
    },
    solc_version="0.8.0",
)
#print(compiled_sol)
#with open("compiled_code.json", "w") as file:
#json.dump(compiled_sol, file)

# get bytecode
# ERC20TOKEN = mean contract function you want deploy in sol code
bytecode = compiled_sol["contracts"]["Dispersev8.sol"]["Disperse"]["evm"]["bytecode"]["object"]# get abi
abi = json.loads(compiled_sol["contracts"]["Dispersev8.sol"]["Disperse"]["metadata"])["output"]["abi"]

#set title
ctypes.windll.kernel32.SetConsoleTitleW("Deploy Disperse On Blockchain Network")
print('')
print('Deploy Disperse On Blockchain Network With Python')
print('This Support Tesnet & Mainnet Ethereum, Binance Smart Chain, Polygon')
print('Polygon zkEVM, Arbitrum, Optimism, Avalanche, zkSync Era, & Base')
print('You Need Gas Fee Depends On Your Choose Blockchain Network Like ETH/BNB/MATIC/OTHER')
print('')

# For connecting to web3
from web3 import Web3
#bsc = "https://bsc-testnet.publicnode.com" #rpc bsctesnet custom #you can find rpc on chainlist.org
inputrpc = str(input("Input Url RPC/Node Blockchain Network : "))
web3 = Web3(Web3.HTTPProvider(inputrpc))
#chain_id = 97 #you can find chainid on chainlist.org
chain_id = int(input("Input Chain ID Blockchain Network : "))

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

address = web3.toChecksumAddress(input("Enter Your Address 0x...: "))
private_key = input("Enter Your Privatekey abcde12345...: ")
Contract = web3.eth.contract(abi=abi, bytecode=bytecode)
# Get the number of latest transaction
nonce = web3.eth.getTransactionCount(address)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(address)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    
UpdateBalance()

#estimate gas limit contract
gas_tx = Contract.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": web3.eth.gas_price,
        "from": address,
        "nonce": nonce
    }
)
gasAmount = web3.eth.estimateGas(gas_tx)

#calculate transaction fee
print('')
gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')

# build transaction
transaction = Contract.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gas": gasAmount,
        "gasPrice": web3.eth.gas_price,
        "from": address,
        "nonce": nonce
    }
)
# Sign the transaction
sign_transaction = web3.eth.account.sign_transaction(transaction, private_key)
# Send the transaction
transaction_hash = web3.eth.send_raw_transaction(sign_transaction.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
#get transaction hash
txid = str(web3.toHex(transaction_hash))
print('')
transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
print('Transaction Success Contract deployed! TX-ID & Contract Address Copied To Clipboard')
print('TX-ID : '+txid+ ' & ' 'Contract Address : '+transaction_receipt.contractAddress)
pc.copy('TX-ID : '+txid+ ' & ' 'Contract Address : '+transaction_receipt.contractAddress)
print('Update Current Balance In 30 Second...')
time.sleep(30)
print('')
UpdateBalance() #get latest balance
print('Will Close Automatically In 30 Second...')
time.sleep(30)