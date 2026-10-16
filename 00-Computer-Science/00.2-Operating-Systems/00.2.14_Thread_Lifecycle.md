# Module 00.2.14 — Thread Lifecycle

## Overview
A simplified thread lifecycle is:
```text
NEW
 ↓
READY
 ↓
RUNNING
 ├──→ WAITING → READY
 ├──→ READY
 └──→ TERMINATED
```
Actual operating systems use more detailed state models.

## NEW
```python
import threading

def work():
    print("Working")

t = threading.Thread(target=work)
```

The thread object exists, but the target function has not started executing.

## `start()`
```python
t.start()
```

Conceptually:
```text
start()
  ↓
READY
  ↓
Scheduler
  ↓
RUNNING
```

`start()` does not guarantee immediate CPU execution.

## READY
A READY thread can execute but is currently waiting for CPU execution.

## RUNNING
A RUNNING thread's instructions are actually being executed by a CPU execution resource.

## RUNNING → READY
A running thread can be preempted:
```text
RUNNING → READY
```
The thread remains alive. Another runnable thread may receive CPU execution.

## RUNNING → WAITING
A thread can wait for a network response, file I/O, database response, lock, another thread, timer/sleep condition, or other event.

## READY vs WAITING
**READY:** “I can run, but I don't currently have CPU time.”

**WAITING:** “I cannot continue until something happens.”

## WAITING → READY
When the required event occurs:
```text
WAITING
   ↓
event occurs
   ↓
READY
   ↓
scheduler selects it
   ↓
RUNNING
```

WAITING does not automatically become RUNNING.

## RUNNING → TERMINATED
When the target function finishes:
```text
RUNNING → TERMINATED
```

## Complete Example
```python
import threading
import time

def work():
    print("Start")
    time.sleep(5)
    print("Finish")

t = threading.Thread(target=work)
t.start()
```

Conceptually:
```text
NEW → READY → RUNNING → WAITING → READY → RUNNING → TERMINATED
```

The CPU does not continuously execute this thread during the sleep interval.

## Multiple Threads Can Have Different States
```text
Process P
├── Thread A → RUNNING
├── Thread B → READY
└── Thread C → WAITING
```

On a multicore system, multiple threads can be RUNNING simultaneously if sufficient CPU execution resources are available.

## Context Switching
```text
Thread A → RUNNING
Thread B → READY
        ↓
Save A context
        ↓
A → READY
        ↓
Restore B context
        ↓
B → RUNNING
```

Preemption and context switching are related but not identical:
- Preemption = taking CPU execution away from a running thread.
- Context switch = changing the active execution context.

## Python `join()`
```python
t.start()
t.join()
```

`join()` means the calling thread waits for the target thread to finish.

## Backend / AI Engineering Connection
A backend process may contain:
```text
AI API Process
├── Thread A → CPU processing
├── Thread B → waiting for DB
├── Thread C → waiting for HTTP/LLM API
└── Thread D → READY
```

This helps reason about CPU-bound vs I/O-bound work, runnable threads, waiting threads, CPU utilization, scheduling, contention, and latency.

## Key Mental Model
```text
CREATE
  ↓
NEW
  ↓ start
READY
  ↓ scheduler
RUNNING
  ├── preempted → READY
  ├── blocked → WAITING → READY
  └── finished → TERMINATED
```

## Revision Questions
1. What happens when a thread is created but `start()` has not been called?
2. Does `start()` guarantee immediate CPU execution?
3. What causes READY → RUNNING?
4. What can cause RUNNING → READY?
5. What can cause RUNNING → WAITING?
6. Why does WAITING → READY happen?
7. Why doesn't WAITING immediately become RUNNING?
8. What happens when a thread's target function finishes?
9. Can multiple threads be RUNNING simultaneously?
10. How does `join()` affect the calling thread?
11. How does thread lifecycle relate to context switching?
12. Explain the complete lifecycle of a thread that performs `time.sleep(5)`.
