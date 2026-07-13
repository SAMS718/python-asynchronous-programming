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
    task1 = asyncio.create_task(get_movie()) #converting movieticket func into task.
    task2 = asyncio.create_task(like_ig())
    await task1 #awaiting it beacause you are liking pictures during in line for movie tickets so entire activity completed in 7 seconds...

asyncio.run(main())

end = time.time()
print(f"The time for both the activities to complete is : {end - start}") #values in seconds... (here it took 7.xxxx for both activities).