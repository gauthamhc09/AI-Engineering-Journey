# Chapter 35 – Tuples

## 1. Introduction

A tuple is an ordered, immutable collection.

Example:

numbers = (10, 20, 30)

The most important difference between a list and a tuple is:

    List  → Mutable
    Tuple → Immutable

Tuples are useful when we have a fixed group of related values that should not be changed after creation.

Examples:

- Coordinates
- RGB values
- Fixed configuration values
- Function return values
- Fixed records
- Dictionary keys
- Pairs of related values

---

# 2. Creating a Tuple

Basic tuple:

numbers = (10, 20, 30)

A tuple can contain different data types:

person = ("Gautham", 33, "Developer")

Other examples:

numbers = (10, 20, 30)

languages = ("Python", "JavaScript", "Rust")

mixed = ("Gautham", 33, True, 17.5)

---

# 3. Tuple vs List

Compare:

numbers_list = [10, 20, 30]

numbers_tuple = (10, 20, 30)

Both are:

- Ordered
- Indexed
- Iterable
- Able to contain duplicate values

The main difference:

    List
      ↓
    Mutable
      ↓
    Can be changed

    Tuple
      ↓
    Immutable
      ↓
    Cannot be changed after creation

---

# 4. Tuple Indexing

Tuples use the same indexing rules as lists.

Example:

numbers = (10, 20, 30, 40)

First element:

print(numbers[0])

Output:

    10

Last element:

print(numbers[-1])

Output:

    40

---

# 5. Tuple Slicing

Tuples support slicing.

Example:

numbers = (10, 20, 30, 40, 50)

First three:

print(numbers[:3])

Output:

    (10, 20, 30)

Last two:

print(numbers[-2:])

Output:

    (40, 50)

Reverse:

print(numbers[::-1])

Output:

    (50, 40, 30, 20, 10)

The result remains a tuple.

---

# 6. Tuple Immutability

This is the most important tuple concept.

Example:

numbers = (10, 20, 30)

This is not allowed:

numbers[0] = 100

Python raises:

    TypeError

because tuples cannot be modified after creation.

Compare with a list:

numbers = [10, 20, 30]

numbers[0] = 100

This works because lists are mutable.

---

# 7. What Does Immutable Mean?

Immutable means:

> The tuple's structure and element references cannot be changed after the tuple is created.

These operations are not allowed:

numbers[0] = 100

numbers.append(40)

numbers.remove(20)

Tuples do not provide mutation methods such as:

- append()
- extend()
- insert()
- remove()
- pop()
- sort()
- reverse()

---

# 8. Tuple Methods

Because tuples are immutable, they have fewer methods than lists.

The two primary tuple methods are:

    count()
    index()

Example:

numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))

Output:

    3

Find an index:

print(numbers.index(30))

Output:

    3

---

# 9. Iterating Through a Tuple

Tuples are iterable.

Example:

languages = ("Python", "JavaScript", "Rust")

for language in languages:
    print(language)

Output:

    Python
    JavaScript
    Rust

Tuples can be used with:

- for loops
- len()
- indexing
- slicing
- membership testing

---

# 10. len() with Tuples

Example:

numbers = (10, 20, 30, 40)

print(len(numbers))

Output:

    4

The `len()` function works with tuples just as it does with lists.

---

# 11. Membership Testing

Use `in` to check whether a value exists.

languages = ("Python", "JavaScript", "Rust")

print("Python" in languages)

Output:

    True

And:

print("Java" in languages)

Output:

    False

---

# 12. Tuple Packing

Python allows multiple values to be packed into a tuple.

Example:

person = "Gautham", 33, "Developer"

This is equivalent to:

person = ("Gautham", 33, "Developer")

This is called:

> Tuple packing

The values are packed into one tuple.

---

# 13. Tuple Unpacking

Tuple unpacking is the opposite of packing.

Example:

person = ("Gautham", 33, "Developer")

name, age, role = person

Now:

name → "Gautham"

age → 33

role → "Developer"

Example:

print(name)
print(age)
print(role)

Output:

    Gautham
    33
    Developer

---

# 14. Unpacking Requires Matching Values

Example:

person = ("Gautham", 33, "Developer")

This works:

name, age, role = person

because:

    3 variables
    3 values

But this does not work:

name, age = person

because:

    2 variables
    3 values

Similarly:

name, age, role, city = person

does not work because there are only three values.

---

# 15. Swapping Variables

Tuple unpacking makes variable swapping simple.

Traditional approach:

a = 10
b = 20

temp = a
a = b
b = temp

Python:

a = 10
b = 20

a, b = b, a

Now:

    a → 20
    b → 10

This is a common Python idiom.

---

# 16. Multiple Assignment

Python supports:

x, y, z = 10, 20, 30

Conceptually:

(x, y, z) = (10, 20, 30)

This uses tuple packing and unpacking.

---

# 17. Single-Element Tuple

This is an important Python gotcha.

This is NOT a tuple:

x = (10)

Python treats it as:

x = 10

To create a single-element tuple:

x = (10,)

The comma is important.

Check:

print(type(x))

Output:

    <class 'tuple'>

---

# 18. Why the Comma Matters

Compare:

a = (10)

b = (10,)

Conceptually:

    (10)
      ↓
    integer

    (10,)
      ↓
    tuple

The comma defines the single-element tuple.

You can technically also write:

x = 10,

which creates:

(10,)

However, `(10,)` is generally clearer.

---

# 19. Nested Tuples

Tuples can contain other tuples.

Example:

data = (
    (1, 2),
    (3, 4)
)

Access:

print(data[0])

Output:

    (1, 2)

Access an individual value:

print(data[1][0])

Output:

    3

This follows the same nested indexing pattern learned with nested lists.

---

# 20. Tuple Containing a List

A tuple can contain mutable objects.

Example:

data = ([1, 2, 3], 10)

The tuple itself is immutable.

This is not allowed:

data[0] = [4, 5, 6]

But the list inside the tuple is still mutable:

data[0].append(4)

Now:

print(data)

Output:

    ([1, 2, 3, 4], 10)

This leads to an important distinction:

> Tuple immutability does not mean every object referenced by the tuple is immutable.

The tuple cannot change its element reference.

But the mutable object inside it can still change internally.

---

# 21. Understanding References

Consider:

numbers = [1, 2, 3]

data = (numbers, 100)

Conceptually:

    data
     |
     +----→ [1, 2, 3]
     |
     +----→ 100

You cannot replace the first element:

data[0] = [4, 5, 6]

But you can mutate the list:

numbers.append(4)

Now:

    data
     |
     +----→ [1, 2, 3, 4]
     |
     +----→ 100

The tuple itself did not change its references.

The list object changed internally.

---

# 22. Tuple vs List

| Feature | List | Tuple |
|---|---|---|
| Ordered | Yes | Yes |
| Indexed | Yes | Yes |
| Slicing | Yes | Yes |
| Iterable | Yes | Yes |
| Mutable | Yes | No |
| append() | Yes | No |
| remove() | Yes | No |
| sort() | Yes | No |
| count() | Yes | Yes |
| index() | Yes | Yes |
| Duplicates allowed | Yes | Yes |

The main difference:

    List  → Changeable collection

    Tuple → Fixed collection

---

# 23. When Should You Use a Tuple?

Use a tuple when the collection represents:

> A fixed group of related values.

Example:

coordinates = (10, 20)

The structure represents:

    x
    y

Another example:

rgb = (255, 128, 0)

The structure represents:

    red
    green
    blue

A tuple communicates that these values form a fixed unit.

---

# 24. Tuple as a Function Return Value

Tuples are commonly used when a function returns multiple values.

Example:

def get_user():
    return "Gautham", 33

Then:

name, age = get_user()

The function returns:

("Gautham", 33)

and tuple unpacking separates the values.

---

# 25. Function Returning Multiple Values

Example:

def calculate(a, b):

    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product

Then:

total, difference, product = calculate(10, 5)

Results:

    total      → 15
    difference → 5
    product    → 50

Python is effectively returning:

(15, 5, 50)

and then unpacking it.

---

# 26. Tuple as a Fixed Record

Example:

stock = ("TCS", 3500, 10)

Possible interpretation:

    Symbol   → TCS
    Price    → 3500
    Quantity → 10

A tuple can represent this fixed structure.

However, a dictionary may be clearer:

stock = {
    "symbol": "TCS",
    "price": 3500,
    "quantity": 10
}

Now the values have explicit names.

The choice depends on:

> How the data will be accessed and what the data represents.

---

# 27. Tuples as Dictionary Keys

Tuples can be used as dictionary keys if their elements are hashable.

Example:

locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

Access:

print(locations[(10, 20)])

Output:

    Point A

Lists cannot be dictionary keys:

locations = {
    [10, 20]: "Point A"
}

This raises an error because lists are mutable and unhashable.

---

# 28. Tuples and Sets

A tuple can also be stored inside a set if its elements are hashable.

Example:

points = {
    (10, 20),
    (30, 40)
}

This works.

But:

points = {
    [10, 20]
}

does not work because lists are unhashable.

---

# 29. Tuple Comparison

Tuples can be compared.

Example:

a = (1, 2)
b = (1, 2)

print(a == b)

Output:

    True

Python compares tuple elements in order.

Example:

a = (1, 2)
b = (1, 3)

print(a < b)

Output:

    True

Python compares the first elements first.

If they are equal, it moves to the next element.

---

# 30. Converting Between Lists and Tuples

List → Tuple:

numbers = [10, 20, 30]

numbers_tuple = tuple(numbers)

Result:

    (10, 20, 30)

Tuple → List:

numbers_list = list(numbers_tuple)

Result:

    [10, 20, 30]

This is useful when you need to switch between mutability models.

---

# 31. Why Not Use Lists Everywhere?

A natural question is:

> If lists can hold multiple values, why use tuples?

The answer is that the collection type communicates intent.

Compare:

coordinates = [10, 20]

with:

coordinates = (10, 20)

The tuple communicates:

> These values form a fixed group.

The list communicates:

> This collection may change.

Immutability can therefore act as a design constraint and prevent accidental modification.

---

# 32. Backend Engineering Connection

Tuples can be useful when returning a fixed group of values.

Example:

def get_portfolio_summary():
    return 500000, 550000, 50000

Then:

invested, current_value, profit = get_portfolio_summary()

This works well for a small, fixed set of values.

However, if the response has many named fields, a dictionary or structured model is often clearer:

{
    "invested": 500000,
    "current_value": 550000,
    "profit": 50000
}

The principle is:

> Use tuples for compact fixed structures; use dictionaries or structured objects when named fields improve clarity.

---

# 33. AI Engineering Connection

Tuples appear frequently in Python data-processing code.

Example:

document = ("doc_001", "Python introduction")

Or:

embedding_info = ("document_001", 768)

Functions may return multiple values:

def process_document(document):
    return document_id, token_count

Then:

document_id, token_count = process_document(document)

Tuples are also common when iterating through dictionaries:

for key, value in data.items():
    print(key, value)

The two values can be unpacked directly into variables.

---

# 34. Tuple Unpacking in for Loops

Consider:

stocks = [
    ("TCS", 3500),
    ("INFY", 1800),
    ("ITC", 500)
]

You can write:

for symbol, price in stocks:
    print(symbol, price)

Output:

    TCS 3500
    INFY 1800
    ITC 500

Each tuple is unpacked automatically.

For example:

("TCS", 3500)

becomes:

    symbol → "TCS"
    price  → 3500

---

# 35. Starred Unpacking

Python supports extended unpacking using `*`.

Example:

numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

Now:

    first  → 1
    middle → [2, 3, 4]
    last   → 5

The starred variable collects the remaining values into a list.

---

# 36. Another Starred Unpacking Example

numbers = (10, 20, 30, 40, 50)

first, *rest = numbers

print(first)
print(rest)

Output:

    10
    [20, 30, 40, 50]

This is useful when you know the first or last values but don't know how many values exist in the middle.

---

# 37. Tuple Immutability and Hashability

An important relationship:

    Mutable
       ↓
    Usually not hashable

    Immutable
       ↓
    May be hashable

A tuple can be hashable if all of its elements are hashable.

This works:

point = (10, 20)

This does not:

point = ([10, 20], 30)

because the tuple contains a list, and lists are unhashable.

Therefore:

> Tuple immutability alone does not guarantee hashability.

The elements inside the tuple also matter.

---

# 38. Common Beginner Mistakes

## Mistake 1 — Forgetting the comma

Wrong:

value = (10)

Correct:

value = (10,)

---

## Mistake 2 — Trying to modify a tuple

Wrong:

numbers = (10, 20, 30)

numbers[0] = 100

Tuples are immutable.

---

## Mistake 3 — Expecting list methods

This does not exist:

numbers.append(40)

Tuples don't have mutation methods.

---

## Mistake 4 — Incorrect unpacking

This fails:

a, b = (10, 20, 30)

because:

    2 variables
    3 values

---

## Mistake 5 — Assuming everything inside a tuple is immutable

This is valid:

data = ([1, 2], 10)

data[0].append(3)

The tuple remains structurally unchanged, while the list inside it is modified.

---

# 39. Tuple vs List — Decision Guide

Use a **list** when:

- The collection will change.
- You need `append()`.
- You need `remove()`.
- You need sorting or mutation.
- The number of elements may change.

Use a **tuple** when:

- The collection represents a fixed group.
- You want immutability.
- You want to prevent accidental modification.
- You need a hashable composite key.
- A function returns a fixed group of values.
- Tuple unpacking makes the code clearer.

---

# 40. Interview Questions

## Beginner

1. What is a tuple?
2. How is a tuple different from a list?
3. Are tuples ordered?
4. Are tuples mutable?
5. How do you access a tuple element?
6. Can tuples be sliced?
7. What methods do tuples provide?
8. Why does `(10)` not create a tuple?
9. How do you create a single-element tuple?

---

## Intermediate

1. What is tuple packing?
2. What is tuple unpacking?
3. How can tuple unpacking be used to swap two variables?
4. What happens if the number of variables doesn't match the number of tuple elements?
5. Can a tuple contain a list?
6. Can a tuple be used as a dictionary key?
7. Why can some tuples be dictionary keys while lists cannot?
8. How do you convert a tuple to a list?
9. How do you convert a list to a tuple?

---

## Advanced

### Question 1

What is the output?

data = (10, 20, 30)

print(data[1])

---

### Question 2

What happens here?

data = (10, 20, 30)

data[0] = 100

Why?

---

### Question 3

What is the type of:

x = (10)

and:

y = (10,)

Why are they different?

---

### Question 4

What happens here?

data = ([1, 2], 10)

data[0].append(3)

print(data)

Does this violate tuple immutability?

Explain why or why not.

---

### Question 5

Why does this work?

locations = {
    (10, 20): "Point A"
}

but this doesn't?

locations = {
    [10, 20]: "Point A"
}

---

# 41. Assignments

## Basic Assignment

Create:

numbers = (10, 20, 30, 40, 50)

Perform:

1. Print the tuple.
2. Print the first element.
3. Print the last element.
4. Print the length.
5. Print the first three elements.
6. Print the tuple in reverse.
7. Check whether `30` exists.
8. Count how many times `20` appears.
9. Find the index of `40`.

---

# 42. Tuple Immutability Assignment

Create:

numbers = (10, 20, 30)

Try:

numbers[0] = 100

Observe the error.

Then explain:

> Why does Python prevent this?

---

# 43. Tuple Packing and Unpacking

Create:

person = ("Gautham", 33, "Developer")

Unpack it into:

name
age
role

Then print all three variables.

---

# 44. Multiple Assignment

Create:

a = 10
b = 20

Swap them without using a temporary variable.

Expected:

    a = 20
    b = 10

---

# 45. Stock Assignment

Create:

stocks = (
    ("TCS", 3500),
    ("INFY", 1800),
    ("ITC", 500)
)

Using a `for` loop:

1. Print each symbol.
2. Print each price.
3. Print symbol and price together using tuple unpacking.

Expected:

    TCS 3500
    INFY 1800
    ITC 500

---

# 46. Function Assignment

Create:

def calculate(a, b):
    ...

It should return:

- Sum
- Difference
- Product

Then unpack:

total, difference, product = calculate(10, 5)

Expected:

    total      → 15
    difference → 5
    product    → 50

---

# 47. Challenge Assignment

Predict the output before executing:

data = (10, 20, 30)

a, b, c = data

print(a)
print(b)
print(c)

Then:

numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

Explain what happens.

---

# 48. Engineering Challenge

Consider:

portfolio = (
    ("TCS", 100, 350000),
    ("INFY", 50, 90000),
    ("ITC", 200, 100000)
)

Each tuple contains:

    (symbol, quantity, invested_value)

Using tuple unpacking:

1. Print every stock symbol.
2. Print every quantity.
3. Print every invested value.
4. Calculate the total invested value.
5. Calculate the total quantity.

Then answer:

> Would you use tuples for a real portfolio application, or would a list of dictionaries be better?

Explain your reasoning.

Consider:

    Tuple:
    ("TCS", 100, 350000)

versus:

    Dictionary:
    {
        "symbol": "TCS",
        "quantity": 100,
        "invested_value": 350000
    }

The important question is not simply which one can store the values.

Ask:

> Which representation makes the meaning of the data clearer?

---

# 49. Chapter Summary

A tuple is:

> An ordered, immutable collection.

Create:

numbers = (10, 20, 30)

Index:

numbers[0]

Slice:

numbers[:2]

Reverse:

numbers[::-1]

Iterate:

for number in numbers:
    print(number)

Count:

numbers.count(20)

Find index:

numbers.index(20)

Single-element tuple:

value = (10,)

Tuple packing:

person = "Gautham", 33, "Developer"

Tuple unpacking:

name, age, role = person

Multiple assignment:

a, b = b, a

---

# 50. Key Takeaways

- Tuples are ordered.
- Tuples are indexed.
- Tuples support slicing.
- Tuples are iterable.
- Tuples are immutable.
- Tuples have fewer methods than lists because they cannot be mutated.
- `count()` and `index()` are the main tuple methods.
- A single-element tuple requires a comma.
- Tuple packing combines values into a tuple.
- Tuple unpacking separates values into variables.
- Tuple unpacking can be used to swap variables.
- Tuples can contain mutable objects such as lists.
- A tuple containing only hashable elements can be used as a dictionary key.
- Tuples are useful for fixed groups of related values.
- Tuples are commonly used when functions return multiple values.
- Tuples can be unpacked directly inside `for` loops.
- Starred unpacking can collect remaining values.
- Tuple immutability does not make objects contained inside the tuple immutable.
- Tuple vs list should be decided based on whether the data represents a fixed or changeable collection.

---

# 51. Chapter Completion Criteria

Before moving to the next chapter, you should be able to explain:

numbers = (10, 20, 30)

Why this works:

numbers[0]

Why this fails:

numbers[0] = 100

Why this is NOT a tuple:

x = (10)

But this IS:

x = (10,)

You should also understand:

name, age = ("Gautham", 33)

and:

a, b = b, a

You should be able to explain:

data = ([1, 2, 3], 10)

data[0].append(4)

and answer:

> Why is the above allowed even though tuples are immutable?

The answer should demonstrate your understanding of the difference between:

    Tuple immutability
          +
    Object mutability
          +
    References

---

# Next Chapter

## Chapter 36 – Sets

Topics:

- Creating sets
- Set uniqueness
- Adding and removing elements
- Membership testing
- Set operations
- Union
- Intersection
- Difference
- Symmetric difference
- Set comprehensions
- Sets vs lists
- Sets vs tuples
- Hashability
- Real-world data processing
- Backend engineering use cases
- AI/data-processing use cases
- Interview questions
- Practical assignments
- Engineering challenges