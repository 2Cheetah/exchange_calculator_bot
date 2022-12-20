# Telegram Bot - Currency Exchange Calculator

## Libraries

- Python 3.8.10
- Aiogram 2.23.1
- Requests 2.28.1

## API keys

To make the Telegram Bot work, you need to create Telegram Bot and get its
API key. Also you need to get API key from Alphavantage. Then you need to 
create keys.py file in `telegram_bot` folder with the following content:

```
from itertools import cycle

ALPHA_API_TOKEN_LIST = [
    'Your Alphavantage API key here',
]
api_token_iterator = cycle(ALPHA_API_TOKEN_LIST)

TELEGRAM_API_TOKEN='Your Telegram Bot API key here'
```
