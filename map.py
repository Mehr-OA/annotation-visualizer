import json
import os


# G#Species is not defined in the excel document

filename_map ="mapping.json"
with open(filename_map, 'r', encoding='utf-8') as f:
    mapping = json.load(f)

filename = "annotations/s11090-017-9845-3_entites.json"
with open(filename, 'r', encoding='utf-8') as f:
    annotations = json.load(f)

entities = annotations["entities"]

list_mapped = []
for obj in entities:
    obj["label"] = obj["text"]
    obj["class"] = mapping[obj["type"]]
    del obj["type"]
    del obj["text"]
    del obj["confidence"]
    list_mapped.append(obj)

mapped_entities = {
    "entities": list_mapped
}

save_name = filename.replace(".json", "_MAPPED.json")
with open(save_name, 'w') as f:
    json.dump(mapped_entities, f, indent=4)
