import json
import requests
import os

folder_path = ["log", "download"]
data = None
total_data = 0
failed_dict = {}
last_data = {}

def create_folders():
    for folder in folder_path:
        if not os.path.exists(f"./{folder}"):
            os.mkdir(folder)

    with open('./log/failed.json', "w") as failed_file:
        pass
    with open('./log/last.json', "w") as last_data_file:
        pass
    print("folder created")

def get_log_data():
    global failed_dict
    global last_data

    with open('./log/failed.json', "r") as failed_file:
        failed_dict = json.load(failed_file)
    with open('./log/last.json', "r") as last_data_file:
        last_data = json.load(last_data_file)
    print(failed_dict)
    print(last_data)

def get_data():
    with open("final_data.json", "r") as data_f:
        data = json.load(data_f)
        total_data = len(data)
        return data, total_data

def save_data(word, url, type):
    global failed_dict
    global last_data
    if type == "failed":
        failed_dict[word]=url
    elif type == "last":
        last_data = word
        
def get_mp3_file(word, url):    
    x = requests.get(url)
    if x.status_code!=200:
        save_data(word, "failed")

def process():
    create_folders()
    get_log_data()


process()