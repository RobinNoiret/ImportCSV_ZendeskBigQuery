#_______________________________________________________________________________________________________________
#                                               Libraries import
#_______________________________________________________________________________________________________________

from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
import pandas as pd
import pandas_gbq
from datetime import datetime, timedelta

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

start_date = datetime(2021, 1, 1)
end_date = start_date + timedelta(days=7)

print("... connecting to zendesk ...")
zenpy_client = Zenpy(**creds)
print("... ... successfully connected to zendesk!")

print("... Querying Zendesk Tickets ...")
raw_ticket_data = zenpy_client.search_export(type='ticket', created_between=(start_date, end_date))     # selected with date range
#raw_ticket_data = zenpy_client.search_export(type='ticket', status='open')                             # selected with status
#raw_ticket_data = zenpy_client.search_export(type='ticket')                                            # select all tickets
print("... ... successfully retreived zendesk tickets!")

print("... converting zendesk raw object data to pandas dataframe ...")
ticket_df = pd.DataFrame(raw_ticket_data)
print("... ... successfully converted python dict to pandas dataframe!")
ticket_df_rowcount = ticket_df.shape[0]
print("... ... which has " + str(ticket_df_rowcount) + " rows of tickets!")

print("... push data in BigQuery ...")
pandas_gbq.to_gbq(ticket_df, table_id, project_id = project_id)
print("... ... successfully import data in BigQuery!")