import json

def convert_json_to_ndjson(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    # Check
    if not isinstance(data, list):
        raise ValueError("Le fichier JSON d'entrée doit contenir une liste d'objets JSON")

    # Write NDJSON file (Newline Delimiter)
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for record in data:
            json_record = json.dumps(record)
            outfile.write(json_record + '\n')

    print(f"Les données ont été converties et enregistrées dans {output_file_path}")

input_file_path = 'Data/Unicode.json'                                 # input data convert in JSON file path
output_file_path = 'Data/NDJSON_data.json'                              # inline JSON path
convert_json_to_ndjson(input_file_path, output_file_path)               # Function call - JSON to NDJSON (ND = Newline Delimiter)