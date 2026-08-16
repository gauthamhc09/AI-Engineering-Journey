# Chapter 41 — Collections Comparison

## Core idea
Choose a collection based on what the data needs to do.

| Collection | Ordered | Mutable | Duplicates | Main access |
|---|---|---|---|---|
| List | Yes | Yes | Yes | Index |
| Tuple | Yes | No | Yes | Index |
| Set | No* | Yes | No | Membership |
| Dictionary | Yes** | Yes | Keys unique | Key |

* Sets should not be used when positional order matters.
** Modern Python dictionaries preserve insertion order, but their main purpose is key-value lookup.

## List
Use when you need an ordered, changeable sequence and duplicates are allowed.

```python
stocks = ["INFY", "TCS", "INFY"]
stocks.append("ITC")
stocks[0]
```

## Tuple
Use for an ordered, fixed collection.

```python
coordinates = (12.97, 77.59)
```

## Set
Use when uniqueness and membership are important.

```python
stocks = {"INFY", "TCS", "INFY"}
```

Useful for removing duplicates and set operations such as union.

## Dictionary
Use when data has a key → value relationship.

```python
stock = {"symbol": "INFY", "price": 1500}
stock["price"]
```

Very common for JSON, API data, configuration, and records.

## Quick decision guide
```text
Ordered + changeable       → List
Ordered + fixed            → Tuple
Unique values              → Set
Key → value relationship   → Dictionary
```

## Example
```python
broker1 = ["INFY", "TCS", "ITC"]
broker2 = ["TCS", "RELIANCE", "ITC"]

unique_stocks = set(broker1) | set(broker2)
```

If an ordered list is required afterward:
```python
unique_stocks = list(set(broker1) | set(broker2))
```

Do not assume that resulting list preserves the original order.

## Key takeaway
Do not ask which collection is best in general. Ask what operations and data structure the problem requires.
