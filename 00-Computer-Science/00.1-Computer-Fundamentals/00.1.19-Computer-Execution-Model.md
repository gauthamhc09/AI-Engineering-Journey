# Concept 19 — Computer Execution Model

## Purpose

Concepts 1–18 introduced individual parts of computer execution.

Concept 19 integrates them into one model:

> A computer executes instructions that repeatedly transform system/program state while the OS, memory hierarchy, CPU, runtime, and hardware cooperate.

## 1. Complete High-Level Model

```text
                    PROGRAM
                       │
                       ▼
                  SSD / Storage
                       │
                       ▼
                Operating System
                       │
                       ▼
                    Process
                       │
                       ▼
                     RAM
                       │
                       ▼
                    Cache
                       │
                       ▼
                  Registers
                       │
                       ▼
                     CPU
              ┌────────┴────────┐
              ▼                 ▼
        Control Logic          ALU
              │                 │
              └────────┬────────┘
                       ▼
                 State Changes
                       │
                       ▼
                    Result
```

This is a conceptual model, not a literal physical pipeline in which every byte travels through every box.

## 2. Example Program

```python
a = 10
b = 20
c = a + b

print(c)
```

### Stage 1 — Storage

The source file exists persistently:

```text
SSD
└── program.py
```

### Stage 2 — Program Startup

When the user runs:

```bash
python program.py
```

the OS becomes involved:

```text
User
 ↓
Shell / command
 ↓
Operating System
 ↓
Start Python process
```

### Stage 3 — Process

A running instance is associated with a process managed by the OS.

```text
program.py ≠ process
```

The process has execution state and OS-managed resources.

### Stage 4 — Memory

The running program and runtime need active working state in memory.

### Stage 5 — Python Runtime

For CPython, a useful conceptual model is:

```text
Python source
      ↓
Parsing
      ↓
Python bytecode
      ↓
CPython runtime
      ↓
execution
```

### Stage 6 — CPU Execution

The CPU repeatedly performs:

```text
FETCH
  ↓
DECODE
  ↓
EXECUTE
  ↓
repeat
```

The Program Counter identifies the address of the next instruction.

### Stage 7 — Registers and ALU

A simplified addition:

```text
R1 = 10
R2 = 20

   ↓
  ALU
10 + 20

   ↓
R3 = 30
```

### Stage 8 — State Change

The fundamental model is:

```text
Current State + Instruction
            ↓
        New State
```

For example:

```text
Before:
a = 10
b = 20
c = ?

After:
a = 10
b = 20
c = 30
```

## 3. Control Flow

A program does not always execute instructions strictly in sequence.

For:

```python
if c > 25:
    ...
```

the CPU conceptually performs:

```text
COMPARE
   ↓
condition?
  ↙  ↘
yes   no
 ↓     ↓
path A path B
```

Branches and jumps can change the Program Counter.

Loops similarly use repeated control flow:

```text
initialize
   ↓
check
   ↓
body
   ↓
update
   ↓
jump back
   ↓
check
   ↓
...
```

## 4. Computation as State Transitions

A useful fundamental model is:

```text
State
  +
Instruction
  ↓
New State
  +
Next Instruction
  ↓
New State
  +
Next Instruction
  ↓
...
```

This sequence of state transitions is computation.

## 5. Abstraction

High-level programming hides enormous amounts of lower-level detail.

For example:

```python
result = a + b
```

hides things such as:

- machine instructions
- registers
- memory addresses
- cache
- CPU control logic

Similarly:

```python
requests.get(url)
```

can hide DNS, TCP, TLS, HTTP, sockets, OS networking, and network hardware.

And:

```python
db.execute(query)
```

can hide connections, query parsing, query planning, indexes, storage, locks, and transactions.

Abstraction allows engineers to work at a useful level without manually controlling every lower-level detail.

Understanding the lower layers helps with reasoning about performance, behavior, failures, and bottlenecks.

## AI Engineering Connection

A high-level call such as:

```python
response = llm.generate(prompt)
```

can involve:

```text
Python application
        ↓
Process
        ↓
Memory
        ↓
Network request
        ↓
Remote AI service
        ↓
GPU / accelerator
        ↓
Model computation
        ↓
Network response
        ↓
Your process
        ↓
Python objects
```

This foundation helps an AI engineer ask:

- Is the bottleneck CPU?
- Memory?
- Cache?
- Network?
- Database?
- Serialization?
- Concurrency?
- Model inference?
- GPU memory?
- I/O?

## Deep Mental Model

> **A computer is a state-changing machine.**

A program provides instructions.

The CPU executes those instructions.

Memory holds information and state.

The OS manages resources and execution.

Hardware represents information and instructions using physical states corresponding to bits.

Therefore:

```text
State
  +
Instruction
  ↓
New State
  +
Next Instruction
  ↓
New State
  +
Next Instruction
  ↓
...
```

## Module 00.1 Completion

1. What Is a Computer
2. Hardware vs Software
3. CPU
4. CPU Cores
5. Registers
6. ALU & Control Unit
7. RAM
8. Cache
9. Storage
10. SSD vs HDD
11. Memory Hierarchy
12. Bits & Bytes
13. Binary Representation
14. Hexadecimal
15. Data Representation
16. Machine Instructions
17. How a Program Runs
18. CPU–Memory Interaction
19. Computer Execution Model

## Final Revision Questions

1. What is the relationship between a program, process, and CPU?
2. Why does a program need RAM?
3. What role do cache and registers play?
4. What does the CPU do during FETCH → DECODE → EXECUTE?
5. What is the role of the Program Counter?
6. How do addresses and data participate in memory access?
7. Why is Python source different from machine instructions?
8. What does it mean to say that computation is a sequence of state changes?
9. Why are abstractions necessary in software engineering?
10. How does this computer execution model help when reasoning about AI systems?
