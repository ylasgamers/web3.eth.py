- You Need Deploy SmartContract First With deploy.py
- After Deploy SmartContract You Will Get Contract Address, Input In Line 28 On File hypercustom.py Like Below
```
Before : contractaddr = web3.to_checksum_address("input_deployed_contract_address")
After : contractaddr = web3.to_checksum_address("0x20E5874890ac7eaF252E07393aE2EAC6ce92e909") #Example
```
- If You Lucky, Because Random Pick Winner Participant Miner Address, Your Deployed SmartContract Will Get Reward HYPERS TOKEN
- You Can Withdraw Token From Your Deployed SmartContract Using File wdtoken.py
- Also You Can Claim GasMax / GasAll From Your Spend Gas Fees Transaction On Your Deployed SmartContract Using File gasclaim.py
