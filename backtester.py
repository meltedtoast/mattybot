from data_fetcher import get_klines
from indicators import apply_indicators
from signals import check_signals

def backtest(symbol, interval, lookback, atr_multiplier=2.0, fee_per_trade=40):
    data = get_klines(symbol, interval, lookback)
    data = apply_indicators(data)
    data = check_signals(data)
    
    position = None
    entry_price = 0
    total_profit = 0
    win_trades = 0
    loss_trades = 0
    total_fees = 0
    results = []

    for i in range(1, len(data)):
        if data['Buy'][i] and position is None:
            position = 'long'
            entry_price = data['close'][i]
            stop_loss = entry_price - atr_multiplier * data['ATR'][i]
            take_profit = entry_price + atr_multiplier * data['ATR'][i]
            results.append(f"Buy at {data.index[i]}: {entry_price}, Stop Loss: {stop_loss}, Take Profit: {take_profit}")

        elif position == 'long':
            # Exit if price hits stop loss or sell signal (KAMA cross)
            if data['close'][i] <= stop_loss or data['Sell'][i]:
                position = None
                exit_price = data['close'][i]
                profit = exit_price - entry_price
                total_fees += fee_per_trade
                net_profit = profit - fee_per_trade
                total_profit += net_profit
                if net_profit > 0:
                    win_trades += 1
                else:
                    loss_trades += 1
                results.append(f"Sell at {data.index[i]}: {exit_price}, Profit: {profit}, Net Profit: {net_profit}, Total Profit: {total_profit}, Fee: {fee_per_trade}")
            elif data['close'][i] >= take_profit:
                position = None
                exit_price = data['close'][i]
                profit = exit_price - entry_price
                total_fees += fee_per_trade
                net_profit = profit - fee_per_trade
                total_profit += net_profit
                win_trades += 1
                results.append(f"Take Profit at {data.index[i]}: {exit_price}, Profit: {profit}, Net Profit: {net_profit}, Total Profit: {total_profit}, Fee: {fee_per_trade}")

    total_trades = win_trades + loss_trades
    win_rate = (win_trades / total_trades) * 100 if total_trades > 0 else 0
    results.append(f"Win Rate: {win_rate}% ({win_trades} wins, {loss_trades} losses)")
    results.append(f"Total Profit: {total_profit}, Total Fees: {total_fees}")

    for result in results:
        print(result)
