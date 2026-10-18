# Concept 4 — CPU Cores

## Core Idea

A **CPU core** is an individual execution unit inside a CPU.

```text
CPU
├── Core 1
├── Core 2
├── Core 3
└── Core 4
```

Multiple cores allow independent work to potentially execute simultaneously.

## Parallelism vs Concurrency

**Parallelism** means actual simultaneous execution of work on different execution units/cores.

```text
Core 1 → Task A
Core 2 → Task B
Core 3 → Task C
Core 4 → Task D
```

**Concurrency** means multiple tasks are in progress, but they do not necessarily execute at exactly the same time. A single core can provide concurrency by switching between tasks.

## Dependency Matters

```text
A → B → C → D
```

If every task depends on the previous one, four cores do not automatically make them parallel.

Independent work can potentially run in parallel:

```text
Task A
Task B
Task C
Task D
```

## Python Connection

- `multiprocessing` can use multiple processes for CPU parallelism.
- `asyncio` is primarily useful for concurrency around I/O rather than making CPU work execute simultaneously.

The detailed relationship between processes, threads, cores, scheduling, and the GIL comes later.

## Key Takeaway
> Multiple CPU cores provide multiple execution units, allowing independent work to potentially run in parallel.
