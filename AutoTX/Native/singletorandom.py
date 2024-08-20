from web3 import Web3, HTTPProvider
import json
import time
import secrets
import random

print("Transfer Native Balance EVM Multiple Chain")
print("From Single To Random New Address")
print("")
web3 = Web3(Web3.HTTPProvider(input("Input RPC Url : ")))

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()

def TransferNative(sender, senderkey, recipient, amount):
    try:
        #estimate gas limit contract
        gas_tx = {
            'chainId': web3.eth.chain_id,
            'from': sender,
            'to': recipient,
            'value': web3.to_wei(amount, 'ether'),
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        }
        gasAmount = web3.eth.estimate_gas(gas_tx)

        auto_tx = {
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gas': gasAmount,
            'to': recipient,
            'value': web3.to_wei(amount, 'ether'),
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        }

        fixamount = '%.18f' % float(amount)
        #sign the transaction
        sign_txn = web3.eth.account.sign_transaction(auto_tx, senderkey)
        #send transaction
        print(f'Processing Send {fixamount} Native To Random New Address : {recipient} ...')
        tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

        #get transaction hash
        txid = str(web3.to_hex(tx_hash))
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print('')
        print(f'Send {fixamount} Native To Random New Address : {recipient} Success!')
        print(f'TX-ID : {txid}')
    except Exception as e:
        print(f"Error : {e}")
    
loop = input("How Many You Want To Transaction ? : ")
senderkey = input("Input Your Privatekey Main EVM Address : ")
for i in range(0,int(loop)):
    amount = random.uniform(0.00001, 0.0001)
    sender = web3.eth.account.from_key(senderkey)
    print("")
    print("Processing Generate Random EVM Address...")
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    recipient = web3.eth.account.from_key(private_key)
    print("")
    TransferNative(sender.address, senderkey, recipient.address, amount)