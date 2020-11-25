import alpaca_trade_api as tradeapi

from config import *

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

response = api.get_barset('UPRO', "1D", 100, "2020-01-01")
print(response.get("UPRO"))