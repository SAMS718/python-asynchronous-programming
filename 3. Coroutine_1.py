#A function which is very cooperative is considered as a CoRoutine... there should be a fluid exchange btw two individual functions then they were considered as COde_Routines.

import asyncio #helps running coroutine in asynchronous fashion.

async def main():
    print("started")

#to execute a co routine function we need a event loop which is Asyncio runs this automatically.
asyncio.run(main())

