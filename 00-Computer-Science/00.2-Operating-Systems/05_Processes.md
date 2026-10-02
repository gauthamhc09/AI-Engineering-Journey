# Module 00.2.5 — Processes

## 1. Why This Concept Exists

When you run:

```bash
python app.py
```

from your perspective, you started a Python program.

But the operating system needs to manage much more than the program's source code. It needs to know:

- Which program is running?
- Where is its memory?
- What instructions is it executing?
- Which files/resources does it have open?
- What CPU time is it using?
- Is it running, waiting, or finished?
- How can the OS manage or terminate it?

The operating system represents a running instance of a program using a **process**.

---

## 2. Definition of a Process

A **process is an OS-managed running instance of a program, together with its execution context and associated resources.**

The key idea is:

> A program is passive code; a process is a running instance of that program being managed by the operating system.

Conceptually:

```text
PROGRAM
Passive code
     |
     | Execute
     v
PROCESS
Running instance
+ execution context
+ OS-managed resources
```

---

## 3. Program vs Process

### Program

A program is a set of instructions/code stored somewhere, such as on an SSD, HDD, or another storage medium.

It is passive until executed.

### Process

A process is a running instance of a program.

For example:

```bash
python app.py
```

`app.py` is the program/code.

The execution of that program results in a process being created and managed by the OS.

---

## 4. One Program Can Have Multiple Processes

Suppose:

```bash
python app.py
python app.py
python app.py
```

There is:

- 1 program
- 3 process instances

Conceptually:

```text
             app.py
          /     |     \
         v      v      v
    Process 1 Process 2 Process 3
```

Each process is separately managed by the OS and has its own execution context and associated resources.

This distinction becomes important for Python's `multiprocessing` and production application workers.

---

## 5. A Process Is More Than Just Code

A process includes more than the program instructions.

Conceptually:

```text
Process
├── Program/code
├── Virtual address space
├── CPU execution context
├── Process identity
├── Open files/resources
├── Execution state
└── Other OS-managed information
```

We will study these components separately in later OS concepts.

For now, the key idea is:

> A process is the OS-level entity representing a running program and the context/resources needed to manage that execution.

---

## 6. Process and CPU

A process is **not** a CPU.

A process is an OS-managed entity whose instructions can be executed by a CPU when the scheduler gives it CPU time.

Conceptually:

```text
Process
   |
   v
OS manages process
   |
   v
Scheduler selects runnable process
   |
   v
CPU executes its instructions
```

Prefer saying:

> "The CPU executes the process's instructions."

rather than:

> "The process goes to the CPU."

---

## 7. Multiple Processes and Multiple CPU Cores

Suppose a computer has:

**4 CPU cores**

and:

**10 runnable processes**

At one exact instant, up to 4 processes can actively execute instructions, assuming one hardware execution context per core.

Conceptually:

```text
        CPU
 ┌──────┬──────┬──────┬──────┐
 │Core 0│Core 1│Core 2│Core 3│
 │  P1  │  P2  │  P3  │  P4  │
 └──────┴──────┴──────┴──────┘

P5 P6 P7 P8 P9 P10
```

The remaining runnable processes are waiting for CPU execution time.

The scheduler can later select different processes:

```text
Time →

Core 0: P1 → P5 → P2 → P8 → ...
Core 1: P2 → P6 → P4 → P9 → ...
Core 2: P3 → P7 → P1 → P10 → ...
Core 3: P4 → P8 → P6 → P3 → ...
```

The OS creates the appearance of many programs running concurrently by scheduling runnable processes over time.

### Important distinction

> **10 processes can be runnable, but only up to 4 can be actively executing at one instant on 4 cores.**

This leads naturally into process scheduling and context switching.

---

## 8. Process Identity — PID

The OS needs a way to identify each process.

A process therefore has a **Process ID (PID)**.

Example:

```text
PID 4120 → Python application
PID 5321 → PostgreSQL
PID 7198 → Another process
```

In Python:

```python
import os

print(os.getpid())
```

Example output:

```text
18452
```

The exact value will vary.

The PID is an identifier that allows the OS and system mechanisms to refer to a particular process.

For example, on Unix/Linux:

```bash
kill 4120
```

refers to the process with PID 4120.

---

## 9. Why the PID Changes

Run:

```python
import os

print(os.getpid())
```

Then run the program again.

You may see:

```text
Process ID: 18231
```

and later:

```text
Process ID: 18274
```

The program is the same, but each execution creates a new process instance, which receives its own process identity.

Conceptually:

```text
Same program
     |
     +── Execution 1 → PID A
     |
     +── Execution 2 → PID B
     |
     +── Execution 3 → PID C
```

---

## 10. Process and Memory

Processes need memory.

The OS provides each process with a **virtual address space** and manages its access to memory.

Conceptually:

```text
Process A
   ↓
Virtual address space A

Process B
   ↓
Virtual address space B

Process C
   ↓
Virtual address space C
```

This contributes to process isolation.

A normal process should not simply be able to read or modify arbitrary memory belonging to another process.

Virtual memory and memory isolation will be studied later.

---

## 11. Process and OS Bookkeeping

The OS must maintain information about every process it manages.

Conceptually, this includes:

```text
Process
├── PID
├── Execution state
├── CPU scheduling information
├── Memory/address-space information
├── Open file/resource information
├── Identity/permissions
├── Resource usage
└── Other process metadata
```

Operating systems maintain internal data structures for this bookkeeping.

A common conceptual term is **Process Control Block (PCB)**.

Do not focus on implementation details yet.

The important idea is:

> The OS needs bookkeeping information to manage each process.

---

## 12. Python Connection

Python provides APIs such as:

```python
from multiprocessing import Process

def worker():
    print("Worker running")

p = Process(target=worker)
p.start()
p.join()
```

At the Python level, `Process` is an abstraction.

At the OS level, the conceptual flow is:

```text
Python multiprocessing API
          |
          v
OS process mechanism
          |
          v
New process
          |
          v
OS scheduler
          |
          v
CPU executes instructions
```

This is the important bridge:

> A Python process API ultimately relies on operating-system mechanisms to create and manage execution contexts.

The exact process-creation mechanism varies by operating system.

---

## 13. FastAPI / Backend Connection

Suppose you run:

```bash
uvicorn main:app
```

The application runs as part of an OS-managed process.

Conceptually:

```text
FastAPI application
        |
        v
Python runtime
        |
        v
OS process
        |
        +---- Memory
        +---- CPU execution
        +---- Network resources
        +---- Files/resources
```

If an architecture uses multiple worker processes:

```text
             FastAPI application
                    |
        ┌───────────┼───────────┐
        v           v           v
     Worker 1    Worker 2    Worker 3
     Process     Process     Process
```

These are separate OS-level processes.

This matters for memory consumption, CPU scheduling, isolation, and scaling.

---

## 14. AI Engineering Connection

Production AI systems often consist of processes such as:

```text
API server process
       |
       +---- Vector DB client/networking
       +---- Embedding/model work
       +---- Database connections
       +---- LLM API requests
```

A production architecture may have multiple worker processes:

```text
Server
  |
  +── API Worker 1
  +── API Worker 2
  +── API Worker 3
  +── Background Worker
```

Understanding processes helps explain:

- FastAPI workers
- model-serving processes
- memory usage
- CPU utilization
- process isolation
- Docker containers
- Kubernetes workloads
- production scaling

For example, if multiple worker processes each load a large model into their own memory, total memory consumption can become a major system-design consideration.

---

## 15. Important Mental Model

Do not think:

> "A process is the CPU."

Wrong.

Do not think:

> "A process is a piece of RAM."

Wrong.

Do not think:

> "A process is just the Python code."

Incomplete.

Use this model:

> **A process is an OS-managed running instance of a program, together with the execution context and resources associated with that instance.**

Then:

```text
Program
   |
   | Execute
   v
Process
   |
   | OS manages it
   v
Scheduler
   |
   | gives CPU execution time
   v
CPU core
   |
   v
Instructions execute
```

---

## 16. Important Terminology

| Term | Meaning |
|---|---|
| Program | Passive code/instructions |
| Process | Running instance managed by the OS |
| PID | Identifier for a process |
| Process state | Current condition of a process, such as runnable or waiting |
| Scheduler | OS component that decides which runnable execution entities receive CPU time |
| Virtual address space | Process-specific view of memory |
| Process isolation | Preventing one process from arbitrarily accessing another process's protected resources |

---

## 17. Common Mistakes

### Mistake 1
"A program and a process are the same thing."

**Correction:** A program is passive code; a process is a running instance managed by the OS.

### Mistake 2
"One program can only have one process."

**Correction:** The same program can have multiple simultaneous process instances.

### Mistake 3
"A process is the CPU."

**Correction:** The CPU executes instructions belonging to a process.

### Mistake 4
"A process is RAM."

**Correction:** A process has a virtual address space and uses memory, but it is not memory itself.

### Mistake 5
"All runnable processes execute simultaneously."

**Correction:** On 4 cores, at most 4 can actively execute at one instant assuming one hardware execution context per core. The scheduler gives others CPU time over time.

### Mistake 6
"The PID manages the process."

**Correction:** The PID identifies the process. The OS manages it.

### Mistake 7
"Calling Python's `Process()` is the same as understanding what an OS process is."

**Correction:** `multiprocessing.Process` is a Python abstraction over OS-level process mechanisms.

---

## 18. Key Takeaways

1. A **program** is passive code/instructions.
2. A **process** is an OS-managed running instance of a program.
3. One program can have multiple process instances.
4. Each process has its own identity, execution context, memory/address-space information, and associated resources.
5. A process has a **PID**.
6. The OS manages processes.
7. The scheduler decides which runnable processes receive CPU execution time.
8. The CPU executes instructions belonging to the selected process.
9. With 4 cores, only up to 4 processes can actively execute at one instant under the stated one-execution-context-per-core assumption.
10. Processes provide an important foundation for isolation, scheduling, multiprocessing, and production application architecture.

---

## 19. Revision Questions

1. What is a process?
2. What is the difference between a program and a process?
3. Can one program have multiple processes? Explain.
4. What is a PID?
5. Why does the PID change when the same Python program is run again?
6. Is a process the same thing as CPU or RAM?
7. What does the OS manage for a process?
8. What is the relationship between a process and the CPU?
9. What does the scheduler do?
10. If there are 100 runnable processes and 8 CPU cores, can all 100 execute instructions at exactly the same instant?
11. How does Python's `multiprocessing.Process` connect to the OS process concept?
12. Why does process knowledge matter when deploying FastAPI or AI applications?

---

## 20. Connection to the Next Concept

We now understand what a process is.

The next question is:

> **What happens to a process from the moment it is created until the moment it finishes?**

That leads to:

**00.2.6 — Process Lifecycle**

We will study the journey:

```text
Created
   ↓
Ready
   ↓
Running
   ↓
Waiting / Blocked
   ↓
Ready
   ↓
Running
   ↓
Terminated
```

We will not jump into scheduling details yet. First, we will understand the lifecycle of a process.
