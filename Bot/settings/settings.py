PAIRNAME = "SOL-PERP"

# Test started: Saturday, 15/03/2022, 12:00 PM
# Next: 18/03/2022, 12:00 PM

RSI_PERIODS = 14

TIMEFRAME = 1
TIMEFRAME_UNIT = 'minute'

FROM = '2022-04-15'
TO = '2022-04-26'

LIMIT =  50000

SUPERTREND_MULTIPLIER = 13
SUPERTREND_PERIODS = 10

# For Longs
RSI_LONG_OVERBOUGHT = 80
RSI_LONG_OVERSOLD = 20
RSI_EMERGENCY_LONG_OVERBOUGHT = 0

#For shorts
RSI_SHORT_OVERBOUGHT = 80
RSI_SHORT_OVERSOLD = 20
RSI_EMERGENCY_SHORT_OVERSOLD = 0
  
# BTC: 1.00(5/6), 0.99(4/5)
# SOL: 1.01, 0.99
# ETH: Best result: 1.03, 0.97

TP_LONG = 1.004
TP_SHORT = 0.996

SL_EMERGENCY_LONG = 0.975
SL_EMERGENCY_SHORT = 1.025

TRADE_SIZE_IN_DOLLAR = 0

#Backtesting variables
wallet = 10000
ORIGINAL_WALLET_VALUE = 10000
LEVERAGE = 1

ENDPOINT_URL = 'https://api.polygon.io/v2/aggs/ticker/X:' + PAIRNAME + '/range/' + str(TIMEFRAME) + '/' + TIMEFRAME_UNIT + '/' + FROM +'/' + TO + '?adjusted=true&sort=asc&limit=' + str(LIMIT) + '&apiKey=9jseziALPR_64OidpVhf7NjiZ9OEWSPO'

EMERGENCY_TRADES_ON = False

FOLDER_NAME = 'Backtesting'