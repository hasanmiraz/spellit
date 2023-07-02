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
        json.dump(failed_dict, failed_file, indent=4)
    with open('./log/last.json', "w") as last_data_file:
        json.dump(last_data, last_data_file, indent=4)
    print("folder created")

def get_log_data():
    global failed_dict
    global last_data

    with open('./log/failed.json', "r") as failed_file:
        failed_dict = json.load(failed_file)
    with open('./log/last.json', "r") as last_data_file:
        last_data = json.load(last_data_file)


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

def write_log():
    with open("./log/failed.json", "w") as failed_file:
        json.dump(failed_dict, failed_file, indent=4)
        
def get_mp3_file(word, url):   
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            } 
    x = requests.get(url, headers=headers)
    if x.status_code!=200:
        save_data(word, url, "failed")
        return None
    return x.content

def write_mp3(word, mp3):
    print(f"saving {word}")
    filepath = f"./download/{word}.mp3"
    with open(filepath, 'wb') as file:
        file.write(mp3)

def process():
    create_folders()
    get_log_data()
    data, total_data = get_data()

    break_at = 5

    count_data = 0
    for word, url in data.items():
        count_data += 1
        print(f"{count_data} out of {total_data} working on {word}")

        if os.path.exists(f"./download/{word}.mp3"):
            continue
        
        mp3_file = get_mp3_file(word, url)

        if mp3_file == None:
            print(f"failed at {count_data} word {word}")
            save_data(word, url, "failed")
            continue
        
        write_mp3(word, mp3_file)

        # break_at -= 1
        # if break_at == 0:
        #     print("breaking")
        #     break;

        
process()
write_log()