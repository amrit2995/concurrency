import asyncio

class PowerError(Exception):
    def __init__(self, message="Power calculation error"):
        self.message = message
        super().__init__(self.message)

async def power(val):
    squared = val**2
    if squared > 2147483647:
        raise PowerError("Power calculation error: Result exceeds maximum integer value")
    return squared


async def main():
    try:
        result = await power(463)
        print(f"Result: {result}")
    except PowerError as e:
        print("Error",e.message)

asyncio.run(main())