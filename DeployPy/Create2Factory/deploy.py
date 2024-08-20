from web3 import Web3, HTTPProvider
import json

web3 = Web3(Web3.HTTPProvider("https://1.rpc.thirdweb.com")) #Replace with rpc some chain

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()
           
create2abi = json.loads('[{"constant":true,"inputs":[{"name":"deploymentAddress","type":"address"}],"name":"hasBeenDeployed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"salt","type":"bytes32"},{"name":"initializationCode","type":"bytes"}],"name":"safeCreate2","outputs":[{"name":"deploymentAddress","type":"address"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"salt","type":"bytes32"},{"name":"initCode","type":"bytes"}],"name":"findCreate2Address","outputs":[{"name":"deploymentAddress","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"salt","type":"bytes32"},{"name":"initCodeHash","type":"bytes32"}],"name":"findCreate2AddressViaHash","outputs":[{"name":"deploymentAddress","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
create2addr = web3.to_checksum_address("0x0000000000FFe8B47B3e2130213B802212439497")
create2contract = web3.eth.contract(address=create2addr, abi=create2abi)

def create2(sender, senderkey, amount, salt, bytecode):
    try:
        gasPrice = web3.eth.gas_price
        nonce = web3.eth.get_transaction_count(sender)
        resultaddr = create2contract.functions.findCreate2Address(salt, bytecode).call()
        #estimate gas limit contract
        gasAmount = create2contract.functions.safeCreate2(salt, bytecode).estimate_gas({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'value': web3.to_wei(amount, 'ether'),
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        create2_tx = create2contract.functions.safeCreate2(salt, bytecode).build_transaction({
            'chainId': web3.eth.chain_id,
            'from': sender,
            'gas': gasAmount,
            'value': web3.to_wei(amount, 'ether'),
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        #sign the transaction
        sign_txn = web3.eth.account.sign_transaction(create2_tx, senderkey)
        #send transaction
        print(f'Processing Deploying With Spesific Address {resultaddr}')
        tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

        #get transaction hash
        txid = str(web3.to_hex(tx_hash))
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print('')
        print(f'Success! Deploying With Spesific Address {resultaddr}')
        print(f'TX-ID : {txid}')
        print('')
    except Exception as e:
        print(f"Error : {e}")

sender = web3.eth.account.from_key('deployer_pvkey')
salt = 0x0 #Replace with salt
bytecode = 0x0 #Replace with bytecode smartcontract
create2(sender.address, sender.key, 0, salt, bytecode)
