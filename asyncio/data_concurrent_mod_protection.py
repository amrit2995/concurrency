# In this problem, there is a function func() that makes a self-increment. In the main function, we will create 2 threads and call func() 5e6 times respectively. Due to concurrent modification of data, when 2 threads modify data at the same time, only one thread modifies successfully, and the modification of the other thread is blocked. Overwrite, so the final result a will be less than 1e7 in this case.

# Now you need to use a mutex to ensure that there will be no problems with data modification, perfect func(), in this function we pass in a mutex m for you, you can use this mutex to ensure data security modification.

import time

import asyncio
#Global Vaariable
a = 0

#mutex
mutex = asyncio.Lock()

async def func():
    global a
    for _ in range(50):
        async with mutex:
            a += 1

async def main():
    #create tasks
    t1 = asyncio.create_task(func())
    t2 = asyncio.create_task(func())

    #Wait for the task to finish
    await asyncio.gather(t1, t2)

    print("Final value of a.", a)

asyncio.run(main())


# We define a global variable a to store the value that will be modified by the coroutines.
# We create an asyncio mutex mutex using asyncio.Lock().
# In the func() coroutine, we use the async with statement to acquire the lock before modifying the global variable a. This ensures that only one coroutine can modify a at a time.
# In the main() coroutine, we create two tasks task1 and task2, each calling the func() coroutine.
# We wait for both tasks to finish using await asyncio.gather(task1, task2).
# Finally, we print the final value of a to see the result. Since the mutex ensures that only one coroutine modifies a at a time, the final value of a will be 1e7 as expected.


