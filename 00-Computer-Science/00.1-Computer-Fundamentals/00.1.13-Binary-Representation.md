# Concept 13 — Binary Representation

## Decimal
Decimal is base 10. For example:

```text
472 = 4×10^2 + 7×10^1 + 2×10^0
```

## Binary
Binary is base 2. Positions represent powers of 2:

```text
2^3  2^2  2^1  2^0
 8    4    2    1
```

## Example
```text
1010₂
```

means:

```text
1×8 + 0×4 + 1×2 + 0×1
= 10
```

Only positions containing `1` contribute.

For example:

```text
10101₂ = 2^4 + 2^2 + 2^0 = 16 + 4 + 1 = 21
```

## Binary Counting
```text
0  → 0000
1  → 0001
2  → 0010
3  → 0011
4  → 0100
5  → 0101
6  → 0110
7  → 0111
8  → 1000
9  → 1001
10 → 1010
11 → 1011
12 → 1100
13 → 1101
14 → 1110
15 → 1111
```

## n Bits
`n` bits provide `2^n` possible values/patterns. For unsigned integers, the range is:

```text
0 → 2^n - 1
```

Thus 8 bits represent `0–255`.

## Why Adding a Bit Doubles Possibilities
Every existing combination can be paired with either `0` or `1` for the new bit:

```text
n bits     → 2^n
n+1 bits   → 2^(n+1) = 2 × 2^n
```

## Key Mental Model
Do not memorize `1010 = 10`; derive it from positional powers of 2.

## AI Connection
Binary representation underlies integer formats and numerical representations such as FP32, FP16, BF16, INT8, and INT4, which affect memory and computation trade-offs.
