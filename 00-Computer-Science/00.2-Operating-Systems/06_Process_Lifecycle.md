# Module 00.2.6 — Process Lifecycle

## Why this concept matters
A process moves through different states during its lifetime rather than simply being “running” or “not running.”

## Simplified lifecycle
```text
NEW → READY → RUNNING
              ↙     ↘
          WAITING   TERMINATED
             ↓
           READY
```
A running process can also be preempted: `RUNNING → READY`.

## States
- **NEW:** process is being created and initialized.
- **READY:** capable of running but waiting for CPU time.
- **RUNNING:** CPU is currently executing its instructions.
- **WAITING/BLOCKED:** cannot continue until an event/resource becomes available.
- **TERMINATED:** execution has ended.

## Important transitions
- `READY → RUNNING`: scheduler selects it.
- `RUNNING → READY`: preemption; it can still run but temporarily loses CPU time.
- `RUNNING → WAITING`: it needs an event/resource such as network or disk I/O.
- `WAITING → READY`: the event occurs; it becomes runnable again.
- `RUNNING → TERMINATED`: execution finishes or the process is terminated.

## Python example
```python
import time
print("Start")
time.sleep(5)
print("End")
```

Conceptually:
```text
RUNNING → WAITING → READY → RUNNING → TERMINATED
```

For a single-threaded process, `sleep()` causes its executing thread to sleep; at this level, describing the process as waiting is a useful simplification.

## Backend / AI connection
A FastAPI or RAG process may repeatedly alternate between CPU execution and waiting for a database, vector DB, network service, or LLM API.

## Key mental model
- READY: “I can run, but I need CPU time.”
- RUNNING: “I am currently executing.”
- WAITING: “I cannot continue until something happens.”
- TERMINATED: “My execution has ended.”

## Common mistake
Do not confuse:
- `RUNNING → READY` = preemption
- `RUNNING → WAITING` = blocking/waiting

## Revision questions
1. What is the difference between READY and WAITING?
2. Why does WAITING normally transition to READY rather than directly to RUNNING?
3. What happens when a running process is preempted?
4. Trace `time.sleep(5)` through the lifecycle.
5. Give a backend example of RUNNING → WAITING → READY → RUNNING.
