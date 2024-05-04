from web3 import Web3
from eth_account import Account
import random

words = []
with open("words.txt", "r") as file:
    for line in file:
        line = line.strip()
        words.append(line)


for i in range(10000000):
    # Anahtar kelimeler
    mnemonic = ""
    for _ in range(12):
        mnemonic += random.choice(words) + " "

    Account.enable_unaudited_hdwallet_features()

    web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_API_KEY'))

    try:
        account = Account.from_mnemonic(mnemonic.strip())
        wallet_address = account.address

        # Cüzdan bakiyesini kontrol etme
        balance = web3.eth.get_balance(wallet_address)

        print(f"{i}cüzdan bulundu")
        if(balance != 0):
            with open("results.txt", "a") as file:
                file.write(f"{mnemonic}\naddress: {wallet_address}\nbalance(wei): {balance}\n\n\n")
    except:
        print(f"{i}cüzdan yok")
        continue
