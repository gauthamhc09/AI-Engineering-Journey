# Chapter 35 --- Classes and Objects

## 35.1 What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming approach where we
model a program using **objects** that contain:

-   **State** → data stored by the object
-   **Behavior** → actions the object can perform

### Example

A bank account can have:

**State** - account holder - account number - balance

**Behavior** - deposit money - withdraw money - check balance

The key idea is:

> **Object = State + Behavior**

------------------------------------------------------------------------

## 35.2 Why Do We Need Objects?

For small programs, dictionaries and functions can be enough:

``` python
account = {
    "holder": "Gautham",
    "balance": 50000
}

def deposit(account, amount):
    account["balance"] += amount
```

As software grows, managing large amounts of related data and the
functions that operate on that data becomes harder.

OOP provides a way to organize related:

``` text
Data + Behavior
```

inside a meaningful object.

This makes larger programs easier to organize, maintain, and extend.

------------------------------------------------------------------------

## 35.3 What is a Class?

A **class** is a blueprint or type used to create objects.

Example:

``` python
class Dog:
    pass
```

`Dog` is a class.

Think of it as:

``` text
Dog
 ↓
Blueprint
```

A class describes the structure and behavior that its objects can have.

------------------------------------------------------------------------

## 35.4 What is an Object?

An **object** is a specific instance created from a class.

Example:

``` python
class Dog:
    pass

dog1 = Dog()
dog2 = Dog()
```

Here:

-   `Dog` → class
-   `dog1` → object
-   `dog2` → object

Conceptually:

``` text
             Dog
            CLASS
              |
       +------+------+
       |             |
      dog1          dog2
     OBJECT        OBJECT
```

### Important

These are two separate objects:

``` python
dog1 = Dog()
dog2 = Dog()
```

Even though they were created from the same class.

------------------------------------------------------------------------

## 35.5 Class vs Object

  Concept          Meaning
  ---------------- -------------------------------------
  Class            Blueprint/type for creating objects
  Object           Specific instance of a class
  Class example    `Car`
  Object example   `car1 = Car()`

### Mental Model

``` text
Class
  ↓
creates
  ↓
Objects
```

For example:

``` python
class Car:
    pass

car1 = Car()
car2 = Car()
```

`Car` is the blueprint.

`car1` and `car2` are actual objects.

------------------------------------------------------------------------

## 35.6 State

**State** is the data currently stored in an object.

For a car:

``` text
brand = "Toyota"
speed = 80
```

For a stock holding:

``` text
symbol = "RELIANCE"
quantity = 10
average_buy_price = 2500
current_price = 2800
```

State describes the object's current condition.

------------------------------------------------------------------------

## 35.7 Behavior

**Behavior** is what an object can do.

Behavior is normally represented by methods.

For a car:

``` text
accelerate()
brake()
stop()
```

For a stock holding:

``` text
calculate_pnl()
calculate_current_value()
```

A useful mental model is:

``` text
State
  ↓
Behavior operates on state
  ↓
State may change
```

Example:

``` text
Initial state:
balance = 50000

deposit(5000)

New state:
balance = 55000
```

------------------------------------------------------------------------

## 35.8 Attributes

An **attribute** is data associated with an object or class.

### Class attribute

``` python
class Car:
    wheels = 4
```

`wheels` is defined on the class.

Objects can access it:

``` python
car1 = Car()
car2 = Car()

print(car1.wheels)
print(car2.wheels)
```

Output:

``` text
4
4
```

### Instance attributes

Different objects can have their own state.

``` python
class Car:
    wheels = 4

car1 = Car()
car2 = Car()

car1.brand = "Toyota"
car1.speed = 80

car2.brand = "BMW"
car2.speed = 120
```

Now:

``` text
car1
├── brand = "Toyota"
└── speed = 80

car2
├── brand = "BMW"
└── speed = 120
```

The objects have independent state.

> Class attributes and instance attributes will be studied in more depth
> in Chapter 37.

------------------------------------------------------------------------

## 35.9 Creating Objects

The basic syntax is:

``` python
object_name = ClassName()
```

Example:

``` python
class Car:
    pass

car1 = Car()
car2 = Car()
```

The `()` are important.

### Correct

``` python
car1 = Car()
```

Creates an object.

### Different meaning

``` python
car1 = Car
```

This makes `car1` refer to the class itself rather than creating an
instance.

This distinction is fundamental in Python.

------------------------------------------------------------------------

## 35.10 Adding Attributes to Objects

Python allows attributes to be added directly to an object:

``` python
object.attribute = value
```

Example:

``` python
class Car:
    pass

car1 = Car()

car1.brand = "Toyota"
car1.speed = 80
```

Now:

``` python
print(car1.brand)
print(car1.speed)
```

Output:

``` text
Toyota
80
```

Another object can have different values:

``` python
car2 = Car()

car2.brand = "BMW"
car2.speed = 120
```

So:

``` text
car1 → Toyota, 80
car2 → BMW, 120
```

This demonstrates that each object can maintain its own state.

------------------------------------------------------------------------

## 35.11 Objects, State, and Behavior

A useful OOP model:

``` text
                OBJECT
                   |
          +--------+--------+
          |                 |
        STATE            BEHAVIOR
          |                 |
      Attributes          Methods
          |                 |
   brand, speed       accelerate()
                      brake()
```

This is one of the most important mental models for OOP.

------------------------------------------------------------------------

## 35.12 Real-World Example

Consider a `StockHolding`.

``` text
StockHolding
│
├── symbol
├── quantity
├── average_buy_price
├── current_price
│
├── calculate_invested_value()
├── calculate_current_value()
└── calculate_pnl()
```

### State

``` text
symbol
quantity
average_buy_price
current_price
```

### Behavior

``` text
calculate_invested_value()
calculate_current_value()
calculate_pnl()
```

The behavior uses the object's state.

This is useful for applications such as:

-   portfolio management
-   banking systems
-   APIs
-   backend services
-   database models
-   AI/ML systems

------------------------------------------------------------------------

# Common Mistakes

## 1. Confusing a class with an object

Incorrect mental model:

``` python
Car == car1
```

They are not the same.

``` text
Car  → class
car1 → object
```

------------------------------------------------------------------------

## 2. Forgetting `()`

``` python
car1 = Car
```

does not create an object.

Use:

``` python
car1 = Car()
```

------------------------------------------------------------------------

## 3. Thinking objects from the same class are the same object

``` python
car1 = Car()
car2 = Car()
```

creates two separate objects.

They share the same class but can have different state.

------------------------------------------------------------------------

## 4. Thinking state and behavior are the same

State is data:

``` text
speed = 80
```

Behavior is an action:

``` text
accelerate()
```

------------------------------------------------------------------------

# Key Takeaways

1.  **OOP organizes programs around objects.**
2.  An **object combines state and behavior**.
3.  **State** is the data currently stored by an object.
4.  **Behavior** represents actions the object can perform.
5.  A **class is a blueprint/type** for creating objects.
6.  An **object is an instance of a class**.
7.  One class can create many separate objects.
8.  Each object can maintain its own state.
9.  Attributes represent data associated with a class or object.
10. Methods represent behavior.
11. `ClassName()` creates an object.
12. `ClassName` without `()` refers to the class itself.

------------------------------------------------------------------------

# Practical Engineering Connection

OOP becomes useful when software contains many related entities with
both data and operations.

Examples:

``` text
Backend
├── User
├── Account
├── Order
├── Product
└── DatabaseConnection
```

AI/LLM systems can also contain objects representing:

``` text
Document
Embedding
Model
Tokenizer
Retriever
VectorStore
Agent
Tool
```

You will encounter these patterns later in backend and AI engineering.

For now, focus on understanding the fundamental relationship:

``` text
Class
  ↓
Objects
  ↓
State + Behavior
```

------------------------------------------------------------------------

# Chapter 35 Completion Checklist

-   [x] Understand what OOP is
-   [x] Understand why OOP exists
-   [x] Understand what an object is
-   [x] Understand state vs behavior
-   [x] Understand what a class is
-   [x] Understand class vs object
-   [x] Understand how to create objects
-   [x] Understand that objects can have independent state
-   [x] Understand basic attributes
-   [x] Understand the difference between `Class` and `Class()`
-   [ ] Create and understand methods
-   [ ] Understand `self`
-   [ ] Demonstrate behavior through methods
-   [ ] Complete Chapter 35 practical challenge
-   [ ] Demonstrate full Chapter 35 understanding

> **Note:** The unchecked items will be completed before Chapter 35 is
> considered fully mastered.
