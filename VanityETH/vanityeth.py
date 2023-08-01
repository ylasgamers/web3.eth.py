from eth_account import Account
import secrets
import ctypes
import time
import pyperclip as pc

#set title
ctypes.windll.kernel32.SetConsoleTitleW("Generate New ETH Address")
print('Generate New ETH Address In Python')

priv = secrets.token_hex(32)
private_key = "0x" + priv
print('Your Privatekey Copied To Clipboard : ',private_key)
acct = Account.from_key(private_key)
print('Your Address : ', acct.address)
pc.copy(private_key)
print('will close automatically in 60 second...')
time.sleep(60)