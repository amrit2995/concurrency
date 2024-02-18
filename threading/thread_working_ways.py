import asyncio

async def at():
    print("thread starter")
    asyncio.sleep(2)
    print("thread end")

# async def main():
#     t1 = asyncio.create_task(at()) # daemon mode # Create a task
#     Don't await the task, allowing it to run in the background
#     print("main coroutine completed")


async def main():
    await at()
    print("main coroutine completed")

asyncio.run(main())