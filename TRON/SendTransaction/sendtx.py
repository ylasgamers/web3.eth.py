from tronpy import Tron
from tronpy.keys import PrivateKey

#client = Tron()  # The default provider, mainnet
client = Tron(network='nile')  # The Nile Testnet is preset

print("")
print("Send Transaction TRON With Custom Note/Messages")
print("If You Using Mainnet Please Change client = Tron(network='nile') To client = Tron()")
print("")

sender = input(str("Enter Your Address As Sender : "))
pvkey = input("Enter Your PrivateKey As Sender : ")
recipient = input(str("Enter Address As Recipient : "))
priv_key = PrivateKey(bytes.fromhex(pvkey))
custmsg = input(str("Enter Custom Note/Messages To Recipient : "))
inputamount = float(input("Enter Amount Of You Want To Send : "))
amount = int((10**6) * inputamount)

def UpdateBalance():
    balance = client.get_account_balance(sender)
    print("")
    print('Your Balance : ' ,balance, 'TRX')
    print("")
    
UpdateBalance()

txn = (
    client.trx.transfer(sender, recipient, amount)
    .memo(custmsg)
    .build()
    .sign(priv_key)
)

print("Transaction Success : "+str(txn.broadcast().wait()))