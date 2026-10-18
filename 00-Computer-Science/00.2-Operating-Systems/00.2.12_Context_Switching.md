# Module 00.2.12 — Context Switching

## 1. Why Context Switching Exists

Suppose Process A is currently running:

```text
CPU → Process A
```

The scheduler decides that Process B should run instead.

The CPU cannot simply forget A and start B. When A runs again later, it must continue from the correct execution point with the correct CPU state.

Therefore, the system needs a mechanism to:

1. save A's execution state,
2. switch to B's execution state,
3. execute B,
4. later restore A's state so A can continue.

This is the basic idea of a **context switch**.

## 2. What Is a Context?

A **context** is the execution state needed to pause an execution unit and later resume it correctly.

Important parts include:

- **Program Counter (PC)** — address of the next instruction to execute,
- CPU registers,
- stack-related execution state,
- other architecture/OS-specific execution state.

## 3. Program Counter

The **Program Counter (PC)** is a CPU register that holds the address of the next instruction to execute.

For example:

```text
PC_A = address of instruction 500
```

This does NOT mean instruction 500 is the value. It means the CPU's next instruction should be fetched from that address.

## 4. Basic Context-Switch Sequence

Suppose A is running and B is READY.

1. A is running.
2. Scheduler decides B should run.
3. Save A's context.
4. A remains alive and, if preempted, generally becomes READY.
5. Restore B's context.
6. B runs.

```text
Process A
   ↓
RUNNING
   ↓
Save A context
   ↓
A → READY

Restore B context
   ↓
B → RUNNING
   ↓
CPU executes B
```

Later, A's context can be restored and A can continue.

## 5. A Process Does Not Restart

Suppose A was executing:

```text
step 498
step 499
step 500  ← interrupted around here
step 501
step 502
```

A context switch does NOT restart A from step 1.

The system preserves enough execution state so that A can later continue from its saved execution point.

## 6. PCB and Context

The **Process Control Block (PCB)** is a conceptual OS data structure containing process-management information.

It can include information related to:

- process identity,
- process state,
- scheduling information,
- resource information,
- saved execution state.

Do not think:

> PCB = the entire process memory.

The PCB is process-management metadata maintained by the OS. The process's actual memory/address space is a separate concept.

## 7. Why Context Switching Has a Cost

A context switch is not free.

The system must perform work to:

- save execution state,
- restore another execution state,
- update scheduling-related state,
- potentially interact with memory-management structures,
- resume execution.

There can also be secondary performance effects involving CPU caches and other hardware state.

Therefore:

> More context switching is not automatically better.

Too many switches can consume CPU time that could otherwise be spent doing useful application work.

## 8. Context Switch Between Processes

A process switch may require the OS to change from Process A's execution context to Process B's.

Because processes generally have separate virtual address spaces, switching processes can involve additional memory-management effects compared with switching between threads of the same process.

The exact cost is architecture- and OS-dependent.

## 9. Context Switch Between Threads

Context switching can also occur between threads.

```text
Thread A → RUNNING
Thread B → READY
```

The scheduler may select B, causing A's relevant execution state to be saved and B's state to be restored.

Threads within the same process share many process-level resources, so thread switching is conceptually related to process switching but is not identical.

The detailed differences will be covered when we study **Threads**.

## 10. Preemption vs Context Switching

These concepts are related but not synonyms.

**Preemption:** The OS takes CPU execution away from a currently running process/thread so another runnable execution unit can run.

```text
RUNNING → READY
```

**Context switch:** The system changes the CPU's active execution context.

```text
Save A
Restore B
```

Preemption can cause a context switch, but a context switch can also occur for other reasons, such as a running task blocking on I/O.

Example:

```text
A is RUNNING
   ↓
A waits for I/O
   ↓
A becomes WAITING
   ↓
OS can switch to B
```

So:

> Preemption is about taking CPU execution away.

> Context switching is about changing execution context.

## 11. Scheduler vs Context Switch

### Scheduler

Decides:

> "Who should run?"

### Context switch

Changes the active execution context so another execution unit can run.

```text
A is running

Scheduler:
"B should run."

       ↓

Context switch:
Save A
Restore B

       ↓

B runs
```

## 12. Python Connection

```python
import multiprocessing

p = multiprocessing.Process(target=work)
p.start()
```

Python requests creation of another process.

Once multiple processes are runnable, the OS scheduler determines when their execution gets CPU time.

Python does not manually perform the low-level CPU context switch.

Conceptually:

```text
Python
  ↓
OS processes
  ↓
READY
  ↓
Scheduler
  ↓
Context switch
  ↓
CPU executes selected process
```

## 13. Backend / AI Engineering Connection

Imagine a FastAPI service with multiple workers:

```text
Worker A
Worker B
Worker C
```

These may compete for CPU resources.

```text
Scheduler
    ↓
select execution context
    ↓
context switch if necessary
    ↓
CPU executes selected work
```

For AI workloads, excessive processes/threads can introduce:

- scheduling overhead,
- context-switch overhead,
- CPU contention,
- memory pressure.

For example, starting many workers that each load a large model can consume substantial memory even before CPU scheduling becomes the main bottleneck.

Understanding context switching therefore helps explain why:

> "More workers" does not automatically mean "more performance."

## 14. Context Switching and Waiting

Context switches do not happen only because of time-slice expiration.

Consider:

```text
Process A → RUNNING
             ↓
       waits for database
             ↓
         WAITING
             ↓
       scheduler can run B
             ↓
         B → RUNNING
```

Later:

```text
Database response arrives
        ↓
A → READY
        ↓
Scheduler selects A
        ↓
Context restored
        ↓
A → RUNNING
```

A can then continue using its preserved execution state.

## 15. Key Mental Model

Remember these three roles:

```text
Scheduler
    ↓
Decides who should run

Context Switch
    ↓
Changes CPU execution context

CPU
    ↓
Executes instructions
```

And:

```text
A RUNNING
   ↓
Save A context
   ↓
Restore B context
   ↓
B RUNNING
```

Later:

```text
Restore A context
   ↓
A RUNNING
   ↓
A continues from its saved execution point
```

## 16. Common Mistakes

- **Context switching terminates the process:** Incorrect. The process normally remains alive.
- **The process starts from the beginning after a context switch:** Incorrect. Its execution state is preserved.
- **The Program Counter stores the next value:** Incorrect. It stores the address of the next instruction.
- **Scheduler and context switch are the same:** Incorrect. Scheduler = decision; context switch = changing execution context.
- **Every context switch is caused by preemption:** Incorrect. Blocking/waiting and other events can also lead to a context switch.
- **PCB contains the entire process:** Incorrect. It contains process-management information; process memory is separate.

## 17. Revision Questions

1. What is a CPU execution context?
2. What information is commonly part of an execution context?
3. What is the Program Counter?
4. Why must the execution context be saved?
5. Explain a context switch from Process A to Process B.
6. What happens to Process A after it is preempted?
7. Why does a context switch have overhead?
8. What is the difference between preemption and context switching?
9. What is the difference between the scheduler and a context switch?
10. What is the role of the PCB?
11. Why is a PCB not the same thing as process memory?
12. Can a context switch happen when a process blocks on I/O?
13. Why can excessive context switching hurt performance?
14. How does this concept matter when running multiple backend/AI workers?

## 18. AI Engineering Connection

Context switching becomes important when moving from simple Python programs to production systems.

A production AI service may have:

```text
API workers
Background workers
Database operations
Vector search
Document processing
Model inference
Network requests
```

The OS must coordinate execution among these workloads.

Understanding context switching helps you reason about:

- CPU utilization,
- process/thread counts,
- worker configuration,
- latency,
- throughput,
- scheduling overhead,
- CPU contention.

This is foundational for understanding why a Python backend can behave very differently in production compared with a simple local script.
