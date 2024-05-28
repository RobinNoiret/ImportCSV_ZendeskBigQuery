import json

def convert_tags_to_list(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                data = json.loads(line)
                # Vérifie si le champ tags existe et est une chaîne de caractères
                if 'tags' in data and isinstance(data['tags'], str):
                    # Convertit la chaîne de caractères en liste
                    data['tags'] = data['tags'].split()
                    print("tags convertis en liste :", data['tags'])
                json.dump(data, f_out)
                f_out.write('\n')

# Utilisation du programme
input_file = 'Data/FinalFinalOutput.json'  # Chemin vers le fichier JSON d'entrée
output_file = 'Data/Output_tags_list.json'  # Chemin vers le fichier JSON de sortie

convert_tags_to_list(input_file, output_file)
