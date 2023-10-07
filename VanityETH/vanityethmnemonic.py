from eth_account import Account
from web3 import Web3
import secrets
import ctypes
import time
import pyperclip as pc

#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()

#set title
ctypes.windll.kernel32.SetConsoleTitleW("Generate New ETH Address With Mnemonic & Privatekey")
print('Generate New ETH Address In Python With Mnemonic & Privatekey')
print('')
web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()
#create random 12 word
acct, mnemonic = Account.create_with_mnemonic()
#convert to privatekey
pvkey = web3.eth.account.from_mnemonic(mnemonic, account_path="m/44'/60'/0'/0/0")
log('Your Address : '+acct.address)
log('12 Word Phrase/Mnemonic : '+str(mnemonic))
log('Private Key : '+str(web3.toHex(pvkey.key)))
log('=================================================================================')
print('Your Address, 12 Word Phrase/Mnemonic & Privatekey Logged To vanityethmnemonic.py.log.txt')
print('Will Close Automatically In 60 Second...')
time.sleep(60)