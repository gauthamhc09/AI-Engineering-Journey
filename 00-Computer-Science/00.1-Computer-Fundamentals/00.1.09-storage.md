# Concept 9 — Storage

## Core Idea

RAM is for active work. **Storage is for keeping information persistently.**

Examples:
- SSD
- HDD
- USB flash drive
- Memory card

```text
Computer
├── RAM → working memory
└── Storage → persistent data
```

## Program Storage vs Execution

Suppose:

```text
portfolio.py
```

exists on an SSD.

When it runs:

```text
SSD
 ↓
RAM
 ↓
CPU
```

The file remains persistently stored while the running program requires working memory.

## Files

Examples:

```text
portfolio.py
photo.jpg
database.db
```

At the device level, information is ultimately represented as bits. The operating system and filesystem provide structure such as files, directories, names, permissions, and metadata.

## Why Storage Is Slower Than RAM

Storage is designed primarily for large, persistent capacity.

RAM is designed primarily for fast active access.

```text
Registers
   ↓
Cache
   ↓
RAM
   ↓
Storage
```

Each level makes different engineering trade-offs.

## Storage Types

### SSD
Persistent storage based on semiconductor flash memory. No spinning magnetic disk or mechanical read/write head.

### HDD
Persistent storage using magnetic rotating platters and a mechanical read/write head.

## Storage Is Not Immediate CPU Working Memory

A simplified path is:

```text
Storage
 ↓
RAM
 ↓
Cache
 ↓
Registers
 ↓
CPU execution
```

## AI Engineering Connection

Storage underpins databases, RAG document storage, model files, logs, uploaded portfolio files, and vector/database persistence.

## Important Refinement

Prefer:

> RAM is volatile memory; SSD/HDD provide non-volatile persistent storage.

"Temporary" can be misleading because RAM can contain data for a long time while powered on. The defining distinction is whether data survives loss of power.

## Key Takeaway

> Storage provides persistent capacity for files and data; RAM provides volatile working memory for active execution.
