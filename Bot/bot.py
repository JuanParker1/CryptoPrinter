import ccxt
import schedule
import pandas as pd
pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

from datetime import datetime
import time
import os
import csv

""" INTERNAL FILE IMPORTS """
from settings import settings
from settings import config
import authentication as auth
""" END OF INTERNAL FILE IMPORTS """

exchange = ccxt.ftx({
    "apiKey": config.FTX_API_KEY,
    "secret": config.FTX_SECRET_KEY
})

def tr(data):
    return 0

def atr(data, period):
    return 0

def supertrend():
    return 0

def check_buy_sell_signals(timestamp, close, in_uptrend, past_closes):
    return 0

def run():
    clearAndWriteLogs()

    print('------------------------------------------------- MAIN EVENT ----------------------------------------------------------------------')
    print('\n')
    print(f"Fetching new bars for {datetime.now().isoformat()}")

    raw_bars = auth.authenticate('GET', settings.ENDPOINT_URL)['results']

    bars = []

    for entry in raw_bars:
        bars.append([entry['t'], entry['o'], entry['h'], entry['l'], entry['c'], entry['v']])
    
    df = pd.DataFrame(bars[:], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    supertrend_data = supertrend(df)

    # ----- LISTS ------
    timestamps = []
    closes = []
    in_uptrends = []

    # For RSI closes
    past_closes = []
    # ------------------

    # ----------- FILL LISTS --------------
    for ts in supertrend_data['timestamp']:
        timestamps.append(ts)

    for c in supertrend_data['close']:
        closes.append(c)

    for iu in supertrend_data['in_uptrend']:
        in_uptrends.append(iu)
    # -------------------------------------

    count = 0

    for x in closes:
        past_closes.append(x)

        timestamp = timestamps[count]
        close = closes[count]
        in_uptrend = in_uptrends[count]

        check_buy_sell_signals(timestamp, close, in_uptrend, past_closes)

        count = count + 1

    print('\n')
    print('-----------------------------------------------------------------------------------------------------------------------------------')

run()

def clearAndWriteLogs():
    with open(os.path.join(settings.FOLDER_NAME, 'Database', 'settings_logs.txt'), 'w') as w:
        w.write("Pair: " + str(settings.PAIRNAME) + '\n' "RSI Periods: " + str(settings.RSI_PERIODS) + '\n' + "Timeframe: " + str(settings.TIMEFRAME) + '\n' + "Limit: " + str(settings.LIMIT) + '\n' + "Suptertrend Multiplier: " + str(settings.SUPERTREND_MULTIPLIER) + '\n' + "Supertrend Periods: "  + str(settings.SUPERTREND_PERIODS) + '\n' + "RSI Long Overbought: " + str(settings.RSI_LONG_OVERBOUGHT) + '\n' + "RSI Long Oversold: " + str(settings.RSI_LONG_OVERSOLD) + '\n' + "RSI Short Overbought: " + str(settings.RSI_SHORT_OVERBOUGHT) + '\n' + "RSI Short Oversold: " + str(settings.RSI_SHORT_OVERSOLD) + '\n' + "Trade Size: " + str(settings.TRADE_SIZE_IN_DOLLAR) + '\n' + "Emergency Trades On: " + str(settings.EMERGENCY_TRADES_ON))
    
    # Clear logs
    
    with open(os.path.join(settings.FOLDER_NAME, 'Database', 'settings_logs.txt'), 'w') as w:
        w.write("")

    with open(os.path.join(settings.FOLDER_NAME, 'Database', 'logs.txt'), 'w') as w:
        w.write("")

    with open(os.path.join(settings.FOLDER_NAME, 'Database', 'orders_logs.txt'), 'w') as w:
        w.write("")

    with open(os.path.join(settings.FOLDER_NAME, 'Database', 'trades_logs.txt'), 'w') as w:
        w.write("")