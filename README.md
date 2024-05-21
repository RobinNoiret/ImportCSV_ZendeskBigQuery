# Zendesk to BigQuery Sync
## Project Description
Zendesk to BigQuery Sync is a Python application designed to **synchronize Zendesk data into Google BigQuery efficiently**. This project was created to address the slow synchronization process of an existing connector. The project includes two versions:

- **Interactive Application**: A GUI-based app that prompts users for their credentials before starting the synchronization.
- **Script Version**: A command-line script where users can input their login information directly into the code. <br>

This project is currently under development.

## Prerequisites
The project requires the following Python libraries:

- zenpy
- pandas
- pandas_gbq

## Installation Instructions
To install the necessary dependencies, run the following commands:

` pip install zenpy \  
pip install pandas \  
pip install pandas-gbq `

## Usage Instructions
### Interactive Application
1. Run the GUI application:

` python tkinterApp.py `

2. Enter your Zendesk email, API token, subdomain, and ticket status.
3. Click the "Start!" button to begin the synchronization process.

### Script Version
1. Open the script file and enter your Zendesk credentials directly in the code.
Run the script:
` python connectorZendeskBigQuery.py `

## Configuration
Currently, the project supports only one authentication method. Additional authentication methods are planned for future development.

## Features
- Synchronizes data from Zendesk to Google BigQuery.

## Troubleshooting
- Ensure all required libraries are installed.
- Verify that your Zendesk credentials are correct.
- Check your internet connection if data retrieval or pushing to BigQuery fails.
