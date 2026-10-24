# Module 00.4 --- Processes, Threads, and Concurrency

## Module goals

By the end of this module, you should be able to:

-   Explain how processes and threads execute.
-   Distinguish concurrency from parallelism.
-   Understand scheduling and context switching.
-   Recognize race conditions and protect shared state.
-   Explain locks, mutexes, semaphores, deadlocks, and starvation.
-   Understand how processes communicate using IPC.
-   Choose between Python threading, multiprocessing, process pools, and
    `asyncio`.
-   Relate concurrency choices to backend services and AI engineering
    workloads.

------------------------------------------------------------------------

## 1. Process vs. Thread

### Process

A **process** is a program that is currently executing, together with
its execution state and resources managed by the operating system.

A process typically has its own virtual address space and resources such
as:

-   Program code and data
-   Heap memory
-   One or more threads
-   Open file descriptors or handles
-   Security and operating-system state

Separate processes are isolated from one another by default. One process
cannot ordinarily access another process's private memory directly.

### Thread

A **thread** is an execution path within a process. A process can
contain one or more threads.

Threads in the same process generally share:

-   Program code
-   Heap and dynamically allocated objects
-   Global variables
-   Process-level resources, such as open files

Each thread has its own:

-   Stack
-   Instruction pointer / program counter
-   CPU register state
-   Scheduling and execution state

### Core comparison

  -----------------------------------------------------------------------
  Feature                 Process                 Thread
  ----------------------- ----------------------- -----------------------
  Address space           Usually separate from   Shared with threads in
                          other processes         the same process

  Memory sharing          Requires an IPC or      Shared heap and globals
                          shared-memory mechanism are directly accessible
                          for ordinary            
                          cross-process           
                          communication           

  Isolation               Stronger by default     Weaker; a bug can
                                                  affect shared process
                                                  state

  Creation and switching  Often more              Often less
                          resource-intensive      resource-intensive

  Failure impact          Often contained to that A serious thread
                          process                 failure can affect the
                                                  whole process
  -----------------------------------------------------------------------

**Important:** "Threads share memory" does not mean each thread has the
same stack. Each thread has its own stack and execution state.

------------------------------------------------------------------------

## 2. CPU Cores and Execution

A CPU core executes machine instructions. A single ordinary software
thread can execute on one core at a time.

-   **One core, multiple runnable threads:** the operating system can
    switch between them so each gets some CPU time.
-   **Multiple cores:** different threads or processes can execute
    simultaneously on different cores.
-   **More threads than cores:** the operating system schedules them,
    and some wait while others run.

The operating system's scheduler decides which runnable thread or
process should run on an available CPU.

------------------------------------------------------------------------

## 3. Scheduling and Execution

**CPU scheduling** is the operating system's process of selecting a
runnable thread or process to execute.

The scheduler may consider priorities, fairness, responsiveness, and
system policy. A thread can be runnable but not currently executing
because another thread has the CPU.

Scheduling matters because it determines how CPU time is shared and
influences responsiveness and throughput.

------------------------------------------------------------------------

## 4. Context Switching

A **context switch** occurs when the CPU stops executing one thread or
process and starts executing another. The system preserves enough
execution state to resume the previous work later.

The saved state may include registers, the instruction pointer, and
other processor or operating-system state.

Context switching enables multitasking but has overhead: the CPU and
operating system perform work that is not directly the application's
intended computation. Switching between processes may involve additional
address-space-related work compared with switching between threads in
the same process, though exact costs depend on the system.

------------------------------------------------------------------------

## 5. Concurrency vs. Parallelism

### Concurrency

**Concurrency** means multiple tasks can make progress during
overlapping periods. Their steps may be interleaved.

Example: one CPU core alternates between two tasks, letting both
progress over time.

### Parallelism

**Parallelism** means multiple tasks are executing at the same instant,
typically on different CPU cores or processing units.

Example: two CPU-bound tasks execute simultaneously on two cores.

  -----------------------------------------------------------------------
                          Concurrency             Parallelism
  ----------------------- ----------------------- -----------------------
  Main idea               Overlapping progress    Simultaneous execution

  Requires multiple       No                      Usually requires
  cores?                                          multiple execution
                                                  units

  Useful for              Coordinating many       Doing work at the same
                          tasks, including I/O    time
  -----------------------------------------------------------------------

A system can support concurrency without parallelism. Parallel execution
is one way to achieve concurrent progress.

------------------------------------------------------------------------

## 6. Shared State

**Shared state** is data that multiple threads or tasks can access.

Examples include a global counter, a shared list, or a mutable object
referenced by multiple threads.

Shared state can be useful, but simultaneous access and updates need
careful coordination. The danger is especially significant when multiple
operations read and modify the same mutable data.

------------------------------------------------------------------------

## 7. Race Conditions

A **race condition** occurs when a result depends on the timing or
interleaving of operations.

Consider a shared counter initially equal to `0`. Two threads each
perform `counter += 1`.

A conceptual read-modify-write sequence is:

1.  Thread A reads `0`.
2.  Thread B reads `0`.
3.  Thread A calculates and writes `1`.
4.  Thread B calculates and writes `1`.

The final value is `1`, although two increments were intended. One
update was lost.

This is a **lost update**, a common example of a race condition.

Do not assume a single source-code line is automatically safe as a
complete logical operation. The relevant behavior depends on the
language, runtime, operation, and synchronization used.

------------------------------------------------------------------------

## 8. Critical Sections

A **critical section** is a part of a program that accesses shared state
or another resource that must be protected from conflicting concurrent
access.

If multiple threads enter an unprotected critical section at the same
time, their operations may interfere.

The goal is to coordinate access so the program preserves its required
invariants.

------------------------------------------------------------------------

## 9. Locks

A **lock** is a synchronization mechanism used to control access to a
shared resource or critical section.

A common pattern is:

1.  Acquire the lock.
2.  Read or modify the shared state.
3.  Release the lock.

Only the thread that owns the lock should release it, according to the
lock's API and usage rules. In Python, a context manager helps ensure
release even if an exception occurs:

``` python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1
```

The lock must protect the whole logical read-modify-write operation, not
merely one arbitrarily chosen line.

Locks can reduce parallel progress if held for too long. Avoid
unnecessary work while holding a lock.

------------------------------------------------------------------------

## 10. Mutex

A **mutex** (mutual-exclusion lock) allows at most one thread to own it
at a time. It is used to ensure exclusive access to a critical section.

In Python, `threading.Lock` is commonly used for this purpose. More
generally, APIs and platforms may distinguish different lock types and
ownership rules.

**Mental model:** one key, one holder at a time.

------------------------------------------------------------------------

## 11. Semaphores

A **semaphore** maintains a count of permits. A task must acquire a
permit before entering the limited resource area and release it when
finished.

A semaphore initialized with three permits can allow up to three
operations to hold permits concurrently.

Python example:

``` python
import threading

db_limit = threading.Semaphore(3)

def query_database():
    with db_limit:
        # Perform the database operation.
        pass
```

Use a semaphore when the requirement is a concurrency limit, such as
limiting simultaneous database operations or requests to a constrained
service.

  Primitive      Typical purpose
  -------------- --------------------------------------
  Lock / mutex   One holder at a time
  Semaphore      Up to a configured number of holders

------------------------------------------------------------------------

## 12. Deadlocks

A **deadlock** occurs when two or more tasks are permanently waiting for
one another's actions or resources, so none of them can proceed.

Example:

-   Thread A acquires Lock 1 and waits for Lock 2.
-   Thread B acquires Lock 2 and waits for Lock 1.
-   Neither releases its held lock, so both wait indefinitely.

This is **circular waiting**.

Common ways to reduce deadlock risk include:

-   Acquire multiple locks in a consistent global order.
-   Avoid holding locks longer than necessary.
-   Avoid waiting for external work while holding a lock.
-   Use timeouts where appropriate and handle timeout failures
    correctly.

A deadlock is not the same as a race condition. A race condition can
produce an incorrect result due to timing; a deadlock prevents progress.

------------------------------------------------------------------------

## 13. Starvation

**Starvation** occurs when a task waits indefinitely or for an
unacceptably long time because other tasks repeatedly get access to the
CPU or a resource first.

Other tasks may continue making progress, unlike a deadlock in which the
involved tasks are stuck waiting on each other.

Scheduling policy, priority choices, and unfair resource acquisition can
contribute to starvation.

------------------------------------------------------------------------

## 14. Synchronization

**Synchronization** coordinates concurrent tasks so they access
resources safely and obey required ordering.

Common mechanisms include:

-   Locks / mutexes
-   Semaphores
-   Events and condition variables
-   Queues
-   Barriers
-   Atomic operations where provided

Synchronization helps protect invariants, avoid data races, and
coordinate producer/consumer workflows. It can also introduce overhead
and, if used incorrectly, deadlock or starvation.

------------------------------------------------------------------------

## 15. Inter-Process Communication (IPC)

Processes have separate address spaces by default. **Inter-process
communication (IPC)** is how processes exchange data or coordinate.

Common IPC approaches include:

-   Pipes
-   Queues
-   Sockets
-   Shared memory
-   Operating-system message mechanisms

An ordinary local variable created in a child process is not
automatically a shared variable visible to its parent. A result must be
returned through a suitable process API or an IPC mechanism.

------------------------------------------------------------------------

## 16. Pipes

A **pipe** is a communication channel through which data flows from one
endpoint to another. A common use is sending output from one process to
another.

Pipes are often suited to stream-like communication. Their exact
behavior, directionality, and setup depend on the operating system and
API.

**Mental model:** a channel that carries data between endpoints.

------------------------------------------------------------------------

## 17. Queues

A **queue** stores items so producers can place work or results into it
and consumers can retrieve them. A queue can be used for thread
coordination or IPC, depending on the queue implementation.

For example, Python's `multiprocessing.Queue` can communicate values
between processes:

``` python
from multiprocessing import Process, Queue

def worker(result_queue):
    result_queue.put(42)

if __name__ == "__main__":
    results = Queue()
    process = Process(target=worker, args=(results,))
    process.start()

    result = results.get()
    process.join()
    print(result)
```

The queue abstracts some of the coordination involved in transferring
values. It does not make all shared-state problems disappear; the
overall design still matters.

------------------------------------------------------------------------

## 18. Shared-Memory IPC

With **shared-memory IPC**, multiple processes map a shared memory
region and use it to exchange data.

Advantages: - Can reduce copying for large data transfers. - Can be
efficient for high-volume communication.

Challenges: - Processes must agree on the shared data layout. -
Concurrent writes may require synchronization. - Incorrect coordination
can cause data corruption or inconsistent reads.

Shared memory is different from an ordinary local variable in one
process.

------------------------------------------------------------------------

## 19. Worker Pools

A **worker pool** maintains a bounded set of workers that process
submitted tasks. Instead of creating a new worker for every task, the
program reuses existing workers.

Benefits: - Limits resource usage. - Avoids repeated worker creation
overhead. - Helps process many independent tasks. - Makes concurrency
limits easier to reason about.

Pool size should be chosen according to the workload and available
resources. More workers do not always mean better performance; they can
increase memory usage and contention.

------------------------------------------------------------------------

## 20. Concurrency Strategy --- Choosing the Right Tool

The best approach depends on whether work is CPU-bound or I/O-bound and
on the runtime.

  -----------------------------------------------------------------------
  Workload                Often a sensible        Why
                          starting point          
  ----------------------- ----------------------- -----------------------
  Many blocking network   Threads or `asyncio`    Tasks spend time
  or file operations                              waiting for I/O

  CPU-heavy pure-Python   Multiprocessing /       Separate processes can
  work in standard        process pool            execute Python code in
  GIL-enabled CPython                             parallel across cores

  Many concurrent         `asyncio`               Event loop can
  operations supported by                         coordinate many tasks
  async libraries                                 without one thread per
                                                  task

  Shared mutable data     Lock or another         Coordinates access to
  between threads         appropriate             shared state
                          synchronization         
                          primitive               

  Limit concurrent access Semaphore or bounded    Enforces a concurrency
  to a service            worker pool             limit
  -----------------------------------------------------------------------

These are starting points, not universal rules. Native libraries may
release the GIL, runtimes differ, and actual performance should be
measured.

------------------------------------------------------------------------

## 21. Python Threading

Python's `threading` module provides threads within a process.

Typical uses: - Network requests - File I/O - Other blocking
operations - Coordinating tasks that share in-process objects

Example:

``` python
import threading

def download_document(url):
    print(f"Downloading {url}")

threads = [
    threading.Thread(target=download_document, args=(url,))
    for url in ["https://example.com/a", "https://example.com/b"]
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
```

`start()` begins the thread's execution. `join()` waits for that thread
to finish.

The example illustrates the API shape; a real downloader would perform
network I/O and handle errors, timeouts, and response data.

Threading does not automatically make CPU-bound Python code execute in
parallel under standard GIL-enabled CPython.

------------------------------------------------------------------------

## 22. Python Multiprocessing

Python's `multiprocessing` module starts separate processes. Each
process has its own interpreter and address space.

Typical uses: - CPU-heavy tasks - Work that benefits from execution
across CPU cores - Isolating independent worker computations

Example:

``` python
from multiprocessing import Process

def calculate():
    result = sum(i * i for i in range(1_000_000))
    print(result)

if __name__ == "__main__":
    process = Process(target=calculate)
    process.start()
    process.join()
```

The `if __name__ == "__main__":` guard is important in environments that
start child processes by importing the main module, such as the `spawn`
start method.

Processes do not automatically share ordinary mutable Python objects.
Use queues, pipes, shared memory, or other supported mechanisms to
communicate.

------------------------------------------------------------------------

## 23. Python Process Pools

A process pool manages a set of reusable worker processes. It is useful
for distributing many independent CPU-heavy tasks without manually
managing each process.

Example:

``` python
from concurrent.futures import ProcessPoolExecutor

def square(number):
    return number * number

if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]

    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(square, values))

    print(results)
```

Important points: - `max_workers` bounds the worker count. - Inputs and
outputs generally need to be transferable/serializable for the chosen
process setup. - Process startup and data-transfer overhead can outweigh
the benefit for tiny tasks. - Pools are most useful when task size and
workload justify their overhead.

------------------------------------------------------------------------

## 24. The Python GIL

The **Global Interpreter Lock (GIL)** in standard GIL-enabled CPython
allows only one thread at a time to execute Python bytecode within a
given interpreter.

Practical implications:

-   Multiple threads can still help with I/O-bound work because blocking
    I/O commonly releases the GIL while waiting.
-   Threads generally do not provide CPU-parallel execution for
    pure-Python CPU-bound code in standard GIL-enabled CPython.
-   Multiple processes can run Python code in parallel on different
    cores.
-   Some native libraries release the GIL while doing work.
-   Free-threaded Python builds also exist, so the GIL model is not
    universal to every Python build.

Do not treat the GIL as a general-purpose lock for your application's
shared data. Use explicit synchronization where required.

------------------------------------------------------------------------

## 25. Asyncio and Event Loops

`asyncio` supports asynchronous programming using an **event loop** that
schedules and coordinates coroutines and tasks.

It is particularly useful for high-concurrency I/O when the operations
use non-blocking asynchronous APIs.

Mental model:

1.  A coroutine runs until it reaches an `await` that cannot complete
    immediately.
2.  It suspends, allowing the event loop to run other ready work.
3.  When the awaited operation completes, the coroutine can resume.

An event loop typically runs tasks cooperatively on its thread. If a
task performs long-running synchronous work without yielding, other
tasks on that loop may be delayed.

Example:

``` python
import asyncio

async def fetch_document(name):
    print(f"Starting {name}")
    await asyncio.sleep(1)  # Placeholder for asynchronous I/O
    print(f"Finished {name}")

async def main():
    await asyncio.gather(
        fetch_document("A"),
        fetch_document("B"),
    )

asyncio.run(main())
```

The sleep is only a demonstration of yielding asynchronously; a real
application would use an async-capable network or file library.

------------------------------------------------------------------------

## 26. Coroutines, `await`, and `create_task`

Calling an `async def` function creates a **coroutine object**. Calling
it alone does not run its body to completion or automatically schedule
it.

``` python
async def task_b():
    print("task_b runs")

async def main():
    coroutine = task_b()  # Creates a coroutine object
    await coroutine      # Runs it as part of this coroutine
```

Alternatively, while an event loop is running, `asyncio.create_task()`
schedules a coroutine as a task:

``` python
async def task_a():
    await asyncio.sleep(1)
    print("task_a finished")

async def main():
    task = asyncio.create_task(task_a())
    print("Main continues")
    await task

asyncio.run(main())
```

`create_task()` schedules the coroutine; it does not guarantee that the
coroutine body executes immediately before the next line. The event loop
runs it when it gets an opportunity.

### Important distinctions

-   `await coroutine`: waits for the coroutine's result and suspends the
    current coroutine when needed.
-   `asyncio.create_task(coroutine)`: schedules the coroutine to run
    concurrently with other tasks on the loop.
-   `coroutine_function()`: creates a coroutine object; by itself, it
    does not schedule the coroutine.
-   Blocking synchronous code on the event-loop thread can delay other
    tasks.

For CPU-heavy synchronous work, consider moving it to an appropriate
executor or process pool rather than blocking the event loop.

------------------------------------------------------------------------

## 27. The Concurrency Mental Model

Use these questions when designing a program:

1.  **What kind of work is it?** CPU-bound, I/O-bound, or a mixture?
2.  **What must be shared?** Is shared mutable state necessary?
3.  **What is the execution boundary?** Same thread, same process, or
    separate processes?
4.  **How will tasks coordinate?** Locks, semaphores, queues, or another
    mechanism?
5.  **How will results move?** Return values, queues, pipes, shared
    memory, or messages?
6.  **What limits concurrency?** CPU cores, memory, database
    connections, remote-service limits, or worker count?
7.  **What can prevent progress?** Blocking operations, deadlocks,
    starvation, or an event loop that does not yield?
8.  **How will performance be verified?** Measure runtime, throughput,
    latency, memory use, and failure behavior.

------------------------------------------------------------------------

## AI Engineering Connections

### Document ingestion for RAG

A document ingestion pipeline might: - Fetch many documents with async
I/O or threads. - Use a semaphore to limit concurrent requests. - Parse
or transform CPU-heavy content using a bounded process pool when
appropriate. - Use a queue to pass jobs and results between pipeline
stages. - Protect shared mutable metadata with suitable synchronization.

### FastAPI services

-   Async endpoints are useful when they call asynchronous I/O
    libraries.
-   Blocking calls inside an async endpoint can stall the event loop.
-   Database connection pools and semaphores can help limit concurrent
    resource usage.
-   CPU-heavy tasks may need a process pool, background worker, or
    separate service, depending on their size and operational
    requirements.

### LLM applications

-   Concurrently retrieve documents or call independent external
    services where appropriate.
-   Respect rate limits and cap concurrency.
-   Use queues and worker pools for background processing.
-   Measure latency, throughput, resource use, and error rates before
    optimizing.

Concurrency is not automatically faster. It adds coordination, resource
use, and failure modes; choose it to match the workload.

------------------------------------------------------------------------

## Common Misconceptions

1.  **"Concurrency means two things execute at the exact same time."**\
    Not necessarily. Tasks can make overlapping progress through
    interleaving on one core.

2.  **"Threads have separate heaps."**\
    Threads in the same process generally share the process heap, but
    each thread has its own stack.

3.  **"A lock makes every part of the program thread-safe."**\
    Only access coordinated by the appropriate locking protocol is
    protected.

4.  **"A semaphore is just another name for a mutex."**\
    A mutex permits one holder; a semaphore can permit a configured
    number of holders.

5.  **"A child process can change the parent's ordinary local
    variable."**\
    Not by default. Use IPC or shared memory where appropriate.

6.  **"Python threads always speed up CPU-heavy Python code."**\
    Not in standard GIL-enabled CPython for pure-Python CPU-bound work.

7.  **"Calling an async function means it starts running."**\
    It creates a coroutine object. Await it or schedule it.

8.  **"Asyncio makes CPU-heavy code non-blocking automatically."**\
    CPU-heavy synchronous work still blocks the event-loop thread unless
    moved or structured to yield.

9.  **"More workers always mean better performance."**\
    Extra workers can increase overhead, memory pressure, and
    contention.

------------------------------------------------------------------------

## Final Revision Checklist

You should be able to explain, in your own words:

-   [ ] Process vs. thread, including memory and stack differences
-   [ ] CPU cores, scheduling, and context switching
-   [ ] Concurrency vs. parallelism
-   [ ] Shared state, race conditions, and lost updates
-   [ ] Critical sections, locks, mutexes, and semaphores
-   [ ] Deadlock vs. starvation
-   [ ] Synchronization and IPC
-   [ ] Pipes, queues, shared memory, and worker pools
-   [ ] Threading vs. multiprocessing in Python
-   [ ] Process pools and bounded worker counts
-   [ ] The GIL and its practical implications
-   [ ] Event loops, coroutines, `await`, and `create_task()`
-   [ ] Why blocking code can stall an event loop
-   [ ] How to choose a concurrency strategy for AI/backend workloads

## Module Completion

**Module 00.4 --- Processes, Threads, and Concurrency: Completed.**

Final consolidation quiz result: **10/10**.

Next module in the learning roadmap: **Module 00.5 --- Big O &
Computational Complexity**.
