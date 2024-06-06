import json

def replace_dashes_with_null(input_path, output_path, fields):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                for field in fields:
                    if field in entry and entry[field] == "-":
                        entry[field] = None
                f_output.write(json.dumps(entry) + '\n')

# Chemins des fichiers JSON
input_path = 'Data/Boolean.json'
output_path = 'Data/Null.json'

# Remplacement des tirets par null
fields_with_dashes = ['Product feedback status [list]', 'POD [list]', 'JIRA URL [txt]', 'Categories [list]']
replace_dashes_with_null(input_path, output_path, fields_with_dashes)