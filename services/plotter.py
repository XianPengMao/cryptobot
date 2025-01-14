import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class Plotter:
    def __init__(self, symbol):
        self.symbol = symbol
        # 设置图表样式
        plt.style.use('seaborn-v0_8-darkgrid')
        
    def plot_backtest_results(self, results):
        """
        绘制回测结果
        
        Args:
            results: 包含价格、信号和收益等数据的DataFrame
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), height_ratios=[2, 1])
        
        # 绘制价格走势和移动平均线
        ax1.plot(results['timestamp'], results['close'], label='价格', color='blue')
        ax1.plot(results['timestamp'], results['MA20'], label='MA20', color='orange', alpha=0.7)
        
        # 绘制买卖信号
        buy_signals = results[results['signal'] == 1]
        sell_signals = results[results['signal'] == -1]
        
        if not buy_signals.empty:
            ax1.scatter(buy_signals['timestamp'], 
                       buy_signals['close'],
                       marker='^', color='green', s=100, label='买入信号')
        
        if not sell_signals.empty:
            ax1.scatter(sell_signals['timestamp'],
                       sell_signals['close'],
                       marker='v', color='red', s=100, label='卖出信号')
        
        # 设置标题和标签
        ax1.set_title(f'{self.symbol} 回测结果')
        ax1.set_xlabel('时间')
        ax1.set_ylabel('价格')
        ax1.legend()
        ax1.grid(True)
        
        # 绘制累计收益
        ax2.plot(results['timestamp'], results['cumulative_returns'], 
                label='累计收益', color='green')
        ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
        ax2.fill_between(results['timestamp'], 
                        results['cumulative_returns'], 
                        0, 
                        alpha=0.3, 
                        color='green', 
                        where=results['cumulative_returns'] >= 0)
        ax2.fill_between(results['timestamp'], 
                        results['cumulative_returns'], 
                        0, 
                        alpha=0.3, 
                        color='red', 
                        where=results['cumulative_returns'] < 0)
        ax2.set_xlabel('时间')
        ax2.set_ylabel('累计收益 (%)')
        ax2.legend()
        ax2.grid(True)
        
        plt.tight_layout()
        plt.savefig(f'backtest_results_{self.symbol}.png')
        plt.close()