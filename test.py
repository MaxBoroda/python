import json
import re



inputfile = open("users.json")

myfile = json.load(inputfile)

print(myfile)
#for line in myfile:
#    print(line.strip())