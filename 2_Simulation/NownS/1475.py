import math

num = input()

data = {}

for i in num:
    try:
        if i == "6" or i == "9":
            data["69"] += 1
        else:
            data[i] += 1
    except KeyError:
        if i == "6" or i == "9":
            data["69"] = 1
        else:
            data[i] = 1
if "69" in data.keys():
    data["69"] = math.ceil(data["69"] / 2)

print(max(data.values()))
