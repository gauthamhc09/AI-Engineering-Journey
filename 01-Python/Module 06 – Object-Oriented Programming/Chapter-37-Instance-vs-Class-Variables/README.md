# Chapter 37 --- Instance vs Class Variables, Encapsulation & Properties

## 37.1 Instance Variables

Instance variables belong to a particular object.

``` python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("Gautham", 85)
student2 = Student("Rahul", 92)
```

Each object has its own `name` and `marks`.

``` text
student1
├── name = "Gautham"
└── marks = 85

student2
├── name = "Rahul"
└── marks = 92
```

Changing one object's instance variable does not change another object's
value.

------------------------------------------------------------------------

## 37.2 Class Variables

A class variable belongs to the class and can be shared through
instances.

``` python
class Car:
    wheels = 4
```

``` python
car1 = Car()
car2 = Car()

print(car1.wheels)  # 4
print(car2.wheels)  # 4
print(Car.wheels)   # 4
```

Conceptually:

``` text
Car
└── wheels = 4
```

### Instance Override / Shadowing

``` python
car1.wheels = 6
```

creates an instance attribute on `car1`.

Now:

``` text
car1.wheels → 6
car2.wheels → 4
Car.wheels  → 4
```

The class variable is unchanged.

This is called **shadowing**.

------------------------------------------------------------------------

## 37.3 Attribute Lookup

For:

``` python
car1.wheels
```

the useful mental model is:

``` text
1. Look on the instance.
2. If not found, look on its class.
3. If not found, continue through the inheritance hierarchy.
```

This explains why an instance can access a class variable without
actually storing it on the instance.

------------------------------------------------------------------------

## 37.4 Class-Level vs Instance-Level State

Ask:

> Does this information belong to one particular object, or does it
> conceptually belong to the class as a whole?

Example:

``` python
class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
```

Here:

-   `holder` → instance state
-   `balance` → instance state
-   `bank_name` → class-level state

The distinction is about **ownership and meaning**, not merely whether
values happen to be identical.

------------------------------------------------------------------------

## 37.5 `__dict__`

`__dict__` lets you inspect an object's or class's namespace.

``` python
class Car:
    wheels = 4

car1 = Car()

print(Car.__dict__)
print(car1.__dict__)
```

Initially, `car1.__dict__` does not contain `wheels`, because `wheels`
belongs to the class.

After:

``` python
car1.wheels = 6
```

`car1.__dict__` contains its own `wheels`.

------------------------------------------------------------------------

## 37.6 Attribute Lookup vs Assignment

Reading:

``` python
car1.wheels
```

performs attribute lookup.

Assignment:

``` python
car1.wheels = 6
```

creates or updates an attribute on `car1`.

It does not automatically modify `Car.wheels`.

------------------------------------------------------------------------

## 37.7 Shared Class State

Class variables can represent state shared across instances.

``` python
class Employee:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1
```

Each new object increments the same class-level counter.

``` python
employee1 = Employee("Gautham")
employee2 = Employee("Rahul")

print(Employee.employee_count)  # 2
```

When modifying class-level state, `ClassName.class_variable` makes the
intention explicit.

------------------------------------------------------------------------

## 37.8 Mutable Class Variables

Be careful with mutable class variables:

-   `list`
-   `dict`
-   `set`

Example:

``` python
class Team:
    players = []
```

There is one shared list at the class level.

Therefore:

``` python
team1 = Team()
team2 = Team()

team1.players.append("Gautham")
```

can result in:

``` python
team1.players  # ["Gautham"]
team2.players  # ["Gautham"]
```

For independent mutable state:

``` python
class Team:
    def __init__(self):
        self.players = []
```

### Engineering Principle

> If mutable state is supposed to be independent per object, initialize
> it on the instance.

------------------------------------------------------------------------

# Encapsulation

## 37.9 Encapsulation

Encapsulation means keeping an object's state and the behavior that
controls that state together, while controlling how outside code
interacts with that state.

Instead of arbitrary modification:

``` python
account.balance = -50000
```

we can expose controlled behavior:

``` python
account.deposit(5000)
account.withdraw(2000)
```

The object becomes responsible for maintaining its own rules and
invariants.

------------------------------------------------------------------------

## 37.10 Public vs Internal Attributes

### Public

``` python
self.name
```

Normal public attribute.

### Internal / Non-public by Convention

``` python
self._balance
```

A single leading underscore communicates that the attribute is an
internal implementation detail.

Python does not enforce this restriction.

### Name-Mangled

``` python
self.__balance
```

A double leading underscore triggers **name mangling**.

Conceptually:

``` text
__balance
    ↓
_BankAccount__balance
```

This is not security or true privacy. It mainly helps avoid accidental
name collisions, especially with inheritance.

------------------------------------------------------------------------

## 37.11 Name Mangling

Example:

``` python
class Parent:
    def __init__(self):
        self.__value = "Parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "Child"
```

The two attributes are effectively different:

``` text
_Parent__value → "Parent"
_Child__value  → "Child"
```

### Key point

Do not think:

``` text
__name = truly private
```

Think:

``` text
__name = name-mangled
```

------------------------------------------------------------------------

## 37.12 Designing a Class Interface

A class can expose a clean public interface while keeping implementation
details internal.

``` python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        ...

    def withdraw(self, amount):
        ...

    def get_balance(self):
        return self._balance
```

The caller interacts with public behavior instead of needing to know how
the state is internally stored.

------------------------------------------------------------------------

# Properties

## 37.13 `@property`

`@property` allows a method to be accessed using attribute syntax.

``` python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
```

Now:

``` python
account.balance
```

calls the property getter.

Not:

``` python
account.balance()
```

### Getter

``` python
@property
def balance(self):
    return self._balance
```

Conceptually:

``` text
account.balance
      ↓
property getter
      ↓
self._balance
```

Properties provide an attribute-like public interface while allowing
logic behind the access.

------------------------------------------------------------------------

## 37.14 `@property.setter`

A setter controls assignment to a property.

``` python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")

        self._price = value
```

Now:

``` python
product.price = 70000
```

runs the setter.

``` python
product.price = -100
```

raises `ValueError`.

### Important constructor pattern

Using:

``` python
self.price = price
```

inside `__init__` means initialization also goes through the setter and
its validation.

------------------------------------------------------------------------

## 37.15 Computed Properties

A property can calculate a value dynamically.

``` python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
```

Now:

``` python
rectangle.area
```

calculates the area dynamically.

There is no need to store:

``` python
self.area
```

### Stored vs Derived State

``` text
Stored state
├── width
└── height

Derived state
└── area
```

### Engineering Principle

> If a value can reliably be derived from existing authoritative state,
> you often don't need to store it separately.

This reduces duplicated state and prevents stale or inconsistent values.

------------------------------------------------------------------------

## Property vs Method

A useful design heuristic:

Use a **method** for an action:

``` python
account.withdraw(5000)
portfolio.add_holding(stock)
```

Use a **property** for something that conceptually behaves like a
characteristic/value:

``` python
account.balance
stock.investment_value
rectangle.area
```

This is a design heuristic, not an absolute rule.

------------------------------------------------------------------------

# Chapter 37 --- Summary

The chapter moved from basic object state to controlled object design:

``` text
Instance variables
        ↓
Class variables
        ↓
Attribute lookup
        ↓
Shadowing
        ↓
Shared state
        ↓
Mutable class variable risks
        ↓
Encapsulation
        ↓
Public / _internal / __name-mangled
        ↓
@property
        ↓
@property.setter
        ↓
Computed properties
```

### Core engineering lessons

-   Know who owns a piece of state.
-   Be careful with shared mutable state.
-   Keep responsibility for valid state with the object that owns it.
-   Use properties when an attribute-like interface needs controlled
    logic.
-   Avoid storing derived state unnecessarily.
