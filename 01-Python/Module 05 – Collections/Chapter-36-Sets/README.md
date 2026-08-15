# Chapter 36 – Sets

## 1. Introduction

A set is an unordered collection of unique elements.

Example:

numbers = {10, 20, 30, 40}

The three most important characteristics of a set are:

    1. Unique elements
    2. No positional indexing
    3. Fast membership testing

Think of a set as:

    Set
      ↓
    Unique values
      ↓
    Membership
      ↓
    Set operations

Sets are useful when we care about:

- Uniqueness
- Membership
- Comparing collections
- Removing duplicates
- Finding common elements
- Finding differences

---

# 2. Creating a Set

A set can be created using curly braces:

numbers = {10, 20, 30}

Another example:

stocks = {"TCS", "INFY", "ITC"}

A set can contain different hashable data types:

data = {10, "Python", 20.5, True}

However, all elements of a set must be hashable.

We will understand hashability later in this chapter.

---

# 3. Sets Automatically Remove Duplicates

One of the most important properties of a set is uniqueness.

Example:

numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

The result contains only:

    {10, 20, 30}

The duplicate values are automatically removed.

Compare:

List:

numbers = [10, 20, 20, 30]

Result:

    [10, 20, 20, 30]


Set:

numbers = {10, 20, 20, 30}

Result:

    {10, 20, 30}

---

# 4. Why Do We Need Sets?

Imagine an application receives:

stocks = [
    "TCS",
    "INFY",
    "TCS",
    "ITC",
    "INFY",
    "RELIANCE"
]

We want to know:

> Which stocks are present?

Duplicates are not useful.

Convert the list to a set:

unique_stocks = set(stocks)

Result:

    {"TCS", "INFY", "ITC", "RELIANCE"}

This is one of the most common practical uses of sets.

---

# 5. Creating a Set from a List

The `set()` function can convert an iterable into a set.

Example:

numbers = [10, 20, 20, 30, 30]

unique_numbers = set(numbers)

print(unique_numbers)

Result:

    {10, 20, 30}

This is useful for deduplication.

---

# 6. Empty Set

This is an important Python detail.

You might think:

data = {}

creates an empty set.

It does NOT.

It creates an empty dictionary.

Check:

data = {}

print(type(data))

Output:

    <class 'dict'>

To create an empty set:

data = set()

Check:

print(type(data))

Output:

    <class 'set'>

Remember:

    {}      → empty dictionary

    set()   → empty set

---

# 7. Sets Are Unordered

Sets do not provide positional ordering.

Example:

numbers = {10, 20, 30}

You cannot reliably think of the set as:

    position 0 → 10
    position 1 → 20
    position 2 → 30

Therefore this is invalid:

numbers[0]

It raises a TypeError.

Why?

Because a set is not designed for positional access.

---

# 8. List vs Set Mental Model

List:

numbers = [10, 20, 30]

Question:

> What is the element at index 0?

Answer:

numbers[0]

Set:

numbers = {10, 20, 30}

Question:

> Does 20 exist?

Answer:

20 in numbers

This is the fundamental difference in how you think about the collections.

    List
      ↓
    Position


    Set
      ↓
    Membership

---

# 9. Membership Testing

Use `in` to check whether an element exists.

Example:

stocks = {"TCS", "INFY", "ITC"}

print("TCS" in stocks)

Output:

    True

And:

print("RELIANCE" in stocks)

Output:

    False

You can also use `not in`:

print("RELIANCE" not in stocks)

Output:

    True

---

# 10. Why Sets Are Useful for Membership Testing

Suppose:

stocks = [
    "TCS",
    "INFY",
    "ITC",
    "RELIANCE"
]

We can check:

"TCS" in stocks

This works.

But sets are specifically designed around membership testing and use hash-based lookup internally.

Example:

stocks = {
    "TCS",
    "INFY",
    "ITC",
    "RELIANCE"
}

Then:

"TCS" in stocks

is generally very fast.

You don't need to understand the internal hash table implementation yet.

For now remember:

> Sets are optimized for membership testing.

---

# 11. Adding One Element

Sets are mutable.

Use:

add()

Example:

stocks = {"TCS", "INFY"}

stocks.add("ITC")

print(stocks)

Now the set contains:

    {"TCS", "INFY", "ITC"}

---

# 12. Adding a Duplicate

What happens if the element already exists?

stocks = {"TCS", "INFY"}

stocks.add("TCS")

print(stocks)

The set remains:

    {"TCS", "INFY"}

No duplicate is created.

This is another consequence of set uniqueness.

---

# 13. `add()` Return Value

Like many list methods, `add()` modifies the set in place.

It does not return the updated set.

Example:

stocks = {"TCS", "INFY"}

result = stocks.add("ITC")

print(result)

Output:

    None

The set itself has changed.

---

# 14. Adding Multiple Elements

Use:

update()

Example:

stocks = {"TCS", "INFY"}

stocks.update(["ITC", "RELIANCE", "HDFCBANK"])

print(stocks)

The set now contains all unique elements.

`update()` accepts an iterable.

For example:

stocks.update(["ITC", "INFY"])

or:

stocks.update(("ITC", "INFY"))

or:

stocks.update({"ITC", "INFY"})

---

# 15. `add()` vs `update()`

This distinction is important.

## add()

Adds one element:

stocks.add("TCS")

## update()

Adds multiple elements from an iterable:

stocks.update(["TCS", "INFY", "ITC"])

Mental model:

    add()
      ↓
    one element


    update()
      ↓
    multiple elements

---

# 16. Removing an Element with `remove()`

Example:

stocks = {"TCS", "INFY", "ITC"}

stocks.remove("ITC")

print(stocks)

`ITC` is removed.

But there is an important behavior.

If the element doesn't exist:

stocks.remove("RELIANCE")

Python raises:

    KeyError

---

# 17. `discard()`

`discard()` also removes an element.

Example:

stocks = {"TCS", "INFY", "ITC"}

stocks.discard("ITC")

This works.

The important difference is what happens if the element doesn't exist.

stocks.discard("RELIANCE")

No error occurs.

Therefore:

    remove()
       ↓
    Error if missing


    discard()
       ↓
    No error if missing

---

# 18. `remove()` vs `discard()`

| Method | Element exists | Element missing |
|---|---|---|
| remove() | Removes it | Raises KeyError |
| discard() | Removes it | Does nothing |

Use `remove()` when:

> The element is expected to exist.

Use `discard()` when:

> You don't care whether the element exists.

---

# 19. Set `pop()`

Sets also have:

pop()

But it behaves differently from list `pop()`.

List:

numbers = [10, 20, 30]

numbers.pop()

removes the last element.

Set:

numbers = {10, 20, 30}

numbers.pop()

removes and returns an arbitrary element.

There is no concept of:

    first element

or:

    last element

in a set.

Therefore, never build logic that depends on which element `set.pop()` removes.

---

# 20. Clearing a Set

To remove all elements:

numbers = {10, 20, 30}

numbers.clear()

print(numbers)

Output:

    set()

The set still exists.

It simply contains no elements.

---

# 21. Set Length

Use:

len()

Example:

stocks = {"TCS", "INFY", "ITC"}

print(len(stocks))

Output:

    3

If duplicates were supplied during creation, they do not contribute to the length.

Example:

numbers = {10, 10, 20, 20, 30}

print(len(numbers))

Output:

    3

---

# 22. Iterating Through a Set

Sets are iterable.

Example:

stocks = {"TCS", "INFY", "ITC"}

for stock in stocks:
    print(stock)

The loop processes every element.

However:

> Do not depend on the iteration order of a set.

If order matters, use a list.

---

# 23. Converting a Set to a List

You can convert a set into a list:

stocks = {"TCS", "INFY", "ITC"}

stock_list = list(stocks)

Now:

    stock_list

is a list.

However, because sets are unordered, you should not expect the resulting list to represent a meaningful original order.

---

# 24. Converting a List to a Set

The reverse is also possible:

stocks = [
    "TCS",
    "INFY",
    "TCS",
    "ITC"
]

unique_stocks = set(stocks)

Result:

    {"TCS", "INFY", "ITC"}

This is one of the most common set operations in real Python programs.

---

# 25. Union

Union combines the unique elements of two sets.

Example:

a = {1, 2, 3}
b = {3, 4, 5}

result = a | b

Result:

    {1, 2, 3, 4, 5}

The common `3` appears only once.

You can also write:

result = a.union(b)

Both represent the same operation.

---

# 26. Union Mental Model

Think:

    A = {1, 2, 3}

    B = {3, 4, 5}

    A ∪ B

Result:

    {1, 2, 3, 4, 5}

Meaning:

> Give me everything that belongs to A or B.

---

# 27. Intersection

Intersection finds the elements common to both sets.

Example:

a = {1, 2, 3}
b = {3, 4, 5}

result = a & b

Result:

    {3}

Method form:

result = a.intersection(b)

Meaning:

> Give me the values that exist in both sets.

---

# 28. Intersection Mental Model

A:

    {1, 2, 3}

B:

    {3, 4, 5}

Common:

    {3}

Therefore:

    A ∩ B = {3}

---

# 29. Difference

Difference finds values that exist in one set but not another.

Example:

a = {1, 2, 3}
b = {3, 4, 5}

result = a - b

Result:

    {1, 2}

Meaning:

> Give me values in A that are not in B.

Method form:

result = a.difference(b)

---

# 30. Difference Is Directional

This is extremely important.

Given:

a = {1, 2, 3}
b = {3, 4, 5}

Then:

a - b

gives:

    {1, 2}

But:

b - a

gives:

    {4, 5}

Therefore:

    a - b != b - a

Always read it as:

> Values in the LEFT set that are not in the RIGHT set.

---

# 31. Symmetric Difference

Symmetric difference finds values that exist in either set but not both.

Example:

a = {1, 2, 3}
b = {3, 4, 5}

result = a ^ b

Result:

    {1, 2, 4, 5}

The common value `3` is removed.

Method form:

result = a.symmetric_difference(b)

Mental model:

    Keep:
        only A
        only B

    Remove:
        common values

---

# 32. Set Operations Summary

Given:

a = {1, 2, 3}
b = {3, 4, 5}

Union:

a | b

    {1, 2, 3, 4, 5}

Intersection:

a & b

    {3}

Difference:

a - b

    {1, 2}

Reverse difference:

b - a

    {4, 5}

Symmetric difference:

a ^ b

    {1, 2, 4, 5}

---

# 33. Operator vs Method

Set operations can be written in two ways.

Union:

a | b

a.union(b)

Intersection:

a & b

a.intersection(b)

Difference:

a - b

a.difference(b)

Symmetric difference:

a ^ b

a.symmetric_difference(b)

Both are valid.

Use whichever makes the code clearer.

---

# 34. Subset

A set A is a subset of B if every element of A is also contained in B.

Example:

a = {1, 2}

b = {1, 2, 3, 4}

print(a.issubset(b))

Output:

    True

Operator:

a <= b

also means:

> A is a subset of B.

---

# 35. Superset

A set A is a superset of B if A contains every element of B.

Example:

a = {1, 2}
b = {1, 2, 3, 4}

print(b.issuperset(a))

Output:

    True

Operator:

b >= a

also represents this relationship.

---

# 36. Disjoint Sets

Two sets are disjoint if they have no common elements.

Example:

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))

Output:

    True

If they share an element:

a = {1, 2}
b = {2, 3}

print(a.isdisjoint(b))

Output:

    False

---

# 37. Set Comprehensions

Sets also support comprehensions.

Example:

numbers = [1, 2, 3, 4, 5]

squares = {number * number for number in numbers}

Result:

    {1, 4, 9, 16, 25}

Compare:

List comprehension:

squares = [number * number for number in numbers]

Set comprehension:

squares = {number * number for number in numbers}

The output collection type is different.

---

# 38. Set Comprehension with Filtering

Example:

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

Result:

    {2, 4, 6}

The same comprehension concepts from Chapter 33 apply.

---

# 39. Sets and Hashability

Set elements must be hashable.

These work:

numbers = {1, 2, 3}

names = {"Gautham", "Rahul"}

points = {(10, 20), (30, 40)}

This does not work:

data = {[1, 2], [3, 4]}

because lists are mutable and unhashable.

Dictionaries are also unhashable:

data = {
    {"name": "Gautham"}
}

This is invalid.

---

# 40. Why Must Set Elements Be Hashable?

Sets use hashing internally.

Conceptually:

    value
      ↓
    hash(value)
      ↓
    location
      ↓
    find the value

For this to work reliably, the hash of an element must remain stable.

Mutable objects can change.

For example:

numbers = [1, 2]

numbers.append(3)

The object changed.

Therefore, lists cannot be set elements.

This connects directly to the immutability concepts learned in Chapter 35.

---

# 41. Tuple vs Set

A tuple can be a set element if its contents are hashable.

Example:

points = {
    (10, 20),
    (30, 40)
}

This works.

Why?

Because tuples are immutable and, when their elements are hashable, the tuple is hashable.

This is one practical connection between:

    Tuples
        ↓
    Immutability
        ↓
    Hashability
        ↓
    Sets

---

# 42. Set vs List

| Feature | List | Set |
|---|---|---|
| Ordered | Yes | No |
| Indexed | Yes | No |
| Duplicates | Allowed | Not allowed |
| Mutable | Yes | Yes |
| Membership testing | Yes | Yes |
| Set operations | No | Yes |
| Hash-based lookup | No | Yes |

Use a list when:

> Order and positional access matter.

Use a set when:

> Uniqueness and membership matter.

---

# 43. Set vs Tuple

| Feature | Tuple | Set |
|---|---|---|
| Ordered | Yes | No |
| Indexed | Yes | No |
| Duplicates | Allowed | No |
| Mutable | No | Yes |
| Set operations | No | Yes |
| Can be hashable | Yes | N/A |
| Main purpose | Fixed structure | Unique values |

Mental model:

    List
      ↓
    Ordered + changeable


    Tuple
      ↓
    Ordered + fixed


    Set
      ↓
    Unique + membership

---

# 44. Practical Stock Example

Suppose:

portfolio_a = {
    "TCS",
    "INFY",
    "ITC",
    "RELIANCE"
}

portfolio_b = {
    "TCS",
    "INFY",
    "HDFCBANK",
    "SBIN"
}

### Common stocks

common = portfolio_a & portfolio_b

Result:

    {"TCS", "INFY"}

### Only in portfolio A

only_a = portfolio_a - portfolio_b

Result:

    {"ITC", "RELIANCE"}

### Only in portfolio B

only_b = portfolio_b - portfolio_a

Result:

    {"HDFCBANK", "SBIN"}

### All unique stocks

all_stocks = portfolio_a | portfolio_b

---

# 45. Backend Engineering Connection

Imagine an API receives duplicate user IDs:

user_ids = [
    101,
    102,
    101,
    103,
    102,
    104
]

Create unique IDs:

unique_users = set(user_ids)

Result:

    {101, 102, 103, 104}

This can be useful for:

- Removing duplicate IDs
- Validating identifiers
- Comparing groups
- Checking permissions
- Detecting missing records

---

# 46. Permission Checking

Suppose:

user_permissions = {
    "read",
    "write",
    "delete"
}

Check:

if "write" in user_permissions:
    print("User can write")

This is a natural set use case.

The question is:

> Does this permission exist?

We don't care about its position.

---

# 47. Duplicate Detection

Suppose:

values = [1, 2, 3, 2, 4, 5, 3]

We can detect duplicates:

if len(values) != len(set(values)):
    print("Duplicates found")

Why?

Original:

    7 values

Unique:

    5 values

Therefore:

    duplicates exist

---

# 48. AI/Data Processing Connection

Sets are useful when processing unique categories, identifiers, or vocabulary.

Example:

document_a_tags = {
    "python",
    "ai",
    "machine-learning"
}

document_b_tags = {
    "python",
    "ai",
    "backend"
}

Common tags:

common_tags = document_a_tags & document_b_tags

Result:

    {"python", "ai"}

Other uses include:

- Unique document IDs
- Unique tokens
- Deduplication
- Category comparison
- Vocabulary comparison
- Permission sets
- Feature/category matching

---

# 49. Common Beginner Mistakes

## Mistake 1 — Empty set

Wrong:

data = {}

Correct:

data = set()

---

## Mistake 2 — Indexing

Wrong:

numbers = {10, 20, 30}

print(numbers[0])

Sets don't support indexing.

---

## Mistake 3 — Expecting duplicates

numbers = {10, 10, 20}

Result:

    {10, 20}

---

## Mistake 4 — Depending on order

Do not assume a set will iterate in a particular order.

---

## Mistake 5 — `remove()` vs `discard()`

remove():

    Raises KeyError if missing.

discard():

    Does nothing if missing.

---

## Mistake 6 — Set `pop()`

Do not assume:

numbers.pop()

means:

> Remove the last element.

For a set, it removes an arbitrary element.

---

# 50. Interview Questions

## Beginner

1. What is a set?
2. Why does a set remove duplicates?
3. Are sets ordered?
4. Can sets be indexed?
5. How do you add an element?
6. How do you remove an element?
7. How do you create an empty set?
8. What is the difference between a set and a list?
9. Can a set contain duplicate values?

---

## Intermediate

1. What is the difference between `add()` and `update()`?
2. What is the difference between `remove()` and `discard()`?
3. What does `set.pop()` do?
4. What is union?
5. What is intersection?
6. What is difference?
7. Why is difference directional?
8. What is symmetric difference?
9. What is a subset?
10. What is a superset?
11. What does `isdisjoint()` mean?
12. Why are sets useful for membership testing?

---

## Advanced

### Question 1

What is the output?

numbers = {1, 2, 2, 3, 3, 3}

print(numbers)

Why?

---

### Question 2

Given:

a = {1, 2, 3}
b = {3, 4, 5}

What are:

a | b

a & b

a - b

b - a

a ^ b

---

### Question 3

Why does:

data = {}

create a dictionary instead of a set?

---

### Question 4

Why does this work?

data = {(10, 20)}

But this does not?

data = {[10, 20]}

---

### Question 5

What is the difference between:

a.remove(10)

and:

a.discard(10)

---

### Question 6

Why are set elements required to be hashable?

---

# 51. Assignments

## Assignment 1 — Basic Set Operations

Create:

numbers = {10, 20, 30, 40, 50}

Perform:

1. Print the set.
2. Print the length.
3. Check whether `30` exists.
4. Check whether `100` exists.
5. Add `60`.
6. Add `60` again.
7. Remove `20`.
8. Discard `100`.
9. Iterate through the set.
10. Clear the set.
11. Print the final set.

---

# 52. Assignment 2 — Duplicate Removal

Given:

numbers = [
    10,
    20,
    10,
    30,
    20,
    40,
    30,
    50
]

Tasks:

1. Convert the list into a set.
2. Print the unique values.
3. Print the number of original values.
4. Print the number of unique values.
5. Determine whether duplicates existed.

Hint:

    Compare:

    len(numbers)

    and:

    len(set(numbers))

---

# 53. Assignment 3 — Stock Set

Create:

stocks = {
    "TCS",
    "INFY",
    "ITC"
}

Perform:

1. Add `"RELIANCE"`.
2. Add `"HDFCBANK"`.
3. Check whether `"TCS"` exists.
4. Check whether `"SBIN"` exists.
5. Remove `"ITC"`.
6. Discard `"SBIN"`.
7. Print the final set.
8. Print the number of stocks.

---

# 54. Assignment 4 — Set Operations

Given:

portfolio_a = {
    "TCS",
    "INFY",
    "ITC",
    "RELIANCE"
}

portfolio_b = {
    "TCS",
    "INFY",
    "HDFCBANK",
    "SBIN"
}

Find:

1. All unique stocks.
2. Stocks present in both portfolios.
3. Stocks only in portfolio A.
4. Stocks only in portfolio B.
5. Stocks present in exactly one portfolio.

Use:

- Union
- Intersection
- Difference
- Symmetric difference

---

# 55. Assignment 5 — Set Comprehension

Given:

numbers = [1, 2, 2, 3, 4, 4, 5, 6]

Using set comprehensions:

1. Create a set of squares.
2. Create a set of even numbers.
3. Create a set of odd numbers.
4. Create a set of numbers greater than `3`.
5. Create a set of doubled values.

---

# 56. Assignment 6 — Permission System

Create:

user_permissions = {
    "read",
    "write"
}

required_permissions = {
    "read",
    "write",
    "delete"
}

Tasks:

1. Find which permissions the user has.
2. Find which required permissions are missing.
3. Check whether the user has all required permissions.
4. Add `"delete"` to the user's permissions.
5. Check again whether all required permissions exist.

Think about how this relates to authentication and authorization.

---

# 57. Assignment 7 — Two Users

Given:

user_a = {
    "Python",
    "React",
    "SQL",
    "Docker"
}

user_b = {
    "Python",
    "FastAPI",
    "SQL",
    "AWS"
}

Find:

1. Skills both users have.
2. Skills only user A has.
3. Skills only user B has.
4. All unique skills.
5. Skills that only one user has.

This is the same set logic used in the portfolio example.

---

# 58. Engineering Challenge

Imagine your application receives stock holdings from two brokers.

Broker A:

broker_a = [
    "TCS",
    "INFY",
    "ITC",
    "TCS",
    "RELIANCE"
]

Broker B:

broker_b = [
    "INFY",
    "HDFCBANK",
    "SBIN",
    "INFY"
]

Tasks:

1. Remove duplicates from each broker.
2. Find stocks held through both brokers.
3. Find stocks held only through Broker A.
4. Find stocks held only through Broker B.
5. Find the complete unique list of stocks.
6. Find stocks that appear in exactly one broker.

Think about why sets are more appropriate than lists for the comparison operations.

---

# 59. Engineering Challenge 2 — Data Validation

Suppose your API receives:

requested_fields = {
    "name",
    "email",
    "phone",
    "address"
}

allowed_fields = {
    "name",
    "email",
    "phone"
}

Tasks:

1. Find fields that are not allowed.
2. Check whether all requested fields are valid.
3. Find the fields that are valid.
4. Explain why a set is a better data structure than a list for this particular validation.

---

# 60. Chapter Summary

A set is:

> An unordered collection of unique values.

Create:

numbers = {1, 2, 3}

Empty set:

numbers = set()

Add one:

numbers.add(4)

Add multiple:

numbers.update([5, 6])

Remove:

numbers.remove(4)

Safe remove:

numbers.discard(100)

Membership:

4 in numbers

Union:

a | b

Intersection:

a & b

Difference:

a - b

Symmetric difference:

a ^ b

Subset:

a.issubset(b)

Superset:

a.issuperset(b)

Disjoint:

a.isdisjoint(b)

Set comprehension:

{x * 2 for x in numbers}

---

# 61. Key Takeaways

- Sets contain unique elements.
- Sets are unordered.
- Sets do not support indexing.
- Sets are mutable.
- Sets are excellent for membership testing.
- `add()` adds one element.
- `update()` adds multiple elements.
- `remove()` raises an error if the element doesn't exist.
- `discard()` does not raise an error if the element is missing.
- `pop()` removes an arbitrary element from a set.
- `set()` creates an empty set.
- `{}` creates an empty dictionary.
- Sets are useful for removing duplicates.
- Union combines unique values.
- Intersection finds common values.
- Difference finds values in one set but not another.
- Symmetric difference finds values present in exactly one set.
- Subsets and supersets describe relationships between sets.
- `isdisjoint()` checks whether two sets have no common values.
- Set elements must be hashable.
- Tuples can be set elements when their contents are hashable.
- Sets are extremely useful for membership checks and collection comparisons.
- Set comprehensions follow the same basic pattern as list comprehensions.
- Choosing a set should be driven by uniqueness and membership requirements.

---

# 62. Important Mental Model

At this point, you have learned four important Python collections:

    LIST
      ↓
    Ordered
      ↓
    Mutable
      ↓
    Duplicates allowed


    TUPLE
      ↓
    Ordered
      ↓
    Immutable
      ↓
    Duplicates allowed


    SET
      ↓
    Unordered
      ↓
    Mutable
      ↓
    Unique values


    DICTIONARY
      ↓
    Key → Value
      ↓
    Lookup by key

The next chapter will focus on dictionaries.

---

# 63. Chapter Completion Criteria

Before moving to Chapter 37, you should be able to answer:

### Question 1

Why would you use:

numbers = {1, 2, 3}

instead of:

numbers = [1, 2, 3]?

---

### Question 2

What happens here?

numbers = {1, 1, 2, 2, 3}

---

### Question 3

What is the difference between:

numbers.remove(10)

and:

numbers.discard(10)

---

### Question 4

Given:

a = {1, 2, 3}
b = {3, 4, 5}

Explain:

a | b

a & b

a - b

a ^ b

---

### Question 5

Why is:

data = set()

different from:

data = {}

---

### Question 6

Why can't this be a set?

data = {[1, 2], [3, 4]}

---

### Question 7

Given:

portfolio_a = {"TCS", "INFY", "ITC"}
portfolio_b = {"INFY", "ITC", "RELIANCE"}

How would you find:

- Common stocks?
- Stocks only in A?
- Stocks only in B?
- All unique stocks?

---

If you can answer these without referring to the notes, you are ready for:

# Next Chapter – Chapter 37: Dictionaries

Dictionaries are particularly important because they become one of the most heavily used Python data structures in **backend development, APIs, JSON, FastAPI, data processing, and AI engineering**.