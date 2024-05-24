import json

# Chemin vers le fichier NDJSON d'entrée
input_file_path = 'Data/NDJSONinput.json'
# Chemin vers le fichier JSON filtré de sortie
filtered_output_file_path = 'Data/filteredOutput.json'

# Mapping des colonnes entre le fichier d'entrée et le schéma BigQuery
column_mapping = {
    "Summation column": "brand_id",
    "Categories [list]": "categories",
    "Created at": "created_at",
    "Group": "group",
    "JIRA URL [txt]": "jira_url",
    "Level [list]": "level",
    "Organization": "organization_id",
    "Organization Name": "organization_name",
    "POD [list]": "pod",
    "Priority": "priority",
    "Product feedback status [list]": "product_feedback_status",
    "Region [list]": "region",
    "Satisfaction Score": "satisfaction_rating",
    "Status": "status",
    "Tags": "tags",
    "Ticket type": "type",
    "Type (custom) [list]": "type_custom",
    "Id": "ticket_id",
    "Ticket Form ID": "ticket_form_id"
}

# Lire et filtrer le fichier NDJSON
filtered_data = []
try:
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            record = json.loads(line.strip())
            filtered_record = {bigquery_col: record.get(file_col, None) for file_col, bigquery_col in column_mapping.items()}
            filtered_data.append(filtered_record)
except json.JSONDecodeError as e:
    print(f"Erreur de décodage JSON : {e}")

# Écrire les données filtrées dans un fichier JSON de sortie
with open(filtered_output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(filtered_data, outfile, indent=4)

print(f"Les données ont été filtrées et enregistrées dans {filtered_output_file_path}")
