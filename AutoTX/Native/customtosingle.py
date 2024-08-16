from web3 import Web3, HTTPProvider
import json
import time
import secrets
import random

print("Transfer Native Balance EVM Multiple Chain")
print("Transfer All Native Balance From Custom/Spesific Address To Single Address")
print("Make Sure Already Input PrivateKey Custom/Spesific Address On pvkeylist.txt !")
print("")
web3 = Web3(Web3.HTTPProvider(input("Input RPC Url : ")))

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()

def TransferNative(sender, senderkey, recipient):
    try:
        gasPrice = web3.eth.gas_price
        #estimate gas limit contract
        gas_tx = {
            'chainId': web3.eth.chain_id,
            'from': sender,
            'to': recipient,
            'value': web3.to_wei(0, 'ether'),
            'gasPrice': gasPrice,
            'nonce': web3.eth.get_transaction_count(sender)
        }
        gasAmount = web3.eth.estimate_gas(gas_tx)
        
        totalfee = web3.from_wei(gasPrice*gasAmount, 'gwei')
        mainbalance = web3.from_wei(web3.eth.get_balance(sender), 'ether')
        totalsend = mainbalance - totalfee

        auto_tx = {
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gas': gasAmount,
            'to': recipient,
            'value': web3.to_wei(totalsend, 'ether'),
            'gasPrice': gasPrice,
            'nonce': web3.eth.get_transaction_count(sender)
        }

        fixamount = '%.18f' % float(totalsend)
        #sign the transaction
        sign_txn = web3.eth.account.sign_transaction(auto_tx, senderkey)
        #send transaction
        print(f'Processing Send {fixamount} Native From {sender} To Single Address : {recipient} ...')
        tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

        #get transaction hash
        txid = str(web3.to_hex(tx_hash))
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print('')
        print(f'Send {fixamount} Native From {sender} To Single Address : {recipient} Success!')
        print(f'TX-ID : {txid}')
    except Exception as e:
        print(f"Error : {e}")
   
recipientaddr = input("Input Recipient Main EVM Address : ")
with open('pvkeylist.txt', 'r') as file:
    local_data = file.read().splitlines()
    for pvkeylist in local_data:
        sender = web3.eth.account.from_key(pvkeylist)
        recipient = web3.to_checksum_address(recipientaddr)
        print("")
        TransferNative(sender.address, sender.key, recipient)