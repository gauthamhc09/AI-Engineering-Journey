# Concept 8 — CPU Cache

## Core Idea

RAM is much faster than persistent storage, but it is still relatively slow compared with the CPU.

A **CPU cache** is a small, fast memory on or very close to the CPU that stores copies of data and instructions the CPU is likely to need again.

```text
CPU
 │
 ├── Registers
 └── Cache
       ↓
      RAM
       ↓
      SSD
```

## Locality

### Temporal Locality

> If something was accessed recently, it is likely to be accessed again soon.

### Spatial Locality

> If something is accessed, nearby memory locations are likely to be accessed soon.

These patterns make caching effective.

## Cache Levels

Modern CPUs commonly have multiple cache levels:

```text
Registers
   ↓
L1
   ↓
L2
   ↓
L3
   ↓
RAM
   ↓
SSD
```

Generally, L1 is smaller/faster than L2, and L2 is smaller/faster than L3. Exact architecture varies by processor.

## Cache Hit

If requested data is found in the cache:

```text
CPU → Cache → Data
```

This is a **cache hit**.

## Cache Miss

If requested data is not found in the cache level being checked, that is a **cache miss**.

A miss can cause the system to check a lower level such as another cache level or RAM.

## Why Not One Huge Cache?

Very fast memory has physical, cost, power, space, and hardware-design trade-offs.

Therefore computers use a hierarchy:

```text
Small + fast
Registers
L1
L2
L3
RAM
SSD
Large + slower
```

## Python Connection

A loop such as:

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    total += number
```

can exhibit memory-access locality. Cache behavior is largely managed by the CPU and memory subsystem; Python does not normally explicitly place individual values into L1.

## AI Engineering Connection

Cache behavior matters in databases, vector databases, AI inference, backend data processing, and other data-intensive workloads. Performance depends on both computation and memory access/data movement.

## Key Takeaway

> CPU cache is small, fast memory close to the CPU that keeps likely-needed data and instructions nearby, exploiting temporal and spatial locality.
