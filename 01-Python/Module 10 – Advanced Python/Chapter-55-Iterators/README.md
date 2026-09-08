# Chapter 55 — Iterators

## 1. What is an Iterator?

An **iterator** is an object that allows us to traverse through data **one item at a time**.

An iterator keeps track of its current position and knows how to provide the next value.

```text
Iterable
   ↓ iter()
Iterator
   ↓ next()
Value
   ↓
Value
   ↓
StopIteration
```

---

## 2. Iterable vs Iterator

### Iterable

An **iterable** is an object that can be iterated over.

Common examples:

- `list`
- `tuple`
- `string`
- `set`
- `dict`

Example:

```python
numbers = [10, 20, 30]
```

The list is an **iterable**.

We can obtain an iterator from it:

```python
iterator = iter(numbers)
```

### Iterator

An **iterator** is an object that produces values one at a time.

```python
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

### Easy mental model

> **Iterable = something you can loop over.**

> **Iterator = something that remembers where you are and gives you the next item.**

---

## 3. The `iter()` Function

Python's built-in `iter()` function obtains an iterator from an iterable.

```python
numbers = [10, 20, 30, 40]

iterator = iter(numbers)
```

Now `iterator` can be consumed using `next()`.

---

## 4. The `next()` Function

`next()` retrieves the next value from an iterator.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

Each call advances the iterator.

---

## 5. Iterator Maintains State

One of the most important properties of an iterator is that it **maintains state**.

Consider:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)
```

Initially, the iterator is conceptually positioned before the first value:

```text
10   20   30
↑
next value
```

After:

```python
next(iterator)
```

it returns `10` and moves forward.

Conceptually:

```text
10   20   30
     ↑
 next value
```

Another `next()` returns `20`, and so on.

This means an iterator remembers **where it currently is**.

---

## 6. `StopIteration`

What happens when there are no more values?

```python
numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # StopIteration
```

Once the iterator is exhausted, calling `next()` raises:

```python
StopIteration
```

`StopIteration` means:

> **There are no more values to produce.**

It is not normally an error in a `for` loop. Python uses it internally to know when iteration is finished.

---

## 7. How a `for` Loop Works Internally

When we write:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Python conceptually performs something similar to:

```python
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
```

Therefore, a `for` loop fundamentally relies on:

```text
iter()
next()
StopIteration
```

This is called the **iterator protocol**.

---

## 8. Iterator Protocol

An object behaves as an iterator by following Python's iterator protocol.

The important methods are:

```python
__iter__()
__next__()
```

### `__iter__()`

Returns an iterator.

### `__next__()`

Returns the next value.

When there are no more values, `__next__()` must raise:

```python
StopIteration
```

---

## 9. Creating a Custom Iterator

We can create our own iterator using a class.

```python
class Counter:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration
```

Usage:

```python
counter = Counter(3)

print(next(counter))
print(next(counter))
print(next(counter))
```

Output:

```text
1
2
3
```

The next call:

```python
next(counter)
```

raises:

```text
StopIteration
```

---

## 10. Using a Custom Iterator with `for`

Because our `Counter` implements the iterator protocol, we can use it with a `for` loop.

```python
counter = Counter(3)

for number in counter:
    print(number)
```

Output:

```text
1
2
3
```

Python internally calls `iter()` and repeatedly calls `next()` until `StopIteration` occurs.

---

## 11. Why Iterators Matter

At first, iterators may seem more complicated than simply using a list.

Their real value becomes clear when dealing with large amounts of data.

Suppose we have:

```text
10 million records
```

Creating and storing all records in memory at once can consume significant memory.

An iterator can instead provide:

```text
record 1
record 2
record 3
...
```

one at a time.

This introduces the idea of **lazy evaluation**.

---

## 12. Lazy Evaluation

**Lazy evaluation** means producing a value only when it is actually needed.

Instead of:

```text
Create everything
      ↓
Store everything
      ↓
Process everything
```

we can have:

```text
Request value
      ↓
Generate value
      ↓
Process value
      ↓
Request next value
```

This can significantly reduce memory usage.

Lazy evaluation becomes especially important in:

- large datasets
- file processing
- database results
- data pipelines
- ML pipelines
- streaming systems
- LLM applications

---

## 13. Iterator Example

Your example:

```python
numbers = [10, 20, 30, 40]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        print("Stop Iteration")
        break
```

Output:

```text
10
20
30
40
Stop Iteration
```

### What happens?

1. `iter(numbers)` creates an iterator.
2. `next(iterator)` returns `10`.
3. The iterator moves forward.
4. `next(iterator)` returns `20`.
5. Then `30`.
6. Then `40`.
7. The next `next()` call finds no remaining value.
8. Python raises `StopIteration`.
9. The `except` block catches it.
10. `break` exits the `while` loop.

Your understanding is correct:

> **The final `next()` does not return a value because the iterator is exhausted; it raises `StopIteration`, which signals that iteration is complete.**

---

# 14. Important Distinction

Do not confuse these:

```python
numbers = [10, 20, 30]
```

with:

```python
iterator = iter(numbers)
```

The list is an **iterable**.

The object returned by `iter(numbers)` is an **iterator**.

A useful relationship is:

```text
Iterable
   │
   │ iter()
   ↓
Iterator
   │
   │ next()
   ↓
Individual values
```

---

# 15. Key Takeaways

Remember these points:

### 1. Iterable

Something that can be iterated over.

```python
numbers = [1, 2, 3]
```

### 2. Iterator

An object that produces values one at a time.

```python
iterator = iter(numbers)
```

### 3. `iter()`

Obtains an iterator from an iterable.

```python
iter(numbers)
```

### 4. `next()`

Gets the next value.

```python
next(iterator)
```

### 5. `StopIteration`

Signals that the iterator has no more values.

### 6. Iterator protocol

Based on:

```python
__iter__()
__next__()
```

### 7. `for` loops use iterators internally

Conceptually:

```python
iterator = iter(iterable)

while True:
    try:
        value = next(iterator)
    except StopIteration:
        break
```

### 8. Iterators maintain state

They remember where they are during iteration.

### 9. Iterators enable lazy processing

Values can be produced one at a time instead of loading everything into memory.

---

# 🧠 Chapter 55 Mental Model

```text
                 ITERABLE
                    │
                  iter()
                    ↓
                 ITERATOR
                    │
                  next()
                    ↓
                  VALUE
                    │
                  next()
                    ↓
                  VALUE
                    │
                  next()
                    ↓
             No more values
                    │
                    ↓
            StopIteration
```

### One sentence to remember

> **An iterable can give you an iterator; an iterator gives you one value at a time and remembers its position until it is exhausted.**

---

# 🔗 Connection to Chapter 56

Iterators are the foundation for **Generators**.

Manually creating an iterator requires:

```python
__iter__()
__next__()
StopIteration
```

Generators give us a much simpler way:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

The `yield` keyword allows Python to automatically handle much of the iterator machinery.

**Next: Chapter 56 — Generators**
