# Module 00.2.15 — Process vs Thread

## First-Principles Definitions
**Process:** A running program with its own address space, execution environment, and OS-managed resources.

**Thread:** An execution unit within a process.

Useful foundation:
```text
Process → resource / address-space boundary
Thread  → execution unit
```

## Processes Have Separate Address Spaces
```text
Process A              Process B
┌──────────────┐       ┌──────────────┐
│ Address A    │       │ Address B    │
│ code         │       │ code         │
│ heap         │       │ heap         │
└──────────────┘       └──────────────┘
```

Separate virtual address spaces provide strong memory isolation.

## Threads Share the Process Address Space
```text
PROCESS
├── Shared address space
├── Code
├── Heap
├── Thread A
├── Thread B
└── Thread C
```

Threads in the same process can access shared process memory.

## Memory Isolation
Processes:
```text
Process A ──X──> Process B memory
```

Threads:
```text
Thread A ──→ shared process memory ←── Thread B
```

Therefore:
> Processes provide stronger memory isolation.
>
> Threads provide easier shared-memory access within a process.

## Communication
Threads can communicate through shared memory, but shared mutable state requires synchronization.

Processes generally use IPC mechanisms such as:
- pipes
- queues
- shared memory mechanisms
- sockets

```text
Process A → IPC → Process B
```

## Creation and Resource Overhead
Creating a process generally requires more OS-managed resources than adding a thread to an existing process.

A process has its own virtual address space, process metadata, resource bookkeeping, at least one thread, and other process-level resources.

Therefore:
> Threads are generally lighter-weight than processes.

“Lighter” does not mean free.

## Context Switching
Both processes and threads can be scheduled and switched.

Thread switch:
```text
Thread A → save context → Thread B → restore context
```

Process switching can involve additional memory-management effects because processes normally have different virtual address spaces. Exact costs depend on OS, CPU architecture, runtime, and workload.

## Failure and Isolation
If one thread causes its process to terminate or corrupts shared process state, other threads in that process can be affected.

A problem confined to Process A's memory is generally isolated from Process B's address space.

This is why multiple processes can provide stronger fault containment.

## One Process Can Have Multiple Threads
```text
Process
├── Thread 1
├── Thread 2
├── Thread 3
└── Thread 4
```

The main thread is simply one thread belonging to the process.

## Python Examples
### Threads
```python
from threading import Thread

t1 = Thread(target=work_a)
t2 = Thread(target=work_b)
t1.start()
t2.start()
```

Conceptually:
```text
Python Process
├── Main Thread
├── Thread t1
└── Thread t2
```

### Processes
```python
from multiprocessing import Process

p1 = Process(target=work_a)
p2 = Process(target=work_b)
p1.start()
p2.start()
```

Conceptually:
```text
Process A → Thread(s)
Process B → Thread(s)
```

The processes have separate address spaces.

## CPU Parallelism
Both processes and threads can potentially execute in parallel:
```text
Core 1 → Process A / Thread 1
Core 2 → Process A / Thread 2
Core 3 → Process B / Thread 1
Core 4 → Process C / Thread 1
```

The OS ultimately schedules execution units onto available hardware execution resources.

## Why Processes Are Useful for Isolation
Separate processes provide stronger memory boundaries and are foundational to application isolation, worker processes, containers, and production infrastructure.

## Why Threads Are Useful for Shared Work
Threads can access shared caches, connection pools, application state, and shared data structures within the same process.

The tradeoff is that shared mutable state requires careful synchronization.

## Fundamental Tradeoff
### Process
```text
├── Stronger isolation
├── Separate address space
├── Generally more resource overhead
└── IPC commonly needed for communication
```

### Thread
```text
├── Shares process address space
├── Easier shared-memory communication
├── Generally lighter
└── Requires careful synchronization
```

Neither is universally better.

## Backend Architecture Example
Multiple processes:
```text
Server
├── Worker Process 1
├── Worker Process 2
└── Worker Process 3
```

Potential benefits: isolation, fault containment, independent lifecycle, use of multiple CPU cores.

Potential drawback: each process may consume substantial memory.

Multiple threads:
```text
Server Process
├── Thread 1
├── Thread 2
├── Thread 3
└── Thread 4
```

Potential benefits: shared in-memory state, convenient communication, generally lower overhead than separate processes.

Potential drawback: shared mutable state can require synchronization.

## AI Engineering Example
Suppose each worker process loads a large model:
```text
Process 1 → model
Process 2 → model
Process 3 → model
Process 4 → model
```

Depending on the runtime and memory-sharing mechanisms, this can require substantial memory.

More workers do not automatically mean more performance. There can be additional memory consumption, scheduling overhead, CPU contention, and other bottlenecks.

A thread-based design may allow threads to share process memory, but useful parallelism depends on the Python runtime, native libraries, GPU usage, synchronization, and workload.

## Python GIL — Important Preview
The OS can schedule multiple Python threads. However, standard CPython's execution model has historically included the **Global Interpreter Lock (GIL)**, which affects whether multiple threads can execute Python bytecode in parallel.

This is a **Python runtime issue, not an operating-system rule**.

Do not conclude “threads cannot run in parallel.” The OS can schedule threads on multiple CPU cores. The question is what the particular runtime permits them to execute concurrently.

## FastAPI Mental Model
```text
Server
├── Process 1
│   ├── Thread 1
│   └── Thread 2
└── Process 2
    ├── Thread 1
    └── Thread 2
```

Processes → separate address spaces.

Threads within each process → shared address space.

## Comparison Table
| Property | Process | Thread |
|---|---|---|
| What is it? | Running program/resource environment | Execution unit inside a process |
| Address space | Separate | Shared within same process |
| Memory isolation | Stronger | Weaker within same process |
| Heap | Own process address space | Shared within process |
| Stack | Each thread has its own stack | Own stack |
| Execution state | Contains execution thread(s) | Own PC/registers/execution state |
| Communication | IPC generally needed | Shared memory can be used |
| Creation overhead | Generally higher | Generally lower |
| Failure isolation | Stronger | Weaker within same process |
| Parallel execution | Possible | Possible |
| Python abstraction | `multiprocessing.Process` | `threading.Thread` |

## Four Rules to Remember
1. **Process → address-space/resource boundary**
2. **Thread → execution unit**
3. **Threads in one process → share process memory/resources**
4. **Separate processes → stronger memory isolation**

## Complete Mental Model
```text
PROGRAM
   ↓
PROCESS
   ↓
contains THREADS
   ↓
THREAD becomes READY
   ↓
SCHEDULER
   ↓
THREAD becomes RUNNING
   ↓
CPU executes instructions
   │
   ├── preemption → READY
   ├── I/O → WAITING → READY
   └── finish → TERMINATED
```

Memory:
```text
Process A                    Process B
──────────                   ──────────
Address Space A              Address Space B
     │                            │
   Thread A                     Thread B
```

## Common Mistakes
- A thread is not a separate process.
- Threads in the same process do not normally have separate address spaces.
- Threads do not automatically execute in parallel.
- Shared memory does not mean simultaneous execution.
- A thread's stack is distinct from the shared process heap.
- More processes do not automatically mean better performance.
- More threads do not automatically mean better performance.
- The GIL is a Python runtime issue, not an OS rule.
- A process's execution environment should not be confused with a thread's CPU execution context.

## Revision Questions
1. What is the fundamental difference between a process and a thread?
2. What is a process's address space?
3. What do threads within the same process share?
4. What execution state is private to each thread?
5. Why do separate processes provide stronger isolation?
6. Why can threads communicate through shared memory?
7. Why does shared memory create synchronization challenges?
8. Why are threads generally lighter than processes?
9. Why can process switching have additional memory-management effects?
10. Can processes and threads both execute in parallel?
11. How do Python `threading.Thread` and `multiprocessing.Process` map to these concepts?
12. Why can more model-serving processes increase memory usage?
13. Why is the GIL a runtime issue rather than an OS rule?
14. Explain: “Processes provide isolation; threads provide shared-memory concurrency.”
