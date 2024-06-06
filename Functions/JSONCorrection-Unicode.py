import json

def decode_and_rewrite_json(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        input_data = f.readlines()

    decoded_data = []
    for line in input_data:
        decoded_data.append(json.loads(line))

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(decoded_data, f, indent=2, ensure_ascii=False)

    print("Fichier JSON décodé et réécrit avec succès.")

# Chemins des fichiers JSON
input_path = 'chemin_vers_le_fichier_input.ndjson'
output_path = 'chemin_vers_le_fichier_output.ndjson'
decode_and_rewrite_json(input_path, output_path)



# Utilisation de la fonction pour décoder et réécrire le fichier JSON
input_path = 'Data/NDJSON_data.json'
output_path = 'Data/Unicode.json'
decode_and_rewrite_json(input_path, output_path)


def decode_and_rewrite_ndjson(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                f_output.write(json.dumps(entry, ensure_ascii=False) + '\n')