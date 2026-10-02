# Module 00.2.7 — Process States

## Why process states exist
The OS needs to know whether a process can execute, is executing, is waiting, or has finished so it can schedule correctly.

A simplified model:
- NEW
- READY
- RUNNING
- WAITING / BLOCKED
- TERMINATED

Actual operating systems may have additional states and terminology.

## READY
A READY process can execute but is waiting for CPU time.

## RUNNING
A RUNNING process is currently having its instructions executed on a CPU execution context.

## WAITING / BLOCKED
A WAITING process cannot continue until an event/resource becomes available, such as:
- network response
- disk I/O
- user input
- timer
- synchronization event
- another process

## TERMINATED
The process has finished and is no longer runnable.

## Critical distinctions
**READY:** “I can run, but I need CPU time.”

**WAITING:** “I cannot continue yet; I need an event/resource.”

**Preemption:** `RUNNING → READY`

**Blocking:** `RUNNING → WAITING`

## Important transitions
```text
NEW → READY
READY → RUNNING
RUNNING → READY
RUNNING → WAITING
WAITING → READY
RUNNING → TERMINATED
```

Becoming READY does not guarantee immediate execution; the scheduler still has to select the process.

## Backend / AI connection
A backend request may follow:
```text
RUNNING → database request → WAITING
→ database response → READY → scheduler → RUNNING
```

## Key mental model
A state describes the process's current ability to execute.

## Revision questions
1. Define READY, RUNNING, WAITING, and TERMINATED.
2. Why is WAITING not a good CPU candidate?
3. Why does preemption move RUNNING → READY?
4. What causes WAITING → READY?
5. Why does READY not mean RUNNING immediately?
