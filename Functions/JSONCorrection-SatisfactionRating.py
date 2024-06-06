import json

def transform_satisfaction_rating(input_path, output_path, fields):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                for field in fields:
                    if field in entry:
                        value = entry[field].lower()
                        if value in ['offered', 'good', 'bad']:
                            value = value
                        elif value == 'not offered':
                            value = 'unoffered'
                        entry[field] = f"{{score={value}}}"
                f_output.write(json.dumps(entry) + '\n')

# Chemins des fichiers JSON
input_path = 'Data/Underscore.json'
output_path = 'Data/SatisRating.json'

# Transformation des évaluations de satisfaction
fields_satisfaction = ['Satisfaction Score']
transform_satisfaction_rating(input_path, output_path, fields_satisfaction)