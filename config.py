import json

config_file = open("config.json","w")

key_count = int(input("How many keys? 4 or 8: "))
while(key_count not in (4,8)):
    print("Invalid response! ",end="")
    key_count = int(input("How many keys? 4 or 8: "))

