# Chapter 39 — Polymorphism

## 39.1 What is Polymorphism?

**Polymorphism** means **“many forms.”**

In Python, polymorphism means that the **same operation or method/interface can behave differently depending on the object using it**.

```python
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
```

Output:

```text
Woof
Meow
```

Both objects use:

```python
.speak()
```

but the behavior is different.

### Core idea

```text
Same interface
      ↓
Different objects
      ↓
Different behavior
```

---

## 39.2 Why Polymorphism Is Useful

Instead of writing type-specific logic:

```python
if animal == "dog":
    ...
elif animal == "cat":
    ...
```

we can write:

```python
for animal in animals:
    animal.speak()
```

The code works with different object types through a common interface.

This makes code:

- Cleaner
- Easier to maintain
- Easier to extend
- Less tightly coupled

---

## 39.3 Polymorphism Through Method Overriding

Polymorphism commonly appears with inheritance and method overriding.

```python
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()
```

Output:

```text
Woof
Meow
Animal speaks
```

The same call:

```python
animal.speak()
```

produces different behavior.

This is **runtime polymorphism**.

---

## 39.4 Polymorphism Does Not Require Inheritance

Python supports polymorphism even when classes are unrelated.

```python
class Dog:
    def speak(self):
        print("Woof")


class Robot:
    def speak(self):
        print("Beep")


class Person:
    def speak(self):
        print("Hello")


objects = [Dog(), Robot(), Person()]

for obj in objects:
    obj.speak()
```

Python doesn't require these classes to have a common parent.

It only matters that they provide the required behavior.

---

## 39.5 Duck Typing

Python follows the philosophy:

> “If it walks like a duck and quacks like a duck, treat it like a duck.”

**Duck typing means Python focuses on what an object can do rather than what class/type it belongs to.**

```python
class Duck:
    def swim(self):
        print("Duck swimming")


class Person:
    def swim(self):
        print("Person swimming")


def make_it_swim(obj):
    obj.swim()


make_it_swim(Duck())
make_it_swim(Person())
```

The function doesn't care about the object's class.

It only cares that the object provides:

```python
.swim()
```

### Key idea

> **Capability matters more than identity.**

---

## 39.6 Duck Typing vs Explicit Type Checking

Traditional type checking might look like:

```python
if isinstance(obj, Duck):
    obj.swim()
```

Pythonic duck typing often looks like:

```python
obj.swim()
```

Instead of asking:

> “Are you a Duck?”

we ask:

> “Can you swim?”

This reduces unnecessary coupling to specific classes.

---

## 39.7 Built-in Polymorphism

Python's built-in functions and operators also demonstrate polymorphism.

### `len()`

```python
print(len("Python"))
print(len([10, 20, 30]))
print(len({"a": 1, "b": 2}))
```

Output:

```text
6
3
2
```

The same function works with different types.

### `+`

```python
print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])
```

Output:

```text
30
Hello World
[1, 2, 3, 4]
```

The same operator behaves differently depending on the objects.

---

## 39.8 Polymorphism Through Functions

```python
def process_payment(payment):
    payment.pay()
```

Different objects can be passed:

```python
process_payment(CreditCardPayment())
process_payment(UPIPayment())
process_payment(PayPalPayment())
```

The function doesn't need to know the concrete class.

This is an example of **loose coupling**.

---

## 39.9 Real-World Example — Payment Systems

```python
class Payment:
    def pay(self):
        print("Processing payment")


class CreditCardPayment(Payment):
    def pay(self):
        print("Processing credit card payment")


class UPIPayment(Payment):
    def pay(self):
        print("Processing UPI payment")


class PayPalPayment(Payment):
    def pay(self):
        print("Processing PayPal payment")


payments = [
    CreditCardPayment(),
    UPIPayment(),
    PayPalPayment()
]

for payment in payments:
    payment.pay()
```

We don't need:

```python
if isinstance(payment, CreditCardPayment):
    ...
elif isinstance(payment, UPIPayment):
    ...
elif isinstance(payment, PayPalPayment):
    ...
```

Instead:

```python
payment.pay()
```

The correct implementation is selected based on the object.

---

## 39.10 LLM Engineering Example

Polymorphism becomes especially useful when working with interchangeable LLM providers.

```python
class OpenAIModel:
    def generate(self, prompt):
        print("Generating using OpenAI")


class AnthropicModel:
    def generate(self, prompt):
        print("Generating using Anthropic")


class GeminiModel:
    def generate(self, prompt):
        print("Generating using Gemini")


def generate_response(model, prompt):
    model.generate(prompt)
```

Now:

```python
generate_response(OpenAIModel(), "Explain RAG")
generate_response(AnthropicModel(), "Explain RAG")
generate_response(GeminiModel(), "Explain RAG")
```

The application code doesn't need to know which provider is being used.

The common interface is:

```python
.generate()
```

This pattern is important in LLM engineering for components such as:

- LLM providers
- Embedding providers
- Vector stores
- Retrievers
- Document loaders
- Notification providers

---

## 39.11 Polymorphism + Inheritance + Overriding

These concepts are closely connected.

```python
class Model:
    def generate(self):
        print("Generating response")


class OpenAIModel(Model):
    def generate(self):
        print("Generating using OpenAI")


class GeminiModel(Model):
    def generate(self):
        print("Generating using Gemini")


models = [
    OpenAIModel(),
    GeminiModel()
]

for model in models:
    model.generate()
```

Here we have:

- Inheritance
- Method overriding
- Runtime polymorphism

---

## 39.12 Polymorphism + `super()`

Polymorphism can also work together with `super()`.

```python
class Model:
    def generate(self):
        print("Base model generating")


class OpenAIModel(Model):
    def generate(self):
        super().generate()
        print("OpenAI processing")


class GeminiModel(Model):
    def generate(self):
        super().generate()
        print("Gemini processing")


models = [
    OpenAIModel(),
    GeminiModel()
]

for model in models:
    model.generate()
```

Output:

```text
Base model generating
OpenAI processing
Base model generating
Gemini processing
```

This connects directly to the concepts learned earlier:

```text
Inheritance
    ↓
Method Overriding
    ↓
super()
    ↓
Polymorphism
```

---

## 39.13 Method Overriding vs Polymorphism

Don't confuse the two.

### Method overriding

A child class provides its own implementation of an inherited method.

```python
class Dog(Animal):
    def speak(self):
        print("Woof")
```

### Polymorphism

Different objects can be used through the same interface.

```python
for animal in animals:
    animal.speak()
```

So:

> **Method overriding is a mechanism that can enable polymorphic behavior.**

Polymorphism is the broader concept.

---

## 39.14 Real-World Mental Model

Think about a remote control.

You press:

```text
POWER
```

The interface is the same.

But:

```text
TV         → turns on TV
AC         → turns on AC
Projector  → turns on projector
```

The common interface is:

```text
power()
```

Different implementations provide different behavior.

That is polymorphism.

---

## 39.15 Three Key Ideas

### 1. Same interface, different behavior

```python
obj.process()
```

can behave differently depending on `obj`.

### 2. Python uses duck typing

```python
obj.process()
```

is often enough.

Python does not necessarily require:

```python
isinstance(obj, SomeClass)
```

### 3. Polymorphism reduces coupling

Instead of:

```python
if type == ...
```

you can often use:

```python
obj.method()
```

This makes applications easier to extend.

---

# Chapter 39 — Final Summary

**Polymorphism = one interface, multiple implementations/behaviors.**

Important forms:

```text
Method overriding
        ↓
Runtime polymorphism

Duck typing
        ↓
Polymorphism without inheritance

Built-in polymorphism
        ↓
len(), +, etc.
```

### Most important pattern

```python
for obj in objects:
    obj.method()
```

You don't need to know the exact type of `obj`.

You only need the object to support the required behavior.

### Mental model

```text
Inheritance
     ↓
Method Overriding
     ↓
Different implementations
     ↓
Polymorphism
     ↓
Same interface → different behavior
```

## Chapter 39 Review

1. What is polymorphism?
2. Does polymorphism require inheritance in Python?
3. What is duck typing?
4. Why can polymorphism be better than a large `if/elif` based on object type?
5. Where does polymorphism happen in this code?

```python
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

### Key Interview Sentence

> **Polymorphism allows us to write code that works with different objects through a common interface, without needing to know their concrete type.**
