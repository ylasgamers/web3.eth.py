from web3 import Web3, HTTPProvider
import json
import time

print("Auto Miner Custom Using Smart Contract")
print("Every 1 Minutes")
print("")
web3 = Web3(Web3.HTTPProvider("https://rpc.blast.io"))

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()
           
contractabi = json.loads('[{"inputs": [{"internalType": "uint256","name": "custom","type": "uint256"}],"name": "MinerCustom","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
contractaddr = web3.to_checksum_address("input_deployed_contract_address")
contract = web3.eth.contract(address=contractaddr, abi=contractabi)

def Miner(sender, senderkey, total):
    try:
        #estimate gas limit contract
        gasAmount = contract.functions.MinerCustom(total).estimate_gas({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })

        mine_tx = contract.functions.MinerCustom(total).build_transaction({
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
        print('')
        print(f'Mine Total : {str(total)} Success!')
        print(f'TX-ID : {txid}')
        print('')
        time.sleep(60) # 1 minutes
    except Exception as e:
        print(f"Error : {e}")
        if str(e) == str("('execution reverted', 'no data')"):
            Miner(sender, senderkey, total)
        else:
            print('')
        if str(e) == str("{'code': -32000, 'message': 'already known'}"):
            Miner(sender, senderkey, total)
        else:
            print('')

senderkey = input('Input Privatekey EVM Address Blast : ')
total = input('How Many You Want To Mine ? Ex 10/20/30/Other : ')
while True:
    sender = web3.eth.account.from_key(senderkey)
    print("")
    Miner(sender.address, sender.key, total)