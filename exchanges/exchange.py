from abc import ABC, abstractmethod
from typing import Optional


class Exchange(ABC):
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.currency: str = ""
        self.asset: str = ""
        self.strategy = None
        self.socket = None
        self.name = self.__class__.__name__.lower()

    def set_currency(self, currency: str):
        self.currency = currency

    def set_asset(self, asset: str):
        self.asset = asset

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_symbol(self) -> str:
        return f"{self.currency}{self.asset}"

    @abstractmethod
    def start_symbol_ticker_socket(self, symbol: str):
        pass

    @abstractmethod
    def close_socket(self):
        pass
