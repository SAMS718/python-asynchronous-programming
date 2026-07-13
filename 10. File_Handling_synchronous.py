import time

start = time.time()

def fetch_file():
    print("Starting to fetch a File")
    time.sleep(1)
    print("Fetching File Completed")

def main():
    print("starting main")
    #Calling function for 3 times and it's taking 3 secs to execute...
    fetch_file()
    fetch_file()
    fetch_file()
    print("main completed")

main()

end = time.time()
print(f"Execution Time : {end - start}")
