# Module 00.2.11 — CPU Scheduling

## 1. Why CPU Scheduling Exists

A computer may have many runnable processes and threads but only a limited number of CPU execution resources.

For example:

- 4 CPU cores
- 100 runnable processes

The OS must decide which runnable execution unit should get CPU time, and when.

This is the problem of **CPU scheduling**.

## 2. What Is CPU Scheduling?

CPU scheduling is the OS mechanism for deciding:

- which runnable process/thread should execute,
- when it should execute,
- how long it may continue executing,
- whether the currently running execution unit should be interrupted.

The scheduler works primarily with **runnable** execution units.

**READY:** Can execute, but is waiting for CPU time.

**WAITING/BLOCKED:** Cannot continue until some event or resource becomes available.

Therefore, a process waiting for network data is generally not a candidate for CPU scheduling until the required event occurs.

## 3. Scheduler vs CPU

The scheduler does not execute application instructions itself.

```text
Runnable processes/threads
          ↓
      Scheduler
          ↓
    "Who should run?"
          ↓
       CPU core
          ↓
Application instructions execute
```

The scheduler makes the allocation decision; the CPU performs the execution.

## 4. Preemptive Scheduling

In **preemptive scheduling**, the OS can interrupt a currently running process/thread and allow another runnable execution unit to run.

```text
Process A → RUNNING
            ↓
       preempted
            ↓
Process A → READY

Process B → RUNNING
```

This prevents one CPU-intensive process from indefinitely monopolizing a CPU.

Modern general-purpose operating systems use preemptive scheduling.

## 5. Non-Preemptive Scheduling

In **non-preemptive scheduling**, the OS does not forcibly take the CPU away from a running process/thread.

The current execution can continue until it:

- finishes,
- blocks/waits,
- or otherwise voluntarily gives up execution.

General-purpose modern OSs rely heavily on preemption for responsiveness.

## 6. Time Slice / Time Quantum

A **time slice** (or time quantum) is a bounded amount of CPU execution time that a runnable process/thread may receive before the scheduler may reconsider what should run.

```text
A → CPU → time slice
B → CPU → time slice
C → CPU → time slice
A → CPU → ...
```

Real scheduling is more sophisticated and can account for priorities, workload characteristics, fairness, and other factors.

## 7. Why Preemption Matters

Without preemption, a CPU-bound process could potentially keep the CPU for a very long time.

```python
while True:
    calculate_something()
```

Preemption allows the OS to maintain responsiveness by switching CPU execution among runnable work.

## 8. Concurrency vs Parallelism

**Concurrency:** Multiple tasks make progress during overlapping periods. With one core:

```text
A → B → A → C → B → A
```

Only one execution occurs at an instant, but multiple tasks can make progress over time.

**Parallelism:** Multiple tasks execute simultaneously using separate hardware execution resources.

```text
Core 1 → Process A
Core 2 → Process B
Core 3 → Process C
Core 4 → Process D
```

So:

> Concurrency = dealing with multiple tasks in overlapping time.

> Parallelism = actual simultaneous execution.

## 9. Classic Scheduling Strategies

### FCFS — First-Come, First-Served

The process that becomes ready first is considered first. It is simple, but a long CPU-bound process at the front can make shorter tasks wait. This can produce the **convoy effect**.

### SJF — Shortest Job First

The scheduler prefers the process expected to require the shortest CPU burst.

```text
A = 10 ms
B = 2 ms
C = 4 ms
```

A shortest-job-first ordering could be:

```text
B → C → A
```

Potential benefit: short jobs finish sooner and average waiting time can be reduced under suitable assumptions.

In real systems, the OS generally cannot know the exact future CPU burst.

### Priority Scheduling

Runnable tasks can have different priorities. Higher-priority work may receive CPU preference.

Potential problem: **starvation**.

## 10. Starvation

**Starvation** occurs when a runnable process/thread is repeatedly denied the CPU or another required resource for an excessively long period because other work is continually favored.

A starving READY process is capable of running but is repeatedly not selected.

## 11. CPU-Bound vs I/O-Bound Work

### CPU-bound

A task spends much of its time performing computation.

Examples:

- large numerical calculations,
- local model computation,
- image processing,
- CPU-heavy parsing.

### I/O-bound

A task frequently waits for external operations.

```text
RUNNING
   ↓
WAITING for network/database/file
   ↓
READY
   ↓
RUNNING
```

Examples:

- HTTP requests,
- database queries,
- reading from storage,
- waiting for network responses.

This distinction becomes important in backend and AI engineering.

## 12. Scheduler vs Context Switch

**Scheduler:** "Who should run next?"

**Context switch:** The mechanism that changes the active execution context so another process/thread can execute.

```text
Scheduler:
"B should run."

       ↓

Context switch:
Save A's context
Restore B's context

       ↓

B executes
```

## 13. Python Connection

```python
from multiprocessing import Process

p = Process(target=work)
p.start()
```

Python creates the process abstraction, but the OS ultimately manages the process and its CPU scheduling.

Conceptually:

```text
Python
  ↓
multiprocessing.Process
  ↓
OS process
  ↓
READY
  ↓
CPU scheduler
  ↓
RUNNING
  ↓
CPU
```

Python does not directly decide which CPU core gets the process at each scheduling point.

## 14. Backend / AI Engineering Connection

A FastAPI service may alternate between CPU work and I/O waits.

```text
Python execution
      ↓
Network request
      ↓
WAITING
      ↓
Other runnable work can execute
      ↓
Response arrives
      ↓
READY
      ↓
Scheduler
      ↓
RUNNING
```

For AI systems, this helps explain CPU-heavy work, network-heavy work, worker counts, scheduling overhead, and latency/throughput tradeoffs.

## 15. Key Mental Model

```text
READY
  ↓
Scheduler chooses
  ↓
RUNNING
  ├── finishes → TERMINATED
  ├── blocks → WAITING
  └── preempted → READY
```

And:

```text
Scheduler = decides who should run
Context switch = changes execution context
CPU = executes instructions
```

## 16. Common Mistakes

- **WAITING means waiting for CPU:** Incorrect. It means waiting for an event/resource.
- **Preemption means termination:** Incorrect. A preempted process normally remains alive and becomes READY.
- **Concurrency means simultaneous execution:** Not necessarily.
- **Scheduler executes the process:** Incorrect. The CPU executes instructions.
- **Every process gets exactly equal CPU time:** Incorrect. Policies can account for priorities and other factors.

## 17. Revision Questions

1. Why does an OS need CPU scheduling?
2. What is the difference between READY and WAITING?
3. What is preemptive scheduling?
4. Why is preemption useful?
5. What is a time slice?
6. Explain concurrency vs parallelism.
7. What is starvation?
8. Compare FCFS, SJF, and priority scheduling.
9. What is the difference between CPU-bound and I/O-bound work?
10. Explain the difference between a scheduler and a context switch.
11. What happens to a process when it is preempted?
12. How does CPU scheduling relate to Python `multiprocessing.Process`?

## 18. AI Engineering Connection

CPU scheduling becomes directly relevant when designing production AI systems containing API workers, background jobs, document processing, embedding generation, database clients, vector search, LLM API calls, and model inference.

Understanding CPU scheduling helps you reason about:

- worker counts,
- CPU saturation,
- responsiveness,
- background processing,
- process/thread contention,
- throughput,
- latency.

The goal is not to memorize scheduling algorithms. The goal is to understand how the OS shares finite CPU execution capacity among competing work.
