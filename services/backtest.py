from datetime import datetime, timedelta
import random
from exchanges.exchange import Exchange
from services.chart import Chart


class Backtest:
    def __init__(self, exchange: Exchange, period_start: str, period_end: str):
        self.exchange = exchange
        self.period_start = datetime.strptime(period_start, "%Y-%m-%dT%H:%M")
        self.period_end = datetime.strptime(period_end, "%Y-%m-%dT%H:%M")
        self.chart = Chart()

    def run(self):
        print(f"Running backtest for {self.exchange.get_symbol()} from {self.period_start} to {self.period_end}")
        
        # 生成模拟价格数据
        current_time = self.period_start
        base_price = 50000.0  # 起始价格
        
        while current_time <= self.period_end:
            # 生成一个随机价格变动（-1% 到 +1%）
            price_change = random.uniform(-0.01, 0.01)
            current_price = base_price * (1 + price_change)
            
            # 生成随机成交量（示例：1-100）
            volume = random.uniform(1, 100)
            
            # 添加数据到图表
            self.chart.add_price(current_time, current_price, volume)
            
            # 打印当前时间和价格
            print(f"{current_time}: {self.exchange.get_symbol()} price = {current_price:.2f}")
            
            # 调用策略的回调函数
            if hasattr(self.exchange, 'strategy') and self.exchange.strategy:
                self.exchange.strategy.process_price({'p': str(current_price)})
            
            # 更新基准价格和时间
            base_price = current_price
            current_time += timedelta(minutes=1)
            
            # 为了演示目的，我们只模拟前100个数据点
            if (current_time - self.period_start).total_seconds() > 6000:
                break
        
        print("Backtest completed")
        
        # 生成并保存图表
        self.chart.plot(
            self.exchange.get_symbol(),
            f"backtest_{self.exchange.get_symbol()}_{self.period_start.strftime('%Y%m%d')}.html"
        )
