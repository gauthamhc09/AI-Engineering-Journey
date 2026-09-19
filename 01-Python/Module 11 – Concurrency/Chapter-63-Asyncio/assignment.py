# "Explain my portfolio risk"

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