# Connection Information

To establish a connection with Google BigQuery, the project requires authentication. Follow the steps below to configure the authentication:

- Project ID: Your Google Cloud project ID. This identifies the project you are working with.
- Dataset ID: The ID of the dataset within Google BigQuery where you intend to store the data.
- Table Name: The name of the destination table within the specified dataset in BigQuery.
- Credentials: Path to your Google Cloud credentials JSON file. These credentials are necessary for authenticating your access to Google Cloud services.


Ensure that you have the necessary permissions to access the specified project, dataset, and table. Additionally, make sure that the provided credentials have appropriate privileges to interact with Google BigQuery, including the ability to read and write data to the specified dataset and table.

For set your credentials you can follow this doc :[click here](https://cloud.google.com/bigquery/docs/authentication/getting-started?hl=fr)
