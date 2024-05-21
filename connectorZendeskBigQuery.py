#_______________________________________________________________________________________________________________
#                                               Libraries import
#_______________________________________________________________________________________________________________

from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
import pandas as pd
import pandas_gbq

#_______________________________________________________________________________________________________________
#                                               Login informations
#_______________________________________________________________________________________________________________

creds = {
    'email': 'your_email',
    'token': 'your_token',
    'subdomain': 'your_subdomain'
}
project_id = "your-project"
table_id = 'your_dataset.your_table'

#_______________________________________________________________________________________________________________
#                                                   Connector
#_______________________________________________________________________________________________________________

print("... connecting to zendesk ...")
zenpy_client = Zenpy(**creds)
print("... ... successfully connected to zendesk!")

print("... Querying Zendesk Tickets ...")
raw_ticket_data = zenpy_client.search_export(type='ticket', status='open')
#raw_ticket_data = zenpy_client.search_export(type='ticket')
print("... ... successfully retreived zendesk tickets!")

print("... converting zendesk raw object data to pandas dataframe ...")
ticket_df = pd.DataFrame(raw_ticket_data)
print("... ... successfully converted python dict to pandas dataframe!")
ticket_df_rowcount = ticket_df.shape[0]
print("... ... which has " + str(ticket_df_rowcount) + " rows of tickets!")

#print("... push data in BigQuery ...")
#pandas_gbq.to_gbq(ticket_df, table_id, project_id = project_id)
#print("... ... successfully import data in BigQuery!")