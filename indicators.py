import ta

def apply_indicators(data):
    data['KAMA3'] = ta.momentum.kama(data['close'], window=3)
    data['KAMA9'] = ta.momentum.kama(data['close'], window=9)
    data['MACD'] = ta.trend.macd(data['close'], window_slow=26, window_fast=12)
    data['MACD_SIGNAL'] = ta.trend.macd_signal(data['close'], window_slow=26, window_fast=12, window_sign=9)
    data['MACD_HIST'] = data['MACD'] - data['MACD_SIGNAL']  # MACD Histogram
    data['ATR'] = ta.volatility.average_true_range(data['high'], data['low'], data['close'], window=14)
    return data
