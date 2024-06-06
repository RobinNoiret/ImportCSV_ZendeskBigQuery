import json

def transform_to_boolean(input_path, output_path, fields):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                for field in fields:
                    if field in entry:
                        value = entry[field].lower()
                        if value == 'yes':
                            entry[field] = True
                        elif value == 'no':
                            entry[field] = False
                f_output.write(json.dumps(entry) + '\n')
    

# Chemins des fichiers JSON
input_path = 'Data/SatisRating.json'
output_path = 'Data/Boolean.json'

# Transformation en booléen
fields_boolean = ['Need partner training [flag]','Need customer training [flag]']
transform_to_boolean(input_path, output_path, fields_boolean)
    