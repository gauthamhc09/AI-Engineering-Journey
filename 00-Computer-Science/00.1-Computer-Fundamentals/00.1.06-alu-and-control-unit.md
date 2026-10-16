# Concept 6 — ALU and Control Unit

## Core Idea

```text
CPU
├── Control Unit → coordinates execution
├── Registers    → hold immediate working values
└── ALU          → performs arithmetic/logic
```

## ALU — Arithmetic Logic Unit

The ALU performs arithmetic and logical operations:

```text
10 + 20
10 - 20
10 × 20
10 > 20
10 == 20
```

If:

```text
Register 1 = 10
Register 2 = 20
```

the ALU can perform:

```text
10 + 20
```

and produce:

```text
30
```

## Control Unit

The **Control Unit (CU)** coordinates the execution of instructions.

At a simplified level:

```text
Instruction
     ↓
Control Unit
     │
     │ control signals
     ↓
Registers / ALU / other CPU components
```

The Control Unit decodes the current instruction and generates control signals that coordinate the appropriate CPU operations.

## Example

Suppose the CPU receives an instruction conceptually equivalent to:

```text
ADD register1, register2
```

with:

```text
register1 = 10
register2 = 20
```

A simplified flow is:

```text
Instruction
     ↓
Control Unit
     │
     │ control signals
     ↓
Registers ─────→ ALU
  10, 20        ADD
                  │
                  ↓
                 30
                  │
                  ↓
               Register
```

## Important Technical Refinement

It is convenient to say:

> "The Control Unit tells the ALU what to do."

Technically, the Control Unit decodes the instruction and generates electrical control signals that coordinate the CPU's circuitry.

## Key Takeaway
> The ALU performs arithmetic and logical operations; the Control Unit coordinates execution by generating control signals based on the current instruction.
