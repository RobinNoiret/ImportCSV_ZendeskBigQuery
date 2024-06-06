import json

def transform_fields_to_lowercase(input_path, output_path, fields_to_lowercase):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                data = json.loads(line)
                for field in fields_to_lowercase:
                    if field in data:
                        data[field] = data[field].lower()
                f_output.write(json.dumps(data) + '\n')

# Chemins des fichiers JSON
input_path = 'Data/NDJSON_data.json'
output_path = 'Data/Lowercase.json'

# Transformation en minuscules
fields_to_lowercase = ['Priority', 'Status', 'Ticket type', 'Severity [list]'] 
transform_fields_to_lowercase(input_path, output_path, fields_to_lowercase)