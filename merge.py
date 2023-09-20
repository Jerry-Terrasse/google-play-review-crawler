import json
import glob

results = []
for f in glob.glob("data/*.json"):
    with open(f, "r") as infile:
        results.extend(json.load(infile))

print(len(results))

with open("merged.json", "w") as outfile:
    json.dump(results, outfile, indent=4, ensure_ascii=False)