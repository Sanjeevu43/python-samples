import asyncio

async def task1(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")
    return f"Result from {name}"

async def main():
    results = await asyncio.gather(
        task1("A", 2),
        task1("B", 1),
        task1("C", 3),
    )

    print("All tasks completed.")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())