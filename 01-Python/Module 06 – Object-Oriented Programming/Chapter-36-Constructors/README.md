# Chapter 36 — Constructors (`__init__`)

## Overview

In Chapter 35, we learned how objects hold state and behavior. `__init__` lets us establish an object's initial state when the object is created.

```text
Class → Create object → __init__() → Initialize state → Ready-to-use object
```

## 36.1 — Why Do We Need `__init__`?

Without it:

```python
class BankAccount:
    pass

sbi = BankAccount()
sbi.balance = 10000
```

With it:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

sbi = BankAccount(10000)
```

The second approach initializes the object immediately and makes required initial state explicit.

## 36.2 — What is `__init__`?

`__init__` is a special method that Python invokes during object initialization.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

For:

```python
sbi = BankAccount(10000)
```

conceptually:

```text
Create object → run __init__ → self.balance = 10000 → object ready
```

Normally, we do not call `__init__` manually.

## 36.3 — `self`, Parameters, and Attributes

Consider:

```python
def __init__(self, balance):
    self.balance = balance
```

- `self` → current object
- `balance` → constructor parameter/input
- `self.balance` → object's attribute/state

For `sbi = BankAccount(10000)`:

```text
self    → sbi
balance → 10000
```

Therefore:

```python
self.balance = balance
```

conceptually becomes:

```python
sbi.balance = 10000
```

## 36.4 — Constructor Parameters vs Object State

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

For:

```python
student1 = Student("Gautham", 34)
```

parameters receive the inputs, and `self.name` / `self.age` become object state.

```text
name → parameter/input
self.name → object state

age → parameter/input
self.age → object state
```

## 36.5 — Parameters Do Not Automatically Become Attributes

This does **not** create `self.name`:

```python
class Product:
    def __init__(self, name):
        print(name)
```

To create the attribute:

```python
self.name = name
```

Parameters and attributes are different concepts.

## 36.6 — Constructor Parameters Can Have Different Names

This is valid:

```python
class BankAccount:
    def __init__(self, name, balance):
        self.account_holder = name
        self.balance = balance
```

Matching names are also common and clear:

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
```

Both are valid.

## 36.7 — Constructor Can Initialize Derived State

A constructor can calculate initial state:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
```

However, storing derived values can create stale state if the underlying values change.

For example, changing `width` later would not automatically update `self.area`.

## 36.8 — Stored State vs Calculated Value

Instead of storing `area`, calculate it when needed:

```python
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width
```

Now the calculation always uses current state.

```text
Stored state: height, width
Derived value: area
```

## 36.9 — `return` vs Storing an Attribute

Storing:

```python
self.area = self.height * self.width
```

adds `area` to object state.

Returning:

```python
return self.height * self.width
```

provides the calculated value without necessarily storing it as object state.

## 36.10 — Constructor vs Normal Method

### `__init__`

Purpose: establish initial object state.

### Normal method

Purpose: perform behavior on an existing object.

```text
__init__() → initialize
normal method → operate after initialization
```

## 36.11 — Constructor Validation

Constructors can reject invalid input:

```python
class Rectangle:
    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be greater than 0")

        self.height = height
        self.width = width
```

This prevents invalid objects from being successfully initialized.

## 36.12 — `raise ValueError`

`raise` explicitly signals an error:

```python
raise ValueError("Initial balance cannot be negative")
```

This tells the caller that the supplied value is invalid.

## 36.13 — Object Invariants

A constructor can establish rules that should remain true for valid objects.

Examples:

```text
Rectangle: height > 0, width > 0
BankAccount: balance >= 0
StockHolding: quantity > 0
```

These rules are commonly called **invariants**.

## 36.14 — Final BankAccount Implementation

```python
class BankAccount:

    def __init__(self, account_holder, initial_balance):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount

    def show_balance(self):
        print(f"{self.account_holder} balance is {self.balance}")
```

Example:

```python
canara = BankAccount("Gautham", 10000)
canara.deposit(5000)
canara.withdraw(3000)
canara.show_balance()
```

Final state:

```text
canara
├── account_holder = "Gautham"
└── balance = 12000
```

## 36.15 — Important Naming Lesson

We changed:

```python
self.initial_balance
```

to:

```python
self.balance
```

because `initial_balance` describes the constructor input, while `balance` represents the account's current state.

```text
initial_balance → constructor input
balance → current object state
```

Good state names should describe what the value represents now.

## 36.16 — Exception Handling Connection

Constructor errors can be handled by the calling code:

```python
try:
    account = BankAccount("Gautham", -5000)
except ValueError as error:
    print(error)
```

The class decides when invalid state should raise an error; the caller decides whether and how to handle it.

# Common Mistakes

1. Forgetting `self` in `__init__`.
2. Forgetting to assign constructor parameters to attributes.
3. Confusing `balance` with `self.balance`.
4. Assuming parameters automatically become attributes.
5. Storing derived state unnecessarily.
6. Using misleading names such as `self.initial_balance` for changing current balance.
7. Putting unrelated behavior into `__init__` instead of normal methods.

# Practical Engineering Connection

Constructors are useful when modeling backend/domain entities such as:

```text
User
Account
Order
Product
Portfolio
StockHolding
APIClient
DatabaseConnection
```

They help ensure objects begin life with valid, meaningful state. This foundation will connect to FastAPI, databases, data models, and eventually AI/LLM systems.

# Key Takeaways

1. `__init__` initializes object state.
2. `self` refers to the current object.
3. Constructor parameters are inputs.
4. `self.attribute` represents object state.
5. Parameters do not automatically become attributes.
6. Constructors can validate input.
7. `raise ValueError` can reject invalid input.
8. Constructors can establish object invariants.
9. Derived values do not always need to be stored.
10. `return` and storing an attribute have different purposes.
11. Good state names should describe current meaning.
12. Normal methods handle behavior after initialization.

# Chapter 36 Completion Checklist

- [x] Understand why `__init__` exists
- [x] Understand what `__init__` does
- [x] Understand automatic object initialization
- [x] Understand constructor parameters
- [x] Understand `self` inside constructors
- [x] Understand `self.attribute = parameter`
- [x] Distinguish parameters from object state
- [x] Understand that parameters do not automatically become attributes
- [x] Initialize multiple objects with different state
- [x] Understand constructor vs normal methods
- [x] Understand derived/calculated values
- [x] Understand `return` vs storing an attribute
- [x] Understand constructor validation
- [x] Understand `raise ValueError`
- [x] Understand basic object invariants
- [x] Connect exception handling with OOP
- [x] Complete Student constructor exercise
- [x] Complete BankAccount constructor exercise
- [x] Complete Rectangle exercise
- [x] Complete constructor validation exercise
- [x] Complete BankAccount practical challenge
- [x] Demonstrate understanding through code
- [x] Apply appropriate state naming

## Chapter 36 Status

**Completed — Core understanding demonstrated.**

Next:

# Chapter 37 — Instance Variables vs Class Variables

We will learn:

- Instance variables
- Class variables
- How attribute lookup works conceptually
- Why each object can have independent instance state
- When class variables are useful
- Common mistakes with mutable class variables
