import json
from numpy import array as arr

config_file = open("config.json","w")

alphabet = arr([chr(a) for a in range(65,91,1)])

#TODO change to pynput as to read special keys like control_R

def invalid_response(reason)->None:
    print("Invalid response! - " + reason)

def set_keys(key_count):
    keys = dict()
    for i in range(1,key_count+1):
        new_key = input(f"Key {i} - Enter a single character (ex: a): ") 
        while(len(new_key)>1):
            invalid_response("Only enter a single/valid character (ex: a): ")
            new_key = input(f"Key {i} - Enter a single character (ex: a): ")
        keys[f"key{i}"] = new_key.lower() if new_key in alphabet else new_key
    json.dump(keys, config_file, indent=2)

    
key_count = int(input("How many keys? 4 or 8: "))
while(key_count not in (4,8)):
    invalid_response("Only valid options are 4 or 8")
    key_count = int(input("How many keys? 4 or 8: "))

set_keys(key_count=key_count)

print("keys set")

