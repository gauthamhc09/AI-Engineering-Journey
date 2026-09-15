# Chapter 60 — Python Dataclasses

## 1. What is a dataclass?
A dataclass is a regular Python class designed to reduce boilerplate when storing structured data.

```python
from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    price: float
```

By default, `@dataclass` generates methods such as `__init__()`, `__repr__()`, and `__eq__()`. Type annotations describe expected types; they do **not** validate values at runtime.

## 2. Equality
Generated equality compares corresponding fields:

```python
Stock("TCS", 3200.0) == Stock("TCS", 3200.0)  # True
```

Ordinary classes can define `__eq__()` too. Without a custom implementation, equality normally compares object identity.

## 3. Custom methods
Dataclasses can have normal methods:

```python
@dataclass
class Stock:
    symbol: str
    price: float
    quantity: int

    def calculate_value(self) -> float:
        return self.price * self.quantity
```

Call `stock.calculate_value()`. Python supplies the instance as `self`.

## 4. Default values and field order
Fields without defaults must come before fields with defaults in the generated initializer.

```python
@dataclass
class Stock:
    symbol: str
    quantity: int = 1
    price: float = 0.0
```

This rule also matters with inheritance.

## 5. Mutable defaults: `default_factory`
Avoid shared mutable defaults such as `holdings: dict = {}`. Use a factory:

```python
from dataclasses import dataclass, field

@dataclass
class Portfolio:
    holdings: dict[str, float] = field(default_factory=dict)
```

Each instance receives a fresh dictionary. Pass the callable `dict`, not `dict()`.

```python
p1 = Portfolio()
p2 = Portfolio()
p1.holdings["TCS"] = 3200.0

print(p1.holdings)  # {'TCS': 3200.0}
print(p2.holdings)  # {}
```

This also works with `list` and `set`.

## 6. `field()` options
- `repr=False`: omits a field from the generated representation, but the attribute still exists.
- `compare=False`: excludes a field from generated equality comparisons.

```python
@dataclass
class Stock:
    symbol: str
    price: float
    internal_id: int = field(compare=False)

Stock("TCS", 3200.0, 101) == Stock("TCS", 3200.0, 202)  # True
```

## 7. `__post_init__()`
The generated `__init__()` calls `__post_init__()` after assigning fields. Use it for extra initialization or validation:

```python
@dataclass
class Stock:
    symbol: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
```

If it raises an exception, construction does not complete successfully.

## 8. `frozen=True`
`@dataclass(frozen=True)` prevents field reassignment after initialization; assignment raises `dataclasses.FrozenInstanceError`. This is shallow immutability: a mutable object inside a frozen dataclass may still be mutated.

## 9. `asdict()` and `astuple()`
```python
from dataclasses import asdict, astuple

asdict(stock)   # dictionary of fields
astuple(stock)  # tuple of field values
```

Values follow field-definition order. Nested dataclasses and containers are recursively converted.

## 10. `replace()`
`replace()` creates a new instance with selected fields changed; it does not mutate the original.

```python
from dataclasses import replace

updated = replace(original, price=3300.0)
```

Unspecified fields retain their original values.

## 11. `ClassVar`
`ClassVar` marks class-level data, not a dataclass field:

```python
from typing import ClassVar

@dataclass
class Stock:
    symbol: str
    currency: ClassVar[str] = "INR"
```

`currency` is excluded from the generated constructor, representation, and field comparisons. `Stock("TCS", "USD")` raises `TypeError`; change it explicitly with `Stock.currency = "USD"`.

## 12. Dataclass inheritance
Child dataclasses include inherited fields before their own fields:

```python
@dataclass
class Asset:
    symbol: str
    price: float

@dataclass
class Stock(Asset):
    quantity: int
```

A required child field cannot follow a defaulted parent field in the generated initializer; that raises `TypeError`. Give the child field a default or redesign the field order.

## 13. `order=True`
Generates ordering comparisons based on fields in definition order, like tuples. It does not automatically sort by price.

```python
@dataclass(order=True)
class Stock:
    symbol: str
    price: float
```

For price-based sorting, use `sorted(stocks, key=lambda stock: stock.price)`.

## 14. `slots=True`
`@dataclass(slots=True)` restricts arbitrary new instance attributes and can reduce memory use when creating many instances. An undeclared attribute assignment may raise `AttributeError`. Availability depends on Python version.

## Chapter summary
Dataclasses are useful when a class primarily represents structured data. They reduce repetitive code while allowing custom methods.

Remember:
- Type hints are not runtime validation.
- Use `default_factory` for mutable defaults.
- `repr=False` affects representation; `compare=False` affects generated equality.
- `__post_init__()` runs after generated initialization.
- `frozen=True` prevents field reassignment, not deep mutation.
- `asdict()` / `astuple()` convert; `replace()` creates a new instance.
- `ClassVar` is class-level, not a dataclass field.
- Inheritance follows field-ordering rules.
- `order=True` compares in field order; `slots=True` restricts dynamic attributes.

## Quick self-check
1. Why use `field(default_factory=list)` instead of `items: list = []`?
2. What does `repr=False` change—and what does it not change?
3. When does `__post_init__()` run?
4. Does `frozen=True` make nested lists immutable?
5. Which field does `order=True` compare first?
6. What does `replace()` return?
