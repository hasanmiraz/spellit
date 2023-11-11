import os
import json

final_array = []
folders = os.listdir("src_data")

for folder in folders:
    files = os.listdir(f"src_data/{folder}")
    for file in files:
        if "mp3" in file:
            file_name = file.replace(".mp3", "")
            final_array.append(file_name)

with open("data.json", "w") as errorLog:
    json.dump(final_array, errorLog, indent=4)