import json
import os

if __name__ == "__main__":
    original_dialogue = []
    translated_dialogue = []
    with open(os.path.join("resources", "localization_update", "original.txt"), "r", encoding="utf-8") as f:
        data: dict = json.load(f)
        original_dialogue = data["_stringTable"]["values"]

    with open(os.path.join("resources", "localization_update", "updated.txt"), "r", encoding="utf-8") as f:
        data: dict = json.load(f)
        translated_dialogue = data["_stringTable"]["values"]

    with open("result.txt", "w", encoding="utf-8") as f:
        for orig, trans in zip(original_dialogue, translated_dialogue):
            f.write(orig.replace('=', '\\='))
            f.write("=")
            f.write(trans.replace('=', '\\='))
            f.write("\n")
