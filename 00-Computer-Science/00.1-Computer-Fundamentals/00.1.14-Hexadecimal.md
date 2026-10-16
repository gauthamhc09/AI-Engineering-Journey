# Concept 14 — Hexadecimal

## What Is Hexadecimal?
Hexadecimal is base 16.

```text
Decimal      → base 10
Binary       → base 2
Hexadecimal  → base 16
```

Symbols:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

where:

```text
A=10, B=11, C=12, D=13, E=14, F=15
```

## Why Hexadecimal?
Long binary values are difficult for humans to read. Hexadecimal gives a compact representation while retaining a direct relationship with binary.

## Four Bits = One Hex Digit
```text
4 bits → 2^4 = 16 combinations
```

Therefore:

```text
4 binary bits ↔ 1 hexadecimal digit
8 bits ↔ 2 hexadecimal digits
```

Mapping:

```text
0000 0
0001 1
0010 2
0011 3
0100 4
0101 5
0110 6
0111 7
1000 8
1001 9
1010 A
1011 B
1100 C
1101 D
1110 E
1111 F
```

## Binary to Hex
```text
10101100
↓
1010 1100
↓
A    C
↓
AC
```

So `10101100₂ = AC₁₆`.

## 0x Prefix
`0x` indicates hexadecimal.

```text
0x10 = 1×16 + 0 = 16 decimal
```

## 0xFF
```text
FF
↓
1111 1111
↓
255
```

Therefore `0xFF = 255`.

## Important
Hexadecimal is not a physical storage type. It is a human-friendly notation for representing binary values.

For example:

```text
Binary:      10101100
Hexadecimal: AC
Decimal:     172
```

These are different representations of the same numerical value.

## Frontend Connection
CSS color `#4338CA` uses hexadecimal notation:

```text
43 38 CA
```

Each pair commonly represents an 8-bit RGB component, so each ranges from `00–FF`, or `0–255`.

## Key Takeaway
Hexadecimal is a compact, human-friendly representation of binary data.
