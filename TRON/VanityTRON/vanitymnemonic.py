from tronpy import Tron
from eth_account import Account
import tronpy
import time

client = Tron()  # The default provider, mainnet
#client = Tron(network="nile")  # The Nile Testnet is preset

#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()

print("Generate Random Tron Address From 12 Word/Mnemonic")
Account.enable_unaudited_hdwallet_features()
acct, mnemonic = Account.create_with_mnemonic()
acctrdm = client.generate_address_from_mnemonic(mnemonic, account_path="m/44'/195'/0'/0/0")
print("Address, PrivateKey, PublicKey : ",acctrdm)
print("12 Word/Mnemonic : "+str(mnemonic))
log(str(acctrdm))
log("12 Word/Mnemonic : "+str(mnemonic))
log('=================================================================================')
print('Your Address, 12 Word/Mnemonic & Privatekey Logged To vanitymnemonic.log.txt')
print('Will Close Automatically In 30 Second...')
time.sleep(30)