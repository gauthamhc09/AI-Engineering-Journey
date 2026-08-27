# Chapter 38 --- Inheritance

## 38.1 What Is Inheritance?

Inheritance allows one class to derive from another.

Terminology:

``` text
Parent / Base / Superclass
        ↓
Child / Derived / Subclass
```

Example:

``` python
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass
```

Now:

``` python
car = Car()
car.start()
```

works because `Car` inherits `start()` from `Vehicle`.

### Core relationship

Inheritance represents an **IS-A** relationship.

``` text
Car IS A Vehicle
Dog IS AN Animal
Developer IS AN Employee
```

Inheritance should represent a meaningful subtype relationship, not
merely convenient code reuse.

------------------------------------------------------------------------

## 38.2 Inherited Methods and Attribute Lookup

Inheritance extends the attribute/method lookup model:

``` text
instance
   ↓
class
   ↓
parent class
   ↓
parent's parent
   ↓
...
```

Example:

``` python
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass
```

``` python
dog.eat()
```

finds `eat()` in `Animal`.

### Important `self` concept

If:

``` python
dog.eat()
```

calls an inherited method, `self` still refers to the actual `dog`
object.

The method is defined in the parent, but operates on the child object
that called it.

------------------------------------------------------------------------

## 38.3 Adding Behavior to a Child

A child can add specialized behavior.

``` python
class Employee:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Employee: {self.name}")


class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing code")
```

A `Developer` can use:

``` python
developer.introduce()
developer.write_code()
```

Conceptually:

``` text
Developer
├── write_code()      ← own
└── Employee
    └── introduce()   ← inherited
```

Inheritance provides common functionality while allowing specialization.

------------------------------------------------------------------------

## 38.4 Method Overriding

A child can provide its own implementation of a parent method.

``` python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")
```

Now:

``` python
dog.speak()
```

uses `Dog.speak()` because Python finds the child implementation first.

This is **method overriding**.

If a child does not override a method, the inherited parent
implementation is used.

------------------------------------------------------------------------

## 38.5 `super()`

`super()` lets a child access the next implementation in the inheritance
hierarchy.

``` python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
```

Output:

``` text
Animal sound
Woof
```

### Accurate mental model

A beginner approximation:

``` text
super()
→ parent behavior
```

More accurately:

``` text
super()
→ continue method lookup according to the MRO
```

This distinction becomes important with multiple inheritance.

------------------------------------------------------------------------

## 38.6 `super()` with `__init__`

When a child defines its own constructor, it can reuse the parent's
initialization:

``` python
class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
```

Creating:

``` python
developer = Developer("Gautham", "Python")
```

produces:

``` text
developer
├── name = "Gautham"       ← Employee initialized
└── language = "Python"    ← Developer initialized
```

### Why `super().__init__()` matters

When the child defines its own `__init__`, the parent initialization
logic is not automatically included in that custom constructor.

Therefore:

``` python
super().__init__(name)
```

reuses the parent constructor.

------------------------------------------------------------------------

## 38.7 Multiple Levels of Inheritance

Inheritance can have multiple levels:

``` text
Vehicle
   ↓
Car
   ↓
ElectricCar
```

Example:

``` python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
```

Creating:

``` python
car = ElectricCar("Tesla", "Model 3", 75)
```

creates the constructor chain:

``` text
ElectricCar.__init__
        ↓
Car.__init__
        ↓
Vehicle.__init__
```

Final state:

``` text
car
├── brand = "Tesla"
├── model = "Model 3"
└── battery_capacity = 75
```

### Engineering Principle

> Each class should initialize the state that it owns, while `super()`
> allows it to reuse the parent's initialization logic.

------------------------------------------------------------------------

# 38.8 Multiple Inheritance and MRO

Python supports multiple inheritance:

``` python
class A:
    ...


class B:
    ...


class C(A, B):
    ...
```

`C` inherits from both `A` and `B`.

------------------------------------------------------------------------

## Why MRO Exists

Suppose:

``` python
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass
```

Both parents have `show()`.

Python needs a deterministic lookup order.

This is the **Method Resolution Order (MRO)**.

For:

``` python
class C(A, B):
    pass
```

the lookup order is:

``` text
C
↓
A
↓
B
↓
object
```

Therefore:

``` python
C().show()
```

uses `A.show()`.

If:

``` python
class C(B, A):
    pass
```

the order becomes:

``` text
C
↓
B
↓
A
↓
object
```

and `B.show()` is found first.

------------------------------------------------------------------------

## Inspecting the MRO

Python provides:

``` python
C.__mro__
```

and:

``` python
C.mro()
```

The chain eventually reaches:

``` python
object
```

because normal Python classes ultimately derive from `object`.

------------------------------------------------------------------------

## `super()` and MRO

The technically important point:

> `super()` does not simply mean "call my direct parent."

It means:

> **Continue method lookup according to the MRO.**

Example:

``` python
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    def show(self):
        super().show()
        print("C")
```

MRO:

``` text
C → A → B → object
```

Inside `C.show()`:

``` python
super().show()
```

continues after `C` in the MRO and finds `A.show()`.

Output:

``` text
A
C
```

------------------------------------------------------------------------

## MRO Chain Example

``` python
class A:
    def process(self):
        print("A")


class B(A):
    def process(self):
        print("B")
        super().process()


class C(B):
    def process(self):
        print("C")
        super().process()
```

Calling:

``` python
obj = C()
obj.process()
```

produces:

``` text
C
B
A
```

Chain:

``` text
C.process()
    ↓
super()
    ↓
B.process()
    ↓
super()
    ↓
A.process()
```

This follows the inheritance hierarchy/MRO.

------------------------------------------------------------------------

# Inheritance vs Composition

Inheritance represents:

``` text
IS-A
```

Examples:

``` text
Car IS A Vehicle
Developer IS AN Employee
Dog IS AN Animal
```

Composition represents:

``` text
HAS-A
```

Example:

``` text
Car
├── Engine
├── GPS
└── AudioSystem
```

A car has an engine; it is not an engine.

### Engineering Principle

> Use inheritance when there is a meaningful subtype relationship. Don't
> use inheritance merely because one class happens to need some code
> from another class.

Composition is often better for HAS-A relationships.

------------------------------------------------------------------------

# Chapter 38 --- Summary

The chapter progressed from basic inheritance to MRO:

``` text
Parent class
      ↓
Inheritance
      ↓
Child class
      ↓
Inherited behavior
      ↓
Method overriding
      ↓
super()
      ↓
Multiple levels
      ↓
Multiple inheritance
      ↓
MRO
```

### Core engineering lessons

-   Inheritance models an IS-A relationship.
-   Child classes can reuse and specialize parent behavior.
-   Inherited methods receive the actual child object as `self`.
-   Method overriding lets a child replace inherited behavior.
-   `super()` lets child classes reuse the next implementation in the
    MRO.
-   `super().__init__()` is important when extending parent
    initialization.
-   MRO determines method lookup order in multiple inheritance.
-   `super()` should be understood in terms of MRO, not simply "parent."
-   Use inheritance carefully; composition is often preferable for HAS-A
    relationships.
