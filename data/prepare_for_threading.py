import json

with open("final_data.json", 'r') as data_file:
    data = json.load(data_file)

alphabet = set()
new_data = dict()
for word, url in data.items():
    if word[0] not in alphabet:
        alphabet.add(word[0])
        new_data[word[0]] = dict()
    new_data[word[0]][word] = url

print(len(alphabet))
print(len(new_data))

with open("threading_data.json", "w") as threading_file:
    json.dump(new_data, threading_file, indent=4)