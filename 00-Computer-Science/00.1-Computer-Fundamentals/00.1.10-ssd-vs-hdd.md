# Concept 10 — SSD vs HDD

## Core Difference

Both provide persistent storage, but they use different technologies:

```text
HDD → magnetic + mechanical
SSD → flash + electronic
```

## HDD

An HDD uses rotating magnetic platters and a mechanical read/write head.

```text
HDD
┌─────────────┐
│ Platter ↻   │
│      ↑      │
│    Head     │
└─────────────┘
```

Access can involve moving the head and waiting for the platter to rotate to the relevant location.

## SSD

An SSD uses flash memory and has no spinning platters or mechanical read/write head.

```text
SSD
┌──────────────────┐
│ Flash memory     │
│ ▣ ▣ ▣ ▣ ▣ ▣     │
└──────────────────┘
```

## Why SSDs Are Generally Faster

HDD:

```text
Move head
 ↓
Wait for platter rotation
 ↓
Reach location
 ↓
Read data
```

SSD:

```text
Request
 ↓
Electronic flash access
 ↓
Data
```

The HDD's mechanical positioning introduces additional latency. SSDs generally have much lower access latency and better random-access performance.

## SSD Does Not Replace RAM

If a computer has:

```text
16 GB RAM
512 GB SSD
```

that is not 528 GB of RAM.

```text
16 GB → RAM → working memory
512 GB → SSD → persistent storage
```

## Why SSD Cannot Simply Replace RAM

RAM and SSD have different characteristics and roles:

```text
RAM
→ working memory
→ volatile
→ designed for memory access

SSD
→ persistent storage
→ non-volatile
→ designed for storage
```

Even a much faster SSD would not make RAM conceptually unnecessary.

## Why RAM Cannot Replace SSD

If data exists only in RAM:

```text
Power OFF
 ↓
RAM contents are lost
```

A file on SSD remains after power-off.

## Other Differences

- HDD has moving parts; SSD has no moving mechanical parts.
- HDDs can produce mechanical noise; SSDs do not have moving mechanical parts.
- SSDs generally tolerate physical shock better while operating.
- SSDs can use less power in many usage patterns, although actual consumption depends on device and workload.

## Important Distinction

RAM and SSD can both support non-sequential access, but they are not equivalent. RAM is a memory system for addressable working memory; an SSD is persistent, block-oriented storage accessed through a storage controller/interface.

## Program Execution Model

```text
SSD
 ↓
RAM
 ↓
Cache
 ↓
Registers
 ↓
CPU / ALU
```

## AI Engineering Connection

For local AI systems, model files may be stored on SSD and loaded into working memory before execution. Application systems similarly move data between persistent storage and working memory during processing.

## Key Takeaway

> HDDs use magnetic storage with mechanical movement; SSDs use flash storage with electronic access. Both are persistent storage, while RAM serves a different role as volatile working memory.
