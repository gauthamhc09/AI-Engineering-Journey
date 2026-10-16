# Concept 7 — RAM

**RAM = Random Access Memory.**

RAM is the computer's main volatile working memory. Running programs need working memory for instructions, data, objects, variables/state, and intermediate information.

```text
CPU
 ↓
RAM
```

Registers are extremely fast but tiny, so RAM provides a much larger working-memory area.

## Random Access

RAM is addressable. Conceptually:

```text
Address   Data
1000      25
1001      42
1002      91
1003      17
```

The CPU can request the data associated with a particular memory address.

## RAM and Python

For:

```python
numbers = [10, 20, 30]
total = sum(numbers)
```

the running program needs memory for the list, elements, Python objects, references, execution state, and other runtime data.

## Volatility

```text
Power OFF
   ↓
RAM contents are lost
```

In contrast, files on persistent storage remain.

## RAM vs Storage

| | RAM | Storage |
|---|---|---|
| Purpose | Active working memory | Persistent data |
| Volatile | Yes | No |
| Speed | Faster | Slower |
| Capacity | Large | Much larger |
| Survives power loss | No | Yes |

## Key Takeaway

> RAM is the computer's main volatile working memory. It provides a relatively fast, addressable space for running programs and their data.
