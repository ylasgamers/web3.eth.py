from tronpy import Tron
from tronpy.keys import PrivateKey

#client = Tron()  # The default provider, mainnet
client = Tron(network='nile')  # The Nile Testnet is preset

print("")
print("Revoke Address/Contract Address In Tron")
print("If You Using Mainnet Please Change client = Tron(network='nile') To client = Tron()")
print("")

sender = input(str("Enter Your Address As Sender : "))
pvkey = input("Enter Your PrivateKey As Sender : ")
ctraddr = input(str("Enter Address/Contract Address To Revoke : "))
tokenaddr = input(str("Enter Token Address To Revoke : "))
priv_key = PrivateKey(bytes.fromhex(pvkey))
contract = client.get_contract(tokenaddr)

def UpdateBalance():
    balance = client.get_account_balance(sender)
    print("")
    print('Your Balance : ' ,balance, 'TRX')
    print("")
    
UpdateBalance()

txn = (
    contract.functions.approve(ctraddr, 0)
    .with_owner(sender)
    .fee_limit(10_000_000)
    .build()
    .sign(priv_key)
)

print("Transaction Success : "+str(txn.broadcast().wait()))