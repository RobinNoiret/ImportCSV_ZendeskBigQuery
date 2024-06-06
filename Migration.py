# ____________________________________________________________________________________________________________________________________________________________________ #
#                                                                           Importing libraries
# ____________________________________________________________________________________________________________________________________________________________________ #

print("... Début du chargement des bibliothèques ...")
import json                                                  # JSON processing
import csv                                                   # CSV processing
import pandas as pd                                          # Data processing
from google.cloud import bigquery                            # BigQuery connection management
from google.cloud.exceptions import NotFound                 # Error management               
import os                                                    # Environmental management
print("... Bibliothèques chargées ...")

# ____________________________________________________________________________________________________________________________________________________________________ #
#                                                                               Variables
# ____________________________________________________________________________________________________________________________________________________________________ #

import credentials

project_id = credentials.project_id                               # BigQuery project identifier
dataset_id = credentials.dataset_id                               # BigQuery dataset identifier
table_name = credentials.table_name                               # Destination table name

key_path = credentials.ospath
key_path = os.path.abspath(key_path)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

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
    # Reading and filtering the NDJSON file
    filtered_data = []
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                record = json.loads(line.strip())
                filtered_record = {bigquery_col: record.get(file_col, None) for file_col, bigquery_col in column_mapping.items()}
                filtered_data.append(filtered_record)
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON : {e}")

    # Writting new data
    with open(filtered_output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(filtered_data, outfile, indent=4)

    print(f"Les données ont été filtrées et enregistrées dans {filtered_output_file_path}")

# Data correction - dates format __________________________________________________________________________________________
def date_correction(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                data = json.loads(line)
                if 'created_at' in data:
                    # Add ":00" and the end of date
                    if len(data['created_at']) == 16:
                        data['created_at'] += ":00"
                json.dump(data, f_out)
                f_out.write('\n')

# Data correction - organization name _____________________________________________________________________________________
def fill_organization_name(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                data = json.loads(line)
                # Check if organization_name is empty
                if not data.get('organization_name'):
                    # use organization_id to complete organization_name
                    data['organization_name'] = data.get('organization_id')
                    print("organization_name rempli avec organization_id :", data)
                json.dump(data, f_out)
                f_out.write('\n')

# Data correction - tags format ___________________________________________________________________________________________
def convert_tags_to_list(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                data = json.loads(line)
                # Check if tags exist and is a string
                if 'tags' in data and isinstance(data['tags'], str):
                    # Convert string into a list
                    data['tags'] = data['tags'].split()
                    print("tags convertis en liste :", data['tags'])
                json.dump(data, f_out)
                f_out.write('\n')

# Data correction - Maj ___________________________________________________________________________________________________
def transform_fields_to_lowercase(input_path, output_path, fields_to_lowercase):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                data = json.loads(line)
                for field in fields_to_lowercase:
                    if field in data:
                        data[field] = data[field].lower()
                f_output.write(json.dumps(data) + '\n')

# Data correction - Boolean _______________________________________________________________________________________________
def transform_to_boolean(input_path, output_path, fields):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                for field in fields:
                    if field in entry:
                        value = entry[field].lower()
                        if value == 'yes':
                            entry[field] = True
                        elif value == 'no':
                            entry[field] = False
                f_output.write(json.dumps(entry) + '\n')

# Data correction - Underscore ____________________________________________________________________________________________
def transform_to_underscore(input_path, output_path, fields):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                for field in fields:
                    if field in entry:
                        entry[field] = entry[field].replace(' ', '_').lower()
                f_output.write(json.dumps(entry) + '\n')

# Data correction - Null __________________________________________________________________________________________________
def replace_dashes_with_null(input_path, output_path, fields):
    with open(input_path, 'r', encoding='utf-8') as f_input:
        with open(output_path, 'w', encoding='utf-8') as f_output:
            for line in f_input:
                entry = json.loads(line)
                for field in fields:
                    if field in entry and entry[field] == "-":
                        entry[field] = None
                f_output.write(json.dumps(entry) + '\n')

# Data correction - Satisfaction rating ___________________________________________________________________________________
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

# ____________________________________________________________________________________________________________________________________________________________________ #
#                                                                               Executions
# ____________________________________________________________________________________________________________________________________________________________________ #

print("... Starting data transformation ...")

# Clean and CSV to JSON convertion _____________________________________________________________________________________
csv_Inputfile_path = 'Data/input.csv'                                   # input CSV file path
json_file_path = 'Data/JSON_data.json'                                  # input data convert in JSON file path
clean_and_convert_csv_to_json(csv_Inputfile_path, json_file_path)       # Function call - CSV 2 JSON

# JSON to NDJSON convertion ____________________________________________________________________________________________
input_file_path = 'Data/JSON_data.json'                                 # input data convert in JSON file path
output_file_path = 'Data/NDJSON_data.json'                              # inline JSON path
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
    "Satisfaction Score": "satisfaction_rating",
    "Status": "status",
    "Tags": "tags",
    "Ticket type": "type",
    "Type (custom) [list]": "type_custom",
    "Id": "ticket_id",
    "Ticket Form ID": "ticket_form_id",
    "Assignee": "assignee",
    "Severity [list]": "severity",
    "Need partner training [flag]": "NT_partner",
    "Need customer training [flag]": "NT_customer"
}
               
input_file_path = 'Data/NDJSON_data.json'                               # inline data file path
filtered_output_file_path = 'Data/FILTERED_data.json'                   # filtred data path
data_filtering(input_file_path,filtered_output_file_path,column_mapping)# Function call - Data filtering

# JSON to NDJSON convertion ____________________________________________________________________________________________
input_file_path = 'Data/FILTERED_data.json'                             # filtred data
output_file_path = 'Data/NDJSON_data2.json'                             # filtered inline JSON path
convert_json_to_ndjson(input_file_path, output_file_path)               # Function call - JSON to NDJSON

# Date format correction _______________________________________________________________________________________________
input_file = 'Data/NDJSON_data2.json'                                   # filtered inline JSON path
output_file = 'Data/DateCorrection.json'                                # JSON with date correction
date_correction(input_file, output_file)                                # Function call - Date format correction

# Organization_name correction _________________________________________________________________________________________
input_file = 'Data/DateCorrection.json'                                 # JSON with date correction
output_file = 'Data/OrgaName.json'                                      # JSON with organization_name correction
fill_organization_name(input_file, output_file)                         # Function call - Organization_name correction

# Correct tag format ___________________________________________________________________________________________________
input_file = 'Data/OrgaName.json'                                       # JSON with organization_name correction
output_file = 'Data/Tag.json'                                           # JSON with tags correction - Output
convert_tags_to_list(input_file, output_file)                           # Function call - Correct tag format

# Lower case Correction ________________________________________________________________________________________________
input_path = 'Data/Tag.json' 
output_path = 'Data/Lowercase.json'
fields_to_lowercase = ['Priority', 'Status', 'Ticket type', 'Severity [list]'] 
transform_fields_to_lowercase(input_path, output_path, fields_to_lowercase)

# Underscore Correction ________________________________________________________________________________________________
input_path = 'Data/Lowercase.json'
output_path = 'Data/Underscore.json'
fields_to_underscore = ['Level [list]', 'Type (custom) [list]']
transform_to_underscore(input_path, output_path, fields_to_underscore)

# Satisfaction rating Correction _______________________________________________________________________________________
input_path = 'Data/Underscore.json'
output_path = 'Data/SatisRating.json'
fields_satisfaction = ['Satisfaction Score']
transform_satisfaction_rating(input_path, output_path, fields_satisfaction)

# Boolean Correction ___________________________________________________________________________________________________
input_path = 'Data/SatisRating.json'
output_path = 'Data/Boolean.json'
fields_boolean = ['Need partner training [flag]','Need customer training [flag]']
transform_to_boolean(input_path, output_path, fields_boolean)

# Null value Correction ________________________________________________________________________________________________
input_path = 'Data/Boolean.json'
output_path = 'Data/Output.json'
fields_with_dashes = ['Product feedback status [list]', 'POD [list]', 'JIRA URL [txt]', 'Categories [list]']
replace_dashes_with_null(input_path, output_path, fields_with_dashes)

print("... Transformation complete ...")

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
json_file_path = output_file
print("... Début du chargement des données ...")
with open(json_file_path, "rb") as source_file:                                                 # rb = read binary => better compatibility and integrity of data
    load_job = client.load_table_from_file(source_file, table_ref, job_config=job_config)       # pushing data on BigQuery
load_job.result()                                                                               # waitting the end of loading
print("... Chargement des données terminé ...")

print(f"Les données du fichier {json_file_path} ont été chargées avec succès dans {table_name}")

client.close()                                                          # Close connection