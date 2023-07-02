import json
import pandas as pd

total_data = 0
with open("data.json", "r") as json_data:
    data_json = json.loads(json_data.read())
    total_data = len(data_json)

df = pd.read_csv(r'unigram_freq.csv')
data_csv = df.drop("count", axis=1)
data_csv = data_csv.values.tolist()

# print(data_csv)

final_dict = {}
# break_at  =1000
for data, link in data_json.items():
    print(f"{total_data} left, working on: {data}")
    total_data-=1
    if [data] in data_csv:
        final_dict[data] = link
    # break_at-=1
    # if break_at == 0:
    #     break
with open("final_data.json", "w") as final_file:
    json.dump(final_dict, final_file, indent=4)
