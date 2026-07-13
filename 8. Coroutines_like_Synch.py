#This code is just coroutine version of previous code which take the same time

import time
import asyncio
start = time.time() #present time while code is at this line...

async def get_movie(): #coroutine 1
    await asyncio.sleep(7) #no "time.xxxxxxxx" in asyncio.
    print("Tickets Got Booked!!!")

async def like_ig(): #coroutine 2
    await asyncio.sleep(3)
    print("You liked a picture!!!")

async def main(): #handling execution for both the above functions...
    await get_movie()
    await like_ig()

asyncio.run(main())

end = time.time()
print(f"The time for both the activities to complete is : {end - start}") #values in seconds...