from web3 import Web3, HTTPProvider
import json
import time
import config

web3 = Web3(Web3.HTTPProvider(config.rpcurl))
chainId = int(config.chainid)

print("Swap Sell DEX V3 | Works Multiple DEX")

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

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
inputamount = float(input(str("Enter Amount Of Token You Want To Sell : "))) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount = int(inputamount * (10**tokenDec))
deadline = int(time.time()) + 1000000

def ApproveToken():        
    #estimate gas limit approve
    gas_approve = token_contract.functions.approve(contract_router, config.apprv).build_transaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.get_transaction_count(sender)
    })
    gasApprove = web3.eth.estimate_gas(gas_approve)

    #calculate transaction fee
    print('')
    print('Processing Approve Spender Token...')
    gasPrice = web3.from_wei(web3.eth.gas_price, 'gwei')
    Caclfee = web3.from_wei(gasPrice*gasApprove, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH')

    #Approve
    Approve = token_contract.functions.approve(contract_router, config.apprv).build_transaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasApprove,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.get_transaction_count(sender)
    })

    sign_approve = web3.eth.account.sign_transaction(Approve, senderkey)
    appvhash = web3.eth.send_raw_transaction(sign_approve.rawTransaction)

    #get transaction hash
    txidappv = str(web3.to_hex(appvhash))
    print('')
    print('Transaction Success TX-ID Result...')
    print(txidappv)
    print('Approved Spender Token Wait 20 Second...')
    time.sleep(20)

def CallMulticall():
    weth_balance = contractwrapped.functions.balanceOf(contract_router).call()
    txSwap = contractrouter.encode_abi(fn_name="exactInputSingle", args=[(tokenaddr, wrapped, feepool, contract_router, amount, 0, 0)])
    txWETH = contractrouter.encode_abi(fn_name="unwrapWETH9", args=[weth_balance, sender])
    txCall = [txSwap, txWETH]  

    #estimate gas limit contract
    txEsGas = contractrouter.encode_abi(fn_name="exactInputSingle", args=[(tokenaddr, wrapped, feepool, contract_router, amount, 0, 0)])
    txEsGasCall = [txEsGas, txWETH]  

    gas_tx = contractrouter.functions.multicall(deadline, txEsGasCall).build_transaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.get_transaction_count(sender)
    })
    gasAmount = web3.eth.estimate_gas(gas_tx)

    #calculate transaction fee
    print('')
    gasPrice = web3.from_wei(web3.eth.gas_price, 'gwei')
    Caclfee = web3.from_wei(gasPrice*gasAmount, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH')
    print('Processing Swap Sell :' ,inputamount ,tokenName, 'To ETH')

    token_tx = contractrouter.functions.multicall(deadline, txCall).build_transaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasAmount,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
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

apprvcheck = int(token_contract.functions.allowance(sender, contract_router).call())
if apprvcheck > amount:
    print('Already Approved! Processing Sell Token...')
    CallMulticall()    
    print('Update Current Balance In 30 Second...')
    time.sleep(30)
    print('')
    UpdateBalance() #get latest balance
else:
    ApproveToken()
    print('Approved! Processing Sell Token...')
    CallMulticall()    
    print('Update Current Balance In 30 Second...')
    time.sleep(30)
    print('')
    UpdateBalance() #get latest balance
