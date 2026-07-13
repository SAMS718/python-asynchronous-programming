#we are using (pokeapi.co) to the receive and work on requests as a part of HTTP.
import aiohttp
import requests
import time
import asyncio

start = time.time()

async def main(): #main coroutine.
    async with aiohttp.ClientSession() as session: #mainly useful to handle the asynchronous requests without any issues in the name of "session"...
        for i in range(1,151):
            url = 'https://pokeapi.co/api/v2/pokemon/6' + str(i)
            async with session.get(url) as resp: #gathering resp in async programming(not by using direct variable).
                pokemon_name = await resp.json() #for simultaneous gathering we're using await here...
                print(pokemon_name['name'])

asyncio.run(main()) #running main coroutine.
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) #To avoid the final exception error...
end = time.time()
print(f"Execution time : {end - start}secs") #Around 25 secs...