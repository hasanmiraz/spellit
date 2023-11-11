import json
from os import path, mkdir
from string import ascii_lowercase
from time import sleep
import requests
from threading import Thread

class Downlaod_mp3:
    file_path = "source/final_data.json"
    data = None
    error_file = "errors.json"

    def __init__(self) -> None:
        self.prepare_paths()
        self.load_file()
        self.download_threading()
    # createing folders to store the source files
    def prepare_paths(self)->None:
        print("creating paths")
        if not path.exists('src_data'):
            mkdir("src_data")
        for alphabet in ascii_lowercase:
            if not path.exists(f"src_data/{alphabet}"):
                mkdir(f"src_data/{alphabet}")
                with open(f"src_data/{alphabet}/{self.error_file}", "w") as file:
                    json.dump({}, file, indent=4)
    
    #loading the data
    def load_file(self)->None:
        print("loading files")
        with open(self.file_path) as file:
            self.data = json.load(file)
        for alphabate, element in self.data.items():
            print(f"{alphabate}: {len(element)}")
        
        print(F"files are loaded. starting download...")
        sleep(5)

    def manage_log(self, error_path, error_data)->None:
        with open(f"{error_path}", "r") as file:
            error_tmp_data = json.load(file)
        key = list(error_data.keys())[0]
        error_tmp_data[key] = error_data[key]

        with open(f"{error_path}", "w") as file:
            json.dump(error_tmp_data, file, indent=4)
    
    def download(self, download_alphabate):
        for word, url in self.data[download_alphabate].items():
            try:
                response = requests.get(url=url)
                if response.status_code == 200:
                    print(f"downloaded from {download_alphabate} thread.")
                    with open(f"src_data/{download_alphabate}/{word}.mp3", "wb") as mp3File:
                        mp3File.write(response.content)
                else:
                    print(f"failed from {download_alphabate} thread.")
                    error_path = f"src_data/{download_alphabate}/{self.error_file}"
                    self.manage_log(error_path,{word: url})
            except Exception as ex:
                print(f"failed from {download_alphabate} thread.")
                error_path = f"src_data/{download_alphabate}/{self.error_file}"
                self.manage_log(error_path,{word: url})

        print(f"thread {download_alphabate} is complete")
            
    def download_threading(self):
        alphabate_dict = {}
        for alphabate in self.data.keys():
            alphabate_dict[alphabate] = Thread(target=self.download, args=(alphabate,))
        for key, value in alphabate_dict.items():
            value.start()
            print(f"started threading with {key}")


main = Downlaod_mp3()