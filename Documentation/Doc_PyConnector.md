# Python Script Documentation

## Table of Contents
1. [Library Imports](#library-imports)
2. [Login Information](#login-information)
3. [Connector](#connector)
4. [Zendesk Ticket Query](#zendesk-ticket-query)
5. [Conversion to Pandas DataFrame](#conversion-to-pandas-dataframe)
6. [Export to BigQuery (Commented)](#export-to-bigquery-commented)

## Library Imports

``` python
from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
import pandas as pd
import pandas_gbq
from datetime import datetime, timedelta
```

This section imports the necessary libraries:
- zenpy for interacting with the Zendesk API.
- pandas for data manipulation.
- pandas_gbq for interacting with Google BigQuery.
- datetime and timedelta for date handling.

If you have any questions about the different libraries, here are the links to the various documentations :
- [Zenpy documentation](http://docs.facetoe.com.au/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Pandas_gbq documentation](https://googleapis.dev/python/pandas-gbq/latest/)
- [Datetime documentation](https://docs.python.org/3/library/datetime.html)
  
## Login Information
```python
creds = {
    'email': 'your_email',
    'token': 'your_token',
    'subdomain': 'your_subdomain'
}
project_id = "your-project"
table_id = 'your_dataset.your_table'
```
This section contains the login information:
- creds: dictionary containing the email, API token, and Zendesk subdomain.
- project_id: Google Cloud project ID.
- table_id: BigQuery table ID in the format dataset.table.

If you have any questions about connection information, here are the links to the various documentation for the solutions used.
- [Zendesk API documentation](https://developer.zendesk.com/api-reference/)
- [Zenpy - Authentification methods](http://docs.facetoe.com.au/zenpy.html#usage)
- [Google Big Query documentation](https://cloud.google.com/bigquery/docs/tables?hl=fr)
  
## Connector
```python
start_date = datetime(2021, 1, 1)
end_date = start_date + timedelta(days=7)

print("... connecting to zendesk ...")
zenpy_client = Zenpy(**creds)
print("... ... successfully connected to zendesk!")
```python

This section establishes a connection to the Zendesk API:
- start_date and end_date: date range for the query.
- Initializes the Zenpy client with the credentials.

## Zendesk Ticket Query
```python
print("... Querying Zendesk Tickets ...")
raw_ticket_data = zenpy_client.search_export(type='ticket', created_between=(start_date, end_date))     # selected with date range
#raw_ticket_data = zenpy_client.search_export(type='ticket', status='open')                             # selected with status
#raw_ticket_data = zenpy_client.search_export(type='ticket')                                            # select all tickets
print("... ... successfully retreived zendesk tickets!")
```

This section performs a query to retrieve Zendesk tickets:
- search_export: method used to export tickets.
- Comments show other filtering options: by status or without any filter.

## Conversion to Pandas DataFrame
```python
print("... converting zendesk raw object data to pandas dataframe ...")
ticket_df = pd.DataFrame(raw_ticket_data)
print("... ... successfully converted python dict to pandas dataframe!")
ticket_df_rowcount = ticket_df.shape[0]
print("... ... which has " + str(ticket_df_rowcount) + " rows of tickets!")
```

This section converts the ticket data to a Pandas DataFrame:
- Converts raw data to a DataFrame.
- Displays the number of rows in the DataFrame.

## Export to BigQuery
```python
#print("... push data in BigQuery ...")
#pandas_gbq.to_gbq(ticket_df, table_id, project_id = project_id)
#print("... ... successfully import data in BigQuery!")
```

This section (commented) shows how to export the data to Google BigQuery:
- to_gbq: method used to send the DataFrame to BigQuery.

## Conclusion
This script connects to the Zendesk API, retrieves tickets within a specified date range, converts the data to a Pandas DataFrame, and shows how to export the data to Google BigQuery. You can adjust the parameters and add comment as needed to tailor the script to your specific requirements.
