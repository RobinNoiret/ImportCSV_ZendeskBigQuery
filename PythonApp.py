from zenpy import Zenpy                         # Zenpy documentation : http://docs.facetoe.com.au/zenpy.html#installation
from zenpy.lib.api_objects import Ticket
import pandas as pd                             # pandas documentation : https://pandas.pydata.org/docs/
import pandas_gbq                               # pandas_gbq documentation: https://pypi.org/project/pandas-gbq/
import json

from logininformations import zendesk_crendentials, gbq_credentials, gbq_tableId, gbq_projectId

file_json_output_filename = "xyz.json"

# For Zendesk Cred format and api docs: https://pypi.org/project/zenpy/
# For GBQ Authentication: https://googleapis.dev/python/pandas-gbq/latest/howto/authentication.html

# Create a Zenpy instance
zenpy_client = Zenpy(zendesk_crendentials)

# Query All Tickets
raw_ticket_data = zenpy_client.search_export(type='ticket')

# Convert Raw Ticket JSON to Python Dict
ticket_dict = raw_ticket_data.to_dict()

# Convert Python Dict to Pandas Dataframe
ticket_df = pd.DataFrame(ticket_dict)

# Write in a JSON file
with open(file_json_output_filename, 'w') as myFile:
	json.dump(ticket_dict, myFile)

#Create BigQuery Instance
pandas_gbq.context.credentials = gbq_credentials
pandas_gbq.context.project = gbq_projectId

#Overwrite existing table with ticket_df
pandas_gbq.to_gbq(ticket_df, gbq_tableId, project_id=gbq_projectId, if_exists='replace')