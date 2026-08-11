# Chapter 26 – Lambda Functions

## What is a Lambda Function?

A lambda function is a small anonymous function created using the `lambda` keyword.

## Syntax

```python
lambda parameters: expression
```

Example:

```python
square = lambda x: x * x
```

## Lambda vs def

Normal function:

```python
def square(x):
    return x * x
```

Lambda:

```python
square = lambda x: x * x
```

Both create function objects.

## Functions as Objects

Python functions are first-class objects.

They can be:

- Assigned to variables
- Passed as arguments
- Returned from functions
- Stored in collections

Example:

```python
def greet():
    print("Hello")

hello = greet

hello()
```

`hello` and `greet` refer to the same function object.

## Lambda and Higher-Order Functions

Functions can accept other functions as arguments.

```python
def apply_operation(x, operation):
    return operation(x)
```

Example:

```python
apply_operation(5, lambda x: x * x)
```

## sorted()

Lambda is commonly used to define a sorting key.

```python
students.sort(key=lambda student: student[1])
```

## map()

`map()` applies a function to each item.

```python
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))
```

## filter()

`filter()` keeps items for which the function returns a truthy value.

```python
numbers = [1, 2, 3, 4]

result = list(filter(lambda x: x % 2 == 0, numbers))
```

## Python Internals

A lambda creates a function object just like a function created with `def`.

The function can be referenced by variables and passed around as an object.

## AI Connection

Lambda functions are useful for:

- Sorting model predictions
- Ranking retrieved documents
- Simple data transformations
- Filtering datasets
- Data preprocessing

Example:

```python
documents.sort(
    key=lambda document: document["score"],
    reverse=True
)
```

## When to Use Lambda

Use lambda when:

- The operation is simple.
- The function is short-lived.
- A function is needed as an argument.
- A sorting/filtering key is required.

## When to Use def

Prefer `def` when:

- The function is reused.
- Logic is complex.
- Multiple statements are needed.
- Documentation is important.
- A meaningful function name improves readability.

## Common Mistakes

- Using `return` inside lambda.
- Making lambda expressions overly complex.
- Confusing `function` with `function()`.
- Immediately executing a lambda when you intended to store it.

## Summary

Lambda functions provide a concise way to create small function objects. Their importance comes from Python's first-class function model, where functions can be stored, passed, and returned like other objects.