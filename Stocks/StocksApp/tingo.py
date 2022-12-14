import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 57b8b1a63c7183ab58eecfb37e6b60d26371b418'
}


def get_data(ticker):
    url = f'https://api.tiingo.com/tiingo/daily/{ticker}'
    response = requests.get(url, headers=headers)
    return response.json()


def get_price(ticker):
    url = f'https://api.tiingo.com/tiingo/daily/{ticker}/prices'
    response = requests.get(url, headers=headers)
    return response.json()[0]
