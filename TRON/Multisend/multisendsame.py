from tronpy import Tron
from tronpy.keys import PrivateKey
import time

#client = Tron()  # The default provider, mainnet
client = Tron(network='nile')  # The Nile Testnet is preset

print("")
print("MultiSend Tron (TRX) With Same Amount")
print("Example This MultiSend To 10 Address")
print("If You Using Mainnet Please Change client = Tron(network='nile') To client = Tron()")
print("")

sender = input(str("Enter Your Address As Sender : "))
pvkey = input("Enter Your PrivateKey As Sender : ")
recipient1 = input(str("Enter Address As Recipient1 : "))
recipient2 = input(str("Enter Address As Recipient2 : "))
recipient3 = input(str("Enter Address As Recipient3 : "))
recipient4 = input(str("Enter Address As Recipient4 : "))
recipient5 = input(str("Enter Address As Recipient5 : "))
recipient6 = input(str("Enter Address As Recipient6 : "))
recipient7 = input(str("Enter Address As Recipient7 : "))
recipient8 = input(str("Enter Address As Recipient8 : "))
recipient9 = input(str("Enter Address As Recipient9 : "))
recipient10 = input(str("Enter Address As Recipient10 : "))
all_recipient = [recipient1,recipient2,recipient3,recipient4,recipient5,recipient6,recipient7,recipient8,recipient9,recipient10]
ctraddr = input(str("Enter Contract Address Disperse.app : "))
priv_key = PrivateKey(bytes.fromhex(pvkey))
inputamount = int(input("Enter Amount Of You Want To Send : "))
calcamount = int((10**6) * inputamount)
contractaddr = client.get_contract(ctraddr)
amount = [calcamount, calcamount, calcamount, calcamount, calcamount, calcamount, calcamount, calcamount, calcamount, calcamount]
amounttotal = int((10**6) * inputamount * 10)

def UpdateBalance():
    balance = client.get_account_balance(sender)
    print("")
    print('Your Balance : ' ,balance, 'TRX')
    print("")
    
UpdateBalance()

txn = (
    contractaddr.functions.disperseEther.with_transfer(amounttotal)(all_recipient, amount)
    .with_owner(sender)
    .fee_limit(100_000_000)
    .build()
    .sign(priv_key)
)

print("Transaction Success : "+str(txn.broadcast().wait()))