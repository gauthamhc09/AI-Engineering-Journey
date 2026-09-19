# Chapter 59 — Type Hinting

## 1. What are type hints?

Type hints (annotations) communicate the types a variable, parameter, or function is expected to use.

```python
price: float = 3200.0

def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

- `price: float` says `price` is expected to be a `float`.
- `quantity: int` says `quantity` is expected to be an `int`.
- `-> float` says the function is expected to return a `float`.

**Important:** Python generally does not enforce type hints at runtime. They help readers, IDEs, and static type checkers identify likely mistakes.

## 2. Variables and return values

```python
name: str = "TCS"

def log_message(message: str) -> None:
    print(message)
```

Use `-> None` when a function is intended not to return a meaningful value.

## 3. Default arguments are different from type hints

```python
def greet(name: str = "Gautham") -> str:
    return f"Hello, {name}"
```

- `name: str` describes the expected type.
- `= "Gautham"` makes the argument optional by providing a default.

A type hint alone does not make an argument optional.

## 4. `Any` vs `object`

- `Any` effectively tells a type checker to allow operations without checking the value's specific type.
- `object` means the value may be any Python object, but operations generally require narrowing or checking the type first.

Prefer a more specific type when you know what the value should be.

## 5. Union types

Use a union when a value may have more than one type.

```python
def format_id(value: int | str) -> str:
    return str(value)
```

`int | str` is the modern syntax. `Union[int, str]` is the older equivalent from `typing`.

When behavior depends on the actual type, check it:

```python
if isinstance(value, int):
    ...
```

## 6. Collection type hints

```python
symbols: list[str] = ["TCS", "INFY"]
prices: dict[str, float] = {"TCS": 3200.0, "INFY": 1800.0}
point: tuple[str, float] = ("TCS", 3200.0)
values: tuple[float, ...] = (1.0, 2.0, 3.0)
unique_symbols: set[str] = {"TCS", "INFY"}
```

Examples:
- `list[str]`: list of strings.
- `dict[str, float]`: dictionary with string keys and float values.
- `tuple[str, float]`: a two-item tuple with those respective types.
- `tuple[float, ...]`: a tuple containing zero or more floats.
- `set[str]`: set of strings.

## 7. Optional values: `T | None`

A function may return a value or `None`:

```python
def get_stock_price(symbol: str) -> float | None:
    prices = {"TCS": 3200.0, "INFY": 1800.0}
    return prices.get(symbol)
```

`float | None` is equivalent to `Optional[float]`.

Check for `None` before using the value as a number:

```python
price = get_stock_price("TCS")

if price is not None:
    print(price * 2)
else:
    print("Stock not found")
```

`Optional[T]` means `T` or `None`; it does **not** mean a function argument can be omitted. A default value is what makes an argument omittable.

## 8. Type aliases

A type alias gives a reusable, readable name to a type.

```python
StockPrices = dict[str, float]

def get_prices() -> StockPrices:
    return {"TCS": 3200.0, "INFY": 1800.0}
```

In Python 3.12+, the `type` statement is also available:

```python
type StockPrices = dict[str, float]
```

The `type` statement requires Python 3.12+. The assignment-style alias works on earlier Python versions when the type syntax itself is supported.

A type alias is a nickname for a type; it does not create a new runtime type or validate values.

## 9. Match the return annotation to the returned value

```python
type StockPrices = dict[str, float]

def find_price(prices: StockPrices, symbol: str) -> float | None:
    return prices.get(symbol)
```

`StockPrices` describes the dictionary. `prices.get(symbol)` returns one price or `None`, so the function's return annotation must be `float | None`, not `StockPrices`.

## 10. Practice example: average

```python
def calculate_average(stock_prices: list[float]) -> float:
    if not stock_prices:
        raise ValueError("stock_prices must not be empty")

    return sum(stock_prices) / len(stock_prices)
```

The empty-list check matters because dividing by `len([])` would cause `ZeroDivisionError`. Raising `ValueError` makes the invalid input explicit; returning `0.0` instead would be a different design choice.

## Chapter summary

Type hints describe expected types and improve readability and static analysis, but generally do not enforce types at runtime. Use collection annotations for structured data, unions for multiple possible types, `T | None` for possibly missing values, and aliases to simplify repeated types. Always make sure a function's return annotation matches what it actually returns.
