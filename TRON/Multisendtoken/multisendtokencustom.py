from tronpy import Tron
from tronpy.keys import PrivateKey
import time

#client = Tron()  # The default provider, mainnet
client = Tron(network='nile')  # The Nile Testnet is preset

print("")
print("MultiSend Token/TRC20 Token In Tron With Custom Amount")
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
tokenaddr = input(str("Enter Token Address : "))
ctraddr = input(str("Enter Contract Address Disperse.app : "))
priv_key = PrivateKey(bytes.fromhex(pvkey))
inputamount1 = int(input("Enter Amount Of You Want Send To Recipient1 : "))
inputamount2 = int(input("Enter Amount Of You Want Send To Recipient2 : "))
inputamount3 = int(input("Enter Amount Of You Want Send To Recipient3 : "))
inputamount4 = int(input("Enter Amount Of You Want Send To Recipient4 : "))
inputamount5 = int(input("Enter Amount Of You Want Send To Recipient5 : "))
inputamount6 = int(input("Enter Amount Of You Want Send To Recipient6 : "))
inputamount7 = int(input("Enter Amount Of You Want Send To Recipient7 : "))
inputamount8 = int(input("Enter Amount Of You Want Send To Recipient8 : "))
inputamount9 = int(input("Enter Amount Of You Want Send To Recipient9 : "))
inputamount10 = int(input("Enter Amount Of You Want Send To Recipient10 : "))
contract = client.get_contract(tokenaddr)
contractaddr = client.get_contract(ctraddr)
amount = [inputamount1, inputamount2, inputamount3, inputamount4, inputamount5, inputamount6, inputamount7, inputamount8, inputamount9, inputamount10]

def UpdateBalance():
    balance = client.get_account_balance(sender)
    symb_token = contract.functions.symbol()
    print("")
    print('Your Balance : ' ,balance, 'TRX')
    print('Token Balance : ',contract.functions.balanceOf(sender), str(symb_token))
    print("")
    
UpdateBalance()

txappv = (
        contract.functions.approve(ctraddr, contract.functions.balanceOf(sender))
        .with_owner(sender)
        .fee_limit(10_000_000)
        .build()
        .sign(priv_key)
)
print("Approved Spender Token : "+str(txappv.broadcast().wait()))
print("Wait For 10 Second...")
time.sleep(10)

txn = (
    contractaddr.functions.disperseToken(tokenaddr, all_recipient, amount)
    .with_owner(sender)
    .fee_limit(100_000_000)
    .build()
    .sign(priv_key)
)

print("Transaction Success : "+str(txn.broadcast().wait()))