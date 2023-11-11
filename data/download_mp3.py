import json
from os import path, mkdir
from string import ascii_lowercase
from time import sleep

class Downlaod_mp3:
    file_path = "source/final_data.json"
    data = None
    error_file_path = "errors.json"

    def __init__(self) -> None:
        # self.prepare_paths()
        self.load_file()

    # createing folders to store the source files
    def prepare_paths(self)->None:
        print("creating paths")
        if not path.exists('src_data'):
            mkdir("src_data")
        for alphabet in ascii_lowercase:
            if not path.exists(f"src_data/{alphabet}"):
                mkdir(f"src_data/{alphabet}")
    
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
        with open(f"{error_path}") as file:
            error_tmp_data = json.load(file)

        error_tmp_data.append(error_data)
        
        with open(f"{error_path}") as file:
            json.dump(file, error_tmp_data, indent=4)


main = Downlaod_mp3()