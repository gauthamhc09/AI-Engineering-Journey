# Chapter 32 – List Slicing

## 1. Introduction

List slicing allows us to extract a portion of a list using a compact syntax.

Indexing allows us to access a single element:

```python
numbers[2]
```

Slicing allows us to access multiple elements:

```python
numbers[1:4]
```

Slicing is useful for:

* Extracting portions of lists
* Selecting ranges of data
* Selecting elements at regular intervals
* Reversing a list
* Creating shallow copies
* Processing subsets of data

The fundamental slicing syntax is:

```python
list[start:stop]
```

The extended syntax is:

```python
list[start:stop:step]
```

---

# 2. Basic Slicing

Consider:

```python
numbers = [10, 20, 30, 40, 50]
```

Indexes:

```text
Index:    0    1    2    3    4
Value:   10   20   30   40   50
```

Now:

```python
numbers[1:4]
```

produces:

```text
[20, 30, 40]
```

Why?

```text
Start → 1 → included
Stop  → 4 → excluded
```

Therefore Python selects:

```text
1
2
3
```

---

# 3. The Most Important Slicing Rule

> **Start is included. Stop is excluded.**

For:

```python
numbers[1:4]
```

think:

```text
1 ≤ index < 4
```

Therefore:

```text
1
2
3
```

are selected.

Index `4` is not selected.

This rule applies regardless of whether positive or negative indexes are used.

---

# 4. Why Is the Stop Index Excluded?

The exclusive stop boundary makes it convenient to divide sequences into sections.

For example:

```python
numbers[0:2]
```

selects:

```text
[10, 20]
```

while:

```python
numbers[2:5]
```

selects:

```text
[30, 40, 50]
```

The boundaries meet cleanly:

```text
0:2
2:5
```

without overlapping.

This is a useful property when dividing data into ranges or batches.

---

# 5. Omitting Start

The start value can be omitted.

```python
numbers[:3]
```

means:

> Start from the beginning and stop before index `3`.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
```

Output:

```text
[10, 20, 30]
```

Equivalent mental model:

```text
[:3]
 ↓
beginning → before index 3
```

---

# 6. Omitting Stop

The stop value can also be omitted.

```python
numbers[2:]
```

means:

> Start at index `2` and continue to the end.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2:])
```

Output:

```text
[30, 40, 50]
```

Mental model:

```text
[2:]
 ↓
index 2 → end
```

---

# 7. Full Slicing Syntax

The complete syntax is:

```python
list[start:stop:step]
```

There are three components:

```text
[start : stop : step]
    │      │      │
    │      │      └── how far to move
    │      └───────── where to stop (excluded)
    └──────────────── where to start
```

Example:

```python
numbers[0:5:2]
```

means:

```text
Start → index 0
Stop  → before index 5
Step  → move by 2
```

---

# 8. Step

The `step` determines how the indexes are traversed.

Consider:

```python
numbers = [10, 20, 30, 40, 50, 60]
```

Then:

```python
numbers[0:6:2]
```

selects:

```text
Indexes:

0 → 2 → 4
```

Result:

```text
[10, 30, 50]
```

### Important terminology

A step of `2` means:

> Move by two index positions.

It is better to say:

```text
step = 2
```

rather than:

```text
skip 2 elements
```

because the exact behavior is movement between indexes.

---

# 9. Default Step

If the step is omitted, it defaults to:

```text
1
```

Therefore:

```python
numbers[0:5]
```

and:

```python
numbers[0:5:1]
```

produce the same result.

---

# 10. Step of 2

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[::2]
```

Indexes selected:

```text
0 → 2 → 4
```

Result:

```text
[10, 30, 50]
```

---

# 11. Step of 3

Example:

```python
numbers[::3]
```

For:

```python
numbers = [10, 20, 30, 40, 50, 60]
```

the indexes are:

```text
0 → 3
```

Result:

```text
[10, 40]
```

---

# 12. Negative Indexing in Slices

Negative indexes can be used with slicing.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

Negative indexes:

```text
Index:   -5   -4   -3   -2   -1
Value:   10   20   30   40   50
```

Therefore:

```python
numbers[-3:]
```

returns:

```text
[30, 40, 50]
```

This means:

> Start at the third element from the end and continue to the end.

---

# 13. Negative Start and Stop

Example:

```python
numbers[-4:-1]
```

Given:

```text
Index:   -5   -4   -3   -2   -1
Value:   10   20   30   40   50
```

Start:

```text
-4 → included
```

Stop:

```text
-1 → excluded
```

Therefore:

```text
[20, 30, 40]
```

The rule remains:

> Start included, stop excluded.

---

# 14. Reversing with Slicing

A negative step moves backwards.

The most common example is:

```python
numbers[::-1]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

reverse_copy = numbers[::-1]
```

Result:

```text
[50, 40, 30, 20, 10]
```

Breakdown:

```text
start → omitted
stop  → omitted
step  → -1
```

Therefore Python traverses the list from the end toward the beginning.

---

# 15. Negative Step with Explicit Boundaries

Example:

```python
numbers = [10, 20, 30, 40, 50]

numbers[4:1:-1]
```

Indexes visited:

```text
4 → 3 → 2
```

Index `1` is excluded.

Result:

```text
[50, 40, 30]
```

Even when moving backwards:

> Start is included and stop is excluded.

---

# 16. `reverse()` vs `[::-1]`

These are not the same operation.

## `reverse()`

```python
numbers.reverse()
```

* Modifies the existing list
* Returns `None`

Example:

```python
numbers = [10, 20, 30]

numbers.reverse()

print(numbers)
```

Result:

```text
[30, 20, 10]
```

The original list has changed.

---

## `[::-1]`

```python
reversed_numbers = numbers[::-1]
```

* Creates a new list
* Does not modify the original list

Example:

```python
numbers = [10, 20, 30]

reversed_numbers = numbers[::-1]
```

Conceptually:

```text
numbers
    ↓
[10, 20, 30]

reversed_numbers
    ↓
[30, 20, 10]
```

They are different list objects.

---

# 17. Slicing Creates a New List

Consider:

```python
numbers = [10, 20, 30, 40]

part = numbers[1:3]
```

Result:

```text
part → [20, 30]
```

`part` is a new list object.

Therefore:

```python
print(numbers is part)
```

returns:

```text
False
```

Conceptually:

```text
numbers ─────→ [10, 20, 30, 40]

part ────────→ [20, 30]
```

The two outer list objects are separate.

---

# 18. Slicing as a Shallow Copy

The following creates a shallow copy:

```python
numbers[:]
```

Example:

```python
numbers = [10, 20, 30]

other = numbers[:]

print(numbers is other)
```

Output:

```text
False
```

This is similar to:

```python
other = numbers.copy()
```

Both create a new outer list.

---

# 19. Shallow Copy and References

Consider:

```python
numbers = [10, 20, 30]

other = numbers[:]
```

Conceptually:

```text
numbers ─────→ [reference → 10
                reference → 20
                reference → 30]

other ───────→ [reference → 10
                reference → 20
                reference → 30]
```

There are two list objects.

The elements inside them are references to the same underlying objects.

For immutable values such as integers, this is usually straightforward.

Nested mutable objects make the situation more important.

---

# 20. Nested Lists and Shallow Copy

Consider:

```python
numbers = [
    [1, 2],
    [3, 4]
]

copy = numbers[:]
```

The outer lists are different:

```text
numbers ─────→ outer list
copy ────────→ different outer list
```

But the inner lists are shared:

```text
numbers ─────→ [1, 2]
                  ↑
copy ─────────────┘
```

and:

```text
numbers ─────→ [3, 4]
                  ↑
copy ─────────────┘
```

Therefore:

> Slicing performs a **shallow copy**, not a recursive deep copy.

This topic will become increasingly important as we work with nested data structures.

---

# 21. Mutation After Slicing

Example:

```python
numbers = [10, 20, 30, 40]

part = numbers[1:3]

part[0] = 999
```

The result is:

```text
numbers → [10, 20, 30, 40]

part    → [999, 30]
```

The original outer list does not change.

Why?

Because `part` is a separate list object.

---

# 22. Out-of-Range Slices

Consider:

```python
numbers = [10, 20, 30]

print(numbers[5:8])
```

Result:

```text
[]
```

A slice beyond the available range generally returns the available portion rather than raising an `IndexError`.

Compare this with direct indexing:

```python
numbers[5]
```

which raises:

```text
IndexError
```

Important distinction:

```text
Direct indexing
→ invalid index can raise an error

Slicing
→ out-of-range boundaries are generally handled gracefully
```

---

# 23. Common Slicing Patterns

### Entire list

```python
numbers[:]
```

Creates a shallow copy.

### First three

```python
numbers[:3]
```

### From index 3 to the end

```python
numbers[3:]
```

### Last three

```python
numbers[-3:]
```

### Every second element

```python
numbers[::2]
```

### Every second element starting at index 1

```python
numbers[1::2]
```

### Reversed copy

```python
numbers[::-1]
```

---

# 24. Python Internals

For:

```python
part = numbers[1:3]
```

Python creates a new list object containing references to the selected elements.

Conceptually:

```text
Original list
┌────────────────────────────┐
│ ref → 10 │ ref → 20 │ ... │
└────────────────────────────┘
              │
              │ selected
              ▼
New list
┌───────────────────┐
│ ref → 20 │ ref → 30 │
└───────────────────┘
```

Therefore:

* A new outer list is created.
* Selected element references are placed into the new list.
* The original outer list is unchanged.
* Nested mutable objects may still be shared.

This is the basis of shallow copying.

---

# 25. Backend Engineering Connection

Slicing can be useful when processing subsets of data.

For example:

```python
records = [
    "record1",
    "record2",
    "record3",
    "record4",
    "record5"
]
```

We can select:

```python
first_batch = records[:2]
```

and:

```python
remaining = records[2:]
```

This provides a simple foundation for working with:

* Batches
* Data subsets
* Pagination concepts
* Processing chunks of records

---

# 26. AI Engineering Connection

AI systems frequently process sequences.

Examples include:

* Token sequences
* Text chunks
* Dataset batches
* Search results
* Feature sequences
* Context windows

For example:

```python
tokens = [101, 2054, 2003, 1996, 2023, 3185]
```

A section of the sequence can be selected using slicing:

```python
tokens[:4]
```

The same basic sequence reasoning later appears in:

* NumPy
* PyTorch
* Tokenizers
* Transformers
* Dataset processing
* RAG pipelines

The technologies will be taught later. For now, the goal is to master Python's sequence model.

---

# 27. Common Beginner Mistakes

## Mistake 1 — Including the stop index

Incorrect assumption:

```python
numbers[1:4]
```

includes index `4`.

Correct:

```text
Indexes selected:
1, 2, 3
```

---

## Mistake 2 — Confusing indexing with slicing

```python
numbers[2]
```

returns one element.

```python
numbers[2:3]
```

returns a new list containing that element.

Example:

```text
numbers[2]
→ 30

numbers[2:3]
→ [30]
```

---

## Mistake 3 — Assuming slicing modifies the original

```python
part = numbers[1:3]
```

does not modify `numbers`.

It creates another list.

---

## Mistake 4 — Confusing `reverse()` with `[::-1]`

```python
numbers.reverse()
```

mutates the original list.

```python
numbers[::-1]
```

creates a reversed copy.

---

## Mistake 5 — Misunderstanding step

```python
numbers[::2]
```

means:

> Move through indexes with a step of 2.

It does not mean "remove two elements between every selected element."

---

## Mistake 6 — Forgetting shallow-copy behavior

Slicing creates a new outer list, but nested mutable objects may still be shared.

---

# 28. Best Practices

### 1. Use slicing when the intent is clear

Prefer:

```python
first_three = numbers[:3]
```

when the goal is clearly to select the first three elements.

### 2. Keep complex slices readable

Compact syntax is useful, but readability is more important than cleverness.

### 3. Understand the memory implications

Slicing creates another list object.

For very large collections, repeated slicing can create additional memory usage.

### 4. Use the correct tool for mutation

If you want to reverse the existing list:

```python
numbers.reverse()
```

If you want a reversed copy:

```python
reversed_numbers = numbers[::-1]
```

### 5. Remember the boundary rule

Always verify:

```text
Start → included
Stop → excluded
```

---

# 29. Interview Questions

## Beginner

1. What is list slicing?
2. What is the syntax for list slicing?
3. Is the start index included?
4. Is the stop index included?
5. What does `numbers[:3]` mean?
6. What does `numbers[2:]` mean?
7. What does `numbers[-3:]` mean?
8. What does `numbers[::-1]` do?
9. What does the step parameter control?
10. Can negative indexes be used in slicing?

---

## Intermediate

1. Why is the stop index excluded?
2. What is the difference between:

   ```python
   numbers[2]
   ```

   and:

   ```python
   numbers[2:3]
   ```
3. Does slicing modify the original list?
4. Why does slicing create a new list?
5. What is a shallow copy?
6. What is the difference between:

   ```python
   numbers.reverse()
   ```

   and:

   ```python
   numbers[::-1]
   ```
7. What happens when a slice goes beyond the list's boundaries?
8. What does `numbers[::2]` mean?
9. What does `numbers[1::2]` mean?
10. Why can slicing have memory implications?

---

## Advanced Reasoning

### 1.

Why does:

```python
numbers[:] is numbers
```

evaluate to `False`?

### 2.

Why can:

```python
copy = original[:]
```

still share nested mutable objects with `original`?

### 3.

Explain the difference between:

```python
numbers[1:4]
```

and:

```python
numbers[1:4:2]
```

### 4.

Why does:

```python
numbers[::-1]
```

produce a new list while:

```python
numbers.reverse()
```

modifies the existing list?

---

# 30. Assignments

## Basic

Given:

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
```

Create slices for:

1. First three elements
2. Last three elements
3. Elements from index `2` to the end
4. Elements from index `1` through `4`
5. Every second element
6. The entire list using slicing
7. A reversed copy

---

## Intermediate

Given:

```python
numbers = [10, 20, 30, 40, 50, 60]
```

Predict the output **before executing**:

```python
print(numbers[1:5])
print(numbers[:4])
print(numbers[3:])
print(numbers[-3:])
print(numbers[::2])
print(numbers[1::2])
print(numbers[::-1])
```

For every slice, identify:

* Start
* Stop
* Step
* Selected indexes
* Final result

---

## Challenge

Predict the output:

```python
numbers = [10, 20, 30, 40]

part = numbers[1:3]

part[0] = 999

print(numbers)
print(part)
print(numbers is part)
```

Then explain:

1. Why the original list does or does not change.
2. Why `part` is a separate object.
3. What slicing created.
4. How this relates to shallow copying.

---

## Engineering Challenge

Create:

```python
stocks = [
    "TCS",
    "INFY",
    "RELIANCE",
    "HDFCBANK",
    "ITC",
    "NESTLE",
    "COLPAL"
]
```

Using **only slicing**, create:

1. The first three stocks.
2. The last three stocks.
3. Stocks at even indexes.
4. Stocks at odd indexes.
5. A reversed copy.
6. A complete shallow copy.

Then verify which objects are the same using `is`.

---

# 31. Chapter 32 Summary

List slicing allows us to extract portions of lists using:

```python
list[start:stop:step]
```

The fundamental rule is:

> **Start is included. Stop is excluded.**

Examples:

```python
numbers[:3]
```

First three elements.

```python
numbers[2:]
```

From index `2` to the end.

```python
numbers[-3:]
```

Last three elements.

```python
numbers[::2]
```

Every second element.

```python
numbers[::-1]
```

Reversed copy.

Slicing creates a new list object.

Therefore:

```python
copy = numbers[:]
```

creates a shallow copy.

The outer list is independent, but nested mutable objects can still be shared.

---

# 32. Key Takeaways

* Slicing extracts multiple elements from a list.
* Slicing uses `[start:stop:step]`.
* Start is included.
* Stop is excluded.
* Step controls movement between indexes.
* Step defaults to `1`.
* Negative indexes can be used.
* Negative steps move backwards.
* `[::-1]` creates a reversed copy.
* `reverse()` modifies the original list.
* Slicing creates a new outer list.
* `[:]` can be used to create a shallow copy.
* Slicing does not recursively copy nested objects.
* Out-of-range slices generally do not raise `IndexError`.
* Slicing is useful for data processing.
* Slicing concepts transfer to AI sequence processing and later tools such as NumPy and PyTorch.
* Memory behavior becomes important when slicing large collections.

---

# Chapter 32 Completion Criteria

Before moving to Chapter 33, you should be able to explain without memorizing:

```text
[start:stop]
[start:stop:step]
[:stop]
[start:]
[::step]
[::-1]
```

and answer:

> **Why does slicing create a new list, while `reverse()` modifies the existing list?**

You should also be comfortable explaining the difference between:

```python
numbers[2]
```

and:

```python
numbers[2:3]
```

Once these concepts are solid, we move to:

# Chapter 33 – List Comprehensions
