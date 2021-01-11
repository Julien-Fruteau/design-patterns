from src.strategy.Order import Order
from src.strategy.AStrategy import AStrategy

class ShippingCost:
    def __init__(self, strategy: AStrategy) -> None:
        self._strategy: AStrategy = strategy

    def shipping_cost(self, order: Order):
        return self._strategy.calculate(order)
