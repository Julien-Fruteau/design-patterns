from src.strategy.Order import Order
from src.strategy.AStrategy import AStrategy


class FedExStrategy(AStrategy):
    def calculate(self, order: Order) -> float:
        return 3.00
