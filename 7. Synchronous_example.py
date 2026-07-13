import time
start = time.time() #present time while code is at this line...

def get_movie():
    time.sleep(7)
    print("Tickets Got Booked!!!")

def like_ig():
    time.sleep(3)
    print("You liked a picture!!!")

def main(): #handling execution for both the above functions...
    get_movie()
    like_ig()

main()
end = time.time()
print(f"The time for both the activities to complete is : {end - start}") #values in seconds...
