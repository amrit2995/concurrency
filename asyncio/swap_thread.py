import asyncio

def func(task1, task2):
    task1_coro = task1.get_coro()
    task1._coro = task2.get_coro()
    task2._coro = task1_coro

async def t1_func():
    print("hello 1")

async def t2_func():
    print("hello 2")

async def main():
    t1 = asyncio.create_task(t1_func())
    t2 = asyncio.create_task(t2_func())
    t1id = t1.get_coro()
    t2id = t2.get_coro()
    await func(t1, t2)
    if (id(t1) == t2id and id(t2) == t1id):
        return True
    else:
        return False

asyncio.run(main())
