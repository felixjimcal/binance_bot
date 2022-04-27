import datetime
import sys
import asyncio
import numpy as np
import pandas as pd
import talib
from binance.client import Client
from binance.enums import *
from binance import AsyncClient, BinanceSocketManager
from utils import credentials

HIGH = 'high'
LOW = 'low'
TIMESTAMP = 'timestamp'
OPEN = 'open'
CLOSE = 'close'
VOLUME = 'volume'
CTM_STRING = 'ctmString'

BUY = 'buy'
FIXED_RISK = 0.02
ATR = 'atr'
PLUS = 'plus'
MIN = 'minus'
LONG_LEGGED = 'll'
SUPPORTS = 'supports'
RESISTANCES = 'resistances'

MACD_1M = 'macd_1m'
MACD_SIGNAL_1M = 'macd_signal_1m'
MACD_HIST_1M = 'macd_hist_1m'


async def main():
    binance_client = await AsyncClient.create(credentials.BINANCE_REAL_API_KEY, credentials.BINANCE_REAL_API_SECRET, testnet=False)
    binance_socket = BinanceSocketManager(binance_client)
    socket_data = binance_socket.symbol_ticker_futures_socket('BTCBUSD')
    async with socket_data as data:
        while True:
            res = await data.recv()
            try:
                bid_price = float(res['data']["a"])
                print(bid_price, datetime.datetime.now())
            except Exception as ex:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print('Fail in so:', ex.args, 'line:', exc_tb.tb_lineno)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
