#!/usr/share/python3
import requests
from keys import api_token_iterator
from supported_currencies import cur_dict


class Currency:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        # Check if provided data is a string
        if not isinstance(value, str):
            raise ValueError(f"Expected string, provided '{value}'")
        
        # Check if provided currency is supported
        if not value.upper() in cur_dict:
            raise ValueError(f"'{value}' is not supported.")
        
        self.value = value.upper()


class Currency_pair:
    cur1 = Currency()
    cur2 = Currency()
    
    def __init__(self, cur1, cur2):
        self.cur1 = cur1
        self.cur2 = cur2

    def get_api_data(self):
        api_key = next(api_token_iterator)
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={self.cur1}&to_currency={self.cur2}&apikey={api_key}"
        response = requests.get(url)
        self.api_data = response.json()

    def exchange_rate(self):
        return float(self.api_data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

# api_data looks like for a currency_pair:
# 
# {
#   'Realtime Currency Exchange Rate': {
#     '1. From_Currency Code': 'USD',
#     '2. From_Currency Name': 'United States Dollar',
#     '3. To_Currency Code': 'MYR',
#     '4. To_Currency Name': 'Malaysian Ringgit',
#     '5. Exchange Rate': '4.42350000',
#     '6. Last Refreshed': '2022-12-19 09:52:33',
#     '7. Time Zone': 'UTC',
#     '8. Bid Price': '4.42350000',
#     '9. Ask Price': '4.42350000'
#   }
# }


if __name__ == "__main__":
    currency_pair = Currency_pair('usd', 'myr')
    currency_pair.get_api_data()
    print(currency_pair.exchange_rate())

    currency_pair = Currency_pair('myr', 'rub')
    currency_pair.get_api_data()
    print(currency_pair.exchange_rate())

    currency_pair = Currency_pair('usd', 'rub')
    currency_pair.get_api_data()
    print(currency_pair.exchange_rate())
