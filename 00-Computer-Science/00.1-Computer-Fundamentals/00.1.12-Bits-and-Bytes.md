# Concept 12 — Bits and Bytes

## Bit
A bit (binary digit) is the smallest unit of digital information and has two possible values:

```text
0
1
```

A bit is an abstract unit of information; hardware implements it using physical states.

## Combinations
For `n` bits:

```text
2^n combinations
```

Examples:

```text
1 bit  → 2
2 bits → 4
3 bits → 8
4 bits → 16
8 bits → 256
```

## Byte
```text
1 byte = 8 bits
```

Therefore one byte has `2^8 = 256` possible bit patterns. If interpreted as an unsigned integer, these represent `0–255`.

## Bit vs Byte
```text
b = bit
B = byte
```

`100 Mbps` means 100 megabits per second. `100 MB` means 100 megabytes.

## Data Representation
At a high level:

```text
Human-readable notation
        ↓
Representation
        ↓
Bits / Bytes
        ↓
Hardware
```

Do not interpret this as Python simply converting every value directly into bits; later concepts such as runtimes, objects, and machine instructions add layers.

## AI Connection
Bits and bytes affect model storage, FP32/FP16/BF16/INT8/INT4 representations, memory usage, bandwidth, files, and data movement.

## Key Takeaway
A bit is a binary digit; a byte is 8 bits; `n` bits provide `2^n` possible patterns.
