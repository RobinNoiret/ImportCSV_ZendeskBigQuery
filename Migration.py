# ____________________________________________________________________________________________________________________________________________________________________ #
#                                                                           Importing libraries
# ____________________________________________________________________________________________________________________________________________________________________ #

print("... Début du chargement des bibliothèques ...")
import json                                                 # JSON processing
import csv                                                  # CSV processing
import pandas as pd                                         # Data processing
from google.cloud import bigquery                           # BigQuery connection management
from google.cloud.exceptions import NotFound                # Error management               
import os                                                   # Environmental management
print("... Bibliothèques chargées ...")

# ____________________________________________________________________________________________________________________________________________________________________ #
#                                                                               Variables
# ____________________________________________________________________________________________________________________________________________________________________ #

project_id = "your_projectID"                          # BigQuery project identifier
dataset_id = "your_datasetID"                                      # BigQuery dataset identifier
table_name = "your_tablename"                                   # Destination table name
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Your_credential_path'

# ____________________________________________________________________________________________________________________________________________________________________ #
#                                                                               Functions
# ____________________________________________________________________________________________________________________________________________________________________ #

# Check dataset existence _________________________________________________________________________________________________
def check_dataset(dataset_ref, client):
    try:
        client.get_dataset(dataset_ref)
        print(f"Dataset {dataset_id} found.")
    except NotFound:
        print(f"Dataset {dataset_id} not found.")
        exit(1)

# Check table existence ___________________________________________________________________________________________________
def check_table(table_ref, client):
    try:
        client.get_table(table_ref)
        print(f"Table {table_name} found.")
    except NotFound:
        print(f"Table {table_name} not found. Creating table schema.")

# CVS to JSON converter function _________________________________________________________________________________________
def clean_and_convert_csv_to_json(csv_Inputfile_path, json_file_path, delimiter=','):
    cleaned_rows = []
    with open(csv_Inputfile_path, 'r', encoding='utf-8') as csv_file:
        # Read CSV file
        csv_reader = csv.reader(csv_file, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Keep header
        headers = next(csv_reader)
        headers = [header.strip() for header in headers]
        
        # Read other line and clean it
        for row in csv_reader:
            cleaned_row = {headers[i]: row[i].strip() for i in range(len(headers))}
            cleaned_rows.append(cleaned_row)

    # Writting clean data
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(cleaned_rows, json_file, indent=4)

    print(f"Les données ont été nettoyées et converties de {csv_Inputfile_path} à {json_file_path}")


# JSON to NDJSON convertion function ____________________________________________________________________________________
def convert_json_to_ndjson(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    # Check
    if not isinstance(data, list):
        raise ValueError("Le fichier JSON d'entrée doit contenir une liste d'objets JSON")

    # Write NDJSON file (Newline Delimiter)
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for record in data:
            json_record = json.dumps(record)
            outfile.write(json_record + '\n')

    print(f"Les données ont été converties et enregistrées dans {output_file_path}")

# Data Filtering function _______________________________________________________________________________________________
def data_filtering(input_file_path, filtered_output_file_path, column_mapping):
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


# ____________________________________________________________________________________________________________________________________________________________________ #
#                                                                               Executions
# ____________________________________________________________________________________________________________________________________________________________________ #

# Clean and CSV to JSON convertion _____________________________________________________________________________________
csv_Inputfile_path = 'Data/input.csv'                                # input CSV file path
json_file_path = 'Data/JSON_data.json'                                  # input data convert in JSON file path
clean_and_convert_csv_to_json(csv_Inputfile_path, json_file_path)       # Function call - CSV 2 JSON

# JSON to NDJSON convertion ____________________________________________________________________________________________
input_file_path = json_file_path                                        # input data convert in JSON file path
output_file_path = 'Data/NDJSON_data.json'                              # inline data file path
convert_json_to_ndjson(input_file_path, output_file_path)               # Function call - JSON to NDJSON (ND = Newline Delimiter)

# Data filtering _______________________________________________________________________________________________________
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
input_file_path = output_file_path                                      # inline data file path
filtered_output_file_path = 'Data/FILTERED_data.json'                   # filtred data
data_filtering(input_file_path, filtered_output_file_path, column_mapping)# Function call - Data filtering

# JSON to NDJSON convertion ____________________________________________________________________________________________
input_file_path = filtered_output_file_path                             # filtred data
output_file_path = 'Data/Output.json'                                   # Final ouput (inline filtred data)
convert_json_to_ndjson(input_file_path, output_file_path)               # Function call - JSON to NDJSON

# BigQuery client initialization with a local login ____________________________________________________________________
client = bigquery.Client(project=project_id)                            # Instantiating the BigQuery client

# Verification Dataset & Table _________________________________________________________________________________________
dataset_ref = client.dataset(dataset_id)                                # Dataset definition
table_ref = dataset_ref.table(table_name)                               # Table definition

check_dataset(dataset_ref, client)                                      # Check dataset existence
check_table(table_ref, client)                                          # Check table existence

# Load job configuration ______________________________________________________________________________________________
print("... Confirguration ...")
job_config = bigquery.LoadJobConfig()                                   # Instantiating the LoadJob for setup
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON # Define the data format
job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND   # Configure the data push settings
print("... Configuration terminé ...")

# Loading JSON data into the BigQuery table ___________________________________________________________________________
print("... Début du chargement des données ...")
with open(json_file_path, "rb") as source_file:                                                 # rb = read binary => better compatibility and integrity of data
    load_job = client.load_table_from_file(source_file, table_ref, job_config=job_config)       # pushing data on BigQuery
load_job.result()                                                                               # waitting the end of loading
print("... Chargement des données terminé ...")

print(f"Les données du fichier {json_file_path} ont été chargées avec succès dans {table_name}")
