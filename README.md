# bot-pangolin-avax
# Crypto Trading Bot using Pangolin API on Avalanche

This Python-based crypto trading bot interacts with the Pangolin decentralized exchange (DEX) on the Avalanche blockchain. It allows users to execute real-time token trading, including buying, selling tokens, and fetching live token prices. The bot uses Pangolin's API endpoints for fast transactions and integrates them into automated trading strategies.

https://medium.com/@elliotpearce01/pangolin-api-effortless-token-trading-on-avalanche-with-fast-transactions-f054616ebbac

## Features

- **Buy Tokens:** The bot allows users to purchase tokens with AVAX (Avalanche's native token). Users can specify the amount of AVAX they want to spend, slippage tolerance, and units.
- **Sell Tokens:** The bot facilitates the selling of tokens in exchange for AVAX, with adjustable slippage tolerance and units.
- **Fetch Live Token Prices:** Users can fetch the real-time price of any token available on Pangolin DEX by providing the token's contract address.
- **Automation:** The bot runs in a loop, executing token buys, sells, and fetching prices at regular intervals.

## How It Works

### 1. **Buying Tokens**
The bot uses the Pangolin API's `buy` endpoint to execute token purchases on the Avalanche blockchain. The user specifies how much AVAX they want to spend, as well as the slippage and unit values for the transaction.

### 2. **Selling Tokens**
The `sell` endpoint of Pangolin is used to sell tokens in exchange for AVAX. Similar to the buying process, the bot allows you to adjust slippage and units before executing the sale.

### 3. **Fetching Live Token Prices**
The bot can fetch the current price of a token by making a request to the `price` endpoint of the Pangolin API. This is useful for checking token market prices before making any trading decisions.

## Requirements

- Python 3.x
- `requests` library for making HTTP requests
  - You can install it with:
    ```bash
    pip install requests
    ```

## Configuration

- **Private Key:** You must provide your private key to authorize transactions. Make sure you handle this securely.
- **Amount to Spend/Token Sell Amount:** Set how much AVAX you want to spend for buying tokens or how many tokens you want to sell.
- **Slippage:** The slippage percentage helps mitigate the risk of price changes during a transaction. You can adjust this value (e.g., 10% or 1%).

## Example Code

```python
import requests
import time

# Your private key
private_key = 'your_private_key_here'

# Buying tokens settings
amount_to_spend = 0.001  # Amount of AVAX you want to spend
slippage = 10           # Slippage tolerance (e.g., 10 for 10%)
units = 1000000         # Default units

# Selling tokens settings
token_to_sell = 1000  # Amount of tokens you want to sell

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
        response.raise_for_status()  # Check for successful response
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
        response.raise_for_status()  # Check for successful response
        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Sale successful! TXID: {response_data['txid']}")
        else:
            print(f"Error during sale: {response_data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Function to get real-time token price
def get_price(token_address):
    url = f'https://avax-explorer.co/api/pangolin/price/{token_address}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for successful response
        price_data = response.json()
        print(f"Current token price: {price_data}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")

# Main bot function
def crypto_bot():
    print("Hello! I am your crypto bot on Pangolin.")

    # Example of buying tokens
    print("Initiating token purchase...")
    buy_tokens(private_key, amount_to_spend, units, slippage)

    # Example of selling tokens
    print("Initiating token sale...")
    sell_tokens(private_key, token_to_sell, units, slippage)

    # Example of getting token price data (e.g., USDT token address)
    token_address = '0x1234567890abcdef1234567890abcdef12345678'  # Replace with the token's address
    print("Fetching current token price...")
    get_price(token_address)

# Run the bot in a loop with a 60-second interval
if __name__ == "__main__":
    while True:
        crypto_bot()  # Run the bot
        time.sleep(60)  # Interval between bot runs (e.g., 60 seconds)
