from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair
from solathon.utils import clean_response, lamport_to_sol, sol_to_lamport
import time

#client = Client("https://rpc.solscan.com") #mainnet
#client = Client("https://api.testnet.solana.com") #testnetㅤ
client = Client("https://api.devnet.solana.com") #devnet

# Requires you to have some SOLs to pay for transaction fees
sender = PublicKey(input("Input Your Publickey/Address Sol : "))
keysender = Keypair.from_private_key(input("Input Your Privatekey : "))
receiver = PublicKey(input("Input Receiver Publickey/Address Sol : "))
inputval = float(input("Input Amount Of You Want To Send : "))
value = sol_to_lamport(inputval)

def GetBalance():
    print("")
    balance = client.get_balance(sender)
    tosol = lamport_to_sol(clean_response(balance))
    print("Your Balance : ",tosol, "SOL")
    print("")
GetBalance()

instruction = transfer(
    from_public_key=keysender.public_key,
    to_public_key=receiver, 
    lamports=int(value) #https://www.solconverter.com/
)

transaction = Transaction(instructions=[instruction], signers=[keysender])

result = client.send_transaction(transaction)
print("Transaction ID : ", clean_response(result))
