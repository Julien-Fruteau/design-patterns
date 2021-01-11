from src.strategy.Order import Order
from src.strategy.AStrategy import AStrategy


class PostalStrategy(AStrategy):
    def calculate(self, order: Order) -> float:
        return 5.00
