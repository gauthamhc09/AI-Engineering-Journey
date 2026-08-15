# Chapter 34 – Nested Lists

## 1. Introduction

A nested list is a list that contains other lists.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

This creates a two-dimensional structure:

    matrix
      |
      +-- [1, 2, 3]
      |
      +-- [4, 5, 6]
      |
      +-- [7, 8, 9]

Nested lists are useful for representing:

- Matrix-like data
- Rows and columns
- Groups of records
- Hierarchical data
- Batches of data
- Sequences of sequences

---

# 2. What Is a Nested List?

A nested list is simply:

> A list containing one or more lists as its elements.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

The outer list contains two inner lists.

    matrix
      |
      +-- [1, 2, 3]
      |
      +-- [4, 5, 6]

---

# 3. Indexing the Outer List

Consider:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

The outer list has:

    Index 0 → [1, 2, 3]
    Index 1 → [4, 5, 6]

Therefore:

print(matrix[0])

Output:

    [1, 2, 3]

And:

print(matrix[1])

Output:

    [4, 5, 6]

---

# 4. Accessing an Individual Element

To access an individual value inside a nested list, use two indexes.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

To access `5`:

matrix[1][1]

Result:

    5

Think of it as two operations:

matrix[1]

gives:

    [4, 5, 6]

Then:

[4, 5, 6][1]

gives:

    5

Therefore:

    matrix[1][1]
          |
          +-- select row
                 |
                 +-- select element

---

# 5. Matrix[row][column]

Consider:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Visual representation:

          column
          0   1   2

        +---+---+---+
row 0   | 1 | 2 | 3 |
        +---+---+---+
row 1   | 4 | 5 | 6 |
        +---+---+---+
row 2   | 7 | 8 | 9 |
        +---+---+---+

Examples:

matrix[0][0]

    → 1

matrix[1][2]

    → 6

matrix[2][1]

    → 8

The first index selects the row.

The second index selects the element within that row.

---

# 6. Modifying Nested Lists

Nested lists are mutable.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix[1][2] = 99

Now:

print(matrix)

Output:

    [
        [1, 2, 3],
        [4, 5, 99]
    ]

We modified:

    row    → 1
    column → 2

---

# 7. Adding to an Inner List

Inner lists are normal Python lists.

Therefore, normal list methods can be used.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix[0].append(4)

Result:

    [
        [1, 2, 3, 4],
        [4, 5, 6]
    ]

`matrix[0]` returns the first inner list.

Then `.append(4)` modifies that inner list.

---

# 8. Iterating Through the Outer List

Given:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

We can iterate through each row:

for row in matrix:
    print(row)

Output:

    [1, 2, 3]
    [4, 5, 6]

The variable `row` represents one inner list at a time.

---

# 9. Nested for Loops

To access every individual element:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in matrix:
    for number in row:
        print(number)

Output:

    1
    2
    3
    4
    5
    6

The outer loop processes each row.

The inner loop processes each element inside that row.

Mental model:

    outer list
        ↓
    select row
        ↓
    iterate through row
        ↓
    select next row
        ↓
    repeat

---

# 10. Flattening a Nested List

Flattening means converting:

    [
        [1, 2, 3],
        [4, 5, 6]
    ]

into:

    [1, 2, 3, 4, 5, 6]

Using nested loops:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = []

for row in matrix:
    for number in row:
        result.append(number)

print(result)

Output:

    [1, 2, 3, 4, 5, 6]

---

# 11. Flattening with a List Comprehension

The same operation can be written as:

result = [number for row in matrix for number in row]

This is equivalent to:

result = []

for row in matrix:
    for number in row:
        result.append(number)

The comprehension should be read as:

    for each row in matrix
        for each number in row
            add number to result

---

# 12. Filtering Nested Lists

We can filter values while flattening.

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

Equivalent loops:

even_numbers = []

for row in matrix:
    for number in row:
        if number % 2 == 0:
            even_numbers.append(number)

---

# 13. Transforming Nested Lists

We can transform every element.

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

Notice that this produces a flat list.

---

# 14. Preserving the Nested Structure

Sometimes we want to transform the values while keeping the original structure.

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

The outer comprehension processes each row.

The inner comprehension processes each number within the row.

---

# 15. Flattened vs Preserved Structure

These two operations are different.

### Flatten

[number for row in matrix for number in row]

Result:

    [1, 2, 3, 4]

### Preserve structure

[
    [number * 2 for number in row]
    for row in matrix
]

Result:

    [
        [2, 4],
        [6, 8]
    ]

Important question:

> Do I want one flat list or do I want to maintain the nested structure?

---

# 16. Uneven Nested Lists

Nested lists do not have to contain rows of equal length.

Example:

data = [
    [1, 2],
    [3, 4, 5],
    [6]
]

This is completely valid Python.

We can still iterate:

for row in data:
    for number in row:
        print(number)

Output:

    1
    2
    3
    4
    5
    6

Python does not require nested lists to be rectangular.

---

# 17. Nested Lists vs Mathematical Matrices

A nested list can represent matrix-like data:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

However, Python's built-in lists do not enforce matrix dimensions.

This is also valid:

data = [
    [1, 2],
    [3, 4, 5]
]

A mathematical matrix normally has consistent dimensions.

Later, libraries such as NumPy provide specialized structures for numerical arrays and matrices.

For now:

> A nested list is simply a list containing other lists.

---

# 18. Slicing Nested Lists

Inner lists can be sliced because they are normal lists.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

Get the first row:

matrix[0]

Result:

    [1, 2, 3]

Get part of the first row:

matrix[0][1:]

Result:

    [2, 3]

This is two operations:

    matrix[0]
        ↓
    [1, 2, 3]
        ↓
    [1, 2, 3][1:]
        ↓
    [2, 3]

---

# 19. Outer List Slicing

We can also slice the outer list.

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix[:1]

Result:

    [[1, 2, 3]]

Notice the difference.

### Indexing

matrix[0]

Result:

    [1, 2, 3]

### Slicing

matrix[:1]

Result:

    [[1, 2, 3]]

This follows the same rule learned in List Slicing:

    Indexing → returns an element

    Slicing → returns a list

---

# 20. Nested Lists and References

Nested lists introduce an important reference concept.

Consider:

row = [1, 2, 3]

matrix = [row, row]

Both elements of `matrix` refer to the same inner list.

Conceptually:

    matrix
      |
      +--------+
      |        |
      ↓        ↓
    [1, 2, 3]  same object

Therefore:

matrix[0][0] = 999

will affect both references.

Result:

    [
        [999, 2, 3],
        [999, 2, 3]
    ]

This happens because both rows refer to the same object.

---

# 21. The Common Nested List Trap

Consider:

matrix = [[0] * 3] * 3

It appears to create:

    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

But the same inner list is referenced three times.

Therefore:

matrix[0][0] = 1

can produce:

    [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ]

This is a very common Python interview question.

---

# 22. Correct Way to Create Independent Rows

Use a list comprehension:

matrix = [[0] * 3 for _ in range(3)]

Now each iteration creates a new inner list.

Conceptually:

    matrix
      |
      +--→ [0, 0, 0]
      |
      +--→ [0, 0, 0]
      |
      +--→ [0, 0, 0]

Each row is independent.

Therefore:

matrix[0][0] = 1

produces:

    [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

---

# 23. Why `_` Is Used

You will often see:

for _ in range(3):
    print("Hello")

The underscore `_` is a conventional variable name used when we do not care about the actual loop value.

For example:

matrix = [[0] * 3 for _ in range(3)]

means:

> Create three independent rows.

The value generated by `range(3)` is not needed.

---

# 24. Nested Lists and Functions

Nested lists can be passed to functions.

Example:

def calculate_total(matrix):
    total = 0

    for row in matrix:
        for number in row:
            total += number

    return total

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(calculate_total(matrix))

Output:

    21

This combines:

- Functions
- Loops
- Nested collections

---

# 25. Backend Engineering Connection

Nested lists can represent grouped records.

Example:

orders = [
    ["Laptop", 2],
    ["Keyboard", 5],
    ["Mouse", 10]
]

We can process them:

for order in orders:
    product = order[0]
    quantity = order[1]

    print(product, quantity)

However, as data becomes more structured, dictionaries may be clearer:

{
    "product": "Laptop",
    "quantity": 2
}

This demonstrates an important engineering principle:

> Choose the collection based on the structure and access pattern of the data.

---

# 26. AI Engineering Connection

Nested collections appear frequently in AI and data processing.

Conceptually:

    Batch
      |
      +-- sample
      +-- sample
      +-- sample

Or:

    Document
      |
      +-- chunk
      +-- chunk
      +-- chunk

Or:

    Batch
      |
      +-- token sequence
      +-- token sequence
      +-- token sequence

Example:

batch = [
    [101, 200, 300],
    [101, 400, 500],
    [101, 600, 700]
]

Later, NumPy and PyTorch provide specialized multidimensional arrays and tensors.

Understanding nested Python lists gives you the foundation for understanding those structures.

---

# 27. Common Beginner Mistakes

## Mistake 1 — Forgetting the second index

Given:

matrix = [
    [1, 2],
    [3, 4]
]

This:

matrix[1]

returns:

    [3, 4]

To get `4`:

matrix[1][1]

---

## Mistake 2 — Confusing indexing and slicing

matrix[0]

returns:

    [1, 2, 3]

while:

matrix[:1]

returns:

    [[1, 2, 3]]

---

## Mistake 3 — Shared inner lists

Be careful with:

matrix = [[0] * 3] * 3

because the rows refer to the same inner list.

---

## Mistake 4 — Overusing nested comprehensions

Nested comprehensions can become difficult to read.

Use normal loops when the logic becomes complicated.

---

## Mistake 5 — Assuming nested lists must have equal lengths

This is valid:

data = [
    [1, 2],
    [3, 4, 5]
]

Python does not require equal row lengths.

---

# 28. Best Practices

### Use nested lists when the hierarchy is natural

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

### Avoid excessive nesting

If you find yourself writing:

data[2][4][1][3]

the data structure may be unnecessarily complicated.

### Be aware of shared references

Especially when constructing nested lists.

### Use dictionaries for structured records

Instead of:

["Gautham", 33, "Developer"]

consider:

{
    "name": "Gautham",
    "age": 33,
    "role": "Developer"
}

when named fields make the data clearer.

---

# 29. Interview Questions

## Beginner

1. What is a nested list?
2. How do you access an element inside a nested list?
3. What does `matrix[0]` return?
4. What does `matrix[0][1]` return?
5. How do you iterate through every element of a nested list?
6. How do you modify an element inside a nested list?
7. Can nested lists have different lengths?
8. Can a list contain more than two levels of nesting?

---

## Intermediate

1. What is the difference between:

matrix[0]

and:

matrix[:1]

2. How would you flatten a two-dimensional list?

3. What is the equivalent normal loop for:

[number for row in matrix for number in row]

4. How do you preserve the nested structure while transforming every element?

5. Why does:

[[0] * 3] * 3

create a reference problem?

6. What is the difference between:

[[0] * 3] * 3

and:

[[0] * 3 for _ in range(3)]

---

## Advanced

### Question 1

Predict the output:

matrix = [
    [1, 2],
    [3, 4]
]

matrix[0][1] = 99

print(matrix)

---

### Question 2

Predict:

matrix = [[0] * 3] * 3

matrix[0][0] = 1

print(matrix)

Explain why this happens.

---

### Question 3

Predict:

matrix = [[0] * 3 for _ in range(3)]

matrix[0][0] = 1

print(matrix)

Explain why this is different from Question 2.

---

### Question 4

Convert this into a list comprehension:

result = []

for row in matrix:
    for number in row:
        result.append(number * 2)

---

# 30. Assignments

## Basic

Create:

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

Perform:

1. Print the first row.
2. Print the second row.
3. Print `50`.
4. Print `90`.
5. Change `50` to `500`.
6. Print the updated matrix.
7. Iterate through every element using nested `for` loops.

---

# 31. Intermediate Assignment

Given:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Create:

1. A flattened list.
2. A list containing only even numbers.
3. A list containing the square of every number.
4. A new matrix where every number is doubled.

Expected doubled matrix:

    [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]
    ]

Use:

- Normal nested loops
- Nested list comprehensions

where appropriate.

---

# 32. Challenge Assignment

Predict the output before executing:

matrix = [[0] * 3] * 3

matrix[0][1] = 5

print(matrix)

Then create the correct version using:

matrix = [[0] * 3 for _ in range(3)]

Perform the same modification.

Compare the results.

The goal is to understand shared references rather than simply memorize the solution.

---

# 33. Engineering Challenge

Given:

students = [
    ["Gautham", 85, 90, 95],
    ["Rahul", 70, 80, 75],
    ["Arun", 95, 92, 88]
]

Using nested loops:

1. Print each student's name.
2. Print each student's marks.
3. Calculate each student's total.
4. Calculate each student's average.

Then consider:

> Is a nested list the best data structure for this information?

Compare it conceptually with:

[
    {
        "name": "Gautham",
        "marks": [85, 90, 95]
    }
]

This is an important data-structure design question.

---

# 34. Chapter Summary

A nested list is:

> A list containing other lists.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

Access an inner list:

matrix[0]

Access an individual element:

matrix[0][1]

Modify an element:

matrix[0][1] = 99

Iterate:

for row in matrix:
    for number in row:
        print(number)

Flatten:

[number for row in matrix for number in row]

Transform while preserving structure:

[
    [number * 2 for number in row]
    for row in matrix
]

---

# 35. Critical Memory Concept

Be careful with:

matrix = [[0] * 3] * 3

The same inner list is referenced multiple times.

Prefer:

matrix = [[0] * 3 for _ in range(3)]

when independent rows are required.

The difference is:

    [[0] * 3] * 3

    row 1 ──┐
    row 2 ──┼──→ SAME list
    row 3 ──┘

versus:

    [[0] * 3 for _ in range(3)]

    row 1 ──→ independent list
    row 2 ──→ independent list
    row 3 ──→ independent list

This is one of the most important memory/reference concepts in this chapter.

---

# 36. Key Takeaways

- A nested list contains lists as elements.
- `matrix[row][column]` performs two indexing operations.
- Nested lists can represent matrix-like and hierarchical data.
- Nested lists can have different row lengths.
- Nested loops are useful for processing nested lists.
- Nested comprehensions can flatten or transform nested structures.
- Slicing works on both outer and inner lists.
- `matrix[0]` returns an inner list.
- `matrix[:1]` returns a new outer list.
- Nested lists can contain multiple levels of nesting.
- Shared references can cause unexpected mutation behavior.
- `[[0] * 3] * 3` shares the same inner list.
- `[[0] * 3 for _ in range(3)]` creates independent rows.
- The appropriate data structure depends on the data and access pattern.
- Nested lists provide a foundation for understanding multidimensional arrays and tensors used in AI engineering.

---

# 37. Chapter Completion Criteria

Before moving to the next chapter, you should be able to explain:

matrix[1][2]

[number for row in matrix for number in row]

[
    [number * 2 for number in row]
    for row in matrix
]

and especially:

[[0] * 3] * 3

versus:

[[0] * 3 for _ in range(3)]

The final comparison is the key memory/reference concept of this chapter.

---

# Next Chapter

## Chapter 35 – Tuples

Topics:

- Tuple creation
- Tuple indexing
- Tuple slicing
- Tuple immutability
- Tuple packing
- Tuple unpacking
- Multiple assignment
- Tuple methods
- Tuple vs list
- When to use tuples
- References and immutability
- Backend and AI engineering use cases
- Interview questions
- Practical assignments