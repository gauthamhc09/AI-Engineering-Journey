# Concept 15 — Data Representation

## Central Idea
If computers fundamentally use bits, how can they represent numbers, text, images, audio, files, and AI data?

The answer is data representation.

## Mental Model
```text
Human meaning
     ↓
Representation rules
     ↓
Numbers / structures
     ↓
Bytes
     ↓
Bits
     ↓
Hardware
```

Reverse:

```text
Hardware
   ↓
Bits
   ↓
Bytes
   ↓
Representation rules
   ↓
Meaning
```

## Bit Patterns Have No Inherent Human Meaning
For example:

```text
01000001
```

cannot be interpreted solely from the bits. Depending on the representation, it may participate in representing a number, character, image/file data, instruction, or other information.

## Numbers
An unsigned binary integer gives a bit pattern numerical meaning.

```text
1010₂
=
1×8 + 0×4 + 1×2 + 0×1
=
10
```

Negative numbers also require representation rules; modern computers commonly use two's complement for signed integers.

## Text
Character encoding maps characters to numerical representations.

Example with ASCII:

```text
"A"
 ↓
65
 ↓
01000001
```

Unicode supports a much larger character repertoire. UTF-8, UTF-16, and UTF-32 are encoding schemes for Unicode.

## Images
```text
Image
 ↓
Pixels
 ↓
Numerical color values
 ↓
Binary data
```

A common 24-bit RGB representation uses 8 bits for each of red, green, and blue, giving 24 bits (3 bytes) per pixel before compression.

## Audio
```text
Sound wave
 ↓
Sampling
 ↓
Numerical values
 ↓
Binary data
```

## Video
```text
Video
 ↓
Images/frames + audio
 ↓
Numerical data
 ↓
Bits / bytes
```

## Files
A CSV, JPEG, PDF, model file, etc. ultimately consists of bytes stored or transmitted according to that format's rules.

## Serialization
Serialization converts structured data into a representation suitable for storage or transmission.

Example:

```python
data = {"price": 1450}
```

Conceptually:

```text
Python object
     ↓
JSON serialization
     ↓
'{"price": 1450}'
     ↓
Encoding
     ↓
Bytes
```

Reverse:

```text
Bytes
 ↓
Decode / parse
 ↓
JSON
 ↓
Application data
```

Keep these concepts distinct:

```text
Serialization
Python object → JSON/structured representation

Encoding
Representation/text → byte representation
```

## API Connection
A FastAPI backend may conceptually send:

```json
{
  "price": 1450,
  "symbol": "RELIANCE"
}
```

The high-level flow is:

```text
Python objects
 ↓
Serialize
 ↓
Representation
 ↓
Encode into bytes
 ↓
Network
 ↓
Bytes
 ↓
Decode / parse
 ↓
Frontend data
```

HTTP and networking details come later.

## AI Engineering Connection
LLM parameters use numerical representations such as:

```text
FP32
FP16
BF16
INT8
INT4
```

Representation affects memory consumption, data movement, computation, model loading, inference performance, and numerical precision.

## Core Principle
> Bits have no useful human meaning by themselves. A representation scheme gives a sequence of bits meaning.

Example:

```text
"A"
 ↓
ASCII representation
 ↓
65
 ↓
01000001
```

## Key Takeaways
1. Digital computers represent information using binary states.
2. Bits do not inherently mean number, text, image, etc.
3. Representation rules give bit patterns meaning.
4. Numbers, text, images, audio, files, and model parameters can ultimately be represented as bits.
5. Serialization converts structured data into a representation suitable for storage/transmission.
6. Encoding determines how information is represented as bytes.
7. Different representations can interpret binary patterns differently.
