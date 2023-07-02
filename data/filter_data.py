import json
import pandas

class FilterData:
    data_path = './source/data.json'
    frequent_used_words_path = './source/unigram_freq.csv'
    save_data_path = './source/final_data.json'

    data = dict()
    

    def read_files(self, path):
        if "json" in path:
            with open(path, "r") as read_file:
                return json.load(read_file)
        elif "csv" in path:
            df = pandas.read_csv(path)
            data_csv = df.drop("count", axis=1)
            return data_csv.values.tolist()
        
    def save_json_file(self, path):
        with open(path, 'w') as write_file:
            json.dump(self.data, write_file, indent=4)
    
    def get_data_from_file(self):
        words_with_url = self.read_files(self.data_path)
        frequent_words = self.read_files(self.frequent_used_words_path)

        return words_with_url, frequent_words
    
    def get_relevant_data(self):
        data1, data2 = self.get_data_from_file()

        to_go = len(data1)
        
        for word, url in data1.items():
            print(f"{to_go} left")
            to_go-=1
            if [word] in data2:
                self.data[word] = url
    
    def alphabatical_threading_data(self):
        data = self.data
        alphabet = set()
        new_data = dict()
        for word, url in data.items():
            if word[0] not in alphabet:
                alphabet.add(word[0])
                new_data[word[0]] = dict()
            new_data[word[0]][word] = url
        self.data = new_data
    
    def process(self):
        self.get_relevant_data()
        self.alphabatical_threading_data()
        self.save_json_file(self.save_data_path)
        


f = FilterData()
f.process()
