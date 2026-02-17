import json

data = json.load(open("../data/qa_dataset.json"))

expanded = data + data

json.dump(expanded, open("../data/qa_dataset.json", "w"))

print("Dataset expanded")