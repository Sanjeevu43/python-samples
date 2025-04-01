import asyncio

async def my_coroutine():
    print("Hello from coroutine!")
    await asyncio.sleep(30)  # Simulate an I/O-bound operation
    print("Coroutine finished.")

async def main():
    print("Starting main function")
    await my_coroutine()
    print("Main function finished")

if __name__ == "__main__":
    asyncio.run(main())
    #main()

#asyncio.run(main()) starts the event loop and runs the main coroutine.