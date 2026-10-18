# Concept 16 — Machine Instructions

## What is a Machine Instruction?

A **machine instruction** is a low-level operation defined by a CPU's **Instruction Set Architecture (ISA)**.

Conceptual examples:

- LOAD — move data from memory into a register
- STORE — move data from a register into memory
- ADD — perform addition
- SUB — perform subtraction
- COMPARE — compare values
- JUMP / BRANCH — change control flow

A machine instruction tells the CPU what operation to perform.

## Python Code Is Not a Machine Instruction

Python:

```python
z = x + y
```

is a high-level statement. The CPU cannot directly execute this Python statement.

A useful conceptual model is:

```text
Python code
    ↓
Python execution machinery
    ↓
lower-level representation
    ↓
machine instructions
    ↓
CPU
```

Do not treat Python source, Python bytecode, and CPU machine instructions as the same thing.

## Instruction Set Architecture (ISA)

An **ISA** defines the instruction vocabulary and rules understood by a CPU architecture.

Examples:

- x86-64
- ARM64 / AArch64
- RISC-V

An ISA defines things such as available instructions, registers, instruction behavior, memory access rules, and instruction encodings.

## Registers + ALU + Instructions

Simplified:

```text
R1 = 10
R2 = 20

ADD R1, R2

R1 = 30
R2 = 20
```

Registers hold active values while the ALU performs the arithmetic operation.

## Instruction vs Data

Both instructions and data are ultimately represented using bits. The difference is how the system interprets them.

```text
Bits
 ├── interpreted as data
 └── interpreted as instructions
```

## LOAD and STORE

```text
LOAD
Memory → Register

STORE
Register → Memory
```

## Control Flow

A high-level statement such as:

```python
if x > 10:
    ...
```

ultimately requires mechanisms such as:

```text
COMPARE
    ↓
condition
    ↓
BRANCH / JUMP
```

Loops similarly require repeated control-flow operations.

## Fetch–Decode–Execute

The CPU repeatedly performs a simplified cycle:

```text
FETCH
  ↓
DECODE
  ↓
EXECUTE
  ↓
repeat
```

- **Fetch:** obtain the next instruction.
- **Decode:** determine what operation the instruction represents.
- **Execute:** perform the required operation.

## Program Counter

The **Program Counter (PC)** holds the address of the next instruction to be fetched.

Branches and jumps can change the PC to another address.

## Important Distinctions

```text
Python source
    ≠
Python bytecode
    ≠
CPU machine instructions
```

Also:

- Machine instructions are operations defined by an ISA.
- The ALU does arithmetic and logical operations, but does not perform every CPU action.
- Python does not simply become one direct sequence of machine instructions in one obvious step; runtime and implementation details matter.

## AI Engineering Connection

High-level AI code such as:

```python
result = model(input)
```

ultimately causes enormous numbers of lower-level operations.

Performance can depend on CPU/GPU execution, memory access, data representation, data movement, batching, kernels, and runtime behavior.

## Summary

> **A machine instruction is a low-level operation defined by the CPU's ISA, and the CPU repeatedly fetches, decodes, and executes such instructions.**

## Revision Questions

1. What is a machine instruction?
2. What does an ISA define?
3. Why is Python code not a machine instruction?
4. What is the role of the Program Counter?
5. What is the difference between LOAD and STORE?
6. What happens during FETCH → DECODE → EXECUTE?
7. Why are Python source, Python bytecode, and machine instructions different?
