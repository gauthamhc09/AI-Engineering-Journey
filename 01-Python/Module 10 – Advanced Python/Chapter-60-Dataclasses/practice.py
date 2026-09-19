from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    quantity: int

stock = Stock("INFY", 5)
# print(stock.quantity)

class StockClass:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

first = StockClass('INFY', 34)
second = StockClass('INFY', 34)

# print(first == second)


from dataclasses import dataclass, field

@dataclass
class Portfolio:
    holdings: dict[str, float] = field(default_factory=dict)

p1 = Portfolio()
p2 = Portfolio()

p1.holdings["TCS"] = 3200.0

# print(p1.holdings)
# print(p2.holdings)

from dataclasses import dataclass, field

@dataclass
class Portfolio:
    name: str
    holdings: dict[str, float] = field(default_factory=dict, repr=False)

p = Portfolio("Long-term")
p.holdings["TCS"] = 3200.0

print(p)
# print(p.holdings)

from dataclasses import dataclass, field

@dataclass
class Stock:
    symbol: str
    price: float
    internal_id: int = field(compare=False)

s1 = Stock("TCS", 3200.0, 101)
s2 = Stock("TCS", 3200.0, 202)

# print(s1 == s2)

from dataclasses import dataclass

@dataclass(frozen=True)
class Stock:
    symbol: str
    price: float

stock = Stock("TCS", 3200.0)
# stock.price = 3300.0
# print(stock)

from typing import ClassVar

@dataclass
class StockClass:
    symbol: str
    currency: ClassVar[str] = "INR"

s = StockClass("TCS")

# print(s)
# print(s.currency)

l = StockClass("INFY")
# a = StockClass("apple", currency="USD") - not possible
# l.currency = "USD"
# StockClass.currency = "USD"
# print(l)

@dataclass
class FastStock:
    symbol: str
    price: float
    
faststock = FastStock("MRF", 23000)
faststock.volume = 100000
print(faststock)