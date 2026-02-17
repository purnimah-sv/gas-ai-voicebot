import json
import random

base = [
    "How to change gas name?",
    "Documents required?",
    "New connection steps?"
]

qa = []

for i in range(10000):
    q = random.choice(base)
    qa.append({"q": q, "a": "Standard gas process answer."})

json.dump(qa, open("../data/qa_dataset.json", "w"))