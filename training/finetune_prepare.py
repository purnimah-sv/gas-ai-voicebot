import json

qa = json.load(open("../data/qa_dataset.json"))

out = open("../data/finetune.jsonl", "w")

for pair in qa:
    row = {
        "messages": [
            {"role": "user", "content": pair["q"]},
            {"role": "assistant", "content": pair["a"]}
        ]
    }
    out.write(json.dumps(row) + "\n")

out.close()
print("Finetune file ready")