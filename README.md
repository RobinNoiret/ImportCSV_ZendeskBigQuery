# Zendesk to BigQuery Sync 🔄

## Project Description 📰
Zendesk to BigQuery Sync is a Python application designed to **efficiently synchronize Zendesk historical data into Google BigQuery**. This project was created to address the slow synchronization process of an existing connector. It includes different codes that complement each other to make the complete solution work.

This project is currently under development. Find the documentation [here](https://github.com/RobinNoiret/Connector_ZendeskBigQuery/blob/986e59d9083749909d9630985a24e82ca984eaa9/Documentation/).

## Prerequisites ⚠
The project requires the following Python libraries:

- json
- csv
- pandas
- google.cloud
- os

### Installation Instructions
To install the necessary dependencies, run the following commands:

```bash
pip install pandas
pip install google.cloud-bigquery
```

## Usage Instructions 💻
Make sure to locate the script file using the cd command in the terminal.

1. Open the script file and enter your information directly in the code (variables section).

```python
# Add your project ID, dataset ID, and table name
project_id = "your_projectID"
dataset_id = "your_datasetID"
table_name = "your_tablename"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Your_credential_path'
```

2. Run the script: ` python connectorZendeskBigQuery.py `

## Configuration ⚙
Currently, the project supports only one authentication method. Additional authentication methods are planned for future development. Actualy, only local credentials work.

More informations :
- Authentification Overview : [click here](https://cloud.google.com/bigquery/docs/authentication?hl=fr)
- First step with Authentification : [click here](https://cloud.google.com/bigquery/docs/authentication?hl=fr)
- Installation G-Cloud CLI : [click here](https://cloud.google.com/sdk/docs/install?hl=fr)

## Troubleshooting 🔨
- Ensure all required libraries are installed.
- Verify your variables in the program
- Verify your Big Query account permissions (Writing rights required)
- Check your internet connection 😂


## Contribution 🤝
Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvement or are experiencing problems.

## Contact

Robin Noiret - contact@robinnoiret.fr
Project Link: [click here](https://github.com/RobinNoiret/Connector_ZendeskBigQuery) `
