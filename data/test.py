import requests

headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

x = requests.get(f"http://dictionary.cambridge.org/us/media/english/us_pron/u/usa/usad_/usad___006.mp3", headers=headers)
print(x)
filename = "abnormal.mp3"
with open(filename, 'wb') as file:
    file.write(x.content)

# x = {"sdf":"ete"}
# print(x)
# def something():
#     global x
#     x["hekl"]="sdfjilj"
#     x["hkl"]="sd2444213j"
# print(x)
