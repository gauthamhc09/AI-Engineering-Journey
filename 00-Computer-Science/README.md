# Computer Science

# 00 --- Computer Science Foundation

This section builds the Computer Science foundation required to become a
strong Python developer, Backend Engineer, and eventually AI/LLM
Engineer.

The goal is **deep understanding**, not memorization or rushing through
topics.

------------------------------------------------------------------------

## Learning Philosophy

-   Learn one concept at a time.
-   Understand **WHY** before **HOW**.
-   Start from first principles.
-   Connect concepts to Python and real systems.
-   Use practical exercises and reasoning questions.
-   Revisit difficult concepts until the mental model is clear.
-   Connect foundational concepts to Backend Engineering, AI
    Engineering, LLM applications, RAG, AI Agents, databases, APIs, and
    production systems.

------------------------------------------------------------------------

# Module 00.1 --- Computer Fundamentals

Understand what a computer actually does and how software eventually
becomes execution on hardware.

### Topics

1.  What Is a Computer?
2.  Hardware vs Software
3.  CPU
4.  CPU Cores
5.  Registers
6.  ALU and Control Unit
7.  RAM
8.  Cache
9.  Storage
10. SSD vs HDD
11. Memory Hierarchy
12. Bits and Bytes
13. Binary Representation
14. Hexadecimal
15. Data Representation
16. Machine Instructions
17. How a Program Runs
18. CPU ↔ Memory Interaction
19. Computer Execution Model

### Goal

Build the mental model:

``` text
Python Code
    ↓
Python Runtime
    ↓
Operating System
    ↓
CPU + Memory
    ↓
Machine Instructions
    ↓
Execution
```

------------------------------------------------------------------------

# Module 00.2 --- Operating Systems

Understand what the Operating System does and how it manages hardware
and running programs.

### Topics

1.  What Is an Operating System?
2.  Kernel
3.  User Space vs Kernel Space
4.  System Calls
5.  What Is a Process?
6.  Process Lifecycle
7.  Process States
8.  Process Creation
9.  Process Termination
10. Process Scheduling
11. CPU Scheduling
12. Context Switching
13. Threads
14. Thread Lifecycle
15. Process vs Thread
16. Shared Memory
17. Virtual Memory
18. Memory Isolation
19. Stack vs Heap
20. File Descriptors
21. Process Resources

### Goal

Understand the relationship between:

``` text
Application
   ↓
Process
   ↓
Thread
   ↓
OS Scheduler
   ↓
CPU
   ↓
Memory
```

------------------------------------------------------------------------

# Module 00.3 --- Memory

Build a deep mental model of how programs use memory.

### Topics

1.  RAM and Physical Memory
2.  Virtual Memory
3.  Virtual Addresses
4.  Pages
5.  Page Tables
6.  Memory Allocation
7.  Stack Memory
8.  Heap Memory
9.  References and Pointers
10. Python Objects in Memory
11. Python Variables and References
12. Garbage Collection
13. Memory Leaks
14. CPU Cache and Locality
15. Memory Access Cost

### Python Connection

Understand what happens conceptually when we write:

``` python
a = [1, 2, 3]
```

What exists in memory? What does `a` represent? Where is the list? What
happens when the object is no longer needed?

------------------------------------------------------------------------

# Module 00.4 --- Processes, Threads & Concurrency

Rebuild Python concurrency knowledge from operating-system fundamentals.

### Topics

1.  Process vs Thread --- Deep Dive
2.  CPU Core and Execution
3.  Scheduling and Execution
4.  Context Switching
5.  Concurrency
6.  Parallelism
7.  Shared State
8.  Race Conditions
9.  Critical Sections
10. Locks
11. Mutex
12. Semaphores
13. Deadlocks
14. Starvation
15. Synchronization
16. Inter-Process Communication
17. Pipes
18. Queues
19. Shared Memory IPC
20. Worker Pools
21. Python Threading
22. Python Multiprocessing
23. Python Process Pools
24. Python GIL
25. asyncio and Event Loops
26. Coroutines and await
27. Concurrency Mental Model

### Goal

Make these Python concepts intuitive:

``` python
threading.Thread
multiprocessing.Process
multiprocessing.Pool

async def
await
asyncio.create_task()
asyncio.gather()
```

------------------------------------------------------------------------

# Module 00.5 --- Big O & Computational Complexity

Learn to reason about how algorithms behave as data grows.

### Topics

1.  What Is an Algorithm?
2.  Why Complexity Matters
3.  Time Complexity
4.  Space Complexity
5.  Big O Notation
6.  O(1)
7.  O(log n)
8.  O(n)
9.  O(n log n)
10. O(n²)
11. O(2ⁿ)
12. Best / Average / Worst Case
13. Amortized Complexity
14. Complexity in Real Systems

### Goal

Learn to look at code and reason about:

``` text
How much work?
How does the work grow?
How much memory?
What happens with 1 million records?
```

Connect this to databases, embeddings, vector search, RAG, and AI
pipelines.

------------------------------------------------------------------------

# Module 00.6 --- Data Structures

Understand why different ways of organizing data exist and when each
structure is useful.

### Topics

1.  Why Data Structures?
2.  Arrays
3.  Python Lists
4.  Linked Lists
5.  Stacks
6.  Queues
7.  Hash Tables
8.  Python Dictionaries
9.  Sets
10. Trees
11. Binary Trees
12. Binary Search Trees
13. Heaps and Priority Queues
14. Graphs
15. Tries
16. Choosing the Right Data Structure

### For Every Data Structure

Understand:

-   What problem does it solve?
-   How does it work internally?
-   What are the trade-offs?
-   What is the time complexity?
-   When should I use it?
-   How does Python implement/use it?
-   Where does it appear in AI systems?

------------------------------------------------------------------------

# Module 00.7 --- Algorithms

Develop algorithmic thinking rather than memorizing interview tricks.

### Topics

1.  Algorithmic Thinking
2.  Linear Search
3.  Binary Search
4.  Sorting Concepts
5.  Bubble Sort
6.  Insertion Sort
7.  Merge Sort
8.  Quick Sort
9.  Recursion
10. Divide and Conquer
11. Two Pointers
12. Sliding Window
13. Hashing-Based Algorithms
14. Tree Traversal
15. BFS
16. DFS
17. Graph Algorithms
18. Greedy Algorithms
19. Dynamic Programming
20. Memoization

------------------------------------------------------------------------

# Module 00.8 --- Networking

Build the foundation needed for Backend and AI systems.

### Topics

1.  What Is a Network?
2.  Client and Server
3.  IP Addresses
4.  MAC Addresses
5.  Ports
6.  TCP
7.  UDP
8.  HTTP
9.  HTTPS
10. DNS
11. Request and Response
12. HTTP Methods
13. HTTP Status Codes
14. HTTP Headers
15. Cookies
16. Sessions
17. TLS
18. REST APIs
19. WebSockets
20. Connection Lifecycle
21. Python HTTP Clients
22. FastAPI Request Lifecycle

### Goal

Understand what actually happens when:

``` python
requests.get(...)
```

or when a FastAPI endpoint receives a request.

Connect this to:

-   LLM APIs
-   Vector DB APIs
-   Microservices
-   Cloud systems
-   AI Agents

------------------------------------------------------------------------

# Module 00.9 --- Databases

Build the database mental model needed for Backend and AI applications.

### Topics

1.  What Is a Database?
2.  Relational Databases
3.  Tables, Rows and Columns
4.  Primary Keys
5.  Foreign Keys
6.  Indexes
7.  B-Tree Concept
8.  SQL
9.  SELECT Queries
10. Joins
11. Transactions
12. ACID
13. Isolation
14. Database Locks
15. Query Execution
16. Connection Pools
17. PostgreSQL
18. Database Performance

### Project Connection

Apply these concepts directly to the Portfolio Intelligence application.

Understand why:

``` sql
SELECT ...
```

can be fast or slow depending on indexes, query structure, data volume,
and database execution.

------------------------------------------------------------------------

# Module 00.10 --- Storage & File Systems

Understand how persistent data is organized and accessed.

### Topics

1.  What Is Storage?
2.  Files
3.  Directories
4.  File Systems
5.  File Paths
6.  File Metadata
7.  Blocks
8.  Disk I/O
9.  Buffering
10. Sequential vs Random Access
11. File Permissions
12. SSD vs RAM
13. Why File I/O Is Slower
14. Python File I/O

### Python Connection

Connect this directly to Python file handling and the behavior of file
operations.

------------------------------------------------------------------------

# Module 00.11 --- Compilers, Interpreters & Runtimes

Understand what happens between Python source code and execution.

### Topics

1.  Compiler
2.  Interpreter
3.  Compiler vs Interpreter
4.  Bytecode
5.  Virtual Machines
6.  Runtime
7.  CPython
8.  Python Parsing
9.  Python Bytecode
10. CPython Execution Model
11. GIL --- Revisited
12. Python Garbage Collection
13. Python Execution Trace

### Goal

Build this mental model:

``` text
.py
 ↓
Parsing
 ↓
Bytecode
 ↓
CPython Runtime
 ↓
Execution
```

------------------------------------------------------------------------

# Module 00.12 --- Software Engineering Foundations

Build engineering habits that scale from small programs to production AI
systems.

### Topics

1.  Abstraction
2.  Modularity
3.  Coupling
4.  Cohesion
5.  Interfaces
6.  APIs
7.  Separation of Concerns
8.  SOLID Principles
9.  Error Handling
10. Logging
11. Testing
12. Unit Testing
13. Integration Testing
14. Debugging
15. Git Fundamentals
16. Configuration
17. Environment Variables

### Goal

Connect software engineering principles to production AI systems.

------------------------------------------------------------------------

# Module 00.13 --- Distributed Systems

Understand how applications behave when multiple machines/services
communicate over networks.

### Topics

1.  What Is a Distributed System?
2.  Service-to-Service Communication
3.  Latency
4.  Throughput
5.  Scalability
6.  Vertical vs Horizontal Scaling
7.  Load Balancing
8.  Caching
9.  Queues
10. Message Brokers
11. Retries
12. Timeouts
13. Idempotency
14. Fault Tolerance
15. Replication
16. Event-Driven Architecture
17. Eventual Consistency
18. CAP Theorem

### AI Engineering Connection

Apply these concepts to:

-   AI APIs
-   RAG systems
-   Agent systems
-   Vector databases
-   Model serving
-   Production AI architectures

------------------------------------------------------------------------

# Module 00.14 --- AI Engineering System Foundations

Bring everything together into an end-to-end AI system mental model.

### Topics

1.  Computer to AI System
2.  CPU, Memory and OS in AI Applications
3.  Networking in AI Applications
4.  Databases in AI Applications
5.  Storage in AI Applications
6.  Concurrency in AI Applications
7.  Distributed Systems in AI
8.  RAG System Architecture
9.  Agent System Architecture
10. Vector Database Architecture
11. LLM API Architecture
12. Model Serving Concepts
13. Portfolio Intelligence System Architecture

### Final Architecture

We should eventually be able to reason through an architecture like:

``` text
                    User
                      │
                      ▼
                API Gateway
                      │
                      ▼
                 FastAPI
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     PostgreSQL   Vector DB    LLM API
          │           │           │
          └───────────┼───────────┘
                      ▼
                 AI Response
```

And explain what happens at every layer:

``` text
CPU
Memory
OS
Processes
Threads
Networking
Databases
Storage
Distributed Systems
AI/LLM Components
```

------------------------------------------------------------------------

# Final Computer Science Mental Model

By the end of this foundation, the goal is to move from:

> "I know how to use the Python API."

to:

> "I understand what the system underneath that API is doing."

The progression is:

``` text
Computer Fundamentals
        ↓
Operating Systems
        ↓
Memory
        ↓
Processes & Concurrency
        ↓
Complexity
        ↓
Data Structures
        ↓
Algorithms
        ↓
Networking
        ↓
Databases
        ↓
Storage
        ↓
Python Runtime
        ↓
Software Engineering
        ↓
Distributed Systems
        ↓
AI Engineering Systems
```

This foundation will then support the longer journey:

``` text
Computer Science
       ↓
Python
       ↓
Backend Engineering
       ↓
AI / ML Fundamentals
       ↓
LLM Engineering
       ↓
Embeddings
       ↓
Vector Databases
       ↓
RAG
       ↓
AI Agents
       ↓
AI Systems
       ↓
Production AI Engineering
       ↓
Deeper Model / Systems Understanding
```

------------------------------------------------------------------------

## Chapter Learning Format

Every chapter will eventually contain:

``` text
README.md
practice.py
```

And every chapter will follow:

1.  First-principles explanation
2.  Why it matters
3.  Analogy when useful
4.  Actual technical model
5.  Python examples where appropriate
6.  Small exercise
7.  User attempts the exercise
8.  Reasoning evaluation
9.  Corrections/refinement
10. AI Engineering connection

At the end of each chapter:

-   Summary
-   Key concepts
-   Common mistakes
-   AI Engineering connection
-   Revision questions

**The folder structure is the roadmap. It does not determine the speed.
We will still learn one concept at a time.**

