# Chapter 42 — OOP Mini-Project: AI Model Manager

## Goal

Build a small AI Model Manager demonstrating:

- Classes & Objects
- Instance Variables
- Inheritance
- Method Overriding
- Polymorphism
- Encapsulation
- Abstraction
- `super()`

---

## 1. Abstract Base Class

```python
from abc import ABC, abstractmethod

class LLM(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def generate(self, prompt):
        pass
```

`LLM` defines the common contract for all LLM implementations.

Every concrete LLM must provide `generate(prompt)`.

---

## 2. Concrete Model Classes

```python
class OpenAIModel(LLM):

    def __init__(self, name):
        super().__init__(name)

    def generate(self, prompt):
        return f"OpenAIModel {prompt}"


class GeminiModel(LLM):

    def __init__(self, name):
        super().__init__(name)

    def generate(self, prompt):
        return f"GeminiModel {prompt}"


class AnthropicModel(LLM):

    def __init__(self, name):
        super().__init__(name)

    def generate(self, prompt):
        return f"AnthropicModel {prompt}"
```

Each subclass inherits from `LLM` and overrides `generate()`.

---

## 3. Important: `super().__init__(name)`

Correct:

```python
super().__init__(name)
```

Incorrect:

```python
super().name = name
```

`super().__init__(name)` calls the parent constructor:

```python
def __init__(self, name):
    self.name = name
```

Therefore the child object receives the `name` instance variable.

---

## 4. ModelManager

```python
class ModelManager:

    def __init__(self):
        self.models = []

    def add_model(self, model):
        self.models.append(model)

    def list_models(self):
        return [model.name for model in self.models]

    def get_model(self, name):
        for model in self.models:
            if model.name == name:
                return model

        raise ValueError(f"{name} not found")

    def generate(self, name, prompt):
        model = self.get_model(name)
        return model.generate(prompt)
```

---

## 5. Why `self.models = []`?

Use:

```python
self.models = []
```

instead of:

```python
models = []
```

inside the class body.

`models = []` would be a class variable shared by all `ModelManager` instances.

`self.models = []` creates a separate list for each manager object.

---

## 6. Adding Models

```python
manager = ModelManager()

manager.add_model(OpenAIModel("openai"))
manager.add_model(GeminiModel("gemini"))
manager.add_model(AnthropicModel("claude"))
```

The manager now contains three model objects.

---

## 7. Listing Models

```python
print(manager.list_models())
```

Output:

```text
['openai', 'gemini', 'claude']
```

We use:

```python
model.name
```

instead of:

```python
model.__class__.__name__
```

because the model has an explicit identifier.

---

## 8. Getting a Model

```python
model = manager.get_model("gemini")
```

Internally:

```python
for model in self.models:
    if model.name == name:
        return model
```

If no model is found:

```python
raise ValueError(f"{name} not found")
```

---

## 9. Generating a Response

```python
response = manager.generate(
    "gemini",
    "Explain RAG"
)

print(response)
```

Output:

```text
GeminiModel Explain RAG
```

Flow:

```text
manager.generate()
        |
        v
get_model("gemini")
        |
        v
GeminiModel object
        |
        v
model.generate(prompt)
        |
        v
GeminiModel.generate()
        |
        v
response
```

---

## 10. Where Polymorphism Happens

The important line is:

```python
model.generate(prompt)
```

`model` can refer to:

```text
OpenAIModel
GeminiModel
AnthropicModel
```

The same method call produces different behavior depending on the actual object.

That is polymorphism.

---

## 11. Abstraction + Polymorphism

### Abstraction

Defines the common interface:

```python
class LLM(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass
```

Meaning:

> Every LLM must provide `generate()`.

### Polymorphism

Allows different implementations:

```text
OpenAIModel     -> generate()
GeminiModel     -> generate()
AnthropicModel  -> generate()
```

The application can call:

```python
model.generate(prompt)
```

without knowing the concrete implementation.

---

## 12. Encapsulation

`ModelManager` owns its internal model collection:

```python
self.models = []
```

and exposes operations through:

```python
add_model()
list_models()
get_model()
generate()
```

The rest of the application does not need to manage the collection directly.

---

## 13. Complete Project

```python
from abc import ABC, abstractmethod


class LLM(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def generate(self, prompt):
        pass


class OpenAIModel(LLM):

    def __init__(self, name):
        super().__init__(name)

    def generate(self, prompt):
        return f"OpenAIModel {prompt}"


class GeminiModel(LLM):

    def __init__(self, name):
        super().__init__(name)

    def generate(self, prompt):
        return f"GeminiModel {prompt}"


class AnthropicModel(LLM):

    def __init__(self, name):
        super().__init__(name)

    def generate(self, prompt):
        return f"AnthropicModel {prompt}"


class ModelManager:

    def __init__(self):
        self.models = []

    def add_model(self, model):
        self.models.append(model)

    def list_models(self):
        return [model.name for model in self.models]

    def get_model(self, name):
        for model in self.models:
            if model.name == name:
                return model

        raise ValueError(f"{name} not found")

    def generate(self, name, prompt):
        model = self.get_model(name)
        return model.generate(prompt)


manager = ModelManager()

manager.add_model(OpenAIModel("openai"))
manager.add_model(GeminiModel("gemini"))
manager.add_model(AnthropicModel("claude"))

print(manager.list_models())

response = manager.generate(
    "gemini",
    "Explain RAG"
)

print(response)
```

---

## 14. What the Project Demonstrated

| OOP Concept | Where it appears |
|---|---|
| Class | `LLM`, `GeminiModel`, `ModelManager` |
| Object | `GeminiModel("gemini")` |
| Instance variable | `self.name`, `self.models` |
| Inheritance | `GeminiModel(LLM)` |
| Method overriding | Each model implements `generate()` |
| `super()` | `super().__init__(name)` |
| Abstraction | `LLM(ABC)` + `@abstractmethod` |
| Polymorphism | `model.generate(prompt)` |
| Encapsulation | `ModelManager` controls its model collection |

---

## 15. Key Lessons

### Abstraction

> Hide implementation details and expose the essential interface.

### Inheritance

> A subclass can inherit common structure and behavior from a parent class.

### Polymorphism

> The same interface can produce different behavior depending on the object.

### Encapsulation

> Keep an object's internal state/implementation controlled behind its methods.

### `super()`

> Used to access and call parent-class functionality, especially the parent constructor.

---

## Chapter 42 Summary

The mini-project combined the OOP concepts into one small system.

We created an abstract `LLM` class with a required `generate()` method. `OpenAIModel`, `GeminiModel`, and `AnthropicModel` inherited from it and provided their own implementations.

`ModelManager` stores these objects, finds a model by its identifier, and delegates generation to the selected model.

The key engineering idea is:

> **The application works with a common interface instead of depending on each model's implementation details.**

This same style of design appears later in backend systems, RAG pipelines, AI applications, and LLM provider integrations.

---

# Module 06 — OOP Complete

- Chapter 36 — OOP Foundations
- Chapter 37 — Classes & Objects
- Chapter 38 — Inheritance
- Chapter 39 — Polymorphism
- Chapter 40 — Encapsulation
- Chapter 41 — Abstraction
- Chapter 42 — Mini-Project

## Next Module

**Module 07 — Exception Handling**

- Chapter 43 — Try-Except
- Chapter 44 — Else and Finally
- Chapter 45 — Raise
- Chapter 46 — Custom Exceptions
