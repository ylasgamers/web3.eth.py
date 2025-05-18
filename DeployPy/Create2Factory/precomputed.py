from web3 import Web3
from solcx import compile_standard, install_solc
import hashlib
import secrets
import json
install_solc('0.8.0')

#log to txt file
def log(txt):
    f = open('precomputed_result.txt', "a")
    f.write(txt + '\n')
    f.close()

with open("msg.sol", "r") as file:
    deploy_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"msg.sol": {"content": deploy_file}},
        "settings": {
             "optimizer": {
             "enabled": bool(True),
             "runs": 200
            },
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] # output needed to interact with and deploy contract 
                }
            }
        },
    },
    solc_version="0.8.0",
)

#your contract bytecode
bytecode = compiled_sol["contracts"]["msg.sol"]["MessageContract"]["evm"]["bytecode"]["object"]

web3 = Web3()

# Calculate the address where the contract will be deployed
def compute_create2_address(factory, salt, bytecode):
    factory_bytes = bytes.fromhex(factory[2:])
    salt_bytes = bytes.fromhex(salt[2:])
    bytecode_hash = web3.keccak(bytes.fromhex(bytecode))
    create2_hash = web3.keccak(b'\xff' + factory_bytes + salt_bytes + bytecode_hash)
    return web3.to_checksum_address(create2_hash[-20:])

while True:
    factory_addr = web3.to_checksum_address('0x0000000000FFe8B47B3e2130213B802212439497') #create2 factory
    salt = f'0x0000000000000000000000000000000000000000{secrets.token_hex(12)}' #random salt
    #sender = web3.to_checksum_address('0xyour_address')
    #salt = f'{sender}{secrets.token_hex(12)}' #random salt with add your address as salt
    precomputed_address = '0x000' #custom precomputed address
    computed_address = compute_create2_address(factory_addr, salt, bytecode)
    precomputed_address_filter = computed_address[:len(precomputed_address)]
    if precomputed_address_filter == precomputed_address:
        print(f'Expectation Address Found! : {computed_address}')
        print(f'Salt : {salt.lower()}')
        print(f'initializationCode/bytecode : Saved On precomputed_result.txt')
        log(f'Address : {computed_address}')
        log(f'Salt : {salt.lower()}')
        log(f'initializationCode/bytecode : 0x{bytecode}')
        log(f'--------------------------------------------------')
        exit()
    else:
        print(f'Expectation Address Not Found! Skip...')
