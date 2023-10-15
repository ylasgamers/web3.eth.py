from tronpy import Tron
import tronpy
import time

client = Tron()  # The default provider, mainnet
#client = Tron(network="nile")  # The Nile Testnet is preset

#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()

print("Generate Random Tron Address From PrivateKey")
priv = tronpy.keys.PrivateKey.random()
privatekey = client.generate_address(priv)
print("Address, PrivateKey, PublicKey : ",privatekey)
log(str(privatekey))
log('=================================================================================')
print('Your Address & Privatekey Logged To vanityprivatekey.log.txt')
print('Will Close Automatically In 30 Second...')
time.sleep(30)