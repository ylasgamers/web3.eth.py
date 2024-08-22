from web3 import Web3, HTTPProvider
import json
import time

print("Withdraw Token From Smart Contract")
print("Only Owner Can Withdraw Token")
print("")
web3 = Web3(Web3.HTTPProvider("https://rpc.blast.io"))

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()
           
contractabi = json.loads('[{"inputs": [{"internalType": "address","name": "token","type": "address"},{"internalType": "address","name": "recipient","type": "address"}],"name": "withdrawToken","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
contractaddr = web3.to_checksum_address("input_deployed_contract_address")
contract = web3.eth.contract(address=contractaddr, abi=contractabi)

def WDToken(sender, senderkey):
    try:
        tokenaddr = web3.to_checksum_address('0x7E82481423B09c78e4fd65D9C1473a36E5aEd405')
        #estimate gas limit contract
        gasAmount = contract.functions.withdrawToken(tokenaddr, sender).estimate_gas({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })

        wd_tx = contract.functions.withdrawToken(tokenaddr, sender).build_transaction({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })
        #sign the transaction
        sign_txn = web3.eth.account.sign_transaction(wd_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

        #get transaction hash
        txid = str(web3.to_hex(tx_hash))
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print('')
        print(f'Withdraw Success!')
        print(f'TX-ID : {txid}')
        print('')
    except Exception as e:
        print(f"Error : {e}")
        if str(e) == str("('execution reverted', 'no data')"):
            WDToken(sender, senderkey)
        else:
            print('')
        if str(e) == str("{'code': -32000, 'message': 'already known'}"):
            WDToken(sender, senderkey)
        else:
            print('')

senderkey = input('Input Privatekey EVM Address Blast : ')
sender = web3.eth.account.from_key(senderkey)
print("")
WDToken(sender.address, sender.key)