import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime


class Chart:
    def __init__(self):
        self.price_data = []
        self.volume_data = []
        
    def add_price(self, timestamp: datetime, price: float, volume: float = 0):
        self.price_data.append({
            'timestamp': timestamp,
            'price': price
        })
        self.volume_data.append({
            'timestamp': timestamp,
            'volume': volume
        })
        
    def plot(self, symbol: str, save_path: str = None):
        # 转换数据为 DataFrame
        df_price = pd.DataFrame(self.price_data)
        df_volume = pd.DataFrame(self.volume_data)
        
        # 创建子图，主图显示价格，副图显示成交量
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.03,
            subplot_titles=(f'{symbol} Price', 'Volume'),
            row_heights=[0.7, 0.3]
        )

        # 添加价格线图
        fig.add_trace(
            go.Scatter(
                x=df_price['timestamp'],
                y=df_price['price'],
                name='Price',
                line=dict(color='#2962FF')
            ),
            row=1, col=1
        )

        # 添加成交量柱状图
        fig.add_trace(
            go.Bar(
                x=df_volume['timestamp'],
                y=df_volume['volume'],
                name='Volume',
                marker_color='#2962FF',
                opacity=0.5
            ),
            row=2, col=1
        )

        # 设置图表样式
        fig.update_layout(
            template='plotly_dark',
            title=f'{symbol} Price Chart',
            showlegend=False,
            height=800,
            xaxis_rangeslider_visible=False,
            margin=dict(t=30, l=0, r=0, b=0)
        )

        # 设置y轴格式
        fig.update_yaxes(title_text='Price', row=1, col=1)
        fig.update_yaxes(title_text='Volume', row=2, col=1)

        # 保存或显示图表
        if save_path:
            fig.write_html(save_path)
        else:
            fig.show() 