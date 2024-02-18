import asyncio


async def sleep_three_seconds():
    await asyncio.sleep(3)

async def main():
    loop  = asyncio.get_event_loop()
    start_time = loop.time()
    await sleep_three_seconds()
    end_time = loop.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime}")

asyncio.run(main())