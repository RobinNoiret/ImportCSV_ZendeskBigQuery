from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
import pandas as pd
import pandas_gbq

# zendesk creds
creds = {
    'email' : 'joe@lumapps.com',
    'token' : 'INSERT_ZENDESK_TOKEN_HERE',
    'subdomain': 'lumapps'
}

print("... connecting to zendesk ...")
zenpy_client = Zenpy(**creds)
print("... ... successfully connected to zendesk!")

print("... Querying Zendesk Tickets ...")
raw_ticket_data = zenpy_client.search_export(type='ticket', status='open')
print("... ... successfully retreived zendesk tickets!")

print("... converting zendesk raw object data to pandas dataframe ...")
ticket_df = pd.DataFrame(raw_ticket_data)
print("... ... successfully converted python dict to pandas dataframe!")
ticket_df_rowcount = ticket_df.shape[0]
print("... ... which has " + str(ticket_df_rowcount) + " rows of tickets!")