from solcx import compile_standard, install_solc
import datetime 
import threading
import asyncio
import requests
import time
import os
import sys
import json
from tronpy import Tron, Contract
from tronpy.keys import PrivateKey
install_solc('0.8.7')

with open("TRC20TOKEN.sol", "r") as file:
    trc20token_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"TRC20TOKEN.sol": {"content": trc20token_file}},
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
    solc_version="0.8.7",
)
#print(compiled_sol)
#with open("compiled_code.json", "w") as file:
#json.dump(compiled_sol, file)

# get bytecode
# TRC20TOKEN = mean contract function you want deploy in sol code
bytecode = compiled_sol["contracts"]["TRC20TOKEN.sol"]["TRC20TOKEN"]["evm"]["bytecode"]["object"]# get abi
abi = json.loads(compiled_sol["contracts"]["TRC20TOKEN.sol"]["TRC20TOKEN"]["metadata"])["output"]["abi"]

#set title
print('')
print('Deploy TRC20TOKEN Standart On Tron')
print('')

#client = Tron()  # The default provider, mainnet
client = Tron(network='nile')  # The Nile Testnet is preset

sender = input(str("Enter Your Address As Sender : "))
pvkey = input("Enter Your PrivateKey As Sender : ")
priv_key = PrivateKey(bytes.fromhex(pvkey))
cntr = Contract(name="TRC20TOKEN", bytecode=bytecode, abi=abi)

print("")
def UpdateBalance():
    balance = client.get_account_balance(sender)
    print("")
    print('Your Balance : ' ,balance, 'TRX')
    print("")
    
UpdateBalance()
print("")

txn = (
    client.trx.deploy_contract(sender, cntr)
    .with_owner(sender)
    .fee_limit(1_000_000_000)
    .build()
    .sign(priv_key)
)

result = txn.broadcast().wait()
print(result)
print('Created:', result['contract_address'])
print('Will Close Automatically In 10 Second...')
time.sleep(10)