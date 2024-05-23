#_______________________________________________________________________________________________________________
#                                               Libraries import
#_______________________________________________________________________________________________________________

import requests                         # HTTP
import json                             # JSON
from google.cloud import bigquery       # BigQuery

#_______________________________________________________________________________________________________________
#                                                   Variables
#_______________________________________________________________________________________________________________

# Zendesk
subdomain = "lumapps"
url = f'https://{subdomain}.zendesk.com/api/v2/'
token = "0kRdUtDeNHhX3warRbXfobwCG5Mk1U983HyNQ4qr"

# BigQuery
project_id = "lumapps-internal-bi"
dataset_id = "lumapps-internal-bi.syncari"
table_name = "zd_tickets"

#_______________________________________________________________________________________________________________
#                                                Fonctions
#_______________________________________________________________________________________________________________

# Initialisation du client BigQuery
print("... création de l'instance BigQuery ...")
#client = bigquery.Client(project=project_id)
print("... création réalisé avec succès ...")

# Fonction pour récupérer le nombre total de tickets
def get_total_tickets():
    print("... récupération du nombre de tickets ...")
    response = requests.get(url + "/tickets/count", headers={"Authorization": "Bearer " + token})
    if response.status_code == 200:
        print("... récupération réalisé avec succès ...")
        data = json.loads(response.content)
        return data["count"]
    else:
        raise Exception("Échec de la récupération du nombre total de tickets : " + str(response.status_code))

# Fonction pour diviser le nombre de tickets en lots
def get_batch_count(total_tickets):
    print("... calcul du nombre d'opération à réaliser ...")
    batch_size = 500  # 1000 par défaut
    batch_count = total_tickets // batch_size
    if total_tickets % batch_size > 0:
        batch_count += 1
    print("... calcul réalisé avec succès ...")
    return batch_count

# Fonction pour charger un lot de tickets dans BigQuery
def load_tickets_batch(batch_number, start_index, end_index):
    print(f"... début de l'import dans BigQuery pour le lot {batch_number} ...")
    params = {"page": batch_number, "per_page": end_index - start_index}
    response = requests.get(url + "tickets", params=params, headers={"Authorization": "Bearer " + token})
    if response.status_code == 200:
        data = json.loads(response.content)
        tickets = data["tickets"]

        # Préparation des données pour l'injection
        print("... préparation des données ...")
        dataset_ref = client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_name)
        job_config = bigquery.LoadJobConfig()
        job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

        # Injection des données dans la table
        print("... injection des données ...")
        load_job = client.load_table_from_json(
            tickets, table_ref, job_config=job_config
        )
        
        load_job.result()  # Attendre la fin du chargement
        print("___________________________________________________")
        print("Lot", batch_number, "chargé avec succès")
        print("___________________________________________________")
    else:
        raise Exception("Échec du chargement du lot " + str(batch_number) + " : " + str(response.status_code))

#_______________________________________________________________________________________________________________
#                                                Exécution
#_______________________________________________________________________________________________________________

total_tickets = get_total_tickets()
batch_count = get_batch_count(total_tickets)

batch_size = 500  # Assurez-vous que cela correspond à la taille du lot définie dans get_batch_count

for batch_number in range(1, batch_count + 1):
    start_index = (batch_number - 1) * batch_size
    end_index = min(batch_number * batch_size, total_tickets)
    load_tickets_batch(batch_number, start_index, end_index)