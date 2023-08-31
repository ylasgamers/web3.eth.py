from eth_account import Account
import secrets
import ctypes
import time
import pyperclip as pc

#set title
ctypes.windll.kernel32.SetConsoleTitleW("Generate New ETH Address")
print('Generate New ETH Address In Python')

#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()

priv = secrets.token_hex(32)
private_key = "0x" + priv
acct = Account.from_key(private_key)
log('Your Address : '+acct.address)
log('Private Key : '+private_key)
log('=================================================================================')
print('Your Address & Privatekey Logged To vanityethlog.py.log.txt')
print('Will Close Automatically In 60 Second...')
time.sleep(60)