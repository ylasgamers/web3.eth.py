from tronpy import Tron
from tronpy.keys import PrivateKey

#client = Tron()  # The default provider, mainnet
client = Tron(network='nile')  # The Nile Testnet is preset

print("")
print("Send Token/TRC20 Token In Tron")
print("If You Using Mainnet Please Change client = Tron(network='nile') To client = Tron()")
print("")

sender = input(str("Enter Your Address As Sender : "))
pvkey = input("Enter Your PrivateKey As Sender : ")
recipient = input(str("Enter Address As Recipient : "))
tokenaddr = input(str("Enter Token Address : "))
priv_key = PrivateKey(bytes.fromhex(pvkey))
inputamount = float(input("Enter Amount Of You Want To Send : "))
contract = client.get_contract(tokenaddr)
dec_token = contract.functions.decimals()
amount = int(float((10**0) * inputamount))

def UpdateBalance():
    balance = client.get_account_balance(sender)
    symb_token = contract.functions.symbol()
    print("")
    print('Your Balance : ' ,balance, 'TRX')
    print('Token Balance : ',contract.functions.balanceOf(sender), str(symb_token))
    print("")
    
UpdateBalance()

txn = (
    contract.functions.transfer(recipient, amount)
    .with_owner(sender)
    .fee_limit(20_000_000)
    .build()
    .sign(priv_key)
)

print("Transaction Success : "+str(txn.broadcast().wait()))