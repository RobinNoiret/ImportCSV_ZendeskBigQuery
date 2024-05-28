

import json

def validate_ndjson(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()  # Enlever les espaces vides
            if not line:  # Skip les lignes vides
                continue
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Invalid JSON on line {line_num}: {e}")
                break  # Stop the loop after finding an invalid line

validate_ndjson("Data/Output.json")


import json

def validate_ndjson(file_path):
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Invalid JSON on line {line_num}: {e}")

validate_ndjson("Data/Output.json")