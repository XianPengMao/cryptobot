from exchanges.exchange import Exchange
from strategies.strategy import Strategy


class Logger(Strategy):
    def __init__(self, exchange: Exchange, timeout=60):
        super().__init__(exchange, timeout)

    def run(self):
        print('*******************************')
        print('Exchange:', self.exchange.name)
        print('Pair:', self.exchange.get_symbol())
        print('Checking current price...')

    def process_price(self, price_data):
        print(f"Processing price: {price_data['p']} {self.exchange.asset}")
