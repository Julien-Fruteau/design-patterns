from src.strategy.ShippingCost import ShippingCost
from src.strategy.Order import Order
from src.strategy.FedExStrategy import FedExStrategy
from src.strategy.PostalStrategy import PostalStrategy
from src.strategy.UPSStrategy import UPSStrategy

order = Order("my-fake-order")

cost = ShippingCost(FedExStrategy())
assert cost.shipping_cost(order) == 3.00

cost = ShippingCost(PostalStrategy())
assert cost.shipping_cost(order) == 5.00

cost = ShippingCost(UPSStrategy())
assert cost.shipping_cost(order) == 4.00
