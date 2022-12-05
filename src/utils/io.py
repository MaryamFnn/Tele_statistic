import json

def read_json(file_path) :
    with open(file_path, encoding="UTF8") as f:
        return json.load(f)

def read_file(file_path):
    with open(file_path, encoding="UTF8") as f:
        return f.read()
