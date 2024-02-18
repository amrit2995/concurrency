import asyncio

async def my_task():
    print("task started")
    try:
        while True:
            await asyncio.sleep(1)
            print("thread running")
    except asyncio.CancelledError:
        print("thread cancelled")

async def main():
    thread = asyncio.create_task(my_task())
    print(f"Task running {not thread.done()}") #check if the task is running

    await asyncio.sleep(5) #simulate some work

    thread.cancel() #interrupt the task
    await asyncio.sleep(1) #wait for the task to stop

    print(f"Task running: {not thread.done()}") #check if the task is running


asyncio.run(main())