import pandas as pd
import json

df = pd.read_excel("Apps.xlsx")

qa_dict = {"data": []}

for index, row in df.iterrows():
    question = row["App Name"]
    answer = row["Privacy Policy"]
    qa_dict["data"].append({"prompt": question, "completion": answer})


qa_data = qa_dict["data"]
with open("data.jsonl", "w") as f:
    for item in qa_data:
        line = json.dumps(item)
        f.write(line + "\n")
model_id="gpt-3.5-turbo"
# !openai tools fine_tunes.prepare_data -f "/content/data.jsonl"
# !openai api fine_tunes.create -t "/content/data.jsonl" -m davinci
import openai

openai.api_key = "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"

models = openai.FineTune.list()

#print(models['data'][0].fine_tuned_model)

# for model in models['data']:
#     print(model)