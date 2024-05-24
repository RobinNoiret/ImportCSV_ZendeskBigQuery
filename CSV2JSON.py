print("... Libraries loading ...")
import csv
import json
print("... Libraries loading done ...")

def csv_to_json(csv_file_path, json_file_path, delimiter=';'):
    # Read the CSV file with the appropriate delimiter
    data = []
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            data.append(row)
    
    # Save JSON data to a file 
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Data have been converted from {csv_file_path} to {json_file_path}")

# Path to output CSV file and JSON file
csv_file_path = 'input.csv'
json_file_path = 'output.json'

csv_to_json(csv_file_path, json_file_path)
