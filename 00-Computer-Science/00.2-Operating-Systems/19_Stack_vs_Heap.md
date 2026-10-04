# 00.2.19 — Stack vs Heap

## 1. Overview
A process has different memory regions. The two important ones here are:
- **Stack** — mainly used for function-call execution and stack frames.
- **Heap** — mainly used for dynamically managed objects/data.

```text
Process
├── Code
├── Global/Data
├── Heap
└── Stack
```

## 2. Stack
The stack is primarily used for function-call execution. Each function call creates a **stack frame**.

```text
Stack
┌─────────────────────┐
│ add() frame         │
│ a = 10              │
│ b = 20              │
│ result = 30         │
└─────────────────────┘
```

Stack frames follow **LIFO — Last In, First Out**.

```text
┌──────────────┐
│ function C   │ ← removed first
├──────────────┤
│ function B   │
├──────────────┤
│ function A   │
└──────────────┘
```

## 3. Recursion
Each recursive call creates another stack frame. Excessive recursion can exhaust stack space, causing a stack overflow or a runtime-specific error such as Python's `RecursionError`.

## 4. Heap
The heap is used for **dynamically managed objects and data**. Heap data can have a lifetime that is not directly tied to one function call.

```text
Heap
┌────────────────────┐
│ Object A           │
├────────────────────┤
│ Object B           │
├────────────────────┤
│ Object C           │
└────────────────────┘
```

## 5. Python Conceptual Model

```python
x = [10, 20, 30]
```

Conceptually:

```text
Execution context
x
│
│ reference
↓
Heap
┌────────────────┐
│ List object    │
│ 10             │
│ 20             │
│ 30             │
└────────────────┘
```

A Python variable/reference refers to an object; the object is managed in dynamically allocated memory. This is a conceptual model, not an exact description of every CPython runtime structure.

## 6. Threads
Threads in the same process have separate stacks but share the process's memory, including its heap.

```text
Process
├── Thread A → own stack
├── Thread B → own stack
├── Thread C → own stack
└── Shared process memory / heap
```

## 7. Stack vs Heap

| Stack | Heap |
|---|---|
| Function-call execution | Dynamically managed objects/data |
| Stack frames | Flexible object/data lifetime |
| LIFO structure | Flexible allocation |
| Generally very fast | More management overhead |
| Each thread has its own stack | Shared by threads in the same process |

Do not rely on the oversimplification that all local variables are on the stack and all global variables are on the heap; actual behavior depends on the language and runtime.

## 8. Why It Matters for AI Engineering
Understanding stack and heap helps with:
- Python memory usage
- Function calls and recursion
- Large data structures
- Object creation
- Multi-threading
- Multi-process memory usage
- Debugging memory-related problems

## 9. Key Points
1. Stack is primarily associated with function-call execution.
2. Each function call creates a stack frame.
3. Stack frames follow LIFO order.
4. Deep recursion can exhaust stack space.
5. Heap is used for dynamically managed objects/data.
6. Each process has its own stack and heap.
7. Threads have separate stacks but share the process's heap/memory.
8. Python variables conceptually refer to dynamically managed objects.

## 10. Mental Model

```text
PROCESS
│
├── STACK
│    ├── Function-call frames
│    ├── Execution state
│    └── LIFO
│
└── HEAP
     ├── Dynamically managed objects
     └── Flexible lifetime
```

> The stack manages function-call execution state, while the heap provides dynamically managed memory for objects and data.
