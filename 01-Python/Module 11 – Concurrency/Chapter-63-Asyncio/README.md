# Chapter 63 — Async in Python

## Core idea

Asynchronous programming lets a program coordinate multiple tasks that spend time waiting, especially for I/O.

> While one task is waiting, another async task can make progress.

Typical I/O:
- HTTP/API calls
- Database queries
- Network operations
- LLM API calls
- Vector database calls

## `async def`

```python
async def fetch_data():
    ...
```

Defines a **coroutine function**. Calling it produces a coroutine object; it must be run by an event loop.

```python
import asyncio

asyncio.run(fetch_data())
```

## Event loop

The event loop coordinates async tasks:

```text
Event Loop
   ├── Task A → await → pause
   ├── Task B → run
   └── Task C → await → pause
```

A typical asyncio program uses one event-loop thread and cooperative scheduling.

## `await`

```python
async def task():
    print("A")
    await asyncio.sleep(2)
    print("B")
```

`await` pauses the current coroutine while the awaited async operation is pending, allowing the event loop to run other async tasks.

The important idea is not simply "wait"; it is:

> Wait without blocking the event-loop thread.

## `asyncio.sleep()` vs `time.sleep()`

Async:

```python
await asyncio.sleep(5)
```

pauses the coroutine and allows other async work to run.

Blocking:

```python
time.sleep(5)
```

blocks the thread running the event loop.

`async def` does **not** magically make blocking code asynchronous.

## Sequential vs concurrent async

Sequential:

```python
user = await fetch_user()
documents = await fetch_documents()
```

If the first takes 2 seconds and the second 3 seconds:

**Total ≈ 5 seconds.**

Concurrent:

```python
user_task = asyncio.create_task(fetch_user())
documents_task = asyncio.create_task(fetch_documents())

user = await user_task
documents = await documents_task
```

Both are scheduled before waiting for results, so their I/O waits overlap.

**Total ≈ 3 seconds.**

## `asyncio.create_task()`

```python
task = asyncio.create_task(coroutine())
```

Schedules a coroutine with the event loop so it can make progress concurrently with other scheduled tasks.

It does not mean CPU-parallel execution.

## `asyncio.gather()`

Conveniently runs multiple awaitables concurrently and collects their results:

```python
results = await asyncio.gather(
    fetch_user(),
    fetch_documents()
)
```

Or:

```python
user, documents = await asyncio.gather(
    fetch_user(),
    fetch_documents()
)
```

## AI Engineering example

```python
import asyncio

async def call_llm():
    print("LLM: Request started")
    await asyncio.sleep(2)
    print("LLM: Response received")
    return "LLM response"

async def search_vector_db():
    print("Vector DB: Search started")
    await asyncio.sleep(3)
    print("Vector DB: Results received")
    return "Relevant documents"

async def get_user_profile():
    print("User API: Request started")
    await asyncio.sleep(1)
    print("User API: Response received")
    return "User profile"

async def main():
    llm_task = asyncio.create_task(call_llm())
    vector_task = asyncio.create_task(search_vector_db())
    user_task = asyncio.create_task(get_user_profile())

    llm_result = await llm_task
    vector_result = await vector_task
    user_result = await user_task

    print(llm_result)
    print(vector_result)
    print(user_result)

asyncio.run(main())
```

The simulated waits are 2, 3, and 1 seconds, so the total is approximately **3 seconds**, not 6.

## Threads vs multiprocessing vs async

```text
Threads          → often useful for I/O-bound concurrency
Multiprocessing  → often useful for CPU-bound parallel work
Async            → often useful for many I/O-bound operations
```

### Mental model

```text
Thread
  → execution path inside a process

Process
  → independent execution environment with its own memory

Pool
  → group of worker processes managed for you

Async Task
  → coroutine scheduled by an event loop

await
  → pause current coroutine and let other async work run
```

## Common mistakes

1. Thinking `async def` automatically makes code concurrent.
2. Using sequential `await task1(); await task2()` when independent tasks could be scheduled together.
3. Calling `time.sleep()` inside async code.
4. Thinking async automatically means multiple CPU cores.
5. Confusing concurrency with parallelism.

## Module 11 — Concurrency complete

- Chapter 61 — Threads ✅
- Chapter 62 — Multiprocessing ✅
- Chapter 63 — Async ✅

### Final takeaway

> **Threads → I/O-bound concurrency**
>
> **Multiprocessing → CPU-bound parallelism**
>
> **Async → I/O-bound concurrency through an event loop**
>
> **`await` → pause the current coroutine without blocking the event loop**
>
> **`create_task()` → schedule a coroutine**
>
> **`gather()` → run multiple awaitables concurrently and collect results**

## AI Engineering connection

A future AI backend may coordinate database, vector DB, and LLM API calls asynchronously, while CPU-heavy preprocessing may be delegated to worker processes. The correct concurrency model depends on the actual bottleneck.
