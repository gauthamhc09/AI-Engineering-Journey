# Module 00.2.10 — Process Scheduling

## Why scheduling exists
CPU capacity is limited. For example:
```text
4 CPU cores
100 READY processes
```
The OS must decide which runnable work receives CPU execution time.

This overall activity is **process scheduling**.

## Scheduler
The scheduler is the OS component responsible for deciding which runnable process/thread should receive CPU execution time.

```text
READY PROCESSES
      ↓
  SCHEDULER
      ↓
CPU execution
      ↓
RUNNING
```

## Scheduling goals
Policies can consider:
- **Fairness:** avoid indefinite CPU monopolization.
- **Responsiveness:** keep interactive workloads responsive.
- **CPU utilization:** use available CPU capacity effectively.
- **Throughput:** complete useful work efficiently.
- **Priorities:** give different workloads different scheduling treatment.

These goals can conflict.

## READY is central
A READY process is capable of running but waiting for CPU time.

A WAITING process is not currently runnable because it is waiting for an event/resource.

Example:
```text
A → RUNNING
B → READY
C → READY
D → WAITING
```
If a CPU slot becomes available, B or C are candidates; D is not.

## What can happen to a running process?
- Finishes: `RUNNING → TERMINATED`
- Blocks: `RUNNING → WAITING`
- Is preempted: `RUNNING → READY`

## Scheduling example
```text
2 CPU cores
A B → RUNNING
C D → READY
```
If A is preempted:
```text
A → READY
C → RUNNING
```

## CPU cores vs scheduler
Hardware provides execution capacity. The scheduler decides how runnable work uses that capacity.

> CPU cores provide execution capacity; the scheduler allocates runnable work to that capacity.

## Process scheduling vs CPU scheduling
For this course:

**00.2.10 Process Scheduling** focuses on the overall model:
```text
Processes → READY → Scheduler → CPU → WAITING/READY/TERMINATED
```

**00.2.11 CPU Scheduling** will go deeper into:
- time slices
- preemptive vs non-preemptive scheduling
- priorities
- scheduling algorithms
- fairness
- responsiveness
- trade-offs

## Python connection
```python
from multiprocessing import Process
```
creates processes through a Python abstraction. Python does not normally control exact CPU allocation; the OS scheduler does.

## AI Engineering connection
A production AI backend may have API workers, background workers, model/embedding workloads, database-related work, and other system processes competing for CPU resources.

I/O-heavy applications may frequently alternate:
```text
RUNNING ↔ WAITING
```

CPU-heavy workloads may consume substantial CPU execution time.

## Common mistakes
- READY does not mean currently running.
- WAITING does not mean waiting for CPU.
- Preemption is RUNNING → READY, not RUNNING → WAITING.
- A process does not literally “move into the CPU”; the CPU executes its instructions.
- Concurrent progress does not mean every process executes simultaneously at one instant.

## Key mental model
```text
READY
  ↓
SCHEDULER
  ↓
RUNNING
  ├──→ READY       (preemption)
  ├──→ WAITING     (blocked)
  └──→ TERMINATED  (finished)
```

## Revision questions
1. Why is process scheduling necessary?
2. What does the scheduler decide?
3. Why is a WAITING process not normally a scheduling candidate?
4. What happens when a process is preempted?
5. With 2 cores and 10 READY processes, can all 10 execute simultaneously at one instant?
6. Explain RUNNING → WAITING → READY → RUNNING using a database/network example.
