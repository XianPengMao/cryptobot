from datetime import datetime
from exchanges.exchange import Exchange


class Importer:
    def __init__(self, exchange: Exchange, period_start: str, period_end: str, interval: int):
        self.exchange = exchange
        self.period_start = datetime.strptime(period_start, "%Y-%m-%dT%H:%M")
        self.period_end = datetime.strptime(period_end, "%Y-%m-%dT%H:%M")
        self.interval = interval

    def process(self):
        print(f"Importing data for {self.exchange.get_symbol()} from {self.period_start} to {self.period_end}")
        print("Import functionality not implemented yet.")
