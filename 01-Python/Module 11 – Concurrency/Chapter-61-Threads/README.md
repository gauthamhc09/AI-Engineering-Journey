# Chapter 61 --- Threads in Python

## 1. What is concurrency?

**Concurrency** means managing multiple tasks so their execution can
overlap. A program may switch between tasks while one is waiting.

**Parallelism** means multiple tasks are executing at the same instant,
typically on different CPU cores.

Threads are especially useful when tasks spend time waiting for I/O.

## 2. What is a thread?

A **thread** is an execution path within a process. Threads in the same
process share memory, which makes communication convenient---but also
creates risks when they access shared mutable data.

Python's `threading` module lets us create and manage threads.

``` python
import threading

def greet(name):
    print(f"Hello, {name}")

thread = threading.Thread(target=greet, args=("Gautham",))
thread.start()
thread.join()
```

Key points:

-   `target` is the function the thread should execute.
-   `args` is a tuple of positional arguments passed to that function.
-   `start()` starts the thread.
-   `join()` makes the calling thread wait until that thread finishes.
-   Use `args=("value",)` for a one-item tuple. The trailing comma
    matters.

## 3. `start()` versus `join()`

-   `start()` begins the thread; it does **not** wait for completion.
-   `join()` waits for the thread to finish.

Starting several threads before joining them allows their work to
overlap:

``` python
import threading
import time

def download(document):
    print(f"{document}: Download starts")
    time.sleep(2)  # Simulates waiting for I/O
    print(f"{document}: Download finished")

threads = []

for doc in ["Doc1", "Doc2", "Doc3"]:
    thread = threading.Thread(target=download, args=(doc,))
    threads.append(thread)

# Start all threads first
for thread in threads:
    thread.start()

# Then wait for all of them
for thread in threads:
    thread.join()

print("All documents are ready!")
```

Because each simulated download waits for about two seconds, the three
tasks can finish in roughly two seconds plus overhead, rather than about
six seconds if run sequentially. Actual timing depends on the work and
environment.

**Important:** If you call `join()` immediately after each `start()` in
the same loop, you wait for each task before starting the next one. That
removes most of the intended overlap.

## 4. I/O-bound versus CPU-bound work

### I/O-bound

A task spends much of its time waiting for something outside the CPU,
such as:

-   HTTP/API responses
-   File reads and writes
-   Database queries

Threads can be useful because another thread can run while one is
waiting.

### CPU-bound

A task spends most of its time performing calculations.

In standard CPython, the **Global Interpreter Lock (GIL)** generally
prevents multiple threads from executing Python bytecode simultaneously.
Therefore, threads usually do not speed up CPU-heavy pure-Python work
across multiple cores.

For CPU-bound work, consider `multiprocessing` or other approaches
appropriate to the workload.

## 5. Race conditions and shared data

A **race condition** occurs when a result depends on the timing or
interleaving of concurrent operations.

For example, two threads might both read the same shared counter value,
increment it, and write it back. One update can overwrite the other.

The GIL does not make every multi-step operation logically atomic and
does not eliminate all race conditions.

## 6. Protecting shared data with `Lock`

A **lock** lets only one thread at a time enter a protected critical
section.

``` python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for _ in range(1000):
        with lock:
            counter += 1
```

-   `threading.Lock()` creates a lock.
-   `with lock:` acquires the lock before the block and releases it when
    the block exits---even if an exception occurs.
-   Keep the protected critical section as small as practical.

### `join()` versus `Lock`

  Tool       Purpose
  ---------- --------------------------------------------------------
  `join()`   Wait for a thread to finish
  `Lock`     Coordinate access to shared data or a critical section

They solve different problems.

## 7. Deadlocks and `RLock`

A **deadlock** is a situation where threads wait indefinitely for
resources held by one another.

A simple example of a self-deadlock is acquiring the same ordinary
`Lock` twice in the same thread without releasing it:

``` python
lock = threading.Lock()

lock.acquire()
lock.acquire()  # The thread waits for a lock it already holds
```

A `threading.RLock()` is a reentrant lock: the same thread can acquire
it multiple times. It must release it the same number of times it
acquired it.

Use `RLock` only when reentrant locking is genuinely needed; it does not
automatically prevent every kind of deadlock.

## 8. Common mistakes to avoid

-   Forgetting to call `start()`.
-   Assuming `start()` waits for the thread to finish.
-   Forgetting `join()` when the main thread must wait for results.
-   Writing `args=doc` instead of `args=(doc,)` when passing one
    positional argument.
-   Calling `join()` after each `start()` in the same loop when the goal
    is overlapping work.
-   Assuming the GIL prevents all race conditions.
-   Protecting shared mutable state inconsistently.
-   Holding locks longer than necessary.

## 9. Connection to AI Engineering

Threads can help when an AI application performs several independent I/O
tasks, for example:

-   Calling multiple external services or APIs
-   Fetching documents from a remote store
-   Waiting for database or network responses

Threads are not automatically the best choice for every AI workload.
CPU-heavy Python processing may call for multiprocessing, while
asynchronous I/O may be a better fit for many concurrent network
operations. Choose based on the bottleneck and the libraries being used.

## 10. Quick revision

-   **Concurrency:** tasks make progress with overlapping execution.
-   **Parallelism:** tasks execute at the same instant.
-   **Thread:** an execution path inside a process; threads share
    process memory.
-   **`start()`:** starts a thread.
-   **`join()`:** waits for a thread to finish.
-   **I/O-bound:** threads can help overlap waiting.
-   **CPU-bound:** standard CPython threads usually do not provide
    parallel execution of pure Python bytecode because of the GIL.
-   **Race condition:** result depends on timing/interleaving.
-   **Lock:** protects a critical section.
-   **Deadlock:** tasks wait indefinitely for resources.
-   **`RLock`:** allows the owning thread to acquire the same lock
    repeatedly.

### Chapter takeaway

Use threads primarily to overlap I/O-bound work. Start independent
threads before joining them, and protect shared mutable state with
synchronization tools such as locks.
