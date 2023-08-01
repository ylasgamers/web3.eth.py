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
     
web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()
my_mnemonic = str(input("Enter your 12 word mnemonic phrase... : "))
account = web3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/60'/0'/0/0")
acc_addr = str(account.address)
acc_key = str(web3.toHex(account.key))
print('Your Address : ',acc_addr)
print('Your Privatekey Copied To Clipboard : ',acc_key)
pc.copy(acc_key)
print('will close automatically in 60 second...')
time.sleep(60)