from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

#client = Client("https://rpc.solscan.com") #mainnet
#client = Client("https://api.testnet.solana.com") #testnetㅤ
client = Client("https://api.devnet.solana.com") #devnet

# Requires you to have some SOLs to pay for transaction fees
sender = Keypair.from_private_key(input("Input Your Privatekey : "))
receiver = PublicKey(input("Input Your Publickey/Address Sol : "))

instruction = transfer(
    from_public_key=sender.public_key,
    to_public_key=receiver, 
    lamports=10000000 #https://www.solconverter.com/
)

transaction = Transaction(instructions=[instruction], signers=[sender])

result = client.send_transaction(transaction)
print("Transaction response: ", result)
