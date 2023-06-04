

import os
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
from deviceId import generate_and_load_id

def generate_name():
    # Path to the external file
    file_path = "name.txt"  

    # Check if the file name.txt exist and contains a string
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            loaded_name = file.read().strip()
            try:
                print("Device Name:", loaded_name)
                return loaded_name
            except:
                print("Name not found.")

    # Generate a new name
    stem_name = "ISD"
    number = random.randint(0, 1000)
    new_name = (stem_name + str(number))
	

    # Save the name in an external file
    with open(file_path, "w") as file:
        file.write(new_name)

    print("A new name has been generated: ", new_name)

    #copy values into the diccionary
    device = {}
    device['deviceId'] = str(generate_and_load_id())
    device['deviceName'] = new_name
    print (device)

    #Establish conecction with MongoDB Atlas
    client = MongoClient("mongodb URI") #to be replaced
    db = client["innovation"]
    collection = db["devices"]
    collection.insert_one(device)
    return new_name

if __name__ == "__main__":
    generate_name()
