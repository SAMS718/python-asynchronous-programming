#we are using (pokeapi.co) to the receive and work on requests as a part of HTTP.
import requests
import time

start = time.time()
#print(resp.status_code) #200-> website is working ; 404-> Error in Loading, etc...

#printing down every pokemon names from key value pairs synchronously...
for i in range(1,151):
    url = 'https://pokeapi.co/api/v2/pokemon/6' + str(i)
    resp = requests.get(url) #sending response through request library and resp variable stores it..
    pokemon_name = resp.json() #returns json keyvalue pairs accordingly...
    print(pokemon_name['name']) # Extracting only pokemon name from key value pair

end = time.time()
print(f"Execution time : {end - start}secs") #approx 83 secs...