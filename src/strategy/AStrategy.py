import abc
from src.strategy.Order import Order


class AStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self, order: Order) -> float:
        pass
