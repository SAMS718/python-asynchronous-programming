import time
import asyncio

start = time.time()

async def fetch_file(): #coroutine 1
    print("Starting to fetch a File")
    await asyncio.sleep(1)
    print("Fetching File Completed")

async def main(): #main coroutine.
    print("starting main")
    await asyncio.gather(fetch_file(),fetch_file(),fetch_file()) #asyncio.gather is mainly useful to combine every function and to execute instead of calling individually...
    print("main completed")

asyncio.run(main())

end = time.time()
print(f"Execution Time : {end - start}") #observe the difference after executing...
#here it starts fetching every file initially and then fetches got completed.
#a change in printing order...
