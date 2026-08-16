# Chapter 43 — Collections Mini-Project

## Project: Portfolio Data Analyzer

Combines:
- Lists
- Tuples
- Sets
- Dictionaries
- Loops
- Conditions
- List comprehensions
- Dictionary comprehensions

## Structure
```python
portfolio = {
    "investor": "Gautham",
    "holdings": [
        {
            "symbol": "INFY",
            "sector": "IT",
            "quantity": 20,
            "buy_price": 1400,
            "current_price": 1500
        }
    ]
}
```

This is:
```text
Dictionary → List → Dictionaries
```

## Holding calculations
```text
invested_value = quantity × buy_price
current_value  = quantity × current_price
pnl            = current_value - invested_value
```

Example:
```python
holding["invested_value"] = holding["quantity"] * holding["buy_price"]
holding["current_value"] = holding["quantity"] * holding["current_price"]
holding["pnl"] = holding["current_value"] - holding["invested_value"]
```

## Analysis
Calculate:
- Total invested value
- Total current value
- Total P&L
- Profitable stocks
- Loss-making stocks
- Best performer
- Worst performer

## Collection examples

### List
```python
stock_symbols = [holding["symbol"] for holding in holdings]
```

### Set
```python
sectors = {holding["sector"] for holding in holdings}
```

### Dictionary
```python
pnl_by_stock = {
    holding["symbol"]: holding["pnl"]
    for holding in holdings
}
```

### Filtered list
```python
high_value_stocks = [
    holding for holding in holdings
    if holding["current_value"] > 30000
]
```

## Finding maximum/minimum safely

Initialize from the first record:

```python
best_pnl = holdings[0]["pnl"]
best_stock = holdings[0]["symbol"]

for holding in holdings:
    if holding["pnl"] > best_pnl:
        best_pnl = holding["pnl"]
        best_stock = holding["symbol"]
```

For minimum:

```python
worst_pnl = holdings[0]["pnl"]
worst_stock = holdings[0]["symbol"]

for holding in holdings:
    if holding["pnl"] < worst_pnl:
        worst_pnl = holding["pnl"]
        worst_stock = holding["symbol"]
```

### Important lesson
Do not reset the tracking variable inside the loop. It must preserve the best/worst value found so far.

## Project takeaway
This project demonstrates how Python collections work together to process structured, real-world portfolio and API-style data.
