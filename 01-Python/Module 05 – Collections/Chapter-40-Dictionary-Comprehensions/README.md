# Chapter 42 — Dictionary Comprehensions

Dictionary comprehension creates dictionaries concisely from an iterable.

## Basic Syntax
```python
{
    key: value
    for item in iterable
}
```

Example:
```python
squares = {
    number: number * number
    for number in range(1, 6)
}
```

Result:
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## With a Condition
```python
even_squares = {
    number: number * number
    for number in range(1, 11)
    if number % 2 == 0
}
```

## Using `.items()`
```python
prices = {
    "INFY": 1500,
    "TCS": 3500,
    "ITC": 500
}

expensive = {
    symbol: price
    for symbol, price in prices.items()
    if price > 1500
}
```

Result:
```python
{"TCS": 3500}
```

## Normal Loop Equivalent
```python
result = {}

for number in range(1, 6):
    result[number] = number * 10
```

Equivalent:
```python
result = {
    number: number * 10
    for number in range(1, 6)
}
```

## Practical Nested Data Example
```python
holdings = [
    {"symbol": "INFY", "value": 30000},
    {"symbol": "TCS", "value": 35000}
]

pnl_like_map = {
    stock["symbol"]: stock["value"]
    for stock in holdings
}
```

## Key Takeaways
- Dictionary comprehension produces `key: value`.
- Add `if` after the `for` to filter.
- Understand the normal loop first.
- Prefer readability over forcing everything into one line.
