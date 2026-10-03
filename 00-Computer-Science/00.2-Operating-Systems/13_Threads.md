# Module 00.2.13 — Threads

## Definition
A **thread is an OS-schedulable unit of execution within a process**.

A process can contain multiple threads:
```text
PROCESS
├── Thread 1
├── Thread 2
└── Thread 3
```

The process provides the broader resource/address-space environment. Threads provide independent execution paths within that environment.

## Thread Execution State
Each thread has its own execution state, including:
- Program Counter (PC)
- CPU registers
- stack
- execution state
- scheduling-related state

## What Threads Share
Threads in the same process generally share:
- virtual address space
- heap
- program code
- global/application data
- many open resources

Each thread has its own execution state and stack.

## Shared Memory and Race Conditions
If two threads access the same mutable data, concurrent updates can race. For example, two threads incrementing `counter = 0` can both read 0 and both write 1, producing 1 instead of the expected 2. Synchronization mechanisms such as locks coordinate access.

## Threads and CPU Parallelism
Multiple threads can execute in parallel when sufficient CPU execution resources are available. With one CPU execution resource, threads can still make concurrent progress through interleaving.

> Multiple threads do not automatically mean parallel execution.

## Thread Scheduling
The OS scheduler ultimately schedules runnable execution units:
```text
Runnable threads
      ↓
Scheduler
      ↓
CPU execution
```

## Thread Context Switching
If Thread A is RUNNING and Thread B is READY, the system can save A's context, make A READY, restore B's context, and make B RUNNING.

## Python Connection
```python
import threading

t = threading.Thread(target=work)
t.start()
```

Conceptually:
```text
Python code
    ↓
threading.Thread
    ↓
Python runtime / OS threading mechanism
    ↓
OS-managed thread
    ↓
Scheduler
    ↓
CPU
```

## Why Threads Are Useful
Threads provide multiple execution paths inside one process and can be useful for workloads involving waiting, such as network or other I/O operations. Do not reduce threads to “I/O only”; usefulness depends on runtime, workload, hardware, and synchronization.

## Backend / AI Engineering Connection
A Python backend may conceptually contain:
```text
FastAPI Process
├── Thread A → Request 1
├── Thread B → Request 2
├── Thread C → Database operation
└── Thread D → Other I/O
```

Threads can share process-level memory, which is useful for shared caches and connection pools, but shared mutable state must be designed carefully.

## Key Mental Model
> **A process is a resource/address-space environment; a thread is an execution unit within that process.**

```text
PROCESS
├── Shared address space
├── Shared resources
├── Thread A
│   ├── PC
│   ├── registers
│   └── stack
└── Thread B
    ├── PC
    ├── registers
    └── stack
```

## Revision Questions
1. What is a thread?
2. What execution state does a thread have?
3. What resources do threads in the same process share?
4. Why does each thread need its own stack?
5. Why can shared memory lead to race conditions?
6. What is the difference between concurrency and parallelism?
7. How does the OS scheduler interact with threads?
8. How does a thread context switch work?
9. How does Python's `threading.Thread` relate to OS-level threading?
10. Why are threads useful for I/O-heavy applications?
