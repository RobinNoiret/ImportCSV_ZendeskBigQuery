import json

def fill_organization_name(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                data = json.loads(line)
                # Vérifie si organization_name est vide
                if not data.get('organization_name'):
                    # Utilise organization_id pour remplir organization_name
                    data['organization_name'] = data.get('organization_id')
                    print("organization_name rempli avec organization_id :", data)
                json.dump(data, f_out)
                f_out.write('\n')

# Utilisation du programme
input_file = 'Data/FinalOutput.json'  # Chemin vers le fichier JSON d'entrée
output_file = 'Data/FinalFinalOutput.json'  # Chemin vers le fichier JSON de sortie

fill_organization_name(input_file, output_file)
