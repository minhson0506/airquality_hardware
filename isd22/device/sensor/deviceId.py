#!/usr/bin/env python

import os
from pymongo import MongoClient
from bson.objectid import ObjectId

def generate_and_load_id():
    #external file path
    file_path = "id.txt"  

    # Check if id.txt exist and contains an ID
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            loaded_id = file.read().strip()
            try:
                loaded_object_id = ObjectId(loaded_id)
                print("Found Id # :", loaded_object_id)
                return loaded_object_id
            except:
                print("Error uploading Id.")

    # Generate a new Id
    new_id = ObjectId()

    # Save Id in an external file
    with open(file_path, "w") as file:
        file.write(str(new_id))

    print("A new Id have been generated: ", new_id)
    return new_id

if __name__ == "__main__":
    generate_and_load_id()
