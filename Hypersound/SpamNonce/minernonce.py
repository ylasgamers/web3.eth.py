from web3 import Web3, HTTPProvider
import json
import time

print("Auto Miner Hypersound Spam Nonce")
print("")
web3 = Web3(Web3.HTTPProvider("https://rpc.blast.io"))

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()
           
tokenabi = json.loads('[{"inputs": [{"internalType": "bytes","name": "extraData","type": "bytes"}],"name": "mine","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
tokenaddr = web3.to_checksum_address("0x7E82481423B09c78e4fd65D9C1473a36E5aEd405")
tokenctr = web3.eth.contract(address=tokenaddr, abi=tokenabi)

def Miner(sender, senderkey):
    try:
        for i in range(0,99999):
            #estimate gas limit contract
            gasAmount = tokenctr.functions.mine(bytes(0)).estimate_gas({
                'chainId': web3.eth.chain_id,
                'from': sender,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(sender)+i
            })

            mine_tx = tokenctr.functions.mine(bytes(0)).build_transaction({
                'chainId': web3.eth.chain_id,
                'from': sender,
                'gas': gasAmount,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(sender)+i
            })
            #sign the transaction
            sign_txn = web3.eth.account.sign_transaction(mine_tx, senderkey)
            #send transaction
            tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

            #get transaction hash
            txid = str(web3.to_hex(tx_hash))
            print('')
            print(f'Mine Success!')
            print(f'TX-ID : {txid}')
            print('')
    except Exception as e:
        print(f"Error : {e}")
        if str(e) == str("('execution reverted', 'no data')"):
            Miner(sender, senderkey)
        else:
            print('')
        if str(e) == str("{'code': -32000, 'message': 'already known'}"):
            Miner(sender, senderkey)
        else:
            print('')

senderkey = input('Input Privatekey EVM Address Blast : ')
while True:
    sender = web3.eth.account.from_key(senderkey)
    print("")
    Miner(sender.address, sender.key)
