# 00.2.21 — Process Resources

## 1. What is a Process Resource?

A **process resource** is anything the operating system allocates, manages, or makes available to a process while it is running.

> **Process = program + execution state + allocated resources**

## 2. Major Process Resources

```text
Process
│
├── CPU
├── Memory
├── Threads
├── Files
├── File Descriptors
├── Network Connections
└── IPC resources
```

## 3. CPU

A process needs CPU time to execute instructions. Multiple processes/threads compete for CPU time, and the OS scheduler decides which runnable execution unit gets CPU time.

This connects to CPU scheduling, preemption, and context switching.

## 4. Memory

A process needs memory for code, data, heap, stack, and other mappings.

```text
Process
│
├── Code
├── Data
├── Heap
├── Stack
└── Other mappings
```

Because of virtual memory:

```text
Process
    ↓
Virtual Address Space
    ↓
Page Tables
    ↓
Physical Memory
```

## 5. Threads

A process can contain one or more threads.

Each thread has its own:
- Program counter
- Registers
- Stack

Threads in the same process share much of the process's memory:

```text
Process
├── Thread A → own stack
├── Thread B → own stack
├── Thread C → own stack
└── Shared process memory / heap
```

## 6. Files

Processes may access files such as data, configuration, models, and logs.

```text
Application
    ↓
Operating System
    ↓
Filesystem
    ↓
Storage
```

## 7. File Descriptors

A process uses file descriptors to refer to open OS-managed resources.

```text
Process
└── FD Table
     ├── 0 → stdin
     ├── 1 → stdout
     ├── 2 → stderr
     ├── 3 → file
     ├── 4 → socket
     └── 5 → pipe
```

## 8. Network Connections

Backend processes can maintain many network connections.

```text
Network connection
       ↓
Socket
       ↓
File descriptor
```

An AI application may communicate with clients, databases, LLM APIs, and vector databases.

## 9. IPC Resources

Processes sometimes need to communicate using IPC mechanisms such as:
- Shared memory
- Pipes
- Other OS IPC mechanisms

## 10. Resource Limits

A process cannot necessarily consume unlimited resources. The OS can impose limits on:
- CPU
- Memory
- Open file descriptors
- Processes/threads
- Other OS resources

Example:

```text
Too many open sockets
        ↓
FD limit reached
        ↓
New connection fails
```

## 11. Process Termination

When a process exits, the OS generally cleans up resources associated with it.

```text
Process exits
     ↓
OS cleanup
     ├── Memory released
     ├── File descriptors closed
     ├── Resources released
     └── Process removed
```

## 12. Why It Matters for AI Engineering

A typical AI request may involve:

```text
User Request
     ↓
FastAPI
     ↓
Retrieve documents
     ↓
Vector DB
     ↓
Embedding model
     ↓
LLM
     ↓
Response
```

These operations consume combinations of:

**CPU + memory + threads + network/file resources.**

Understanding process resources helps explain:
- Memory usage
- CPU usage
- Worker scaling
- Connection limits
- Resource leaks
- Multi-process behavior
- Production deployment problems

## 13. Program vs Process

A **program** is a passive set of instructions.

A **process** is a running instance of a program with execution state and allocated resources.

```text
Program
┌──────────────────┐
│ FastAPI code     │
└──────────────────┘
        │
        ↓ executed
Process
┌──────────────────────────┐
│ Code                     │
│ CPU state                │
│ Virtual memory           │
│ Heap                     │
│ Stack                    │
│ Threads                  │
│ File descriptors         │
│ Network connections      │
│ Other resources          │
└──────────────────────────┘
```

## 14. Complete Process Mental Model

```text
                         PROCESS
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ↓                 ↓                 ↓
        CPU              MEMORY            THREADS
          │                 │                 │
    Scheduling        Virtual Memory    Thread A/B/C
    Registers         Stack / Heap       Own stacks
    Program Counter   Shared Memory      Shared heap
          │                 │
          └────────┬────────┘
                   │
                   ↓
              I/O RESOURCES
                   │
          ┌────────┼────────┐
          ↓        ↓        ↓
        Files    Sockets   Pipes
          │        │        │
          └────────┼────────┘
                   ↓
          File Descriptors
```

## 15. Key Points

1. A process needs resources to execute.
2. Major resources include CPU, memory, threads, files, file descriptors, network connections, and IPC resources.
3. The OS manages these resources.
4. Each process has its own virtual memory context.
5. A process can contain multiple threads.
6. Threads have their own execution state but share much of the process's memory.
7. File descriptors provide process-level handles to OS-managed I/O resources.
8. Processes have resource limits.
9. Resource management is important for reliable production systems.
10. When a process terminates, the OS generally cleans up its associated resources.

## 16. Key Mental Model

> **A process is a running program together with the CPU state, memory, threads, I/O handles, and other resources required to execute it.**

## 17. Connection to the AI Journey

```text
AI Application
      ↓
Backend Process
      ↓
CPU + Memory + Threads + I/O
      ↓
Operating System
      ↓
Hardware
```

Understanding this foundation will make later topics such as **FastAPI, async I/O, multiprocessing, Docker, Linux, model serving, RAG systems, and production AI systems** much easier to reason about.
