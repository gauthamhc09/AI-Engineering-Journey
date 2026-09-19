import asyncio

async def task1():
    print("Task 1")
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    print("Task 2")
    await asyncio.sleep(2)
    print("Task 2 done")
    
# t1 = asyncio.create_task(task1)
# t2 = asyncio.create_task(task2)

async def fetch_user():
    await asyncio.sleep(2)
    return "User data"

async def fetch_documents():
    await asyncio.sleep(3)
    return "Documents"

async def run_fun():
    user = await fetch_user()
    documents = await fetch_documents()
    
    print(user, documents)

asyncio.run(run_fun())


