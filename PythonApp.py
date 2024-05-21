from zenpy import Zenpy                         # Zenpy documentation : http://docs.facetoe.com.au/zenpy.html#installation
from zenpy.lib.api_objects import Ticket
import pandas as pd                             # pandas documentation : https://pandas.pydata.org/docs/
import pandas_gbq                               # pandas_gbq documentation: https://pypi.org/project/pandas-gbq/
import json

zendesk_crendentials = {
    'email' : 'robin.noiret@lumapps.com',
    'token' : 'ilzu3bo1tRJLTYkFBkfB4VVgqXwAPUS5Gu6D5E4s',
    'subdomain': 'lumapps'
}
gbq_credentials = 'From google-auth or pydata-google-auth library'
gbq_tableId = 'BigQuery table Id of the zendesk tickets table'
gbq_projectId = 'BigQuery project Id that the table is in'


# For Zendesk Cred format and api docs: https://pypi.org/project/zenpy/
# For GBQ Authentication: https://googleapis.dev/python/pandas-gbq/latest/howto/authentication.html

# Create a Zenpy instance
zenpy_client = Zenpy(**zendesk_crendentials)

# Query All Tickets
raw_ticket_data = zenpy_client.search_export(type='ticket')

# Convert Raw Ticket JSON to Python Dict
ticket_dicts = [ticket.to_dict() for ticket in raw_ticket_data]

# Convert Python Dict to Pandas Dataframe
ticket_df = pd.DataFrame(ticket_dicts)

print(ticket_df)

#Create BigQuery Instance
pandas_gbq.context.credentials = gbq_credentials
pandas_gbq.context.project = gbq_projectId

#Overwrite existing table with ticket_df
pandas_gbq.to_gbq(ticket_df, gbq_tableId, project_id=gbq_projectId, if_exists='replace')