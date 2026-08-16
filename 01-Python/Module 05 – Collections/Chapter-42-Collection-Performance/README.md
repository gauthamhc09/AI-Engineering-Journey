# Chapter 42 — Collection Performance

## Why performance matters
The collection you choose affects how efficiently Python can search and access data.

## List membership
```python
"TCS" in stocks
```
A list may need to examine many elements.

Approximate complexity:
```text
O(n)
```

## Set membership
```python
"TCS" in stocks
```
Sets use hashing and provide approximately constant-time average membership checks:
```text
O(1) average
```

## Dictionary key lookup
```python
prices = {"INFY": 1500, "TCS": 3500}
prices["TCS"]
```

Approximately:
```text
O(1) average
```

## Practical comparison
```text
List       → ordered sequence
Set        → unique values + fast membership
Dictionary → key → value lookup
```

## Important trade-off
Do not choose a set or dictionary only because it is often faster.

If order and positional access matter:
```python
items = ["A", "B", "C"]
items[0]
```
a list is the natural choice.

## Backend example
For:
```text
user_id → user information
```
a dictionary is natural:
```python
users = {
    101: {"name": "Anita"},
    102: {"name": "Rahul"}
}
users[102]
```

For repeated membership checks:
```python
user_ids = {101, 102, 103}
101 in user_ids
```

## Key takeaway
Data requirements come first; performance is considered after choosing an appropriate structure.
