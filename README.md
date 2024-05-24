# Zendesk to BigQuery Sync 🔄
## Project Description 📰
Zendesk to BigQuery Sync is a Python application designed to **synchronize Zendesk data into Google BigQuery efficiently**. This project was created to address the slow synchronization process of an existing connector. This project includes different codes that complement each other to make the complete solution work.

This project is currently under development. Find the documentation [here](https://github.com/RobinNoiret/Connector_ZendeskBigQuery/blob/986e59d9083749909d9630985a24e82ca984eaa9/Documentation/Doc_PyConnector.md)

## Prerequisites ⚠
The project requires the following Python libraries:

- json
- pandas
- google.cloud

### Installation Instructions
To install the necessary dependencies, run the following commands:

` pip install pandas \  
pip install google.cloud-bigquery `

## Usage Instructions 💻
be sure to locate the script file using the **cd** command in the terminal.

### Script Version
1. Open the script file and enter your informations directly in the code (part variables).
Run the script:

` python connectorZendeskBigQuery.py `

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

Project Link: [click here](https://github.com/RobinNoiret/Connector_ZendeskBigQuery)
