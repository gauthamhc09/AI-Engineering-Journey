def calculate_price(price:" float", quantity: int) -> float:
    return price * quantity

# print(calculate_price("10", 2))

def calculate_discount(price: float, discount_percentage: float = 10.0) -> float:
    discount_price = (price * discount_percentage) / 100
    return price - discount_price

# print(calculate_discount(100.0))
# print(calculate_discount(200.0, 25.0))


# {
#     "Explain machine learning": 3,
#     "What is a neural network": 5
# }

def analyze_prompts(prompts: list[str]):
    
    result: dict[str, int] = {}
    
    for prompt in prompts:
        word_count = len(prompt.split())
        result[prompt] = word_count
        
    return result
prompts = [
    "Explain machine learning",
    "What is a neural network"
]

# print(analyze_prompts(prompts))

# def calculate_average(stock_prices: list[float]) -> float:
#     total: float = 0
#     for stock_price in stock_prices:
#         total+=stock_price
#     return total/len(stock_prices)

def calculate_average(stock_prices: list[float]) -> float:
    if not stock_prices:
        return 0.0

    total = sum(stock_prices)
    return total / len(stock_prices)

# print(calculate_average([100.0, 200.0, 300.0]))

from typing import Optional

def find_stock(symbol: str) -> Optional[str]:
    if symbol == "RELIANCE":
        return "Reliance Industries"
    return None


# def find_stock(symbol: str) -> Optional[str]:
#     print(symbol)
    
# print(find_stock("RELIANCE"))
# Reliance Industries

# print(find_stock("UNKNOWN"))
# None

def get_instrument_price(symbol: str) -> float | None:
    prices = {
        "RELIANCE": 1450.0,
        "TCS": 3200.0
    }
    
    return prices.get(symbol)

symbol = "INFY"
price = get_instrument_price(symbol)

if price is not None:
    print(f"The price for {symbol} is {price}")
else:
    print(f"{symbol} not found")
# price = get_instrument_price("INFY")

def get_stock_price(symbol: str) -> float | None:
    prices = {
        "RELIANCE": 1450.0,
        "TCS": 3200.0,
        "INFY": 1800.0
    }
    
    return prices.get(symbol)
type StockPrices = dict[str, float]

def get_stock(symbol: str) -> float | None:
    prices: StockPrices = {
        "RELIANCE": 1450.0,
        "TCS": 3200.0,
        "INFY": 1800.0
    }
    stock = prices.get(symbol)
    return stock


def get_all_stock() -> StockPrices:
    return {
            "RELIANCE": 1450.0,
            "TCS": 3200.0,
            "INFY": 1800.0
        }
print(get_stock_price("TCS"))       # 3200.0
print(get_stock_price("UNKNOWN") ) # None
print(get_stock("TCS"))       # 3200.0
print(get_all_stock())

