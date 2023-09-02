from web3 import Web3
import datetime 
import threading
import asyncio
import requests
import time
import os
import sys
import ctypes
import pyperclip as pc

#set title
ctypes.windll.kernel32.SetConsoleTitleW("Convert Mnemonic Phrase To Privatekey")
print('Convert 12 Word Mnemonic Phrase To Privatekey')

#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()
     
web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()
my_mnemonic = str(input("Enter Your 12 Word Mnemonic Phrase... : "))
account = web3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/60'/0'/0/0")
acc_addr = str(account.address)
acc_key = str(web3.toHex(account.key))
log('Your Address : '+acc_addr)
log('Private Key : '+acc_key)
log('=================================================================================')
print('Your Address & Privatekey Logged To mnemoniclog.py.log.txt')
print('Will Close Automatically In 60 Second...')
time.sleep(60)