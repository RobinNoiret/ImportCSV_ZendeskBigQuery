# Librairies importation
import csv      # CSV library
import json     # JSON library

# Convertion function
def clean_and_convert_csv_to_json(csv_file_path, json_file_path, delimiter=','):
    cleaned_rows = []
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        # Read CSV file
        csv_reader = csv.reader(csv_file, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Keep header
        headers = next(csv_reader)
        headers = [header.strip() for header in headers]
        
        # Read other line and clean it
        for row in csv_reader:
            cleaned_row = {headers[i]: row[i].strip() for i in range(len(headers))}
            cleaned_rows.append(cleaned_row)

    # Writting clean data
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(cleaned_rows, json_file, indent=4)

    print(f"Les données ont été nettoyées et converties de {csv_file_path} à {json_file_path}")

# Variables
csv_file_path = 'Data/input.csv'
json_file_path = 'Data/JSONinput.json'

# Execution
clean_and_convert_csv_to_json(csv_file_path, json_file_path)
