# Chapter 33 – List Comprehensions

## 1. Introduction

List comprehensions provide a concise way to create a new list from an existing iterable.

Instead of writing:

result = []

for number in numbers:
    result.append(number * 2)

we can write:

result = [number * 2 for number in numbers]

Both approaches produce the same result.

List comprehensions are especially useful for:

- Transforming data
- Filtering data
- Creating derived lists
- Cleaning data
- Processing collections
- Simple data-preprocessing tasks

The goal is not simply to write shorter code.

The important goal is to understand:

> How a normal `for` loop that builds a list can be expressed as a list comprehension.

---

# 2. Basic Syntax

The basic syntax is:

[expression for item in iterable]

Example:

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)

Output:

    [1, 4, 9, 16, 25]

Break the syntax into three parts:

    [ expression for item in iterable ]
          |           |          |
          |           |          +-- source collection
          |           +------------- loop variable
          +------------------------- value added to new list

---

# 3. Mental Model

Consider:

squares = [number * number for number in numbers]

Read it as:

> For each number in numbers, calculate `number * number` and put the result into a new list.

Equivalent normal loop:

squares = []

for number in numbers:
    squares.append(number * number)

This mental translation is one of the most important skills for understanding list comprehensions.

---

# 4. First Example

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)

Output:

    [2, 4, 6, 8, 10]

Processing:

    1 → 1 * 2 → 2
    2 → 2 * 2 → 4
    3 → 3 * 2 → 6
    4 → 4 * 2 → 8
    5 → 5 * 2 → 10

---

# 5. The Expression Comes First

This is one of the unusual parts of list comprehension syntax.

Normal loop:

for number in numbers:
    print(number * 2)

List comprehension:

[number * 2 for number in numbers]

The value/expression being produced comes before the `for`.

Think:

    Normal loop:

    for number in numbers
        ↓
    number * 2


    List comprehension:

    number * 2
        ↓
    for number in numbers

---

# 6. Creating a New List

List comprehensions create a new list.

Example:

numbers = [1, 2, 3, 4]

squares = [number * number for number in numbers]

The original list remains unchanged.

Conceptually:

    numbers
       ↓
    [1, 2, 3, 4]

          |
          | transform
          ↓

    squares
       ↓
    [1, 4, 9, 16]

This is different from methods such as `append()` that mutate an existing list.

---

# 7. Transforming Strings

List comprehensions work with strings as well.

Example:

names = ["gautham", "rahul", "arun"]

upper_names = [name.upper() for name in names]

print(upper_names)

Output:

    ["GAUTHAM", "RAHUL", "ARUN"]

Equivalent loop:

upper_names = []

for name in names:
    upper_names.append(name.upper())

---

# 8. Filtering with `if`

List comprehensions can filter elements.

Syntax:

[item for item in iterable if condition]

Example:

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)

Output:

    [2, 4, 6]

The condition determines whether an element is included.

---

# 9. Understanding Filtering

Consider:

[number for number in numbers if number % 2 == 0]

Read it as:

> For every number in numbers, include the number only if it is even.

Equivalent loop:

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

The comprehension is simply a compact representation of this pattern.

---

# 10. Filtering vs Transformation

These are different operations.

## Filtering

[number for number in numbers if number > 5]

This decides:

> Which elements should remain?

Example:

numbers = [1, 2, 3, 6, 7, 8]

Result:

    [6, 7, 8]

---

## Transformation

[number * 2 for number in numbers]

This decides:

> What should each element become?

Example:

numbers = [1, 2, 3]

Result:

    [2, 4, 6]

---

# 11. Filtering + Transformation

Both can be performed together.

Example:

numbers = [1, 2, 3, 4, 5, 6]

even_squares = [
    number * number
    for number in numbers
    if number % 2 == 0
]

Result:

    [4, 16, 36]

Processing:

    1 → odd → ignore
    2 → even → 2 * 2 → 4
    3 → odd → ignore
    4 → even → 4 * 4 → 16
    5 → odd → ignore
    6 → even → 6 * 6 → 36

Equivalent loop:

even_squares = []

for number in numbers:
    if number % 2 == 0:
        even_squares.append(number * number)

---

# 12. Three Core Patterns

These three patterns are fundamental.

## Pattern 1 — Transform

[expression for item in iterable]

Example:

[number * 2 for number in numbers]

---

## Pattern 2 — Filter

[item for item in iterable if condition]

Example:

[number for number in numbers if number % 2 == 0]

---

## Pattern 3 — Filter + Transform

[expression for item in iterable if condition]

Example:

[number * 2 for number in numbers if number % 2 == 0]

The third pattern is particularly useful in data processing.

---

# 13. Conditional Expression

List comprehensions can also use `if/else`.

Syntax:

[true_value if condition else false_value for item in iterable]

Example:

numbers = [1, 2, 3, 4, 5]

result = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]

print(result)

Output:

    ["odd", "even", "odd", "even", "odd"]

---

# 14. Filtering vs Conditional Transformation

This distinction is important.

## Filtering

[number for number in numbers if number % 2 == 0]

Result:

    [2, 4]

Odd numbers disappear.

---

## Conditional transformation

["even" if number % 2 == 0 else "odd"
 for number in numbers]

Result:

    ["odd", "even", "odd", "even", "odd"]

Every input element produces an output.

Think:

    Filtering
        ↓
    Some elements disappear.


    Conditional transformation
        ↓
    Every element gets transformed.

---

# 15. Important Syntax Difference

Filtering:

[number for number in numbers if number > 5]

The `if` comes at the end.

Conditional expression:

[number if number > 5 else 0 for number in numbers]

The `if/else` expression comes before the `for`.

These are different patterns.

---

# 16. Nested Loops

List comprehensions can represent nested loops.

Normal loops:

pairs = []

for x in [1, 2]:
    for y in [10, 20]:
        pairs.append((x, y))

Equivalent comprehension:

pairs = [(x, y) for x in [1, 2] for y in [10, 20]]

Result:

    [(1, 10), (1, 20), (2, 10), (2, 20)]

The order follows the same order as the nested loops.

---

# 17. Nested List Comprehension

Consider:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

To flatten the matrix:

result = [
    number
    for row in matrix
    for number in row
]

Result:

    [1, 2, 3, 4, 5, 6]

Equivalent loops:

result = []

for row in matrix:
    for number in row:
        result.append(number)

---

# 18. Filtering Nested Data

We can combine nested loops and filtering.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

even_numbers = [
    number
    for row in matrix
    for number in row
    if number % 2 == 0
]

Result:

    [2, 4, 6]

---

# 19. Transforming Nested Data

Example:

matrix = [
    [1, 2],
    [3, 4]
]

squares = [
    number * number
    for row in matrix
    for number in row
]

Result:

    [1, 4, 9, 16]

The result is a flat list.

---

# 20. Preserving Nested Structure

A nested comprehension can preserve the structure.

Example:

matrix = [
    [1, 2],
    [3, 4]
]

result = [
    [number * 2 for number in row]
    for row in matrix
]

Result:

    [
        [2, 4],
        [6, 8]
    ]

The inner comprehension creates each transformed row.

The outer comprehension creates the new matrix.

---

# 21. List Comprehensions with Functions

List comprehensions can call functions.

Example:

def square(number):
    return number * number

numbers = [1, 2, 3, 4]

squares = [square(number) for number in numbers]

print(squares)

Output:

    [1, 4, 9, 16]

This connects list comprehensions directly to functions.

---

# 22. List Comprehensions with Functions and Conditions

Example:

def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if is_even(number)
]

Result:

    [2, 4, 6]

This combines:

    Functions
        +
    Collections
        +
    Control Flow

---

# 23. Backend Engineering Connection

List comprehensions are common when processing API data.

Example:

users = [
    {"name": "Gautham", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Arun", "active": True}
]

Extract names:

names = [user["name"] for user in users]

Result:

    ["Gautham", "Rahul", "Arun"]

Filter active users:

active_users = [
    user
    for user in users
    if user["active"]
]

Extract names of active users:

active_names = [
    user["name"]
    for user in users
    if user["active"]
]

These patterns are very common in backend development.

---

# 24. AI Engineering Connection

List comprehensions are frequently useful in data preprocessing.

Example:

documents = [
    "Python is useful",
    "Python supports AI",
    "Machine learning uses data"
]

Convert text to lowercase:

cleaned = [document.lower() for document in documents]

Calculate lengths:

lengths = [len(document) for document in documents]

Filter longer documents:

long_documents = [
    document
    for document in documents
    if len(document) > 20
]

The general pattern is:

    Raw collection
          ↓
    Filter / Transform
          ↓
    New collection

This pattern appears throughout data-processing and AI pipelines.

---

# 25. Don't Use Comprehensions for Side Effects

A list comprehension is designed to create a list.

Avoid:

[print(number) for number in numbers]

Although it technically executes, it creates a list of `None` values unnecessarily.

Prefer:

for number in numbers:
    print(number)

Use a comprehension when the intention is:

> Create a new list.

Use a normal loop when the intention is:

> Perform an action for every element.

---

# 26. When to Use List Comprehensions

List comprehensions are ideal for simple operations.

### Simple transformation

squares = [number * number for number in numbers]

### Simple filtering

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

### Simple filter + transformation

even_squares = [
    number * number
    for number in numbers
    if number % 2 == 0
]

These are readable and expressive.

---

# 27. When NOT to Use List Comprehensions

Avoid forcing complicated logic into one comprehension.

For example:

result = [
    complicated_function(x)
    for x in data
    if complicated_condition(x)
]

If the logic becomes difficult to understand, use a normal loop:

result = []

for x in data:
    if complicated_condition(x):
        processed = complicated_function(x)
        result.append(processed)

The second version may be longer but can be easier to understand and maintain.

Important engineering principle:

> Shorter code is not automatically better code.

Readability and maintainability matter.

---

# 28. Performance Consideration

List comprehensions are often concise and efficient for straightforward list construction.

However, do not choose them simply because they are shorter.

A good priority is:

    Correctness
        ↓
    Readability
        ↓
    Maintainability
        ↓
    Performance optimization when necessary

For very large datasets, other approaches may be more appropriate, such as:

- Generators
- NumPy
- Pandas
- PyTorch
- Iterators

These will be covered later.

---

# 29. Converting Normal Loops to Comprehensions

## Example 1

Normal loop:

result = []

for number in numbers:
    result.append(number * 10)

Comprehension:

result = [number * 10 for number in numbers]

---

## Example 2

Normal loop:

result = []

for number in numbers:
    if number > 3:
        result.append(number)

Comprehension:

result = [number for number in numbers if number > 3]

---

## Example 3

Normal loop:

result = []

for number in numbers:
    if number > 3:
        result.append(number * 10)

Comprehension:

result = [
    number * 10
    for number in numbers
    if number > 3
]

---

# 30. Common Beginner Mistakes

## Mistake 1 — Incorrect ordering

Correct:

[number * 2 for number in numbers]

The expression comes before the `for`.

---

## Mistake 2 — Confusing filtering and transformation

Filtering:

[number for number in numbers if number > 5]

Transformation:

[number * 2 for number in numbers]

Filtering + transformation:

[number * 2 for number in numbers if number > 5]

---

## Mistake 3 — Forgetting that a new list is created

squares = [number * number for number in numbers]

does not modify `numbers`.

---

## Mistake 4 — Using comprehensions for side effects

Avoid:

[print(number) for number in numbers]

Prefer:

for number in numbers:
    print(number)

---

## Mistake 5 — Creating unreadable comprehensions

A very complicated comprehension may be harder to maintain than a normal loop.

---

# 31. Three Core Mental Models

Whenever you see:

[expression for item in iterable]

translate it mentally into:

result = []

for item in iterable:
    result.append(expression)

---

Whenever you see:

[expression for item in iterable if condition]

translate it into:

result = []

for item in iterable:
    if condition:
        result.append(expression)

---

Whenever you see:

[true_value if condition else false_value for item in iterable]

think:

> Every element produces a result, but the result depends on the condition.

---

# 32. Interview Questions

## Beginner

1. What is a list comprehension?
2. Why are list comprehensions useful?
3. What is the basic syntax?
4. How do you create a list of squares using a comprehension?
5. How do you filter even numbers?
6. Can a list comprehension contain an `if` condition?
7. Does a list comprehension modify the original list?
8. What does the expression part represent?

---

## Intermediate

### 1.

Convert this loop into a comprehension:

result = []

for number in numbers:
    result.append(number * 2)

---

### 2.

Convert this loop:

result = []

for number in numbers:
    if number > 10:
        result.append(number)

---

### 3.

What is the difference between filtering and conditional transformation?

---

### 4.

What is the difference between:

[number for number in numbers if number > 5]

and:

[number * 2 for number in numbers if number > 5]

---

### 5.

When should you prefer a normal `for` loop over a comprehension?

---

### 6.

Why is using a comprehension for `print()` generally a bad idea?

---

### 7.

Can list comprehensions contain nested loops?

---

### 8.

Can list comprehensions call functions?

---

## Advanced Reasoning

### Question 1

What is the equivalent normal loop for:

result = [x * x for x in numbers if x % 2 == 0]

---

### Question 2

What does this produce?

result = [
    "even" if x % 2 == 0 else "odd"
    for x in numbers
]

Does it filter anything?

---

### Question 3

Why is:

[number for number in numbers if number > 5]

different from:

[number if number > 5 else 0 for number in numbers]

---

### Question 4

When would a normal loop be more readable than a list comprehension?

---

# 33. Assignments

## Basic Assignment

Create:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Using list comprehensions:

1. Create a list containing the squares.
2. Create a list containing the cubes.
3. Create a list containing only even numbers.
4. Create a list containing only odd numbers.
5. Create a list containing numbers greater than `5`.
6. Create a list containing the doubled values of even numbers.

---

# 34. Intermediate Assignment

Create:

stocks = ["tcs", "infy", "itc", "reliance", "nestle"]

Using list comprehensions:

### 1. Convert everything to uppercase

Expected:

    ["TCS", "INFY", "ITC", "RELIANCE", "NESTLE"]

### 2. Create a list containing the length of every stock symbol.

### 3. Create a list containing only symbols whose length is greater than `3`.

### 4. Create a list containing symbols converted to uppercase only if their length is greater than `3`.

---

# 35. Challenge Assignment

Convert each normal loop into a list comprehension.

## Challenge 1

numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 10)

---

## Challenge 2

numbers = [1, 2, 3, 4, 5, 6]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number)

---

## Challenge 3

numbers = [1, 2, 3, 4, 5, 6]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number * number)

---

## Challenge 4

Given:

names = ["gautham", "rahul", "arun", "suresh"]

Create:

    ["GAUTHAM", "RAHUL", "ARUN", "SURESH"]

using a comprehension.

---

## Challenge 5

Given:

numbers = [1, 2, 3, 4, 5]

Create:

    ["odd", "even", "odd", "even", "odd"]

using a conditional expression inside a comprehension.

---

# 36. Engineering Challenge

Given:

users = [
    {"name": "Gautham", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Arun", "active": True},
    {"name": "Suresh", "active": False}
]

Using list comprehensions:

### Task 1

Extract all names.

Expected:

    ["Gautham", "Rahul", "Arun", "Suresh"]

### Task 2

Extract only active users.

### Task 3

Extract the names of active users.

Think carefully about the difference between:

    filtering users

and:

    filtering + extracting a field

This pattern is directly relevant to backend/API development.

---

# 37. Chapter Summary

A list comprehension provides a concise way to construct a new list.

Basic transformation:

[expression for item in iterable]

Filtering:

[item for item in iterable if condition]

Filtering + transformation:

[expression for item in iterable if condition]

Conditional transformation:

[true_value if condition else false_value for item in iterable]

Nested loops can also be represented:

[expression for item1 in iterable1 for item2 in iterable2]

---

# 38. Key Takeaways

- List comprehensions create new lists.
- They are concise representations of common `for` loop patterns.
- The expression comes before the `for`.
- Conditions can filter elements.
- Filtering removes elements from the resulting list.
- Transformation changes what gets placed into the resulting list.
- Filtering and transformation can be combined.
- Conditional expressions can transform every element differently.
- Nested loops can be represented using nested comprehension clauses.
- Functions can be called inside comprehensions.
- Comprehensions are useful for backend data processing.
- Comprehensions are useful for AI/data preprocessing.
- Avoid using comprehensions merely for side effects.
- Normal `for` loops are preferable when logic becomes complex.
- Readability is more important than making code as short as possible.

---

# 39. Chapter Completion Criteria

Before moving to the next chapter, you should be able to look at:

result = [x * 2 for x in numbers if x % 2 == 0]

and immediately translate it into:

result = []

for x in numbers:
    if x % 2 == 0:
        result.append(x * 2)

You should also understand the difference between:

[x for x in numbers if x > 5]

and:

[x * 2 for x in numbers if x > 5]

and:

["yes" if x > 5 else "no" for x in numbers]

These represent:

    Filter
       ↓
    Transform
       ↓
    Conditional Transform

---

# Next Chapter

## Chapter 34 – Nested Lists

Topics:

- Creating nested lists
- Accessing rows and columns
- Nested indexing
- Modifying nested elements
- Iterating through nested lists
- Nested `for` loops
- Flattening nested lists
- Nested list comprehensions
- Preserving nested structure
- Shared references
- The `[[0] * 3] * 3` trap
- Creating independent nested lists
- Nested lists vs dictionaries
- Backend engineering use cases
- AI engineering use cases
- Interview questions
- Practical assignments
- Engineering challenge