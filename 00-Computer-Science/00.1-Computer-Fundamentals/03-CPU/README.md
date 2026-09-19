# Concept 3 — CPU

## Core Idea

CPU stands for **Central Processing Unit**. The CPU is responsible for executing machine instructions.

```text
Instruction
     ↓
    CPU
     ↓
Machine state changes
```

## CPU Mental Model

```text
CPU
├── Registers
├── ALU
└── Control Unit
```

## Example

For:

```text
10 + 20
```

the CPU executes instructions that cause the addition to happen.

**CPU execution** means the CPU performs the operation specified by a machine instruction, causing machine state to change.

## ALU

The **Arithmetic Logic Unit (ALU)** performs arithmetic and logical operations such as:

```text
10 + 20
10 - 20
10 × 20
10 > 20
10 == 20
```

## CPU and Memory

A simplified model is:

```text
Memory
   ↓
CPU
   ↓
Operation
   ↓
New state
```

## Key Takeaway
> The CPU executes machine instructions and performs the operations specified by those instructions.
