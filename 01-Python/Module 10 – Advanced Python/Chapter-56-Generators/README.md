# Chapter 56 — Generators

## 1. What is a Generator?

A **generator** is a special type of iterator that produces values lazily, one at a time.

Generators use the `yield` keyword.

```python
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

After all values are produced, another `next()` raises `StopIteration`.

---

## 2. `yield` vs `return`

### `return`

```python
def example():
    return 10
```

`return` gives a value back and **ends the function**.

### `yield`

```python
def example():
    yield 10
```

`yield`:

1. Produces a value.
2. Pauses the function.
3. Preserves its execution state.
4. Allows execution to resume later.

```text
yield → PAUSE → state preserved → next() → RESUME
```

---

## 3. Generator State

Consider:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

When:

```python
gen = numbers()
```

the generator object is created.

Then:

```python
next(gen)
```

produces `1` and pauses.

The next:

```python
next(gen)
```

resumes **from where it previously paused** and produces `2`.

It does not restart from the beginning.

### Mental model

```text
next()
 ↓
yield 1
 ↓
PAUSE

next()
 ↓
resume
 ↓
yield 2
 ↓
PAUSE

next()
 ↓
resume
 ↓
yield 3
 ↓
PAUSE
```

---

## 4. Generator Function vs Generator Object

```python
def numbers():
    yield 1
    yield 2
```

`numbers` is a **generator function**.

```python
gen = numbers()
```

`gen` is a **generator object**.

```text
Generator function
        ↓ call
Generator object
        ↓ next()
Values
```

---

## 5. Generator is an Iterator

A generator object behaves as an iterator.

Therefore:

```python
gen = numbers()

next(gen)
next(gen)
```

works.

It can also be used with a `for` loop:

```python
for number in numbers():
    print(number)
```

Generators handle the iterator machinery for us.

With a custom iterator, we would manually implement:

```python
__iter__()
__next__()
```

---

## 6. Generators with Loops

```python
def numbers():
    for i in range(1, 6):
        yield i
```

Usage:

```python
for number in numbers():
    print(number)
```

Output:

```text
1
2
3
4
5
```

Values can be generated one at a time rather than being stored as a complete collection.

---

## 7. Lazy Evaluation

Generators use **lazy evaluation**.

Lazy evaluation means:

> A value is produced only when it is needed.

Instead of:

```text
Create everything
↓
Store everything
↓
Process everything
```

a generator can do:

```text
Request value
↓
Generate value
↓
Process value
↓
Request next value
```

This can greatly reduce memory usage for large datasets.

---

## 8. Example — Even Numbers

```python
def even_numbers(limit):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number
```

Usage:

```python
for number in even_numbers(10):
    print(number)
```

Output:

```text
0
2
4
6
8
10
```

---

## 9. Infinite Generators

Generators can represent an infinite sequence.

```python
def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1
```

Usage:

```python
gen = infinite_numbers()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
1
2
3
4
```

The generator can continue indefinitely because it produces only the next requested value.

---

## 10. Generator Expressions

A generator expression is a compact generator syntax.

### List comprehension

```python
numbers = [x * 2 for x in range(5)]
```

Creates the complete list immediately:

```text
[0, 2, 4, 6, 8]
```

### Generator expression

```python
numbers = (x * 2 for x in range(5))
```

Produces values lazily:

```python
print(next(numbers))  # 0
print(next(numbers))  # 2
```

Remember:

```text
[ ] → List comprehension
( ) → Generator expression
```

---

## 11. List vs Generator

### List

```python
numbers = [x * 2 for x in range(1_000_000)]
```

- Eager
- Creates all values immediately
- Stores values in memory
- Can be iterated multiple times
- Supports indexing

Example:

```python
numbers[500]
```

### Generator

```python
numbers = (x * 2 for x in range(1_000_000))
```

- Lazy
- Produces values on demand
- Generally uses much less memory
- Normally consumed once
- Does not provide random indexing like a list

Mental model:

> **List = "Give me everything now."**

> **Generator = "Give me each value when I need it."**

---

## 12. Generator Expressions with Functions

Generator expressions work well with functions such as `sum()`.

Instead of:

```python
sum([x * 2 for x in range(1_000_000)])
```

we can write:

```python
sum(x * 2 for x in range(1_000_000))
```

The second approach can process values lazily instead of first creating a million-element list.

---

## 13. `yield from`

`yield from` allows one generator to yield values from another iterable or generator.

```python
def numbers():
    yield 1
    yield 2
    yield 3

def more_numbers():
    yield 4
    yield 5
    yield 6

def all_numbers():
    yield from numbers()
    yield from more_numbers()
```

Then:

```python
for number in all_numbers():
    print(number)
```

Output:

```text
1
2
3
4
5
6
```

Think of:

```python
yield from numbers()
```

as:

> **"Yield every value produced by this iterable/generator."**

---

## 14. Generators and Files

Generators are useful for processing large files incrementally.

```python
def read_logs(filename):
    with open(filename) as file:
        for line in file:
            yield line
```

Usage:

```python
for line in read_logs("application.log"):
    process(line)
```

This avoids needing to load the entire file into memory at once.

---

## 15. Generator Pipelines

Generators can be chained into processing pipelines.

```python
def numbers():
    for i in range(1, 11):
        yield i

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number

def squares(numbers):
    for number in numbers:
        yield number ** 2
```

Pipeline:

```python
data = numbers()
even = even_numbers(data)
result = squares(even)

for number in result:
    print(number)
```

Output:

```text
4
16
36
64
100
```

Conceptually:

```text
numbers()
   ↓
1 2 3 4 5 6 7 8 9 10
   ↓
filter
   ↓
2 4 6 8 10
   ↓
transform
   ↓
4 16 36 64 100
```

Generators allow these stages to process data incrementally.

---

## 16. Generator Memory Efficiency

Compare:

```python
numbers = [x for x in range(10_000_000)]
```

with:

```python
numbers = (x for x in range(10_000_000))
```

The list stores all values.

The generator produces values on demand.

```text
List
→ eager
→ stores values
→ higher memory usage

Generator
→ lazy
→ produces values on demand
→ lower memory usage
```

### Important nuance

Generators are **not automatically faster**.

Their primary advantages are:

- Lazy evaluation
- Memory efficiency
- Streaming
- Incremental processing

A list may be preferable when you need repeated access or random indexing.

---

## 17. Generators Are Normally Consumed Once

```python
gen = (x for x in range(5))

for number in gen:
    print(number)
```

Output:

```text
0
1
2
3
4
```

The generator is now exhausted.

A second loop:

```python
for number in gen:
    print(number)
```

produces nothing.

To iterate again, create a new generator:

```python
gen = (x for x in range(5))
```

You normally cannot reset an exhausted generator.

---

## 18. Generator Exhaustion

Once a generator has no more values:

```python
next(gen)
```

raises:

```text
StopIteration
```

This connects directly to Chapter 55:

```text
Generator
   ↓
yield values
   ↓
yield values
   ↓
no more values
   ↓
StopIteration
```

---

## 19. Real-World Uses

Generators are useful for:

- Large files
- Large datasets
- Database result processing
- Data pipelines
- Streaming data
- Log processing
- ETL pipelines
- ML/data processing
- API streaming
- LLM token streaming

---

## 20. LLM/AI Connection

Suppose an LLM produces:

```text
The
 capital
 of
 India
 is
 New
 Delhi
```

A streaming system can provide pieces progressively instead of waiting for the complete response.

A simplified generator-like example:

```python
def generate_response():
    yield "The"
    yield " capital"
    yield " of"
    yield " India"
    yield " is"
    yield " New"
    yield " Delhi."
```

Then:

```python
for token in generate_response():
    print(token, end="")
```

Actual LLM streaming APIs use more sophisticated mechanisms, but the underlying idea of **incrementally producing data instead of waiting for the complete result** is closely related.

---

## 21. Iterable → Iterator → Generator

Chapter 55:

```text
Iterable
   ↓ iter()
Iterator
   ↓ next()
Values
```

Chapter 56:

```text
Generator function
       ↓ call
Generator object
       ↓ next()
Values
```

Therefore:

> **A generator is a convenient, lazy way to create an iterator.**

---

## 22. Generator Mental Model

```text
                 GENERATOR
                     │
                   yield
                     ↓
                  PAUSE
                     │
                     ↓
              state preserved
                     │
                   next()
                     ↓
                  RESUME
                     │
                     ↓
                   yield
                     │
                  PAUSE
                     │
                    ...
                     │
              no more values
                     ↓
              StopIteration
```

---

# 23. Key Takeaways

Remember these 7 points:

### 1. Generators use `yield`

```python
def numbers():
    yield 1
```

### 2. Calling a generator function creates a generator object

```python
gen = numbers()
```

### 3. `yield` pauses execution

The function's state is preserved.

### 4. `next()` resumes execution

It continues from the previous `yield`.

### 5. A generator is an iterator

It follows the iterator protocol.

### 6. Generators are lazy

Values are produced only when needed.

### 7. Generators are useful for large or streaming data

They can reduce memory usage and support incremental processing.

---

# 🧠 Final Mental Model

```text
NORMAL FUNCTION

call
 ↓
execute
 ↓
return
 ↓
DONE


GENERATOR

call
 ↓
generator object
 ↓
next()
 ↓
execute
 ↓
yield value
 ↓
PAUSE + REMEMBER STATE
 ↓
next()
 ↓
RESUME
 ↓
yield next value
 ↓
...
 ↓
StopIteration
```

### One sentence to remember

> **A generator produces values lazily, pauses at `yield`, remembers its state, and resumes from that point when `next()` is called.**

---

# Chapter 56 — Summary

**Generators are essentially a convenient mechanism for creating lazy iterators.** The most important concept is the execution model:

```text
yield → pause → preserve state → next() → resume
```

This foundation will be useful later for **streaming, FastAPI responses, async generators, data pipelines, and LLM token streaming**.
