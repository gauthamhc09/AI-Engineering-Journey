# Module 00.2.4 — System Calls

## Core Idea
A system call is a controlled mechanism through which a user-space program requests a service from the operating-system kernel.

## Why System Calls Exist
Applications run with restricted privileges, but they still need OS-managed services such as file I/O, networking, process management, device access, and waiting for OS-managed events.

The problem is:

> How can a user-space program safely request a service from the privileged kernel?

The answer is: **system calls**.

## Mental Model
```text
USER SPACE
Application
    |
    | System Call
    v
KERNEL SPACE
Kernel
    |
    v
OS-managed resource/service
```

## System Call vs Python Function
Do not equate a Python API with a system call.

For example:

```python
open("data.txt")
```

`open()` is a Python API/function. Its implementation can ultimately request an OS file service through one or more system calls.

Conceptually:

```text
Python code
    |
    v
Python API
    |
    v
Python runtime / library machinery
    |
    v
OS interface
    |
    v
System call
    |
    v
Kernel
```

Exact implementation details vary by OS and runtime.

## Normal Function Call vs System Call
A normal function call can remain inside user-space execution:

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

Conceptually:

```text
Program -> function call -> user-space code -> CPU
```

A system call requests a privileged OS service:

```text
User-space application
        |
        v
System-call mechanism
        |
        v
Kernel
        |
        v
OS service/resource
```

## File Example
For:

```python
f = open("data.txt")
data = f.read()
```

a simplified conceptual path is:

```text
Python program
      |
      v
Python file API
      |
      v
OS interface
      |
      v
System call(s)
      |
      v
Kernel
      |
      v
Filesystem / storage subsystem
      |
      v
Storage, if needed
```

Important: a file operation does not necessarily mean the physical SSD is accessed every time. The OS/filesystem can satisfy operations using memory caches or other mechanisms.

## What Happens During a System Call?
1. The user-space program executes.
2. It needs an OS-managed service.
3. The runtime/library uses the system-call mechanism.
4. CPU-supported mechanisms allow controlled entry into privileged kernel execution.
5. The kernel validates and handles the request.
6. The kernel returns a result or error and control returns to user space.

Conceptually:

```text
USER SPACE
    |
    | request
    v
KERNEL SPACE
    |
    | perform service
    v
KERNEL SPACE
    |
    | result
    v
USER SPACE
```

A system call does not mean the application freely promotes itself to kernel privilege.

## The CPU Is Still Involved
The kernel is software. The CPU executes kernel instructions just as it executes application instructions.

```text
CPU
 |
 +--> user-space instructions
 |
 +--> kernel instructions
```

There is no separate "kernel CPU." The difference is the privilege level and access rights under which instructions execute.

## Examples of OS Services
Exact system-call interfaces differ between operating systems. Conceptually, system calls support:

| Requirement | OS service |
|---|---|
| Open a file | Filesystem service |
| Read/write a file | File I/O |
| Create/manage processes | Process management |
| Network communication | Networking |
| Wait for events | OS scheduling/I/O mechanisms |
| Device access | Device management |
| OS-managed memory | Memory-management mechanisms |

On Linux/Unix systems you may encounter names such as `read`, `write`, `openat`, `socket`, and `execve`. Do not memorize these yet; understand the mechanism first.

## System Calls Are Not Needed for Every Python Operation
For:

```python
x = 10
y = 20
z = x + y
```

there is no inherent need for a system call.

```text
Python program
     |
     v
User-space execution
     |
     v
CPU
     |
     v
Computation
```

By contrast, an operation involving an OS-managed resource can require system call(s).

Useful distinction:

```text
Pure computation
      |
      v
Usually stays in user space

OS-managed service/resource
      |
      v
May require system call(s)
```

## Why Applications Do Not Directly Access Hardware
If applications could freely control hardware, programs could interfere with each other, violate isolation, compromise security, and each need to understand hardware-specific details.

Instead:

```text
Application
    |
System Call
    |
Kernel
    |
Hardware / OS-managed resource
```

The OS provides controlled abstractions.

## Networking Example
An AI application might execute:

```python
response = requests.get(url)
```

Conceptually:

```text
AI application
      |
      v
Python HTTP library
      |
      v
Networking APIs
      |
      v
System call(s)
      |
      v
Kernel networking subsystem
      |
      v
Network interface
      |
      v
Internet
      |
      v
Remote server
```

This is directly relevant to LLM API calls, vector-database queries, database connections, and other network I/O.

## AI Engineering Connection
A RAG application may look like:

```text
User question
    ↓
FastAPI application
    ↓
Embedding model/API
    ↓
Vector database
    ↓
Retrieved documents
    ↓
LLM API
    ↓
Response
```

The Python application is a user-space process. Network communication and other OS-managed operations rely on kernel facilities and, where appropriate, system calls.

Understanding this foundation will help later with:

- processes
- threads
- blocking I/O
- async I/O
- sockets
- file descriptors
- production performance

## Common Mistakes
1. **Every Python operation is a system call.** No; ordinary computation can remain in user space.
2. **`open()` is itself a system call.** No; it is a Python API that can ultimately involve system calls.
3. **A system call creates kernel space.** No; kernel space already exists.
4. **The kernel is hardware.** No; it is privileged software executed by the CPU.
5. **Every file operation physically accesses the SSD.** No; caches can satisfy operations.
6. **System calls are just normal function calls.** No; they use a controlled OS/hardware mechanism to request privileged services.

## Key Takeaways
1. A system call is a controlled mechanism for a user-space program to request a kernel service.
2. System calls exist because applications operate with restricted privileges.
3. A Python API is not necessarily the same thing as the underlying system call.
4. `open()` is a Python API that can ultimately involve system calls.
5. Normal computation such as `x + y` does not inherently require a system call.
6. File, network, process, and device operations can require kernel services.
7. The CPU executes both user-space and kernel-space instructions.
8. A system call does not create kernel space.
9. System calls provide controlled access to OS-managed resources.
10. System calls are foundational for understanding processes, threads, networking, I/O, and async programming.

## Revision Questions
1. What is a system call?
2. Why do system calls exist?
3. What is the difference between a Python API and a system call?
4. Is `open()` itself a system call?
5. Why can `x + y` execute without a system call?
6. Describe the conceptual path of `open("data.txt")`.
7. What happens when a system call transitions into kernel execution?
8. Why cannot applications simply access hardware directly?
9. Does every file operation necessarily access the physical SSD?
10. How can system calls be involved when an AI application calls an external LLM API?
11. Why is understanding system calls useful for learning threads and async I/O?

## Connection to the Next Concept
We have established:

```text
Application
    ↓
User Space
    ↓
System Call
    ↓
Kernel
    ↓
OS-managed resources
```

The next question is:

> **What does the operating system consider a running program?**

This leads to **Module 00.2.5 — Processes**.
