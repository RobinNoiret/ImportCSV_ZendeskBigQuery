import csv
import json

def clean_and_convert_csv_to_json(csv_file_path, json_file_path, delimiter=','):
    cleaned_rows = []
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        # Lire le fichier CSV en tenant compte des guillemets doubles mal placés
        csv_reader = csv.reader(csv_file, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Obtenir les en-têtes
        headers = next(csv_reader)
        headers = [header.strip() for header in headers]
        
        # Lire les lignes restantes et nettoyer les données
        for row in csv_reader:
            cleaned_row = {headers[i]: row[i].strip() for i in range(len(headers))}
            cleaned_rows.append(cleaned_row)

    # Écrire les données nettoyées en JSON
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(cleaned_rows, json_file, indent=4)

    print(f"Les données ont été nettoyées et converties de {csv_file_path} à {json_file_path}")

# Chemin vers le fichier CSV d'entrée et le fichier JSON de sortie
csv_file_path = 'input.csv'
json_file_path = 'output.json'

clean_and_convert_csv_to_json(csv_file_path, json_file_path)
