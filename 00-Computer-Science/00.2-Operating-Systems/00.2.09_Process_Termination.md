# Module 00.2.9 — Process Termination

## Fundamental idea
Process termination is when a process finishes execution and the OS begins finalizing and reclaiming resources associated with it.

```text
RUNNING → TERMINATED
```

## Causes
### Normal completion
The program reaches the end of execution.

### Explicit termination
For example:
```python
import sys
sys.exit()
```

### External termination
A user, administrator, another process, service manager, or OS mechanism may request termination. Exact mechanisms depend on the OS.

## Resource cleanup
A process may have memory/address-space resources, open files, execution state, and other OS-managed resources. The OS generally reclaims/releases resources associated with a terminated process.

## Exit status
A process can terminate with an exit status. Conventionally:
- `0` → success
- non-zero → some kind of error/failure

The exact meaning of non-zero values depends on the program.

## Zombie process
On Unix/Linux-like systems, a terminated child can temporarily retain limited termination information until its parent collects the exit status.

A terminated child whose termination status has not yet been collected is called a **zombie process**.

A zombie is **not executing**.

## Python exception vs process termination
An exception is a Python/runtime-level event. Process termination is an OS-level lifecycle event.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Handled")

print("Program continues")
```

The process continues because the exception is handled.

Therefore:
> Exception ≠ Process termination

An unhandled exception can cause a Python process to terminate.

## Backend / AI connection
A FastAPI worker can terminate because of shutdown, deployment/restart, container stop, fatal error, or external termination. Production systems can detect termination and start replacement workers.

## Key mental model
1. Termination means execution has ended.
2. The OS reclaims/releases process resources.
3. Termination can be normal or abnormal.
4. Exceptions and process termination are different levels of abstraction.
5. A zombie has terminated but may retain limited bookkeeping temporarily.

## Revision questions
1. What happens when a program reaches the end of execution?
2. Difference between WAITING and TERMINATED?
3. Can a handled exception terminate the process?
4. What happens to process resources after termination?
5. What is a zombie process?
