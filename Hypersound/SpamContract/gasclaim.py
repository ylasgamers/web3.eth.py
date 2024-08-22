from web3 import Web3, HTTPProvider
import json
import time

print("Gas Claim From Smart Contract")
print("Only Owner Can Gas Claim")
print("")
web3 = Web3(Web3.HTTPProvider("https://rpc.blast.io"))

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()
           
contractabi = json.loads('[{"inputs": [{"internalType": "bool","name": "isAll","type": "bool"},{"internalType": "bool","name": "isMax","type": "bool"}],"name": "claimGas","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
contractaddr = web3.to_checksum_address("input_deployed_contract_address")
contract = web3.eth.contract(address=contractaddr, abi=contractabi)

def claimGasAll(sender, senderkey):
    try:
        #estimate gas limit contract
        gasAmount = contract.functions.claimGas(True, False).estimate_gas({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })

        gas_tx = contract.functions.claimGas(True, False).build_transaction({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })
        #sign the transaction
        sign_txn = web3.eth.account.sign_transaction(gas_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

        #get transaction hash
        txid = str(web3.to_hex(tx_hash))
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print('')
        print(f'Claim GasAll Success!')
        print(f'TX-ID : {txid}')
        print('')
    except Exception as e:
        print(f"Error : {e}")
        if str(e) == str("('execution reverted', 'no data')"):
            claimGasAll(sender, senderkey)
        else:
            print('')
        if str(e) == str("{'code': -32000, 'message': 'already known'}"):
            claimGasAll(sender, senderkey)
        else:
            print('')

def claimGasMax(sender, senderkey):
    try:
        #estimate gas limit contract
        gasAmount = contract.functions.claimGas(False, True).estimate_gas({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })

        gas_tx = contract.functions.claimGas(False, True).build_transaction({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender)
        })
        #sign the transaction
        sign_txn = web3.eth.account.sign_transaction(gas_tx, senderkey)
        #send transaction
        tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

        #get transaction hash
        txid = str(web3.to_hex(tx_hash))
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print('')
        print(f'Claim GasMax Success!')
        print(f'TX-ID : {txid}')
        print('')
    except Exception as e:
        print(f"Error : {e}")
        if str(e) == str("('execution reverted', 'no data')"):
            claimGasMax(sender, senderkey)
        else:
            print('')
        if str(e) == str("{'code': -32000, 'message': 'already known'}"):
            claimGasMax(sender, senderkey)
        else:
            print('')

senderkey = input('Input Privatekey EVM Address Blast : ')
sender = web3.eth.account.from_key(senderkey)
print('0. Claim GasAll')
print('1. Claim GasMax')
choose = input('Choose : ')
if 0 == int(choose):
    claimGasAll(sender.address, sender.key)
else:
    claimGasMax(sender.address, sender.key)