from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
import pandas as pd
import pandas_gbq

# zendesk creds
creds = {
    'email' : '...',
    'token' : '...',
    'subdomain': '...',
}
project_id = "my-project"
table_id = 'my_dataset.my_table'

print("... connecting to zendesk ...")
zenpy_client = Zenpy(**creds)
print("... ... successfully connected to zendesk!")

print("... Querying Zendesk Tickets ...")
#raw_ticket_data = zenpy_client.search_export(type='ticket', status='open')
raw_ticket_data = zenpy_client.search_export(type='ticket')
print("... ... successfully retreived zendesk tickets!")

print("... converting zendesk raw object data to pandas dataframe ...")
ticket_df = pd.DataFrame(raw_ticket_data)
print("... ... successfully converted python dict to pandas dataframe!")
ticket_df_rowcount = ticket_df.shape[0]
print("... ... which has " + str(ticket_df_rowcount) + " rows of tickets!")

print("... Print ROWS ...")
print(ticket_df)

#print("... push data in BigQuery ...")
#pandas_gbq.to_gbq(ticket_df, table_id, project_id = project_id)
#print("... ... successfully import data in BigQuery!")