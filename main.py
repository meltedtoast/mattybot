from backtester import backtest
from binance.client import Client
import time

if __name__ == "__main__":
    symbol = 'BTCUSDT'
    interval = Client.KLINE_INTERVAL_15MINUTE
    lookback = 1000
    atr_multiplier = 2.0
    fee_per_trade = 40

    while True:
        backtest(symbol, interval, lookback, atr_multiplier, fee_per_trade)
        time.sleep(60)  # Wait for the next interval
