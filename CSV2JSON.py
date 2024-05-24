import csv
import json

def csv_to_json(csv_file_path, json_file_path, delimiter=';'):
    # Lire le fichier CSV avec le délimiteur approprié
    data = []
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            data.append(row)
    
    # Sauvegarder les données JSON dans un fichier
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Les données ont été converties de {csv_file_path} à {json_file_path}")

# Chemin vers le fichier CSV et le fichier JSON de sortie
csv_file_path = 'input.csv'
json_file_path = 'output.json'

csv_to_json(csv_file_path, json_file_path)
