import asyncio

async def task1(): 
    print("task started")
    await asyncio.sleep(7)
    print("task ended")

async def main():
    t1 = asyncio.create_task(task1())
    await asyncio.sleep(1)
    print(f"task{' ' if t1.done() else ' not '}done")
    await t1
    print(f"task{' ' if t1.done() else ' not '}done")

asyncio.run(main())