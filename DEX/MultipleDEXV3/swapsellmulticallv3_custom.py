from web3 import Web3, HTTPProvider
import json
import time
import config

web3 = Web3(Web3.HTTPProvider(config.rpcurl))
chainId = int(config.chainid)

print("Swap Sell DEX V3 | Works Multiple DEX")

#connecting web3
if  web3.isConnected() == True:
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
tokenName = token_contract.functions.name().call()
tokenSymbol = token_contract.functions.symbol().call()
tokenDec = token_contract.functions.decimals().call()
wrapped = contractrouter.functions.WETH9().call()
contractwrapped = web3.eth.contract(address=wrapped, abi=config.tokenabi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH')
    #Get token balance account
    token_balance = token_contract.functions.balanceOf(sender).call() / (10**tokenDec)
    print('Token Balance' ,token_balance, tokenSymbol)
    
UpdateBalance()

print('')
inputamount = float(input(str("Enter Amount Of Token You Want To Sell : "))) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount = int(inputamount * (10**tokenDec))
deadline = int(time.time()) + 1000000

def ApproveToken():        
    #estimate gas limit approve
    gas_approve = token_contract.functions.approve(contract_router, config.apprv).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.getTransactionCount(sender)
    })
    gasApprove = web3.eth.estimateGas(gas_approve)

    #calculate transaction fee
    print('')
    print('Processing Approve Spender Token...')
    gasPrice = web3.fromWei(web3.eth.gasPrice, 'gwei')
    Caclfee = web3.fromWei(gasPrice*gasApprove, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH')

    #Approve
    Approve = token_contract.functions.approve(contract_router, config.apprv).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasApprove,
        'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.getTransactionCount(sender)
    })

    sign_approve = web3.eth.account.sign_transaction(Approve, senderkey)
    appvhash = web3.eth.send_raw_transaction(sign_approve.rawTransaction)

    #get transaction hash
    txidappv = str(web3.toHex(appvhash))
    print('')
    print('Transaction Success TX-ID Result...')
    print(txidappv)
    print('Approved Spender Token Wait 20 Second...')
    time.sleep(20)

def CallMulticall():
    weth_balance = contractwrapped.functions.balanceOf(contract_router).call()
    txSwap = contractrouter.encodeABI(fn_name="exactInputSingle", args=[(tokenaddr, wrapped, feepool, contract_router, amount, 0, 0)])
    txWETH = contractrouter.encodeABI(fn_name="unwrapWETH9", args=[weth_balance, sender])
    txCall = [txSwap, txWETH]  

    #estimate gas limit contract
    txEsGas = contractrouter.encodeABI(fn_name="exactInputSingle", args=[(tokenaddr, wrapped, feepool, contract_router, amount, 0, 0)])
    txEsGasCall = [txEsGas, txWETH]  

    gas_tx = contractrouter.functions.multicall(deadline, txEsGasCall).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.getTransactionCount(sender)
    })
    gasAmount = web3.eth.estimateGas(gas_tx)

    #calculate transaction fee
    print('')
    gasPrice = web3.fromWei(web3.eth.gasPrice, 'gwei')
    Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH')
    print('Processing Swap Sell :' ,inputamount ,tokenName, 'To ETH')

    token_tx = contractrouter.functions.multicall(deadline, txCall).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasAmount,
        'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.getTransactionCount(sender)
    })

    #sign the transaction
    sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
    #send transaction
    tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    #get transaction hash
    txid = str(web3.toHex(tx_hash))
    print('')
    print('Transaction Success TX-ID Result...')
    print(txid)

ApproveToken()    
CallMulticall()    
print('Update Current Balance In 30 Second...')
time.sleep(30)
print('')
UpdateBalance() #get latest balance