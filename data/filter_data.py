import json
import pandas

class FilterData:
    data_path = 'main data/data.json'
    frequent_used_words_path = 'main data/unigram_freq.csv'
    data = "helo"
    
    def get_data(self):
        print(self.data)



f = FilterData()
f.get_data()