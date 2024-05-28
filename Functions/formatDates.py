import json

def process_ndjson(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                data = json.loads(line)
                if 'created_at' in data:
                    # Ajoute ":00" à la date si les secondes sont manquantes
                    if len(data['created_at']) == 16:
                        data['created_at'] += ":00"
                json.dump(data, f_out)
                f_out.write('\n')
# Utilisation du programme
input_file = 'Data/OutputHey.json'  # Chemin vers le fichier JSON d'entrée
output_file = 'Data/FinalOutput.json'  # Chemin vers le fichier JSON de sortie

process_ndjson(input_file, output_file)
