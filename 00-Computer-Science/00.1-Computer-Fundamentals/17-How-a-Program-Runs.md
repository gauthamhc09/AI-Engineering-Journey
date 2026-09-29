# Concept 17 — How a Program Runs

## Why This Concept Matters

We have learned CPU, registers, ALU, RAM, cache, storage, bits, data representation, and machine instructions.

Now we connect them by asking:

> What actually happens when a Python program is run?

Example:

```python
x = 10
y = 20
z = x + y

print(z)
```

## 1. Program Stored on Storage

The `.py` file initially exists as persistent data on storage such as an SSD.

```text
SSD
└── calculator.py
```

At this stage:

> The program is stored data. It is not executing.

## 2. Running the Program

When you execute:

```bash
python calculator.py
```

the operating system becomes involved.

```text
User
 ↓
Shell / command
 ↓
Operating System
 ↓
Start Python process
```

The OS manages the resources required by the running program.

## 3. Python Process

A running instance is associated with a process managed by the OS.

```text
Python process
│
├── program/runtime state
├── memory
├── stack
├── heap
├── threads
└── other resources
```

Important:

```text
program.py ≠ process
```

A file is persistent data; a process is a running instance with execution state and OS-managed resources.

## 4. RAM Becomes Involved

The program and runtime need working memory.

Conceptually:

```text
SSD
 ↓
RAM
 ↓
cache
 ↓
CPU
```

RAM holds active working state.

Storage and RAM have different roles:

- Storage — persistent
- RAM — volatile working memory

## 5. Python Execution Machinery

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

The CPU ultimately executes machine instructions associated with the runtime and system.

Do not collapse this into:

```text
Python source → machine code
```

## 6. CPU Execution

At the CPU level:

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

## 7. Registers and ALU

For an addition, a simplified model might be:

```text
R1 = 10
R2 = 20

ADD R1, R2

R1 = 30
R2 = 20
```

The ALU performs the arithmetic operation.

This is a simplified CPU-level model, not an exact mapping of Python variables to registers.

## 8. State Changes

The fundamental model is:

```text
Current State + Instruction
            ↓
       New State
```

For example:

```text
a = 10
b = 20
c = ?
```

After the relevant computation:

```text
a = 10
b = 20
c = 30
```

## 9. Program Output

Avoid thinking:

```text
CPU → RAM → translate bits back into Python → 30
```

Instead:

```text
CPU + runtime + memory
        ↓
runtime state changes
        ↓
Python-level result
        ↓
output mechanisms
        ↓
characters "30"
        ↓
terminal/display
```

There is not generally a final step where CPU bits are simply translated back into Python.

## 10. Complete Simplified Journey

```text
Python source code
       ↓
Python execution machinery
       ↓
OS / Process
       ↓
RAM
       ↓
Cache / Registers
       ↓
CPU
       ↓
FETCH
       ↓
DECODE
       ↓
EXECUTE
       ↓
State changes
       ↓
Result
```

## AI Engineering Connection

A simple AI call such as:

```python
response = model.generate(input)
```

can involve:

```text
Python application
    ↓
process
    ↓
memory
    ↓
network
    ↓
remote service / model
    ↓
computation
    ↓
network
    ↓
your process
    ↓
Python objects
```

This foundation lets an AI engineer reason about where computation, memory, networking, and I/O occur.

## Summary

> **Running a program means creating a managed execution context, loading and maintaining active state, and repeatedly executing operations that change that state.**

## Revision Questions

1. Where does a `.py` file initially live?
2. What does the OS do when the program is started?
3. What is a process?
4. Why is RAM involved?
5. Why is Python source not itself a CPU machine instruction?
6. What is the role of the Program Counter?
7. How do registers and the ALU participate in computation?
8. Why is `CPU → RAM → translate back to Python` an oversimplification?
