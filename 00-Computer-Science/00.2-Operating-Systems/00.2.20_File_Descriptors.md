# 00.2.20 — File Descriptors

## 1. What is a File Descriptor?
A **file descriptor (FD)** is a small integer/handle that a process uses to refer to an open OS-managed I/O resource.

Examples:
- Regular files
- Network sockets
- Pipes
- Standard input/output/error
- Other OS-managed I/O resources

> A file descriptor is a process-level handle used to interact with an OS-managed I/O resource.

## 2. Why Do We Need File Descriptors?
Applications do not directly manage hardware resources. They interact with the OS through system calls.

```text
Application
    ↓
System call
    ↓
Operating System
    ↓
OS-managed resource
```

Example:

```text
open("data.txt")
       ↓
OS opens the resource
       ↓
fd = 3
       ↓
read(3)
       ↓
OS reads from the associated resource
```

## 3. File Descriptor Table
Each process has a file descriptor table.

```text
Process
└── File Descriptor Table
       ├── 0 → stdin
       ├── 1 → stdout
       ├── 2 → stderr
       ├── 3 → file
       ├── 4 → pipe
       └── 5 → network socket
```

The integer itself does not contain the file or socket. It identifies an entry associated with the OS-managed resource.

## 4. Standard File Descriptors
On Unix/Linux systems:

```text
0 → stdin  → Standard Input
1 → stdout → Standard Output
2 → stderr → Standard Error
```

## 5. Opening and Closing Resources
Opening a resource causes the OS to provide a descriptor.

```text
open file A → fd 3
close file A

open file B → fd 3
```

The descriptor number can be reused; it is not permanently associated with one file.

## 6. Sockets
File descriptors are not limited to regular files. Network sockets are also OS-managed I/O resources.

```text
Client
   ↓
Network
   ↓
Socket
   ↓
fd = 5
   ↓
Application
```

For backend systems:

```text
HTTP connection
      ↓
TCP socket
      ↓
File descriptor
      ↓
OS I/O
      ↓
FastAPI / Uvicorn
```

## 7. Pipes and IPC
Pipes can also be represented using file descriptors.

```text
Process A
    │ write
    ↓
  Pipe
    │ read
    ↓
Process B
```

This connects file descriptors with IPC.

## 8. File Descriptor Leak
A **file descriptor leak** occurs when a program opens OS-managed resources but fails to close them when no longer needed.

```text
Request 1 → socket → fd 10 → never closed
Request 2 → socket → fd 11 → never closed
Request 3 → socket → fd 12 → never closed
...
```

Eventually the process may run out of available file descriptors and fail to open new files, sockets, or other resources.

## 9. Why It Matters for FastAPI / AI Applications
AI/backend applications may use:
- HTTP client connections
- Database connections
- Files
- Network sockets
- Pipes
- Other I/O resources

Understanding FDs helps explain:
- Too many open connections
- Connection/resource leaks
- Socket management
- Server scalability
- Async I/O
- Linux process behavior

## 10. Connection to Async
Async servers can manage many I/O connections.

```text
FastAPI / Uvicorn
       │
       ├── fd 10 → Client A
       ├── fd 11 → Client B
       ├── fd 12 → Client C
       └── fd 13 → Client D
```

Event-driven systems can monitor many file descriptors and react when I/O becomes ready.

You do not need `epoll`, `select`, or `kqueue` at this stage.

## 11. Key Points
1. A file descriptor is a small integer/handle used by a process to refer to an open OS-managed resource.
2. Each process has a file descriptor table.
3. `0` → stdin.
4. `1` → stdout.
5. `2` → stderr.
6. FDs can refer to files, sockets, pipes, and other I/O resources.
7. The integer itself does not contain the resource; it identifies an associated resource.
8. Descriptors can be reused after resources are closed.
9. Failing to close resources can cause FD leaks.
10. FDs are important for backend networking and asynchronous I/O.

## 12. Mental Model

```text
                 PROCESS
                    │
                    ↓
          File Descriptor Table
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
      0             1            2
    stdin         stdout       stderr

       3 ─────→ File
       4 ─────→ Pipe
       5 ─────→ Network Socket
```

> A file descriptor is a process-level handle that lets a program interact with an OS-managed I/O resource such as a file, socket, or pipe.
