# Chapter 18 – For Loops

## What is a for loop?

A `for` loop iterates over each element of an iterable.

```python
for variable in iterable:
    # code
```

---

## Why use a for loop?

Use a `for` loop when you need to process every item in a sequence.

Examples:

- Lists
- Strings
- Tuples
- Sets
- Dictionaries
- range()

---

## while vs for

| while | for |
|--------|-----|
| Unknown number of iterations | Iterate over a sequence |
| Manual update | Automatic update |
| Condition-based | Iterable-based |

---

## range()

### range(stop)

```python
range(5)
```

Output

```
0 1 2 3 4
```

---

### range(start, stop)

```python
range(2,6)
```

Output

```
2 3 4 5
```

---

### range(start, stop, step)

```python
range(2,11,2)
```

Output

```
2 4 6 8 10
```

Negative step

```python
range(10,0,-1)
```

Output

```
10 9 8 7 6 5 4 3 2 1
```

---

## Important Rules

- Stop value is excluded.
- `range()` is memory efficient.
- `for` loops automatically update the loop variable.

---

## Python Internals

`range()` creates a lightweight range object storing:

- start
- stop
- step

It does **not** create a full list of numbers.

Each iteration retrieves the next value as needed.

---

## Best Practices

- Prefer `for item in collection`.
- Avoid `range(len(collection))` unless you need indexes.
- Use meaningful variable names.
- Keep loop bodies small.

---

## AI Applications

- Training loops
- Processing batches
- Reading datasets
- Token generation
- API responses
- Embedding pipelines

---

## Interview Questions

1. Difference between `while` and `for`
2. Explain `range()`
3. What is an iterable?
4. Why is `range()` memory efficient?
5. How does a `for` loop work internally?

---

## Mini Project

Student Marks Analyzer

Features

- Read marks
- Highest mark
- Lowest mark
- Average
- Pass count

Without using:

- max()
- min()
- sum()