from web3 import Web3, HTTPProvider
import json
import logging
import datetime 
import threading
import asyncio
import requests
import time
import os
import sys
import ctypes
import pyperclip as pc

#bsc = "https://bsc-testnet.publicnode.com" #rpc bsctesnet custom #you can find rpc on chainlist.org
inputrpc = str(input("Input Url RPC/Node Blockchain Network : "))
web3 = Web3(Web3.HTTPProvider(inputrpc))
#chain_id = 97 #you can find chainid on chainlist.org
chainId = int(input("Input Chain ID Blockchain Network : "))

ctypes.windll.kernel32.SetConsoleTitleW("Auto Claim & Sell Presale On Launchpad AIO Blockchain Network")
print('')
print('Auto Claim & Sell Presale On Launchpad Pinksale AIO Blockchain Network')
print('This Support Only Blockchain Network Available On Launchpad Pinksale')
print('')

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

sender = web3.toChecksumAddress(input("Enter Your Address 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter Your Privatekey abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
contract_presale = web3.toChecksumAddress(input("Enter Contract Address Presale : "))
tokenaddr = web3.toChecksumAddress(input('Enter Token Address 0x...: '))
contract_router = web3.toChecksumAddress(input("Enter Contract Address Router DEX : "))
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price
#chainId = 56

presaleabi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Cancelled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"volume","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"total","type":"uint256"}],"name":"Claimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"volume","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"total","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Contributed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"liquidity","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Finalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"completed","type":"bool"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"KycUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"LiquidityWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"PoolUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"VestingTokenWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawnContribution","type":"event"},{"inputs":[{"internalType":"address[]","name":"users","type":"address[]"}],"name":"addWhitelistedUsers","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cancel","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"claimedOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"completedKyc","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contribute","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"contributionOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountInWei","type":"uint256"}],"name":"convert","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cycle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cycleReleasePct","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"distributePurchasedTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"distributeRefund","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"distributedType","type":"uint8"}],"name":"distributionCompleted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address payable","name":"to_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token_","type":"address"},{"internalType":"address","name":"to_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"endTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"finalize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"finishTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user_","type":"address"}],"name":"getContributionAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContributorCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"getContributors","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNumberOfWhitelistedUsers","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"distributedType","type":"uint8"}],"name":"getUndistributedIndexes","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getUpdatedState","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint8","name":"","type":"uint8"},{"internalType":"bool","name":"","type":"bool"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"startIndex","type":"uint256"},{"internalType":"uint256","name":"endIndex","type":"uint256"}],"name":"getWhitelistedUsers","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"governance","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"hardCap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[4]","name":"_addrs","type":"address[4]"},{"internalType":"uint256[2]","name":"_rateSettings","type":"uint256[2]"},{"internalType":"uint256[2]","name":"_contributionSettings","type":"uint256[2]"},{"internalType":"uint256[2]","name":"_capSettings","type":"uint256[2]"},{"internalType":"uint256[3]","name":"_timeSettings","type":"uint256[3]"},{"internalType":"uint256[2]","name":"_feeSettings","type":"uint256[2]"},{"internalType":"bool","name":"_useWhitelisting","type":"bool"},{"internalType":"uint256","name":"_liquidityPercent","type":"uint256"},{"internalType":"uint256","name":"_refundType","type":"uint256"},{"internalType":"string","name":"_poolDetails","type":"string"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_vcTgeReleasePct","type":"uint256"},{"internalType":"uint256","name":"_vcCycleReleasePct","type":"uint256"},{"internalType":"uint256","name":"_vcCycle","type":"uint256"}],"name":"initializeContributorVesting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_totalVestingTokens","type":"uint256"},{"internalType":"uint256","name":"_tgeLockDuration","type":"uint256"},{"internalType":"uint256","name":"_tgeReleasePct","type":"uint256"},{"internalType":"uint256","name":"_cycle","type":"uint256"},{"internalType":"uint256","name":"_cycleReleasePct","type":"uint256"}],"name":"initializeVesting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"isUserWhitelisted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liquidityBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liquidityListingRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liquidityLockDays","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liquidityPercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liquidityUnlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockId","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxContribution","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minContribution","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolDetails","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolState","outputs":[{"internalType":"enum BasePool.PoolState","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"purchasedOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"refundType","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"refundedOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"users","type":"address[]"}],"name":"removeWhitelistedUsers","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"router","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"governance_","type":"address"}],"name":"setGovernance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"use","type":"bool"}],"name":"setUseWhitelisting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"softCap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tgeLockDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tgeReleasePct","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tgeTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalClaimed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalRaised","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalRefunded","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalVestedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalVestingTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalVolumePurchased","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"completed_","type":"bool"}],"name":"updateCompletedKyc","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"details_","type":"string"}],"name":"updatePoolDetails","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"useWhitelisting","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"vcCycle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"vcCycleReleasePct","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"vcTgeReleasePct","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"withdrawCancelledTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawContribution","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawVestingToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"withdrawableContributorVestingTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdrawableTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')
router_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
tokenabi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
contractpresale = web3.eth.contract(address=contract_presale, abi=presaleabi)
contractrouter = web3.eth.contract(address=contract_router, abi=router_abi)
token_contract = web3.eth.contract(address=tokenaddr, abi=tokenabi)
tokenName = token_contract.functions.name().call()
tokenSymbol = token_contract.functions.symbol().call()
wrapped = contractrouter.functions.WETH().call()

#Claim presale
def ClaimPresale():
    #estimate gas limit contract
    nonce = web3.eth.getTransactionCount(sender)
    gas_tx = contractpresale.functions.claim().buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': nonce
    })
    gasAmount = web3.eth.estimateGas(gas_tx)

    #calculate transaction fee
    print('')
    gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
    Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')
    print('Processing Claim', tokenName, 'TOKEN')

    token_tx = contractpresale.functions.claim().buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasAmount,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': nonce
    })

    #sign the transaction
    sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
    #send transaction
    tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    #get transaction hash
    txid = str(web3.toHex(tx_hash))
    print('')
    print('Claimed Success TX-ID : ', txid)

#sell
def SellNow():
    nonce2 = web3.eth.getTransactionCount(sender)
    token_approve = token_contract.functions.balanceOf(sender).call()

    #estimate gas limit approve
    gas_approve = token_contract.functions.approve(contract_router, token_approve).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce2
    })
    gasApprove = web3.eth.estimateGas(gas_approve)

    #calculate transaction fee
    print('')
    print('Processing Approve Spender Token...')
    gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
    Caclfee = web3.fromWei(gasPrice*gasApprove, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')

    #Approve
    Approve = token_contract.functions.approve(contract_router, token_approve).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasApprove,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce2
    })

    sign_approve = web3.eth.account.sign_transaction(Approve, senderkey)
    web3.eth.send_raw_transaction(sign_approve.rawTransaction)
    print('Approved Spender Token Wait 5 Second...')
    time.sleep(5)
    print('')

    deadline = int(time.time()) + 1000000

    #estimate gas limit contract
    nonce3 = web3.eth.getTransactionCount(sender)
    gas_tx = contractrouter.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(token_approve, 0, [tokenaddr, wrapped], sender, deadline).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': nonce3
    })
    gasAmount = web3.eth.estimateGas(gas_tx)

    #calculate transaction fee
    print('')
    amountFromWei = web3.fromWei(token_approve, 'ether')
    gasPrice = web3.fromWei(web3.eth.gas_price, 'gwei')
    Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
    print('Transaction Fee :' ,Caclfee, 'ETH/BNB/MATIC/OTHER')
    print('Processing Swap Sell :' ,amountFromWei ,tokenName, 'TO ETH/BNB/MATIC/OTHER')

    token_tx = contractrouter.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(token_approve, 0, [tokenaddr, wrapped], sender, deadline).buildTransaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasAmount,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': nonce3
    })

    #sign the transaction
    sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
    #send transaction
    tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

    #get transaction hash
    txid = str(web3.toHex(tx_hash))
    print('')
    print('Transaction Success TX-ID Copied To Clipboard')
    print(txid)
    pc.copy(txid)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH/BNB/MATIC/OTHER')
    #Get token balance account
    token_balance = token_contract.functions.balanceOf(sender).call()
    balance_token = web3.fromWei(token_balance, 'ether')
    print('Token Balance' ,balance_token, tokenSymbol)
    
UpdateBalance()
print('Waiting For Finalized Presale...')
print("") #line break

def foundFinalized(event):
    try:
        print('Presale Has Been Finalized...')
        print('Processing Claim Presale')
        ClaimPresale()
        print('Wait 5 Second To Sell')
        time.sleep(5)
        SellNow()
        print('Update Current Balance In 10 Second...')
        time.sleep(10)
        print('')
        UpdateBalance() #get latest balance
        print('Will Exit Automatically In 5 Second...')
        time.sleep(5)
        exit()
        

    except:
        pass
        
async def finalizedLoop(event_filter, poll_interval):
    while True:
        try:
            for Finalized in event_filter.get_new_entries():
                foundFinalized(Finalized)
            await asyncio.sleep(poll_interval)
        except:
            pass
           
def listenForFinalized():
    event_filter = contractpresale.events.Finalized.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                finalizedLoop(event_filter, 0)))       
                # log_loop(block_filter, 2),
                # log_loop(tx_filter, 2)))
                 
    finally:
        # close loop to free up system resources
        #loop.close()
        #print("loop close")
        listenForFinalized()

        #beware of valueerror code -32000 which is a glitch. make it ignore it and go bakc to listening

listenForFinalized()

input("")