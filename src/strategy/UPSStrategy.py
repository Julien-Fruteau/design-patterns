from src.strategy.Order import Order
from src.strategy.AStrategy import AStrategy


class UPSStrategy(AStrategy):
    def calculate(self, order: Order) -> float:
        return 4.00
