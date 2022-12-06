import json
data = {'x': 10, 'y': 20, 'size': 1.5}
with open('data.jason', 'w') as f: # 이렇게 하면 close가 필요없다
    json.dump(data, f)

f = open('data.txt', 'w')
f.write(str(data))
f.close()

