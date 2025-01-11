from exchanges.exchange import Exchange


class Binance(Exchange):
    def __init__(self, api_key: str, api_secret: str):
        super().__init__(api_key, api_secret)
        print("Binance exchange initialized in test mode")
        self.currency = None
        self.asset = None
        self.strategy = None

    def set_currency(self, currency: str):
        self.currency = currency

    def set_asset(self, asset: str):
        self.asset = asset

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_symbol(self) -> str:
        return f"{self.currency}{self.asset}"

    def symbol_ticker(self) -> float:
        print(f"Getting price for {self.get_symbol()}")
        return 50000.0  # 返回测试用的固定价格

    def start_symbol_ticker_socket(self, callback):
        print(f"Starting price stream for {self.get_symbol()}")
        # 在测试模式下，直接调用回调函数一次
        callback({'p': '50000.0'})

    def close_socket(self):
        print("Closing socket connection")
