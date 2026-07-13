import asyncio
loop = asyncio.new_event_loop() #using asyncio's functions...
#print(loop) -> #in this direct case loop doesn't run.(Refer screenshots)
#defining a task
task = asyncio.sleep(2)
#executing it using our loop
loop.run_until_complete(task)
print("Done")