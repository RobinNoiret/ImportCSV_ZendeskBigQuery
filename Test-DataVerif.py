import pandas as pd
from zenpy import Zenpy

# Remplacer les informations de connexion par un dictionnaire contenant vos identifiants
creds = {
    'email' : '...',
    'token' : '...',
    'subdomain': '...',
}

print("... connecting to zendesk ...")
zenpy_client = Zenpy(**creds)
print("... ... successfully connected to zendesk!")

print("... Querying Zendesk Tickets ...")
raw_ticket_data = zenpy_client.search_export(type='ticket', status='open')
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
