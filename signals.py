def check_signals(data):
    # Entry: KAMA 3 crosses above KAMA 9 and Linda MACD Uptrend
    data['Buy'] = (
        (data['KAMA3'] > data['KAMA9']) & 
        (data['KAMA3'].shift(1) <= data['KAMA9'].shift(1)) & 
        (data['MACD_HIST'] > data['MACD_HIST'].shift(1))  # Linda MACD uptrend condition
    )
    # Exit: KAMA 3 crosses below KAMA 9
    data['Sell'] = (
        (data['KAMA3'] < data['KAMA9']) & 
        (data['KAMA3'].shift(1) >= data['KAMA9'].shift(1))
    )
    return data
