import alpaca_trade_api as tradeapi
import sched, time

from config import *

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)
account = api.get_account()

def ping_upro():
    upro = api.get_last_quote("UPRO")

    last_ask = upro.askprice

    if (last_ask < 60):
        print("less")
    else:
        print("more", last_ask)

def poll_upro(sc): 
    print("pinging upro")
    ping_upro()

    # do your stuff
    s.enter(15, 1, poll_upro, (sc,))

s = sched.scheduler(time.time, time.sleep)

s.enter(15, 1, poll_upro, (s,))
s.run()




# print(api.list_positions())
