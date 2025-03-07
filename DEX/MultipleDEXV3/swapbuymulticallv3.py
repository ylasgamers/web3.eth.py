from web3 import Web3, HTTPProvider
import json
import time
import config

web3 = Web3(Web3.HTTPProvider(config.rpcurl))
chainId = web3.eth.chain_id
print("Swap Buy DEX V3 | Works Multiple DEX")

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()

sender = config.sender
senderkey = config.pvkey
tokenaddr = config.tokenaddr
contract_router = config.routeraddr
feepool = int(config.feepool)
#============================================================================
contractrouter = web3.eth.contract(address=contract_router, abi=config.router_abi)
token_contract = web3.eth.contract(address=tokenaddr, abi=config.tokenabi)
contractfactory = web3.eth.contract(address=contractrouter.functions.factory().call(), abi=config.factory_abi)
tokenName = token_contract.functions.name().call()
tokenSymbol = token_contract.functions.symbol().call()
tokenDec = token_contract.functions.decimals().call()
wrapped = contractrouter.functions.WETH9().call()
getpool = contractfactory.functions.getPool(wrapped, tokenaddr, feepool).call()
contractwrapped = web3.eth.contract(address=wrapped, abi=config.tokenabi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.from_wei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH')
    #Get token balance account
    token_balance = token_contract.functions.balanceOf(sender).call() / (10**tokenDec)
    print('Token Balance' ,token_balance, tokenSymbol)
    
UpdateBalance()

print('Search/Checking Pool...')
if config.nulladdr == getpool:
    print("Pool Not Found Or Created/Try Change Fee Pool On Config")
    exit()
else:
    print("Pool Found! With Address : ",getpool)

print('Liquidity Checking...')
lpcheck = contractwrapped.functions.balanceOf(getpool).call()    
if 0 < lpcheck:
    print('Liquidity Found! With', lpcheck / 10**contractwrapped.functions.decimals().call(), contractwrapped.functions.symbol().call())
else:
    print('Liquidity Empty!')
    exit()

print('')
inputamount = float(input("Enter Amount Of You Want To Buy [ETH] : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount = web3.to_wei(float(inputamount), 'ether')
deadline = int(time.time()) + 1000000

txSwap = contractrouter.encode_abi(fn_name="exactInputSingle", args=[(wrapped, tokenaddr, feepool, sender, amount, 0, 0)])
txCall = [txSwap]

#estimate gas limit contract
gasAmount = contractrouter.functions.multicall(deadline, txCall).estimate_gas({
    'chainId': chainId,
    'from': sender,
    'value': amount,
    'gasPrice': web3.eth.gas_price,
    'nonce': web3.eth.get_transaction_count(sender)
})

#calculate transaction fee
print('')
amountFromWei = web3.from_wei(amount, 'ether')
gasPrice = web3.from_wei(web3.eth.gas_price, 'gwei')
Caclfee = web3.from_wei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH')
print('Processing Swap Buy :' ,amountFromWei, 'ETH For Token' ,tokenName)

token_tx = contractrouter.functions.multicall(deadline, txCall).build_transaction({
    'chainId': chainId,
    'from': sender,
    'value': amount,
    'gas': gasAmount,
    'gasPrice': web3.eth.gas_price,
    'nonce': web3.eth.get_transaction_count(sender)
})

#sign the transaction
sign_txn = web3.eth.account.sign_transaction(token_tx, senderkey)
#send transaction
tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

#get transaction hash
txid = str(web3.to_hex(tx_hash))
print('')
print('Transaction Success TX-ID Result...')
print(txid)
print('Update Current Balance In 30 Second...')
time.sleep(30)
print('')
UpdateBalance() #get latest balance
