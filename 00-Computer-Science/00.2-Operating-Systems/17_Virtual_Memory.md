# 00.2.17 — Virtual Memory

## 1. What is Virtual Memory?

Virtual memory is a memory abstraction that gives each process its own virtual address space.

The OS and hardware translate virtual addresses into physical memory addresses.

```text
Process
   ↓
Virtual Address
   ↓
OS / Hardware translation
   ↓
Physical Memory
```

## 2. Why Do We Need Virtual Memory?

### A. Memory Isolation

Each process gets its own virtual address space.

```text
Process A → Virtual Address Space A
Process B → Virtual Address Space B
```

This prevents processes from normally accessing each other's private memory.

### B. Address Abstraction

Programs do not need to know the physical RAM location of their data.

They work with virtual addresses, while the OS and hardware manage the mapping to physical memory.

## 3. Virtual Pages and Physical Frames

Virtual memory is divided into fixed-size chunks called **pages**.

Physical memory is divided into fixed-size chunks called **frames**.

```text
Virtual Memory              Physical RAM

Page 0 ────────────────→    Frame 7
Page 1 ────────────────→    Frame 2
Page 2 ────────────────→    Frame 15
Page 3 ────────────────→    Frame 4
```

The important terminology:

- **Virtual page** — a chunk of a process's virtual address space.
- **Physical frame** — a fixed-size chunk of physical memory.
- **Page table** — maps virtual pages to physical frames.

## 4. Page Tables

A page table contains the mappings used to translate virtual addresses to physical memory.

Conceptually:

```text
Virtual Page       Physical Frame
     0 ───────────────→ 7
     1 ───────────────→ 2
     2 ───────────────→ 15
     3 ───────────────→ 4
```

The OS manages these mappings, while memory-management hardware performs the address translation.

## 5. Same Virtual Address, Different Processes

Process A and Process B can both use virtual address `0x5000`.

That does not mean they access the same physical memory.

```text
Process A                         Process B

0x5000                            0x5000
   │                                 │
   ↓                                 ↓
Page Table A                     Page Table B
   │                                 │
   ↓                                 ↓
Frame 10                         Frame 25
```

Therefore:

```text
A's 0x5000 ≠ B's 0x5000
```

## 6. Connection to Shared Memory

Shared memory is possible because the OS can deliberately map memory into multiple processes.

```text
Process A ──┐
            ↓
       Same physical
          memory
            ↑
Process B ──┘
```

So virtual memory provides the mechanism through which controlled shared mappings can be created.

## 7. Virtual Memory Is Not Simply "More RAM"

Virtual memory is primarily an address-space abstraction.

It does not magically turn 16 GB of RAM into 32 GB of RAM.

Virtual memory can work with mechanisms such as paging and swapping, but virtual memory itself should not be equated with swap.

## 8. Why It Matters for AI Engineering

Virtual memory helps you understand:

- Why processes are isolated.
- Why multiple backend workers have separate address spaces.
- Why multiple processes can consume substantial memory.
- How large AI workloads interact with system memory.
- How shared memory between processes is possible.
- Why memory usage matters when deploying AI services.

## 9. Key Points

1. Every process has a virtual address space.
2. Programs normally use virtual addresses.
3. The OS and hardware translate virtual addresses to physical memory.
4. Virtual memory is divided into pages.
5. Physical memory is divided into frames.
6. Page tables map virtual pages to physical frames.
7. Each process normally has its own memory mappings.
8. This provides the foundation for memory isolation.
9. The same virtual address in two processes can refer to different physical memory.
10. The OS can deliberately create shared mappings.

## 10. Key Mental Model

```text
Process
   ↓
Virtual Address Space
   ↓
Virtual Pages
   ↓
Page Table
   ↓
Physical Frames
   ↓
RAM
```

> A process works with virtual addresses, while the OS and hardware translate those virtual addresses to physical memory and enforce access permissions.
