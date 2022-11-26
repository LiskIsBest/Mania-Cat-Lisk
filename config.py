import json

config_file = open("config.json","w")

alphabet = [chr(a) for a in range(65,91,1)]

def invalid_response(reason)->None:
    print("Invalid response! - " + reason)

def set_keys():
    keys = dict()
    for i in range(1,5):
        new_key = input(f"Key {i} - Enter a single character (ex: a): ") 
        while(len(new_key)>1):
            invalid_response("Only enter a single/valid character (ex: a): ")
            new_key = input(f"Key {i} - Enter a single character (ex: a): ")
        keys[f"key{i}"] = new_key.lower() if new_key in alphabet else new_key
    json.dump(keys, config_file, indent=2)

set_keys()

print("keys set")

