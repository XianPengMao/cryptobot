import pandas as pd

class Backtest:
    def __init__(self, exchange, period_start, period_end):
        self.exchange = exchange
        self.period_start = period_start
        self.period_end = period_end
        
    def run(self):
        print(f"Running backtest for {self.exchange.symbol} from {self.period_start} to {self.period_end}")
        
        # 存储回测数据
        data = []
        cumulative_return = 0
        last_price = None
        
        try:
            historical_prices = self.exchange.get_historical_prices(self.period_start, self.period_end)
            
            # 检查获取的历史价格
            if not historical_prices:
                print("Error: No historical prices returned from exchange.")
                return pd.DataFrame(columns=['timestamp', 'close', 'signal', 'cumulative_returns'])
            
            for timestamp, price in historical_prices:
                print(f"{timestamp}: {self.exchange.symbol} price = {price}")
                print(f"Processing price: {price} EUR")
                
                # 计算简单的收益率（如果有上一个价格）
                if last_price is not None:
                    trade_return = ((price - last_price) / last_price) * 100
                    cumulative_return += trade_return
                
                # 简单的交易信号示例
                signal = 0
                if last_price is not None:
                    if price > last_price:
                        signal = 1  # 买入信号
                    elif price < last_price:
                        signal = -1  # 卖出信号
                
                # 保存数据
                data.append({
                    'timestamp': pd.to_datetime(timestamp),
                    'close': float(price),
                    'signal': signal,
                    'cumulative_returns': cumulative_return
                })
                
                last_price = price
            
            # 转换为DataFrame并返回
            if data:  # 确保有数据
                results_df = pd.DataFrame(data)
                print("Backtest completed successfully")
                print(f"Generated {len(results_df)} data points")
                return results_df
            else:
                print("Warning: No data collected during backtest")
                return pd.DataFrame(columns=['timestamp', 'close', 'signal', 'cumulative_returns'])
                
        except Exception as e:
            print(f"Error during backtest: {str(e)}")
            return pd.DataFrame(columns=['timestamp', 'close', 'signal', 'cumulative_returns'])