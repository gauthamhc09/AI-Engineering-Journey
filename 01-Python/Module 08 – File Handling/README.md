# Module 08 — Files, Data & Logging

## Module Overview

This module covers practical Python skills for working with files, structured data, and application logging.

- Chapter 47 — File Handling
- Chapter 48 — CSV Files
- Chapter 49 — JSON
- Chapter 50 — Logging

These concepts connect directly to backend and AI/LLM engineering:

```text
React
  ↕
JSON
  ↕
FastAPI
  ↕
Python
  ↕
PostgreSQL

CSV  → data ingestion
JSON → APIs / structured data / LLM communication
Logging → debugging / observability
```

---

# Chapter 47 — File Handling

## Opening a file

Python uses `open()` to work with files.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

The `with` statement automatically handles closing the file.

## File modes

| Mode | Meaning |
|---|---|
| `"r"` | Read |
| `"w"` | Write — overwrites existing content |
| `"a"` | Append — adds to existing content |
| `"x"` | Create a new file; fails if it already exists |

Example:

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Python")
```

Append:

```python
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nAI")
```

## Reading

Read the entire file:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Read line by line:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
```

## Writing

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Python")
```

### Mental model

```text
open()
  ↓
read / write
  ↓
with block ends
  ↓
file automatically closes
```

---

# Chapter 48 — CSV Files

## What is CSV?

CSV = Comma-Separated Values.

It is commonly used for tabular data:

```text
symbol,quantity,price
RELIANCE,10,2500
INFY,20,1500
TCS,5,3500
```

Think:

```text
CSV → spreadsheet-like / rows and columns
```

CSV is common in financial data, broker exports, datasets, reports, and data ingestion.

## The `csv` module

```python
import csv
```

### `csv.reader()`

```python
with open("portfolio.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

A row becomes:

```python
["RELIANCE", "10", "2500"]
```

CSV values initially come in as strings.

## Header row

```python
with open("portfolio.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        print(row)
```

`next(reader)` retrieves the next row, commonly the header.

## Type conversion

Because CSV values are strings:

```python
quantity = int(row["quantity"])
price = float(row["price"])
```

This converts:

```text
"10" → 10
"2500" → 2500.0
```

## `csv.DictReader`

Each row becomes a dictionary:

```python
with open("portfolio.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Example:

```python
{
    "symbol": "RELIANCE",
    "quantity": "10",
    "price": "2500"
}
```

Then:

```python
symbol = row["symbol"]
quantity = int(row["quantity"])
price = float(row["price"])
```

`DictReader` is usually preferable when column names make the data clearer.

## Writing CSV

```python
import csv

with open("portfolio.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["symbol", "quantity", "price"])
    writer.writerow(["RELIANCE", 10, 2500])
    writer.writerow(["INFY", 20, 1500])
```

Multiple rows:

```python
writer.writerows([
    ["RELIANCE", 10, 2500],
    ["INFY", 20, 1500],
    ["TCS", 5, 3500]
])
```

## `csv.DictWriter`

```python
import csv

portfolio_data = [
    {"symbol": "RELIANCE", "quantity": 10, "price": 2500},
    {"symbol": "INFY", "quantity": 20, "price": 1500}
]

with open("portfolio.csv", "w", encoding="utf-8", newline="") as file:
    fieldnames = ["symbol", "quantity", "price"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(portfolio_data)
```

## CSV mental model

```text
CSV file
   ↓
DictReader
   ↓
Python dictionaries
   ↓
validation / conversion
   ↓
application logic
```

Portfolio Intelligence connection:

```text
Broker CSV
   ↓
CSV parser
   ↓
DictReader
   ↓
normalize columns
   ↓
internal holding model
   ↓
PostgreSQL
```

---

# Chapter 49 — JSON

## What is JSON?

JSON = JavaScript Object Notation.

JSON is a text-based format used to represent and exchange structured data.

Example:

```json
{
    "name": "Gautham",
    "age": 33,
    "role": "AI Engineer"
}
```

A Python dictionary and a JSON object look similar, but they are not the same thing. A dictionary is a Python data structure; JSON is a data representation format.

## Why JSON matters

JSON is commonly used between React and FastAPI, backend services, external APIs, LLM APIs, and configuration systems.

Typical flow:

```text
React
  ↓
JSON request
  ↓
FastAPI
  ↓
Python
  ↓
business logic
  ↓
JSON response
  ↓
React
```

## JSON data types

JSON supports:

- string
- number
- boolean
- null
- array
- object

Important mapping:

| JSON | Python |
|---|---|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` / `float` |
| `true` | `True` |
| `false` | `False` |
| `null` | `None` |

## The `json` module

```python
import json
```

Four important functions:

```python
json.dumps()
json.loads()
json.dump()
json.load()
```

## `json.dumps()` — Python → JSON string

```python
portfolio = {
    "name": "My Portfolio",
    "value": 500000,
    "active": True
}

portfolio_json = json.dumps(portfolio)
```

`portfolio_json` is a string:

```python
type(portfolio_json)
# str
```

Mental model:

```text
Python object
    ↓
json.dumps()
    ↓
JSON string
```

## `json.loads()` — JSON string → Python

```python
data = '{"name": "Gautham", "age": 33}'

result = json.loads(data)
```

Now:

```python
type(result)
# dict
```

Mental model:

```text
JSON string
    ↓
json.loads()
    ↓
Python object
```

## `json.dump()` — Python → JSON file

```python
portfolio = {
    "name": "My Portfolio",
    "value": 500000,
    "pnl": 25000
}

with open("portfolio.json", "w", encoding="utf-8") as file:
    json.dump(portfolio, file)
```

## `json.load()` — JSON file → Python

```python
with open("portfolio.json", "r", encoding="utf-8") as file:
    portfolio = json.load(file)
```

## Four-function memory trick

```text
                 STRING        FILE

Python → JSON    dumps          dump
JSON → Python    loads          load
```

`"s"` = string.

## Pretty JSON

```python
json.dump(
    portfolio,
    file,
    indent=4
)
```

## Nested JSON

```python
portfolio = {
    "name": "My Portfolio",
    "holdings": [
        {
            "symbol": "RELIANCE",
            "quantity": 10
        },
        {
            "symbol": "INFY",
            "quantity": 20
        }
    ]
}
```

Access INFY's quantity:

```python
portfolio["holdings"][1]["quantity"]
```

Result:

```text
20
```

Mental structure:

```text
dict
  ↓
list
  ↓
dict
```

## JSON and APIs

Conceptually:

```text
Python backend
     ↓
Python dict
     ↓
JSON response
     ↓
React frontend
```

## JSON and LLM APIs

Conceptually:

```text
Python application
       ↓
JSON request
       ↓
LLM API
       ↓
JSON response
       ↓
Python application
```

## JSON validation

JSON can contain missing fields, wrong types, unexpected fields, or invalid values.

Example:

```json
{
    "quantity": "ten"
}
```

instead of:

```json
{
    "quantity": 10
}
```

Backend frameworks such as FastAPI commonly use Pydantic for validation:

```text
JSON request
     ↓
Pydantic validation
     ↓
Python object
     ↓
business logic
```

## CSV vs JSON

```text
CSV
 ↓
tabular / rows + columns

JSON
 ↓
structured / nested data
```

---

# Chapter 50 — Logging

## What is logging?

Logging means recording events that happen inside an application.

Example:

```text
2026-09-01 09:30:10 INFO Portfolio loaded
2026-09-01 09:30:11 INFO Calculating P&L
2026-09-01 09:30:12 WARNING Price unavailable
2026-09-01 09:30:13 ERROR Database connection failed
```

Logging is much more useful than scattering `print()` statements throughout a production application.

## Python's logging module

```python
import logging
```

Basic example:

```python
logging.basicConfig(level=logging.INFO)

logging.info("Portfolio loaded")
logging.warning("Price is missing")
logging.error("Database connection failed")
```

## Log levels

From least severe to most severe:

```text
DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL
```

### DEBUG

Detailed information useful for development/troubleshooting.

```python
logging.debug("Processing holding RELIANCE")
```

### INFO

Normal application activity.

```python
logging.info("Portfolio loaded successfully")
```

### WARNING

Something unexpected happened, but the application can continue.

```python
logging.warning("Price data unavailable for XYZ")
```

### ERROR

Something failed.

```python
logging.error("Database query failed")
```

### CRITICAL

A very serious failure that may prevent the application from functioning.

```python
logging.critical("Application cannot start")
```

## Logging threshold

If:

```python
logging.basicConfig(level=logging.WARNING)
```

then:

```text
DEBUG     ❌
INFO      ❌
WARNING   ✅
ERROR     ✅
CRITICAL  ✅
```

The configured level acts as a threshold.

## Logging to a file

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

## Log format

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

Useful fields:

```text
%(asctime)s   → timestamp
%(levelname)s → log level
%(message)s   → actual message
```

## Module-level logger

In larger applications:

```python
import logging

logger = logging.getLogger(__name__)
```

Then:

```python
logger.info("Portfolio loaded")
logger.error("Database failed")
```

`__name__` identifies the current module, which makes logging modular and scalable.

## Logging exceptions

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.error("Calculation failed")
```

Even better inside an exception handler:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Calculation failed")
```

`logger.exception()` logs the message along with traceback information.

### `error()` vs `exception()`

```python
logger.error("Something failed")
```

→ logs the error message.

```python
logger.exception("Something failed")
```

→ logs the message plus traceback information and is intended for use while handling an exception.

## Re-raising after logging

Useful pattern:

```python
try:
    ...
except SomeError:
    logger.exception("Operation failed")
    raise
```

Flow:

```text
operation
   ↓
exception
   ↓
log exception + traceback
   ↓
raise
   ↓
higher-level caller handles it
```

## Logging variables

```python
symbol = "RELIANCE"
quantity = 10

logger.info(
    "Processing %s with quantity %s",
    symbol,
    quantity
)
```

## Don't log sensitive information

Never casually log:

- passwords
- API keys
- access tokens
- JWT tokens
- credit card information
- private credentials

## Logging in AI/LLM systems

A production AI system might log:

```text
INFO  - Received user request
INFO  - Retrieved 5 documents
INFO  - Constructed context
INFO  - Calling LLM
INFO  - LLM response received
ERROR - Vector database unavailable
```

This becomes part of observability.

Later, observability expands into:

```text
Logs
Metrics
Traces
```

---

# Module 08 — Final Mental Model

## Files

```text
with open(...)
   ↓
read / write
   ↓
automatic cleanup
```

## CSV

```text
CSV
 ↓
DictReader
 ↓
Python dictionaries
 ↓
validation / conversion
```

## JSON

```text
Python dict
   ↕
JSON
```

Core functions:

```python
json.dumps()
json.loads()
json.dump()
json.load()
```

## Logging

```text
Application
    ↓
events
    ↓
logging
    ↓
DEBUG / INFO / WARNING / ERROR / CRITICAL
    ↓
terminal / file / monitoring
```

---

# Module 08 — Key Takeaways

1. Use `with open(...)` for safe file handling.
2. `"w"` overwrites; `"a"` appends.
3. CSV is ideal for tabular data.
4. `csv.DictReader` provides dictionary-style row access.
5. CSV values initially arrive as strings.
6. JSON is ideal for structured and nested data.
7. `dumps`/`loads` work with JSON strings.
8. `dump`/`load` work with JSON files.
9. JSON is fundamental to APIs and LLM integrations.
10. Logging is preferable to `print()` for application observability.
11. Log levels range from DEBUG through CRITICAL.
12. `logger.exception()` captures traceback information inside exception handling.
13. `logger = logging.getLogger(__name__)` is the scalable module-level pattern.
14. Never expose secrets or sensitive credentials in logs.

---

# Module 08 — Final Connection to Your AI Engineering Roadmap

```text
                AI / LLM APPLICATION
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
      React            FastAPI          LLM APIs
        │                │                │
        └──────────── JSON ───────────────┘
                         │
                       Python
                         │
              ┌──────────┼──────────┐
              ↓          ↓          ↓
             CSV        JSON      Logging
              │          │          │
              └──────────┼──────────┘
                         ↓
                    PostgreSQL
                         ↓
                 Production System
```

## Module 08 Status

**Complete.** ✅
