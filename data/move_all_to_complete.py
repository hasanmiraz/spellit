import os
import json

final_array = {}

folders = os.listdir("src_data")

for folder in folders:
    files = os.listdir(f"src_data/{folder}")

    json_files = [file for file in files if ".json" in file]
    with open(f"src_data/{folder}/{json_files[0]}") as errorfile:
        final_array[folder] = json.load(errorfile)

with open("errorLog.json", "w") as errorLog:
    json.dump(final_array, errorLog, indent=4)