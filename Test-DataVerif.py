import json
from datetime import datetime, timedelta
from zenpy import Zenpy
import pandas as pd

# Credentials
creds = {
    'email': 'your_email',
    'token': 'your_token',
    'subdomain': 'your_subdomain'
}

# Dates de la première semaine de 2021
start_date = datetime(2021, 1, 1)
end_date = start_date + timedelta(days=7)

print("... connecting to zendesk ...")
zenpy_client = Zenpy(**creds)
print("... ... successfully connected to zendesk!")

print("... Querying Zendesk Tickets ...")
raw_ticket_data = zenpy_client.search_export(type='ticket', created_between=(start_date, end_date))
print("... ... successfully retrieved zendesk tickets!")

# Créer une liste pour stocker les tickets
ticket_list = []

# Extraire les informations de chaque ticket et les ajouter à la liste
for ticket in raw_ticket_data:
    ticket_list.append(ticket.to_dict())  # Utilisez to_dict() pour convertir l'objet en dictionnaire

print("... converting zendesk raw object data to pandas dataframe ...")
ticket_df = pd.DataFrame(ticket_list)
print("... ... successfully converted python dict to pandas dataframe!")

ticket_df_rowcount = ticket_df.shape[0]
print("... ... which has " + str(ticket_df_rowcount) + " rows of tickets!")

print("... Print ROWS ...")
print(ticket_df.head())  # Afficher les premières lignes pour vérifier les colonnes

print("... JSON file writing ...")
# Écrire le DataFrame en JSON
ticket_df.to_json('data.json', orient='records', lines=True)
print("... Writing complete! ...")
