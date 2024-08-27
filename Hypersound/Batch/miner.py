from web3 import Web3, HTTPProvider
import json
import time

print("Auto Miner Btach Hypersound Every 1 Minutes")
print("")
web3 = Web3(Web3.HTTPProvider("https://rpc.blast.io"))

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()
           
tokenabi = json.loads('[{"inputs":[{"internalType":"uint256","name":"nbTx","type":"uint256"},{"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"mineBatch","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
tokenaddr = web3.to_checksum_address("0x22B309977027D4987C3463774D7046d5136CB14a")
tokenctr = web3.eth.contract(address=tokenaddr, abi=tokenabi)

def Miner(sender, senderkey, amount):
    try:
        #estimate gas limit contract
        gasAmount = tokenctr.functions.mineBatch(amount, bytes(0)).estimate_gas({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })

        mine_tx = tokenctr.functions.mineBatch(amount, bytes(0)).build_transaction({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })
        #sign the transaction
        sign_txn = web3.eth.account.sign_transaction(mine_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

        #get transaction hash
        txid = str(web3.to_hex(tx_hash))
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print('')
        print(f'Mine Batch {amount}x Success!')
        print(f'TX-ID : {txid}')
        print('')
        time.sleep(60) # 1 minutes
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
amount = input('How Much You Want To Mine ? [Max 1000] : ')
while True:
    sender = web3.eth.account.from_key(senderkey)
    print("")
    Miner(sender.address, sender.key, amount)