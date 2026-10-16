# 00.2.16 — Shared Memory

## 1. What is Shared Memory?

Shared memory is an IPC (Inter-Process Communication) mechanism that allows two or more processes to access the same region of physical memory.

Normally, processes have separate address spaces:

```text
Process A                 Process B
┌──────────────┐          ┌──────────────┐
│ Code         │          │ Code         │
│ Heap         │          │ Heap         │
│ Stack        │          │ Stack        │
└──────────────┘          └──────────────┘
      │                         │
      └────── isolated ─────────┘
```

With shared memory, the OS deliberately maps a common memory region into multiple processes.

```text
Process A ──┐
            ↓
      Shared Memory
            ↑
Process B ──┘
```

## 2. Why is it IPC?

Processes are normally isolated and cannot directly access each other's private memory.

Shared memory provides a controlled way for processes to exchange data by reading and writing to a common memory region.

## 3. How Does It Work?

Each process still has its own virtual address space.

For example:

```text
Process A                 Process B
0x5000                    0x9000
   │                         │
   └──────────┬──────────────┘
              ↓
       Same physical page
```

The virtual addresses do not need to be the same. The OS can map both virtual addresses to the same physical memory pages.

## 4. Why is Shared Memory Efficient?

Once the shared region is established, both processes can access the same underlying memory rather than repeatedly copying large amounts of data between processes.

```text
Process A
    ↓
┌───────────────┐
│ Shared Memory │
└───────────────┘
    ↑
Process B
```

This can make shared memory very efficient for large or frequent data exchange.

## 5. The Major Problem: Race Conditions

Shared memory introduces concurrency problems.

Example:

```text
counter = 0
```

Both processes execute:

```text
counter = counter + 1
```

Conceptually:

```text
Process A              Process B
Read 0
                       Read 0
Add 1
                       Add 1
Write 1
                       Write 1

Final = 1   ❌
```

The expected result was 2.

This is a race condition.

## 6. Synchronization

Shared memory answers:

> Where do processes exchange data?

Synchronization answers:

> How do processes safely coordinate access to that data?

Common synchronization mechanisms include:

- Mutexes
- Semaphores
- Condition variables
- Read-write locks
- Atomic operations

Example:

```text
Process A
   ↓
Lock
   ↓
Read → Modify → Write
   ↓
Unlock

Process B
   ↓
Wait
   ↓
Lock
   ↓
Read → Modify → Write
   ↓
Unlock
```

## 7. Shared Memory vs Threads

Threads inside the same process naturally share the process's heap and global memory.

```text
Process
├── Thread A ──┐
├── Thread B ──┼── Shared process memory
└── Thread C ──┘
```

Separate processes normally need an IPC mechanism such as shared memory to intentionally share data.

## 8. Key Points

1. Shared memory is an IPC mechanism.
2. Multiple processes can access the same physical memory region.
3. Different processes can use different virtual addresses for the same shared region.
4. Shared memory can be efficient because data does not need to be repeatedly copied.
5. Shared memory introduces race conditions.
6. Synchronization is needed when processes concurrently access shared data.

## 9. Key Mental Model

> Shared memory allows isolated processes to intentionally share a physical memory region, while synchronization controls how they safely access the shared data.
