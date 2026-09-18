# Chapter 62 --- Multiprocessing in Python

## 1. What is multiprocessing?

**Multiprocessing** means running work in separate processes.

Each process has its own Python interpreter and memory space. Separate
processes can execute on different CPU cores, making multiprocessing
especially useful for **CPU-bound work**.

### Threads vs Processes

  -----------------------------------------------------------------------
                          Threads                 Processes
  ----------------------- ----------------------- -----------------------
  Memory                  Shared within a process Separate memory spaces

  Best suited for         I/O-bound work          CPU-bound work

  Communication           Shared memory is        Explicit communication
                          convenient              often required

  Overhead                Usually lower           Usually higher

  CPython GIL             Limits parallel Python  Separate processes
                          bytecode execution      avoid this limitation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 2. Creating a process

Python provides the `multiprocessing` module.

``` python
from multiprocessing import Process

def work():
    print("Work is running")

if __name__ == "__main__":
    process = Process(target=work)
    process.start()
    process.join()

    print("Main process finished")
```

### `start()`

Starts the child process. It does **not** wait for completion.

### `join()`

Waits for the child process to finish. It does **not** retrieve the
function's return value.

------------------------------------------------------------------------

## 3. The `__main__` guard

Use:

``` python
if __name__ == "__main__":
```

around multiprocessing startup code.

This is important because child processes may start a fresh Python
interpreter. The guard prevents process-creation code from being
unintentionally executed again.

------------------------------------------------------------------------

## 4. Processes have separate memory

Normal Python variables are not automatically shared between processes.

Conceptually:

``` text
Process A              Process B
─────────              ─────────
Memory A               Memory B
counter = 10           counter = 0
```

Therefore, processes need explicit mechanisms when they need to
communicate.

------------------------------------------------------------------------

## 5. Sharing results with `Queue`

`multiprocessing.Queue` provides a way for processes to exchange data.

``` python
from multiprocessing import Process, Queue

def calculate(queue):
    result = 10 * 5
    queue.put(result)

if __name__ == "__main__":
    queue = Queue()

    process = Process(
        target=calculate,
        args=(queue,)
    )

    process.start()

    result = queue.get()

    process.join()

    print("Result:", result)
```

Output:

``` text
Result: 50
```

### Key idea

> Processes do not automatically share ordinary Python variables, but
> they can communicate using multiprocessing mechanisms such as `Queue`.

------------------------------------------------------------------------

## 6. CPU-bound work

Multiprocessing is particularly useful for CPU-heavy tasks such as:

-   Large numerical calculations
-   CPU-heavy data processing
-   Image processing
-   Complex transformations
-   Computational simulations

Example:

``` python
from multiprocessing import Process
import os

def calculate(number):
    result = sum(i * i for i in range(number))
    print(f"PID {os.getpid()} calculated: {result}")

if __name__ == "__main__":
    p1 = Process(target=calculate, args=(1_000_000,))
    p2 = Process(target=calculate, args=(1_000_000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both calculations finished")
```

The two processes can potentially execute on different CPU cores.

------------------------------------------------------------------------

## 7. Process Pool

Creating and managing many processes manually can become tedious.

`multiprocessing.Pool` manages a group of worker processes.

``` python
from multiprocessing import Pool, cpu_count

def square(number):
    return number * number

if __name__ == "__main__":
    worker_count = min(4, cpu_count())

    with Pool(processes=worker_count) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])

    print(results)
```

Output:

``` text
[1, 4, 9, 16, 25]
```

The pool handles much of the worker-process orchestration for you.

------------------------------------------------------------------------

## 8. `pool.map()`

`map()` applies a function to every item.

``` python
def cube(number):
    return number * number * number

results = pool.map(cube, [2, 3, 4])
```

Result:

``` python
[8, 27, 64]
```

An important property of `map()` is that the returned results preserve
the **input order**, even if tasks finish at different times.

------------------------------------------------------------------------

## 9. `pool.apply_async()`

`apply_async()` lets you submit a task without immediately waiting for
its result.

``` python
from multiprocessing import Pool
import time

def square(number):
    time.sleep(2)
    return number * number

if __name__ == "__main__":
    with Pool(processes=2) as pool:
        result1 = pool.apply_async(square, (5,))
        result2 = pool.apply_async(square, (10,))

        print("Main process is doing something else...")

        answer1 = result1.get()
        answer2 = result2.get()

    print(answer1)
    print(answer2)
```

### `.get()`

Retrieves the result. If the task has not finished, `.get()` waits.

------------------------------------------------------------------------

## 10. `map()` vs `apply_async()`

  -----------------------------------------------------------------------
                          `pool.map()`            `pool.apply_async()`
  ----------------------- ----------------------- -----------------------
  Main idea               Process many inputs     Submit individual tasks
                                                  asynchronously

  Results                 Returned as a list      Retrieved with `.get()`

  Ordering                Preserves input order   More flexible

  Use case                Batch-style processing  Flexible asynchronous
                                                  submission
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 11. `join()` vs Queue vs `.get()`

These solve different problems:

### `join()`

``` python
process.join()
```

**Waits** for a process to finish.

### `Queue`

``` python
queue.put(result)
result = queue.get()
```

**Communicates data** between processes.

### `AsyncResult.get()`

``` python
result = pool.apply_async(calculate, (10,))
answer = result.get()
```

**Retrieves the result** of an asynchronous pool task.

Remember:

``` text
join()       → wait
Queue        → communicate
.get()       → retrieve async result
```

------------------------------------------------------------------------

## 12. Common mistakes

### Forgetting `start()`

``` python
process = Process(target=work)
process.join()
```

The process was never started.

Correct:

``` python
process.start()
process.join()
```

### Thinking `join()` returns the result

``` python
result = process.join()
```

This does not retrieve the function's return value.

Use `Queue` or another communication mechanism.

### Assuming processes share variables

Changing a normal variable in one process does not automatically change
it in another.

### Creating too many processes

More processes does not automatically mean better performance.

Processes have startup, memory, and communication overhead. Worker count
should match the workload and machine.

### Forgetting the main guard

Use:

``` python
if __name__ == "__main__":
```

around multiprocessing startup code.

------------------------------------------------------------------------

## 13. Connection to AI Engineering

Multiprocessing can be useful for CPU-heavy AI/data workloads such as:

-   CPU-heavy document preprocessing
-   Large-scale data transformation
-   Image preprocessing
-   Feature preparation
-   Batch processing
-   Numerical calculations

However, different workloads call for different concurrency models:

``` text
Waiting for APIs/network → Threads / Async
CPU-heavy Python work   → Multiprocessing
GPU model computation   → GPU/framework-specific parallelism
```

The important AI Engineering skill is to identify the **bottleneck**
before choosing a concurrency model.

------------------------------------------------------------------------

## 14. Mental model

``` text
COMPUTER
   │
   ├── PROCESS
   │      │
   │      ├── THREAD
   │      ├── THREAD
   │      └── THREAD
   │
   ├── PROCESS
   │      │
   │      ├── THREAD
   │      └── THREAD
   │
   └── PROCESS
          │
          └── THREAD
```

### Thread

An execution path inside a process.

### Process

An independent execution environment with its own memory.

### Pool

A group of worker processes managed for you.

------------------------------------------------------------------------

## 15. Quick Revision

``` text
Multiprocessing
      ↓
Multiple independent processes
      ↓
Separate memory
      ↓
Useful for CPU-bound parallel work
      ↓
Use Queue/Pipe/etc. for communication
      ↓
Pool manages worker processes
```

### Core API

``` python
from multiprocessing import Process, Pool, Queue
```

Process:

``` python
p = Process(target=work)
p.start()
p.join()
```

Queue:

``` python
queue.put(result)
result = queue.get()
```

Pool:

``` python
with Pool(4) as pool:
    results = pool.map(function, items)
```

Async pool task:

``` python
result = pool.apply_async(function, args)
answer = result.get()
```

## Final takeaway

> **Threads → usually useful for I/O-bound concurrency**
>
> **Processes → usually useful for CPU-bound parallelism**
>
> **Pool → manages a group of worker processes**
>
> **Queue → communicates data between processes**
>
> **`join()` → waits; it doesn't retrieve return values**
