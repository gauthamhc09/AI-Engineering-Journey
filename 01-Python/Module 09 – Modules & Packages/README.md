# Module 09 — Modules & Packages

## Overview

Module 09 covers how Python projects are organized and how their dependencies are managed.

### Chapters

| Chapter | Topic |
|---|---|
| 51 | Modules |
| 52 | Packages |
| 53 | Virtual Environments |
| 54 | pip |

The progression is:

```text
Modules
   ↓
Packages
   ↓
Virtual Environments
   ↓
pip + requirements.txt
```

---

# Chapter 51 — Modules

## 51.1 What is a Module?

A **module is a Python file (`.py`) containing Python code**.

Example:

```text
calculator.py
```

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

Another Python file can import and reuse these functions.

```text
project/
├── calculator.py
└── main.py
```

```python
# main.py

import calculator

print(calculator.add(10, 5))
```

Output:

```text
15
```

### Mental model

```text
Module = one Python .py file
```

---

## 51.2 Why Modules?

Modules allow us to split a large application into smaller, logical pieces.

Instead of:

```text
main.py
└── 5000 lines of code
```

we can have:

```text
project/
├── main.py
├── database.py
├── authentication.py
├── portfolio.py
├── market_data.py
└── utils.py
```

Each module can have a specific responsibility.

This is related to **separation of concerns**.

---

## 51.3 `import`

Basic syntax:

```python
import module_name
```

Example:

```python
import math

print(math.sqrt(25))
```

The general pattern is:

```text
module.function()
```

Example:

```python
math.sqrt(25)
```

means:

> Call `sqrt()` from the `math` module.

---

## 51.4 `from ... import ...`

You can import a specific object:

```python
from math import sqrt

print(sqrt(25))
```

Multiple objects:

```python
from math import sqrt, factorial

print(sqrt(25))
print(factorial(5))
```

### Comparison

```python
import math

math.sqrt(25)
```

vs.

```python
from math import sqrt

sqrt(25)
```

Using `import math` makes the source of the function explicit.

---

## 51.5 Import Aliases

Use `as` to create an alias.

```python
import math as m

print(m.sqrt(25))
```

Common examples in AI/data work:

```python
import pandas as pd
import numpy as np
```

Then:

```python
pd.DataFrame(...)
np.array(...)
```

---

## 51.6 Aliasing Individual Imports

```python
from math import sqrt as square_root

print(square_root(25))
```

---

## 51.7 Avoid `from module import *`

Python allows:

```python
from math import *
```

but this is generally discouraged in professional code.

Why?

Because it makes it unclear where names came from.

Prefer:

```python
import math

math.sqrt(25)
```

or explicit imports:

```python
from math import sqrt
```

---

## 51.8 What Can a Module Contain?

A module can contain:

### Variables

```python
PI = 3.14159
```

### Functions

```python
def area(radius):
    return PI * radius ** 2
```

### Classes

```python
class Circle:
    pass
```

### Constants

```python
MAX_RETRIES = 3
```

### Executable code

```python
print("Module loaded")
```

---

## 51.9 `if __name__ == "__main__":`

This is one of the most important module concepts.

Example:

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
```

### Running directly

```bash
python calculator.py
```

Python sets:

```python
__name__ = "__main__"
```

Therefore the block executes.

### Importing

```python
import calculator
```

Python sets:

```python
__name__ = "calculator"
```

Therefore:

```python
__name__ == "__main__"
```

is `False`.

### Mental model

```text
Run file directly
    ↓
__name__ == "__main__"
    ↓
execute main/test code


Import file
    ↓
__name__ == module name
    ↓
don't execute the main block
```

This allows a file to be both:

- reusable as a module
- executable as a standalone program

---

## 51.10 Standard Library Modules

Python includes many modules without requiring installation.

Examples:

```python
import math
import random
import os
import sys
import json
import datetime
import pathlib
import logging
```

These belong to the **Python Standard Library**.

---

## 51.11 Three Sources of Python Modules

### 1. Your own modules

```text
portfolio.py
database.py
utils.py
```

### 2. Python Standard Library

```python
import os
import json
import logging
```

### 3. Third-party packages

```python
import pandas
import numpy
import fastapi
import requests
```

Third-party packages generally need to be installed separately.

---

# Chapter 52 — Packages

## 52.1 What is a Package?

A package is a directory used to organize related Python modules.

Example:

```text
project/
├── main.py
└── calculator/
    ├── addition.py
    └── multiplication.py
```

Here:

```text
calculator/
```

is the package and:

```text
addition.py
multiplication.py
```

are modules.

### Mental model

```text
Module  → .py file
Package → directory that organizes modules
```

---

## 52.2 Why Packages?

As applications grow, keeping every `.py` file in one directory becomes difficult.

Instead of:

```text
project/
├── users.py
├── authentication.py
├── portfolio.py
├── market_data.py
├── parser.py
├── database.py
└── ...
```

we can organize them:

```text
project/
├── main.py
├── authentication/
│   ├── login.py
│   └── permissions.py
├── portfolio/
│   ├── holdings.py
│   └── calculations.py
└── database/
    ├── connection.py
    └── queries.py
```

This gives the project a hierarchy.

---

## 52.3 Importing From a Package

Suppose:

```text
calculator/
├── addition.py
└── multiplication.py
```

`addition.py`:

```python
def add(a, b):
    return a + b
```

Then:

```python
from calculator.addition import add

print(add(10, 20))
```

Breakdown:

```text
calculator
    ↓
package

addition
    ↓
module

add
    ↓
function
```

---

## 52.4 Different Import Styles

You can write:

```python
import calculator.addition

print(calculator.addition.add(10, 20))
```

or:

```python
from calculator import addition

print(addition.add(10, 20))
```

or:

```python
from calculator.addition import add

print(add(10, 20))
```

---

## 52.5 `__init__.py`

A package often contains:

```text
calculator/
├── __init__.py
├── addition.py
└── multiplication.py
```

Historically, `__init__.py` was required for Python to recognize a directory as a regular package.

Since Python 3.3, **namespace packages** can exist without `__init__.py`.

However, `__init__.py` is still extremely common and useful in real projects.

It can be empty:

```python
```

or contain package-level code/imports.

---

## 52.6 Using `__init__.py` for Exports

Suppose:

```text
calculator/
├── __init__.py
├── addition.py
└── multiplication.py
```

`__init__.py`:

```python
from .addition import add
from .multiplication import multiply
```

Then:

```python
from calculator import add, multiply

print(add(10, 20))
print(multiply(5, 4))
```

The dot means:

```text
current package
```

---

## 52.7 Relative Imports

Inside a package:

```python
from .addition import add
```

The `.` means:

> Import from the current package.

Example:

```text
services/
├── __init__.py
├── user.py
└── payment.py
```

Inside `payment.py`:

```python
from .user import User
```

---

## 52.8 Absolute Imports

Example:

```python
from calculator.addition import add
```

This refers to the package through its project/package path.

---

## 52.9 Nested Packages

Packages can contain packages.

Example:

```text
app/
├── main.py
├── api/
│   ├── __init__.py
│   └── routes/
│       ├── __init__.py
│       ├── users.py
│       └── portfolio.py
└── services/
    ├── __init__.py
    ├── portfolio.py
    └── market_data.py
```

This is common in production applications.

---

## 52.10 Package Hierarchy

Consider:

```text
services/
└── portfolio/
    ├── __init__.py
    └── calculations.py
```

An import might be:

```python
from services.portfolio.calculations import calculate_pnl
```

Breakdown:

```text
services
    ↓
package

portfolio
    ↓
subpackage

calculations
    ↓
module

calculate_pnl
    ↓
function
```

---

## 52.11 Module vs Package vs Library

### Module

Usually one `.py` file:

```text
calculator.py
```

### Package

A collection/namespace of related modules:

```text
calculator/
├── addition.py
└── multiplication.py
```

### Library

A broader term for reusable software functionality.

A library may contain multiple packages and modules.

---

## 52.12 Package Structure in AI Engineering

A RAG application might eventually look like:

```text
rag_app/
├── main.py
├── ingestion/
│   ├── loaders.py
│   ├── chunking.py
│   └── embedding.py
├── retrieval/
│   ├── retriever.py
│   └── reranker.py
├── generation/
│   ├── llm.py
│   └── prompt.py
├── database/
│   ├── vector_store.py
│   └── models.py
└── utils/
    ├── logging.py
    └── config.py
```

This is the practical importance of modules and packages.

---

# Chapter 53 — Virtual Environments

## 53.1 The Problem

Different projects may require different package versions.

For example:

```text
Project A
    pandas 2.x

Project B
    pandas 1.x
```

If both projects use one global environment, dependency conflicts can occur.

---

## 53.2 Virtual Environment

A **virtual environment** is an isolated Python environment for a project.

Conceptually:

```text
Computer
├── Project A
│   └── .venv/
│       ├── pandas 2.x
│       └── numpy 2.x
│
└── Project B
    └── .venv/
        ├── pandas 1.x
        └── numpy 1.x
```

The projects can use different dependency versions.

---

## 53.3 Creating a Virtual Environment

Python provides the built-in `venv` module.

```bash
python -m venv .venv
```

Breakdown:

```text
python
  ↓
Python interpreter

-m
  ↓
run a Python module

venv
  ↓
virtual environment module

.venv
  ↓
environment directory name
```

`.venv` is a common convention.

---

## 53.4 What Gets Created?

On macOS/Linux:

```text
project/
├── .venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
└── main.py
```

On Windows:

```text
.venv/
├── Include/
├── Lib/
├── Scripts/
└── pyvenv.cfg
```

You normally don't edit these files manually.

---

## 53.5 Activating on macOS/Linux

```bash
source .venv/bin/activate
```

The terminal usually changes to something like:

```text
(.venv) user@computer project %
```

The `(.venv)` indicates the environment is active.

---

## 53.6 What Activation Does

Activation changes which Python and package executables your shell resolves to.

Before:

```text
python
  ↓
default/system Python
```

After activation:

```text
(.venv)

python
  ↓
.venv/bin/python
```

Similarly:

```text
pip
  ↓
.venv/bin/pip
```

Therefore:

```bash
pip install pandas
```

installs into the active environment.

---

## 53.7 Checking Which Python Is Active

Use:

```bash
which python
```

You should see a path containing:

```text
.venv/bin/python
```

Another useful command:

```bash
python -c "import sys; print(sys.executable)"
```

This shows the exact Python executable being used.

---

## 53.8 Installing Packages in a Virtual Environment

After activation:

```bash
pip install requests
```

The package is installed into the current virtual environment.

---

## 53.9 Deactivating

```bash
deactivate
```

The `(.venv)` indicator disappears.

---

## 53.10 Standard Workflow

```bash
mkdir my_project
cd my_project

python -m venv .venv

source .venv/bin/activate

pip install requests

python main.py

deactivate
```

This is the basic Python project lifecycle.

---

## 53.11 `.venv` and Git

You normally do **not** commit `.venv/` to Git.

Add this to `.gitignore`:

```text
.venv/
```

Why?

The environment can contain many files and platform-specific data.

Instead of committing the environment itself, commit a dependency definition such as:

```text
requirements.txt
```

Mental model:

```text
Environment itself
    ❌ commit

Instructions to recreate environment
    ✅ commit
```

---

## 53.12 Virtual Environment vs Virtual Machine

A Python virtual environment:

```text
isolates Python dependencies
```

A virtual machine:

```text
virtualizes an entire operating system
```

They are very different.

---

## 53.13 Virtual Environment vs Docker

A virtual environment mainly isolates:

```text
Python environment + packages
```

Docker can isolate a much broader application environment:

```text
application
dependencies
system libraries
runtime
```

Docker will be covered later.

---

## 53.14 Why Virtual Environments Matter for AI/LLM Work

AI projects often have many dependencies:

```text
FastAPI
Pydantic
PyTorch
Transformers
NumPy
LangChain
Vector database clients
```

Different projects can require different versions.

Therefore:

```text
AI Project A → .venv
RAG Project  → .venv
FastAPI App  → .venv
ML Project   → .venv
```

This prevents dependency conflicts.

---

# Chapter 54 — pip

## 54.1 What is `pip`?

`pip` is Python's package installer.

It can:

- install packages
- uninstall packages
- upgrade packages
- inspect packages
- install specific versions
- install dependencies from a file

Example:

```bash
pip install requests
```

---

## 54.2 PyPI

Many Python packages are distributed through:

**PyPI — Python Package Index**

Conceptually:

```text
PyPI
  ↓
pip
  ↓
your virtual environment
  ↓
installed package
```

---

## 54.3 Installing a Package

```bash
pip install requests
```

Then:

```python
import requests
```

The basic relationship is:

```text
pip
 ↓
install package
 ↓
import package in Python
```

---

## 54.4 Check Installed Packages

```bash
pip list
```

This displays installed packages and their versions.

---

## 54.5 Inspect a Package

```bash
pip show requests
```

This can show:

- package name
- version
- installation location
- dependencies

---

## 54.6 Installing a Specific Version

```bash
pip install requests==2.31.0
```

Syntax:

```text
package==version
```

Exact versions are useful when an application depends on a known version.

---

## 54.7 Version Constraints

Minimum version:

```bash
pip install requests>=2.31.0
```

Less than a version:

```bash
pip install requests<3.0
```

Range:

```bash
pip install requests>=2.31,<3
```

Meaning:

```text
2.31 ≤ version < 3
```

---

## 54.8 Upgrading

```bash
pip install --upgrade requests
```

or:

```bash
pip install -U requests
```

---

## 54.9 Uninstalling

```bash
pip uninstall requests
```

---

## 54.10 `requirements.txt`

A project needs a way to specify its dependencies.

Example:

```text
fastapi==0.115.0
numpy==2.0.0
pandas==2.2.2
requests==2.32.3
```

This file is:

```text
requirements.txt
```

It allows another developer or environment to recreate the dependencies.

---

## 54.11 Creating `requirements.txt`

A common approach:

```bash
pip freeze > requirements.txt
```

`pip freeze` shows installed packages and their versions.

Example:

```bash
pip freeze
```

might output:

```text
certifi==...
charset-normalizer==...
idna==...
requests==...
urllib3==...
```

Then:

```bash
pip freeze > requirements.txt
```

saves the output.

---

## 54.12 Installing From `requirements.txt`

Create/activate a virtual environment and run:

```bash
pip install -r requirements.txt
```

`-r` means:

> Read requirements from this file.

Workflow:

```text
requirements.txt
       ↓
      pip
       ↓
install dependencies
       ↓
new environment
```

---

## 54.13 `pip` and Virtual Environments

The two concepts work together:

```text
.venv
  ↓
isolates environment

pip
  ↓
installs packages into that environment
```

Always be conscious of which environment is active before installing packages.

---

## 54.14 `python -m pip`

You may see:

```bash
pip install requests
```

or:

```bash
python -m pip install requests
```

The second form explicitly uses the `pip` associated with the selected Python interpreter.

This can reduce confusion when multiple Python installations/environments exist.

Useful command:

```bash
python -m pip --version
```

---

## 54.15 Check Where `pip` Comes From

```bash
which pip
```

After activating `.venv`, it should normally point inside:

```text
.venv/bin/pip
```

Another option:

```bash
python -m pip --version
```

---

## 54.16 Installing Multiple Packages

```bash
pip install fastapi uvicorn pydantic
```

Multiple packages can be installed in one command.

---

## 54.17 Dependencies

Installing one package can install other packages it depends on.

Example:

```text
requests
├── urllib3
├── certifi
├── idna
└── charset-normalizer
```

This is called **dependency resolution**.

---

## 54.18 Direct vs Transitive Dependencies

If your application explicitly installs:

```text
requests
```

then `requests` is a:

> **Direct dependency**

Its dependencies such as:

```text
urllib3
certifi
idna
```

are:

> **Transitive dependencies**

Conceptually:

```text
Application
    ↓
requests
(direct)
    ↓
urllib3
certifi
idna
(transitive)
```

---

## 54.19 Why Version Management Matters

An application may depend on a particular API or behavior.

For example:

```text
Application
    ↓
expects library version 2
    ↓
library version 3
    ↓
breaking changes
    ↓
application fails
```

Dependency versions therefore matter in real-world applications.

---

# Practical Workflow

A typical Python project can follow this workflow:

```bash
mkdir my_project
cd my_project

python -m venv .venv

source .venv/bin/activate

python -m pip install fastapi uvicorn

python main.py

python -m pip freeze > requirements.txt

deactivate
```

Project structure:

```text
my_project/
├── .venv/               # do not commit
├── main.py              # source code
├── requirements.txt     # dependencies
└── .gitignore           # ignores .venv
```

Another developer can recreate the environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# Module 09 — Master Mental Model

```text
                    PYTHON PROJECT
                          │
                          ↓
                     MODULES
                          │
                    .py files
                          │
                          ↓
                     PACKAGES
                          │
                organized modules
                          │
                          ↓
                VIRTUAL ENVIRONMENT
                          │
                        .venv
                          │
                          ↓
                         pip
                          │
                install/manage packages
                          │
                          ↓
                  requirements.txt
                          │
                          ↓
              recreate project environment
```

---

# Quick Reference

## Modules

```python
import math
```

```python
from math import sqrt
```

```python
import pandas as pd
```

```python
if __name__ == "__main__":
    ...
```

---

## Packages

```text
calculator/
├── __init__.py
├── addition.py
└── multiplication.py
```

```python
from calculator.addition import add
```

Relative import:

```python
from .addition import add
```

---

## Virtual Environment

Create:

```bash
python -m venv .venv
```

Activate macOS/Linux:

```bash
source .venv/bin/activate
```

Check Python:

```bash
which python
```

or:

```bash
python -c "import sys; print(sys.executable)"
```

Deactivate:

```bash
deactivate
```

---

## pip

Install:

```bash
pip install requests
```

Specific version:

```bash
pip install requests==2.31.0
```

Upgrade:

```bash
pip install -U requests
```

Remove:

```bash
pip uninstall requests
```

List:

```bash
pip list
```

Inspect:

```bash
pip show requests
```

Freeze:

```bash
pip freeze > requirements.txt
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

# Module 09 — Final Summary

The four chapters solve four different problems:

```text
Chapter 51 — Modules
"What if my Python file becomes too large?"
        ↓
Split code into .py files.


Chapter 52 — Packages
"What if I have many related modules?"
        ↓
Organize modules into packages/folders.


Chapter 53 — Virtual Environments
"What if different projects need different dependencies?"
        ↓
Give each project its own isolated Python environment.


Chapter 54 — pip
"How do I install and manage those dependencies?"
        ↓
Use pip and dependency files such as requirements.txt.
```

## The one-line definitions

> **Module** = a Python file.

> **Package** = a way to organize related Python modules.

> **Virtual environment** = an isolated Python environment for a project.

> **pip** = a tool for installing and managing Python packages.

---

# Why Module 09 Matters for Your AI Engineering Path

Later you'll see projects such as:

```text
rag_app/
├── .venv/
├── requirements.txt
├── app/
│   ├── main.py
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── database/
│   └── utils/
└── tests/
```

You should now recognize the major pieces:

```text
.py files          → modules
folders            → packages
.venv              → isolated Python environment
pip                → dependency management
requirements.txt   → dependency specification
```

This is the bridge from **learning Python syntax** to **building real Python applications**.
