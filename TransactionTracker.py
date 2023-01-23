import requests
import json

# Replace with the address of the whale wallet you want to track
wallet_address = '0x123...'

# Helper function to get the transactions for a given wallet address
def get_transactions(address):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}'
    response = requests.get(url)
    return json.loads(response.text)['result']

# Helper function to get the balance of a given wallet address
def get_balance(address):
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}'
    response = requests.get(url)
    return int(json.loads(response.text)['result']) / 1e18

# Get the current balance of the wallet
current_balance = get_balance(wallet_address)

# Get the transactions for the wallet
transactions = get_transactions(wallet_address)

# Iterate through the transactions to identify buys, sells, DEX swaps, and CEX swaps
for tx in transactions:
    if tx['to'] == wallet_address:
        print(f'Buy: {tx["value"]/1e18} ETH at {tx["timeStamp"]}')
    elif tx['from'] == wallet_address:
        print(f'Sell: {tx["value"]/1e18} ETH at {tx["timeStamp"]}')
    elif tx['input'].startswith('0x'):
        print(f'DEX Swap: {tx["value"]/1e18} ETH at {tx["timeStamp"]}')
    else:
        print(f'CEX Swap: {tx["value"]/1e18} ETH at {tx["timeStamp"]}')
