import secrets
import sha3
from web3 import Web3
from solcx import compile_standard, install_solc
install_solc('0.8.0')

with open("msg.sol", "r") as file:
    sol_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"msg.sol": {"content": sol_file}},
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

# get bytecode
bytecode = compiled_sol["contracts"]["msg.sol"]["MessageContract"]["evm"]["bytecode"]["object"]# get abi

#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()

# Initialize Web3 (you may not need this for salt generation, but it's useful for address computation)
web3 = Web3()

# Function to generate a random salt
def generate_random_salt():
    # Generate a random 32-byte value
    return secrets.token_hex(32)  # Returns a 64-character hexadecimal string

def compute_create2_address(factory_address, salt, bytecode):
    """
    Computes the address of a contract deployed using CREATE2.
    :param factory_address: Address of the factory contract.
    :param salt: Salt used for deployment.
    :param bytecode: Bytecode of the contract to be deployed.
    :return: Computed address of the deployed contract.
    """
    # Encode inputs to bytes32
    factory_address_bytes = web3.to_bytes(hexstr=factory_address)
    salt_bytes = web3.to_bytes(hexstr=salt)
    bytecode_bytes = web3.to_bytes(hexstr=bytecode)

    # Create a new Keccak-256 hash object
    k = sha3.keccak_256()
    k.update(b'\xFF' + factory_address_bytes + salt_bytes + sha3.keccak_256(bytecode_bytes).digest())
    # Compute the address
    create2_hash = k.digest()
    #print(web3.to_hex(create2_hash))
    
    # Extract the last 20 bytes of the hash
    return web3.to_hex(create2_hash[-20:])

while True:
    random_salt = generate_random_salt()
    filter_salt = random_salt[40:]
    deployer = '0000000000000000000000000000000000000000' # Replace with deployer/your address/zero address without 0x
    salt = deployer+filter_salt

    factory_address = '0x0000000000FFe8B47B3e2130213B802212439497'  # Replace with the address of the factory contract

    # Compute the contract address
    computed_address = compute_create2_address(factory_address, salt, bytecode)
    expect_spesificaddr = '0x000' #custom spesific contract address
    computed_address_filter = computed_address[:len(expect_spesificaddr)]
    if expect_spesificaddr == computed_address_filter:
        print(f"Expect contract address found! : {computed_address}")
        print(f"Generated salt : 0x{salt}")
        log(f"Expect contract address found! : {computed_address}")
        log(f"Generated salt : 0x{salt}")
        log(f"Bytecode : 0x{bytecode}")
        log('---------------------------------------')
        exit()
    else:
        print(f"Expect contract address not found! , Skipping...")
