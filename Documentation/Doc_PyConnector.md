# Python Script Documentation

## Table of Contents
1. [Library Imports](#library-imports)
2. [Login Informations](#login-information)
3. [Process](#process)

## Library Imports

``` python
import json
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.exceptions import NotFound
import os
```

This section imports the necessary libraries:
- json for use jsonformat manipulation.
- pandas for data manipulation.
- google.cloud for interacting with Google BigQuery.
- os for the local credentials interactions.

If you have any questions about the different libraries, here are the links to the various documentations :
- [Zenpy documentation](http://docs.facetoe.com.au/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Google.cloud documentation](https://cloud.google.com/python/docs?hl=fr)
- [os documentation]([https://docs.python.org/3/library/datetime.html](https://docs.python.org/fr/3/library/os.html))
  
## Login Informations
```python
project_id = "your_projectID"
dataset_id = "your_datasetID"
table_name = "your_tablename"
json_file_path = "your_path"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'your_credential_path'
```
  
## Process
1. Get the CSV export from Zendesk
2. Run CSV2JSON conversion program
  -> Remember to change source and destination file paths
3. Run the main Zendesk2BigQuery program
  -> Fill in the necessary information
