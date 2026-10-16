# Concept 11 — Memory Hierarchy

## Why Memory Hierarchy Exists
No single memory technology is simultaneously extremely fast, extremely large, cheap, persistent, low-power, and close to the CPU. Computers therefore use multiple levels.

## Hierarchy
```text
CPU
 ↓
Registers
 ↓
L1 Cache
 ↓
L2 Cache
 ↓
L3 Cache
 ↓
RAM
 ↓
SSD / HDD
```

Broadly, higher levels are smaller, faster, and closer to the CPU; lower levels are larger, slower, and farther away. SSD/HDD provide persistent storage.

## Locality

### Temporal locality
If something was accessed recently, it is likely to be accessed again soon.

```python
x = 10
print(x)
print(x)
print(x)
```

### Spatial locality
If a memory location was accessed, nearby locations are likely to be accessed soon.

```python
numbers = [1, 2, 3, 4]
numbers[0]
numbers[1]
numbers[2]
numbers[3]
```

## Cache Hit / Miss
A cache hit means requested data is found at the cache level being checked. A cache miss means it is not found at that level and the system must look farther down the hierarchy.

## Important Correction
Do not imagine every datum physically travels through every level each time. The hierarchy is a set of levels from which requests can be satisfied.

## Performance
Program performance is not just CPU speed:

```text
CPU computation
+
Memory access
+
Cache behavior
+
Data locality
+
I/O
```

A fast CPU can still spend time waiting for data.

## AI Engineering Connection
Memory hierarchy matters for model weights, vector search, batching, caching, memory bandwidth, data movement, and LLM inference.

## Key Takeaway
No single memory technology provides all desirable properties. The hierarchy balances speed, capacity, cost, and persistence.
