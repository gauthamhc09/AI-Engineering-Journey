# Concept 2 — Hardware vs Software

## Core Idea

```text
Computer
├── Software → instructions
└── Hardware
    ├── CPU
    ├── RAM
    └── Storage
```

**Hardware** is the physical machinery: CPU, RAM, SSD/HDD, keyboard, display, etc.

**Software** is the collection of instructions/programs that tell hardware what to do.

## Program vs Running State

For:

```python
x = 10
```

the `.py` file is software stored persistently on storage. When the program runs, its active state is represented in working memory and CPU execution machinery.

```text
Python file
   ↓
Storage
   ↓
Program starts
   ↓
Running state
   ↓
RAM / CPU execution
```

When the program closes, the running state is generally lost, while the `.py` file remains on storage.

## Important Refinement

Python source does not execute on the physical CPU in the same form in which it was written. There are execution layers between Python source and hardware. Later we will study the path in detail.

## Key Takeaway
> Software provides instructions; hardware provides the physical machinery that executes those instructions.
