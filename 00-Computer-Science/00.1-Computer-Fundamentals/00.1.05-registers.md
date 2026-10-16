# Concept 5 — CPU Registers

## Core Idea

A **register** is a very small, extremely fast storage location inside the CPU.

Registers hold information that the CPU is actively working with.

```text
CPU
┌────────────────────┐
│     Registers      │
│       ALU          │
│   Control Unit     │
└────────────────────┘
```

## Why Registers?

For:

```text
10 + 20
```

a simplified model is:

```text
RAM
 ↓
Registers
 ├── 10
 └── 20
 ↓
ALU
 ↓
30
```

The ALU needs operands immediately available for the operation. Registers provide this immediate working storage.

## Registers vs RAM

| | Registers | RAM |
|---|---|---|
| Location | Inside CPU | Separate from CPU |
| Size | Very small | Much larger |
| Speed | Extremely fast | Slower than registers |
| Purpose | Immediate CPU work | Larger working memory |

Do not think of registers merely as "faster RAM." They are CPU-resident storage locations that form part of the CPU's execution machinery.

## Example

For:

```python
x = 10
y = 20
z = x + y
```

a simplified execution model is:

```text
Memory
  ↓
Registers
  ↓
ALU
  ↓
Register
  ↓
Memory
```

Modern CPUs are more complex because of caches, pipelines, instruction formats, and other mechanisms. This simplified model builds the foundational mental model first.

## Registers Can Hold Different Information

Depending on CPU architecture, registers can hold things such as:

- Values being operated on
- Memory addresses
- Instruction-related information
- Stack-related information
- Status/flags
- Other CPU control information

## Key Takeaway
> Registers are small, extremely fast CPU-resident storage locations used for immediate execution work.
