import json

with open('data.jason', 'r') as f:
    data = json.load(f)
f = open('data.txt', 'r')
data = f.read()
f.close()
print(data)
