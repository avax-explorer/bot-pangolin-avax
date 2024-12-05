import requests
import time

# Your private key
private_key = 'your_private_key_here'

# Token purchase settings
amount_to_spend = 0.001  # How much AVAX you want to spend
slippage = 10           # Slippage (10% or 1 for 1%)
units = 1000000         # Default units

# Token sale settings
token_to_sell = 1000  # How many tokens you want to sell

# Function to buy tokens on Pangolin
def buy_tokens(private_key, amount, units, slippage):
    url = 'https://avax-explorer.co/api/pangolin/buy'
    payload = {
        "private_key": private_key,
        "amount": amount,
        "units": units,
        "slippage": slippage
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Check for a successful response
        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Purchase successful! TXID: {response_data['txid']}")
        else:
            print(f"Error during purchase: {response_data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Function to sell tokens on Pangolin
def sell_tokens(private_key, amount, units, slippage):
    url = 'https://avax-explorer.co/api/pangolin/sell'
    payload = {
        "private_key": private_key,
        "amount": amount,
        "units": units,
        "slippage": slippage
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Check for a successful response
        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Sale successful! TXID: {response_data['txid']}")
        else:
            print(f"Error during sale: {response_data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Function to get the current token price
def get_price(token_address):
    url = f'https://avax-explorer.co/api/pangolin/price/{token_address}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for a successful response
        price_data = response.json()
        print(f"Current token price: {price_data}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")

# Main bot function that will call the necessary actions
def crypto_bot():
    print("Hello! I am your crypto bot on the Pangolin platform.")

    # Example token purchase
    print("Starting token purchase...")
    buy_tokens(private_key, amount_to_spend, units, slippage)

    # Example token sale
    print("Starting token sale...")
    sell_tokens(private_key, token_to_sell, units, slippage)

    # Example to get the current token price (e.g., USDT token address)
    token_address = '0x1234567890abcdef1234567890abcdef12345678'  # Replace with the desired token address
    print("Fetching current token price...")
    get_price(token_address)

# Run the bot
if __name__ == "__main__":
    while True:
        crypto_bot()  # Start the bot
        time.sleep(60)  # Interval between bot executions (e.g., 60 seconds)

