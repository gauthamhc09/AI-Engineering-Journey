# Module 07 — Exception Handling

## Chapters
- Chapter 43 — `try` / `except`
- Chapter 44 — `else` / `finally`
- Chapter 45 — `raise`
- Chapter 46 — Custom Exceptions

---

# Chapter 43 — `try` / `except`

An exception is a problem that occurs during program execution.

Common exceptions:
- `ValueError` — correct type but invalid value
- `TypeError` — inappropriate/incompatible type
- `IndexError` — list index does not exist
- `KeyError` — dictionary key does not exist
- `ZeroDivisionError` — division by zero

Basic syntax:

```python
try:
    # code that might fail
except SomeException:
    # handle the exception
```

Example:

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number")
```

### Execution rule

Python executes `try` from top to bottom. Once an exception occurs, the remaining statements in that `try` block are skipped.

```python
try:
    print("A")
    x = 10 / 0
    print("B")
except ZeroDivisionError:
    print("C")
```

Output:

```text
A
C
```

### Multiple exceptions

```python
try:
    x = int(input("Enter number: "))
    result = 100 / x
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Capture the exception

```python
try:
    number = int("hello")
except ValueError as e:
    print(e)
```

Prefer specific exceptions such as `ValueError` over a bare `except:` when possible.

---

# Chapter 44 — `else` and `finally`

## `else`

`else` runs only when the `try` block completes successfully.

```python
try:
    number = int("100")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful")
```

Mental model:

```text
try     → attempt
except  → failure
else    → success
```

## `finally`

`finally` runs regardless of whether an exception occurred.

```python
try:
    number = int("hello")
except ValueError:
    print("Invalid number")
finally:
    print("Finished")
```

Output:

```text
Invalid number
Finished
```

`finally` is commonly used for cleanup, such as closing files or connections.

Complete flow:

```text
try
 ↓
exception?
 ├── NO  → else
 └── YES → matching except
              ↓
           finally
              ↓
           continue
```

---

# Chapter 45 — `raise`

`raise` lets your code deliberately trigger an exception.

```python
raise ValueError("Invalid value")
```

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

This is useful for enforcing application/business rules.

### `raise` inside a function

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount
```

The function detects the invalid condition; the caller can decide how to handle it.

### `TypeError` vs `ValueError`

Use `TypeError` when the type is inappropriate:

```python
if not isinstance(age, int):
    raise TypeError("Age must be an integer")
```

Use `ValueError` when the type is acceptable but the value is invalid:

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

### Bare `raise`

Inside an `except` block:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Logging error")
    raise
```

`raise` without an argument means **re-raise the exception currently being handled**.

It does NOT mean "raise whatever error happens next."

---

# Chapter 46 — Custom Exceptions

A custom exception is a class created for a meaningful application/domain failure.

```python
class InsufficientBalanceError(Exception):
    pass
```

Raise it:

```python
raise InsufficientBalanceError("Insufficient balance")
```

Catch it:

```python
try:
    balance = withdraw(1000, 1500)
except InsufficientBalanceError:
    print("Withdrawal failed")
```

### Why use custom exceptions?

Instead of:

```python
raise ValueError("Insufficient balance")
```

you can use:

```python
raise InsufficientBalanceError("Insufficient balance")
```

This makes the domain meaning explicit.

Examples:

```text
PortfolioNotFoundError
UnsupportedBrokerError
InsufficientBalanceError
InvalidTransactionError
```

Don't create custom exceptions for every small validation problem. Use built-in exceptions when they communicate the problem well.

### Custom exception hierarchy

```python
class PortfolioError(Exception):
    pass

class PortfolioNotFoundError(PortfolioError):
    pass

class InvalidPortfolioError(PortfolioError):
    pass
```

Hierarchy:

```text
Exception
    ↓
PortfolioError
    ├── PortfolioNotFoundError
    └── InvalidPortfolioError
```

Terminology:
- `PortfolioError` → base/parent class
- `PortfolioNotFoundError` → subclass/child class
- An object created from `PortfolioNotFoundError` → instance

You can catch either a specific child:

```python
except PortfolioNotFoundError:
```

or the broader parent:

```python
except PortfolioError:
```

### Custom exceptions can store data

```python
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Balance is {balance}, but withdrawal requires {amount}"
        )
```

---

# Real-World Backend Mental Model

Exception handling is important in backend and AI/LLM applications:

```text
API Request
    ↓
Service / Business Logic
    ↓
Validation
    ↓
raise appropriate exception
    ↓
API layer handles/translates exception
    ↓
HTTP response
```

This pattern will become especially useful with FastAPI, databases, external APIs, file processing, and LLM services.

---

# Module 07 Cheat Sheet

| Concept | Meaning |
|---|---|
| `try` | Attempt code that might fail |
| `except` | Handle an exception |
| `else` | Execute only if `try` succeeds |
| `finally` | Execute regardless of success/failure |
| `raise` | Deliberately raise/propagate an exception |
| Custom exception | Application-specific exception class |

## One-line mental model

```text
try → attempt
except → failure
else → success
finally → cleanup
raise → signal a problem
custom exception → meaningful domain-specific failure
```

## Most important rules

1. Once an exception occurs in `try`, remaining `try` statements are skipped.
2. Only a matching `except` handles that exception.
3. `else` runs only when `try` succeeds.
4. `finally` runs regardless of success or failure.
5. `raise` lets your code deliberately signal an invalid condition.
6. `raise` without an argument inside `except` re-raises the current exception.
7. Custom exceptions should inherit from `Exception` or an appropriate custom base.
8. Prefer specific exceptions when possible.
9. Custom exceptions are useful for meaningful domain failures.
10. `PortfolioNotFoundError` is a subclass of `PortfolioError`, not an instance.

---

# Module 07 Summary

Exception handling makes failures controlled, explicit, and meaningful.

```text
try/except
    ↓
else for successful execution
    ↓
finally for cleanup
    ↓
raise for deliberate errors
    ↓
custom exceptions for domain-specific failures
```
