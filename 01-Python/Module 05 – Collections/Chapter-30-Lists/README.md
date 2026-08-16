# Chapter 30 – Lists

## 1. Introduction

A Python **list** is an ordered, mutable collection used to store multiple objects together as one logical unit.

Instead of creating separate variables:

```python
stock1 = "TCS"
stock2 = "INFY"
stock3 = "RELIANCE"
```

we can group the related values:

```python
stocks = ["TCS", "INFY", "RELIANCE"]
```

Collections make it easier to:

* Store related data
* Access elements
* Iterate over data
* Modify data
* Add and remove elements
* Pass groups of data to functions
* Process data automatically

Lists are one of the most frequently used data structures in Python.

---

# 2. What Is a List?

A list stores multiple objects in a defined sequence.

```python
marks = [85, 92, 78, 88]
```

Conceptually:

```text
marks
  │
  ▼
┌────────────────────────┐
│ 85 │ 92 │ 78 │ 88      │
└────────────────────────┘
```

The entire list is one Python object containing references to its elements.

### Core characteristics

A Python list is:

* Ordered
* Mutable
* Indexable
* Iterable
* Able to contain duplicate values
* Able to contain different object types
* Able to contain other collections

---

# 3. Creating Lists

The basic syntax is:

```python
list_name = [element1, element2, element3]
```

Example:

```python
numbers = [10, 20, 30, 40]
```

Strings:

```python
languages = ["Python", "Java", "C++"]
```

Booleans:

```python
results = [True, False, True]
```

Mixed types:

```python
data = ["Gautham", 33, True, 17.5]
```

Python permits different types inside the same list.

However, technically valid does not always mean good design. A list should generally contain data that has a meaningful relationship.

---

# 4. Lists Store References to Objects

Python variables refer to objects.

Consider:

```python
numbers = [10, 20, 30]
```

A simplified mental model is:

```text
numbers
   │
   ▼
┌─────────────────────────┐
│      list object        │
│                         │
│  reference → 10        │
│  reference → 20        │
│  reference → 30        │
└─────────────────────────┘
```

The list contains references to objects.

This explains why a list can contain different types:

```python
data = [10, "Python", True]
```

The list can contain references to an integer object, string object, and boolean object.

---

# 5. List Ordering

Lists maintain the order of their elements.

```python
numbers = [10, 20, 30, 40]
```

The sequence is:

```text
10 → 20 → 30 → 40
```

If we create:

```python
numbers = [40, 10, 30, 20]
```

Python preserves that order.

The elements are therefore associated with positions.

This allows us to access elements using **indexes**.

---

# 6. Indexing

Python uses **zero-based indexing**.

Example:

```python
numbers = [10, 20, 30, 40]
```

The indexes are:

```text
Index:     0      1      2      3
           │      │      │      │
Value:    10     20     30     40
```

Therefore:

```python
numbers[0]
```

returns:

```text
10
```

And:

```python
numbers[2]
```

returns:

```text
30
```

### Important rule

The first element is always at index `0`.

---

# 7. Why Indexing Starts at Zero

An index can be thought of as an **offset from the beginning**.

For:

```python
numbers = [10, 20, 30, 40]
```

the first element is:

```text
0 positions from the beginning
```

The second is:

```text
1 position from the beginning
```

The third is:

```text
2 positions from the beginning
```

Therefore:

```text
Index = offset from the beginning
```

This mental model becomes useful when learning slicing and other sequence operations.

---

# 8. Negative Indexing

Python also supports negative indexes.

Example:

```python
numbers = [10, 20, 30, 40]
```

Positive indexes:

```text
Index:      0      1      2      3
Value:     10     20     30     40
```

Negative indexes:

```text
Index:     -4     -3     -2     -1
Value:     10     20     30     40
```

Therefore:

```python
numbers[-1]
```

returns:

```text
40
```

And:

```python
numbers[-2]
```

returns:

```text
30
```

### Useful mental model

```text
[10, 20, 30, 40]
 ↑              ↑
first           last

 0              -1
```

Negative indexing is particularly useful when accessing elements from the end of a list.

---

# 9. List Length

Python's built-in `len()` function returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

Important distinction:

```text
Number of elements = 4
Highest positive index = 3
```

The relationship is:

```text
highest valid positive index = len(list) - 1
```

For example:

```python
numbers = [10, 20, 30, 40]
```

has:

```text
len(numbers) → 4
valid indexes → 0, 1, 2, 3
```

---

# 10. Mutability

One of the most important properties of a list is **mutability**.

A mutable object can be changed after it has been created.

Example:

```python
marks = [80, 90, 70]
```

We can modify an existing element:

```python
marks[0] = 85
```

The list becomes:

```python
[85, 90, 70]
```

We modified the existing list object.

We did not need to create a completely new variable.

---

# 11. Updating List Elements

List elements can be changed using their indexes.

```python
marks = [80, 90, 70]

marks[1] = 95

print(marks)
```

Result:

```text
[80, 95, 70]
```

The index identifies which element should be changed.

### Important

The index must refer to an existing element.

For example:

```python
marks = [80, 90, 70]
marks[1] = 95
```

is valid.

But:

```python
marks[3] = 100
```

is not valid because index `3` does not currently exist.

---

# 12. List References and Mutation

This is an important connection to Python's object/reference model.

Consider:

```python
marks = [80, 90, 70]
other = marks
```

Both variables refer to the same list object.

Conceptually:

```text
marks ───────┐
             │
             ▼
        [80, 90, 70]
             ▲
             │
other ───────┘
```

Now:

```python
marks[0] = 100
```

The list becomes:

```text
[100, 90, 70]
```

Since `other` refers to the same list, it also sees:

```python
print(other)
```

Output:

```text
[100, 90, 70]
```

---

# 13. Identity vs Equality

Two important concepts:

## Equality

```python
a == b
```

asks:

> Do these objects have equal values?

## Identity

```python
a is b
```

asks:

> Are these references pointing to the exact same object?

Example:

```python
numbers = [10, 20, 30]
other = numbers

print(numbers is other)
```

Output:

```text
True
```

because both variables reference the same list object.

### Important

Assignment:

```python
other = numbers
```

does **not** create an independent copy of the list.

Copying will be studied more deeply when we discuss list memory and copying behavior.

---

# 14. Iterating Over Lists

Lists work naturally with `for` loops.

Example:

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

Output:

```text
Python
Java
C++
```

The loop processes each element sequentially.

Mental model:

```text
List
 ↓
Take an element
 ↓
Process it
 ↓
Take the next element
 ↓
Continue
```

This connects directly to the loops learned in Module 03.

---

# 15. Lists and Functions

Lists work naturally with functions.

Example:

```python
def calculate_total(marks):
    # process marks
    pass
```

We can pass the entire collection:

```python
marks = [85, 92, 78, 88]

calculate_total(marks)
```

Instead of passing individual values:

```python
calculate_total(mark1)
calculate_total(mark2)
calculate_total(mark3)
```

This connects Module 04:

```text
Functions
```

with Module 05:

```text
Collections
```

Together they provide a powerful foundation for data processing.

---

# 16. Adding Elements

Lists can grow after creation.

For example:

```python
stocks = ["TCS", "INFY"]
```

We can add another stock:

```python
stocks.append("RELIANCE")
```

Result:

```text
["TCS", "INFY", "RELIANCE"]
```

The important concept for this chapter is:

> Lists are mutable and can change their contents after creation.

The different list methods used for adding elements will be covered systematically in:

**Chapter 31 – List Methods**

---

# 17. Removing Elements

Elements can also be removed from a list.

Conceptually:

```text
Before:
["TCS", "INFY", "ITC"]

After:
["TCS", "INFY"]
```

Python provides several methods for removing elements.

These will be covered in detail in:

**Chapter 31 – List Methods**

---

# 18. Lists with Mixed Data

Python allows heterogeneous lists:

```python
data = [10, "Python", True, 25.5]
```

This is valid because the list stores references to objects, and those objects can have different types.

However, good software design matters.

For example:

```python
marks = [85, 92, 78, 88]
```

is easier to reason about than:

```python
marks = [85, "ninety-two", True, "78"]
```

Python's flexibility should not be confused with a requirement to mix unrelated data.

### Best practice

Use heterogeneous lists when the mixed types have a meaningful relationship.

---

# 19. Nested Lists

A list can contain another list.

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Conceptually:

```text
matrix
 │
 ├── [1, 2, 3]
 ├── [4, 5, 6]
 └── [7, 8, 9]
```

This is called a **nested list**.

Nested lists can represent:

* Matrix-like structures
* Rows and columns
* Groups of records
* Hierarchical data

Nested lists will be covered in greater depth in:

**Chapter 34 – Nested Lists**

---

# 20. List Memory Model

A simplified mental model:

```python
numbers = [10, 20, 30]
```

can be represented as:

```text
numbers
   │
   ▼
┌─────────────────────┐
│     List Object     │
├─────────────────────┤
│ reference → 10      │
│ reference → 20      │
│ reference → 30      │
└─────────────────────┘
```

The list contains references to objects.

This helps explain why:

```python
data = [10, "Python", True]
```

is possible.

The list can reference objects of different types.

### Important distinction

Think separately about:

```text
The list object
```

and:

```text
The objects referenced by the list
```

This distinction becomes very important when we study:

* References
* Mutation
* Copying
* Shallow copy
* Deep copy

---

# 21. Lists vs Individual Variables

### Individual variables

```python
stock1 = "TCS"
stock2 = "INFY"
stock3 = "ITC"
```

### Collection

```python
stocks = ["TCS", "INFY", "ITC"]
```

The collection gives us a single logical object representing the group.

We can then:

```python
for stock in stocks:
    print(stock)
```

or pass the entire collection to a function:

```python
process_stocks(stocks)
```

This is significantly more scalable and maintainable.

---

# 22. Backend Development Connection

Lists are heavily used in backend applications.

For example:

```python
products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor"
]
```

A backend service might iterate over these records:

```python
for product in products:
    print(product)
```

Or pass the collection to another function:

```python
validate_products(products)
```

API responses frequently contain collections of records or values.

---

# 23. AI Engineering Connection

Lists are fundamental to AI and LLM engineering.

An AI system may process:

```text
Documents
    ↓
Document chunks
    ↓
Tokens
    ↓
Token IDs
    ↓
Embeddings
    ↓
Search results
    ↓
Model response
```

Many of these stages involve sequences or collections of values.

For example:

```python
documents = [
    "Document 1",
    "Document 2",
    "Document 3"
]
```

or conceptually:

```python
tokens = [101, 2054, 2003, 1996]
```

Lists therefore provide an important foundation for understanding later technologies such as:

* NumPy
* Pandas
* PyTorch
* Transformers
* Hugging Face
* RAG pipelines
* Dataset processing

These technologies will be studied later. For now, the important point is understanding the underlying collection concept.

---

# 24. Common Beginner Mistakes

## Mistake 1 — Forgetting zero-based indexing

Incorrect assumption:

```python
numbers[1]
```

means the first element.

Correct:

```python
numbers[0]
```

is the first element.

---

## Mistake 2 — Using an invalid index

Given:

```python
numbers = [10, 20, 30]
```

the valid positive indexes are:

```text
0
1
2
```

Therefore:

```python
numbers[3]
```

is invalid.

---

## Mistake 3 — Confusing assignment with copying

```python
other = numbers
```

does not create an independent list.

Both variables refer to the same object.

---

## Mistake 4 — Forgetting that lists are mutable

```python
numbers[0] = 100
```

modifies the existing list.

---

## Mistake 5 — Overusing mixed-type lists

Python allows:

```python
data = [10, "Python", True]
```

but unrelated types should not be mixed without a meaningful reason.

---

# 25. Best Practices

### 1. Use meaningful names

Prefer:

```python
student_marks = [85, 92, 78]
```

over:

```python
x = [85, 92, 78]
```

### 2. Keep related data together

If values logically form a group, use an appropriate collection.

### 3. Understand mutation

Know when an operation modifies an existing object.

### 4. Don't assume assignment creates a copy

Remember:

```python
other = original
```

creates another reference to the same object.

### 5. Consider data consistency

A list can technically contain anything, but its contents should normally have a meaningful relationship.

### 6. Use the collection based on requirements

Do not choose a list simply because its syntax is familiar.

Consider:

* Order
* Mutability
* Duplicates
* Required operations
* Data relationships

---

# 26. Interview Questions

## Beginner

1. What is a list?
2. How do you create a list?
3. What index does the first list element have?
4. What is negative indexing?
5. How do you find the length of a list?
6. Are Python lists mutable?
7. Can a list contain different data types?
8. Can a list contain another list?

## Intermediate

1. Why does Python use zero-based indexing?
2. What is the difference between positive and negative indexing?
3. What happens when two variables reference the same list?
4. Why does modifying one reference affect the other?
5. What is the relationship between list mutability and references?
6. Why can a heterogeneous list be valid Python but still be poor design?
7. Why are lists useful with loops?
8. Why are lists useful as function arguments?
9. What is the difference between `is` and `==`?
10. What does `len(list)` return?

---

# 27. Assignments

## Basic

Create three lists:

### List 1

Five integers.

### List 2

Five programming languages.

### List 3

Five stock symbols.

For each list:

1. Print the complete list.
2. Print the first element.
3. Print the last element.
4. Print the length.
5. Iterate through the list using a `for` loop.

---

## Intermediate

Create a list containing five student marks.

Your program should:

1. Print the marks.
2. Print the first mark.
3. Print the last mark.
4. Modify one mark.
5. Print the updated list.
6. Iterate through all marks.
7. Print the number of marks.

Focus on understanding list behavior rather than using advanced methods.

---

## Challenge

Predict the output **before running**:

```python
stocks = ["TCS", "INFY", "ITC"]

portfolio = stocks

stocks[1] = "RELIANCE"

print(stocks)
print(portfolio)
print(stocks is portfolio)
```

Then explain:

1. Why `stocks` contains the result it does.
2. Why `portfolio` contains the result it does.
3. Why `stocks is portfolio` has its result.
4. Whether `portfolio` is an independent copy.
5. What object both variables refer to.

Do not simply provide the output. Explain the reference relationship.

---

# 28. Chapter 30 Summary

A Python list is:

> **An ordered, mutable collection of objects.**

Core characteristics:

```text
List
 │
 ├── Ordered
 ├── Mutable
 ├── Indexable
 ├── Iterable
 ├── Allows duplicates
 ├── Can contain different object types
 ├── Can contain nested lists
 └── Contains references to objects
```

Basic syntax:

```python
numbers = [10, 20, 30]

numbers[0]
numbers[-1]

len(numbers)

numbers[0] = 100
```

Important mental model:

```text
Variable
   │
   ▼
List Object
   │
   ├── reference → object
   ├── reference → object
   └── reference → object
```

And:

```python
other = numbers
```

means:

> `other` refers to the same list object.

It does **not** create an independent copy.

---

# 29. Key Takeaways

* Lists group related data into one logical unit.
* Lists maintain element order.
* Python uses zero-based indexing.
* Negative indexing accesses elements from the end.
* `len()` returns the number of elements.
* Lists are mutable.
* Existing list elements can be modified.
* Lists can grow and shrink.
* Lists can be iterated with `for` loops.
* Lists can be passed to functions.
* Lists can contain different types.
* Lists can contain other lists.
* List elements are references to objects.
* Assignment creates another reference rather than an independent copy.
* `is` checks object identity.
* `==` checks value equality.
* Lists are fundamental to backend and AI data processing.
* Collection selection should always be based on requirements.

---

## Next Chapter

# Chapter 31 – List Methods

We will formally study:

* `append()`
* `extend()`
* `insert()`
* `remove()`
* `pop()`
* `clear()`
* `index()`
* `count()`
* `sort()`
* `reverse()`
* `copy()`

We will pay particular attention to the difference between:

```text
Methods that mutate the list
        vs
Methods that return a value
        vs
Methods that return None
```

This distinction is extremely important for writing correct Python code.
