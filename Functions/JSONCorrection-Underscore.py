import json

def transform_to_underscore(input_path, output_path, fields):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                for field in fields:
                    if field in entry:
                        entry[field] = entry[field].replace(' ', '_').lower()
                f_output.write(json.dumps(entry) + '\n')


# Chemins des fichiers JSON
input_path = 'Data/Lowercase.json'
output_path = 'Data/Underscore.json'

# Transformation avec underscores
fields_to_underscore = ['Level [list]', 'Type (custom) [list]']
transform_to_underscore(input_path, output_path, fields_to_underscore)