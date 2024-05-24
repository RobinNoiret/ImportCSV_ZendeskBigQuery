import json

# First execution _________________________________
# Input file path
#input_file_path = 'Data/JSONinput.json'
# Output file path
#output_file_path = 'Data/NDJSONinput.json'

# Second execution ________________________________
# Input file path
input_file_path = 'Data/filteredOutput.json'
# Output file path
output_file_path = 'Data/Output.json'


# JSON file read
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
