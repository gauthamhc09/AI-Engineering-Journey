# Module 00.2.8 — Process Creation

## Fundamental idea
A **program** is passive code/instructions. A **process** is an OS-managed execution instance of a program.

```text
Program → process creation → Process
```

When you run:
```bash
python app.py
```
the OS/runtime establishes a process environment in which the program can execute.

Conceptually:
```text
python app.py
  ↓
process creation
  ↓
process environment established
  ↓
READY
  ↓
scheduler
  ↓
RUNNING
  ↓
CPU executes instructions
```

## What the OS establishes/manages
- **Process identity:** e.g. PID.
- **Address space:** virtual memory environment.
- **Execution context:** information required to manage execution.
- **Resources and bookkeeping:** state, scheduling information, memory information, open resources, security information.

The **Process Control Block (PCB)** is a conceptual OS data structure containing process-management information.

## Creation does not mean immediate execution
A new process generally becomes runnable first:
```text
Process created → READY → Scheduler → RUNNING
```

## One program, multiple processes
Running `python app.py` three separate times creates three process instances of the same program.

## Unix/Linux concepts
Unix-like systems have mechanisms such as `fork()` and `exec()`. At this stage:
- `fork()` creates a new process based on an existing process.
- `exec()` replaces the current process's program/execution image with another program.

## Python connection
```python
from multiprocessing import Process

def work():
    print("Working")

p = Process(target=work)
p.start()
```

Conceptually:
```text
Python API → Python runtime → OS process mechanism
→ new process → READY → scheduler → CPU
```

## AI/backend connection
Production API systems may use multiple worker processes. If each worker loads a large AI model, memory requirements become an important deployment consideration.

## Key mental model
> A program is passive. A process is an OS-managed execution instance of that program.

## Revision questions
1. Difference between a program and a process?
2. What happens conceptually when `python app.py` is executed?
3. Why doesn't creation imply immediate CPU execution?
4. Can one program have multiple process instances?
5. What does `multiprocessing.Process` abstract?
