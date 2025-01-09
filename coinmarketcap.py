import requests

# Replace 'your_api_key_here' with your CoinMarketCap API key
api_key = 'your_api_key_here'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Parameters to fetch BTC data
parameters = {
    'symbol': 'BTC',
    'convert': 'USD'
}

# Headers with the API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9abf79a7-d103-40ab-a43e-740639ce7cab',
}

try:
    # Making the API request
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Extracting data from the response
    data = response.json()
    btc_price = data['data']['BTC']['quote']['USD']['price']

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
