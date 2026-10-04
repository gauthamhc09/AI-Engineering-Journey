# 00.2.18 — Memory Isolation

## 1. What is Memory Isolation?

Memory isolation is the OS mechanism that prevents one process from directly accessing or modifying another process's private memory.

```text
Process A                  Process B
┌──────────────┐          ┌──────────────┐
│ Code         │          │ Code         │
│ Heap         │          │ Heap         │
│ Stack        │          │ Stack        │
└──────────────┘          └──────────────┘
      │                         │
      └──── cannot directly access ────┘
```

More precisely:

> Each process is restricted to the memory regions that the OS has permitted it to access.

## 2. Why Do We Need It?

Without memory isolation, one process could potentially:

- Read another process's data.
- Modify another process's memory.
- Corrupt another process.
- Access information it should not have access to.

Memory isolation improves:

- Reliability
- Security
- Stability
- Process independence

## 3. How Does the OS Achieve It?

Memory isolation is closely connected to virtual memory.

Each process has its own virtual address space and memory mappings.

```text
Process A
   ↓
Virtual Address
   ↓
Process A's mappings
   ↓
Allowed physical memory

Process B
   ↓
Virtual Address
   ↓
Process B's mappings
   ↓
Allowed physical memory
```

The OS controls these mappings and permissions.

## 4. Same Virtual Address

Two processes can use the same virtual address, such as `0x5000`, without accessing the same memory.

```text
Process A                    Process B

0x5000                       0x5000
   │                            │
   ↓                            ↓
Page Table A                Page Table B
   │                            │
   ↓                            ↓
Frame 10                    Frame 25
```

The address spaces are separate.

## 5. What Happens With Forbidden Memory Access?

If a process tries to access memory that is not mapped or does not have the required permission, the memory-management hardware detects the invalid access and the OS handles the resulting fault.

This can result in the process being terminated.

A common example is:

```text
Segmentation fault
```

## 6. Memory Permissions

Memory regions can have different permissions.

For example:

```text
Readable     ✅
Writable     ❌
Executable   ❌
```

Or:

```text
Readable     ✅
Writable     ✅
Executable   ❌
```

The OS and hardware use these permissions as part of memory protection.

## 7. Memory Isolation and Shared Memory

Memory isolation does not mean that processes can never share memory.

It means:

> Processes cannot access each other's private memory unless the OS deliberately permits the access.

For shared memory:

```text
Process A ──┐
            ↓
       Shared Region
            ↑
Process B ──┘
```

The OS deliberately maps the shared region into the selected processes.

Therefore:

**Shared memory is controlled sharing, not a failure of isolation.**

## 8. Processes vs Threads

### Processes

Separate processes normally have separate virtual address spaces:

```text
Process A → Memory A
Process B → Memory B
```

They need IPC mechanisms to communicate.

### Threads

Threads within the same process share the process's address space:

```text
Process
├── Thread A ──┐
├── Thread B ──┼── Shared process memory
└── Thread C ──┘
```

This is why shared data between threads can create race conditions.

## 9. Why It Matters for AI Engineering

When running an AI/backend system with multiple workers:

```text
FastAPI
   │
   ├── Worker 1
   ├── Worker 2
   └── Worker 3
```

Each worker is typically a separate process with its own virtual address space.

Memory isolation helps prevent one worker from casually corrupting another worker's private memory.

This is useful for:

- Backend workers
- Background processes
- Model-serving processes
- AI services
- Multi-process applications

## 10. Key Points

1. Processes normally have separate virtual address spaces.
2. The OS and hardware enforce memory protection.
3. A process cannot normally access another process's private memory.
4. Memory pages can have access permissions such as read/write/execute.
5. Invalid memory access can cause a memory fault such as a segmentation fault.
6. Shared memory is deliberate, controlled sharing.
7. Threads within the same process share the process's address space.

## 11. Key Mental Model

```text
Virtual Memory
      ↓
Each process gets its own
virtual address space
      ↓
Page Tables + Permissions
      ↓
Memory Isolation
      ↓
Processes cannot normally
access each other's private memory
      ↓
OS can deliberately create
shared mappings
      ↓
Shared Memory
```

> Memory isolation protects each process's private memory, while the OS can deliberately allow controlled sharing when required.
