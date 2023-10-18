# OS Tested
- Windows 7/10/11
- Android 7 - 12

# List
- Send Single Transaction
- Send Token/TRC20 Token Sigle Transaction
- Multisend Transaction / Multisend Token/TRC20
- Generate Vanity TRON Privatekey / Mnemonic
- Deploy Contract/Standart Token

# Blockchain List
- TRON Testnet (Nile) & Mainnet
  
# Requirements
- Need Python 3.7.2
```
python -m pip install --upgrade pip
python -m pip install tronpy
python -m pip install tronpy[mnemonic]
python -m pip install eth_account==0.5.9
python -m pip install pyperclip==1.8.2
python -m pip install requests==2.27.1
python -m pip install py-solc-x
```
- For Android Using Termux Download [Here](https://f-droid.org/repo/com.termux_118.apk) [Tutorial](https://mega.nz/file/Y1g0xKDL#lyusdWOXV1YG38ikxQ2pr7fADXPFkPEtoYHNgqAo-mY)
- After Install You Need Setting Allow App Permission Storage/Files & Media
```
pkg update && upgrade
pkg install tur-repo
pkg install python-is-python3.7
pip install pyperclip==1.8.2
pip install requests==2.27.1
pip install tronpy
pip install tronpy[mnemonic]
pip install py-solc-x
```
- How Run ? Example You Put yourfile.py On Folder /sdcard/Download
```
cd /sdcard/Download enter
python yourfile.py enter
```
