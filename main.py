from kite_trade import *
#import kiteconnect
#Logging to your Zerodha Account 
enctoken = ""
kite = KiteApp(enctoken=enctoken)


#Just to fetch and check some data
# Basic calls
'''print(kite.margins())
print(kite.orders())
print(kite.positions())

# Get instrument or exchange
print(kite.instruments())
print(kite.instruments("NSE"))
print(kite.instruments("NFO"))

# Get Live Data
print(kite.ltp("NSE:RELIANCE"))
print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
print(kite.quote(["NSE:NIFTY BANK", "NSE:ACC", "NFO:NIFTY22SEPFUT"]))

# Get Historical Data
import datetime
instrument_token = 9604354
from_datetime = datetime.datetime.now() - datetime.timedelta(days=7)     # From last & days
to_datetime = datetime.datetime.now()
interval = "5minute"
print(kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False))'''

#Check the price of NIFTY which can be modified
price = kite.get_quote('NSE:NIFTY')

# Place Order

'''order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="ACC",
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=1,
                         product=kite.PRODUCT_MIS,
                         order_type=kite.ORDER_TYPE_MARKET,
                         price=None,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="TradeUsingAlgo")

print(order)'''

# Place a buy order if the price is above 17000
if price > 17000:
    kite.place_order(kite.EXCHANGE_NSE, kite.ORDER_TYPE_MARKET, kite.TRANSACTION_TYPE_BUY, instrument_token='256265', quantity=1)

# Place a sell order if the price is below 16800
elif price < 16800:
    kite.place_order(kite.EXCHANGE_NSE, kite.ORDER_TYPE_MARKET, kite.TRANSACTION_TYPE_SELL, instrument_token='256265', quantity=1)