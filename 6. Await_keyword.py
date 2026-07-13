#Await should always be inside a Co-Routine Function, Not outside it...
import asyncio

async def square(num): #coroutine func1
    return num**2

async def main(): #coroutine func2
    x = await square(5) #here Await is useful in a way that after square(5) it's holding this coroutine func2 and going to func1 to print the required square value.
    print(x)

    y = await square(10)
    print(y)

    z = x+y
    print(z)

asyncio.run(main()) #generic event_loop

#Basically, This code works like a basic synchronous programme function; Working further it will be deep.



    