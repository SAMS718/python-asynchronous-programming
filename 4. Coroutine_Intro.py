import asyncio #available in python 3.11 and above no need to install.

#coroutine function
async def main(): 
    print("Started Asyncio in Python")

#print(main()) -> prints individual object id of coroutine function  rather than function.

asyncio.run(main()) #how we run asyncio functions...