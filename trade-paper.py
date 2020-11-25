import requests, json

from config import *

ENDPOINT_URL = "https://paper-api.alpaca.markets"

ACCOUNT_URL = "{}/v2/account".format(ENDPOINT_URL)
ORDERS_URL = "{}/v2/orders".format(ENDPOINT_URL)

headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=headers)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "type": type,
        "side": side,
        "time_in_force": time_in_force,
    }
    r = requests.post(ORDERS_URL, json=data, headers=headers)
    return json.loads(r.content)

def get

def get_orders():
    r = requests.get(ORDERS_URL,  headers=headers)
    return json.loads(r.content)

# order = create_order("UPRO", 100, "buy", "market", "day")
# print(order)
print(get_orders())



