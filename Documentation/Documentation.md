# Documentation for Zendesk to BigQuery Sync

## Introduction
Zendesk to BigQuery Sync is a Python application designed to **efficiently synchronize Zendesk data into Google BigQuery**. This project was created to address the slow synchronization process of an existing connector. It includes different codes that complement each other to make the complete solution work.

This project is currently under development.

## Summary
- [Libraries](Libraries.md)
- [Connection Information](Connection.md)
- [Functions](Functions.md)
- [Execution](Execution.md)

## Q&A
#### **Q1: What is the purpose of this project?**

Answer: The purpose of this project is to efficiently synchronize Zendesk data into Google BigQuery, providing a faster and more reliable solution compared to existing synchronization methods.


#### **Q2: What are the prerequisites for running this project?**

Answer: The prerequisites for running this project include having Python installed on your system, along with necessary libraries such as pandas and google-cloud-bigquery. Additionally, you will need a Google Cloud project with a valid project ID, a configured BigQuery dataset, and the required permissions to access these resources.


#### **Q3: How are connections to BigQuery managed?**

Answer: Connections to BigQuery are managed using the google.cloud libraries in Python. You need to provide the appropriate credentials, such as the project ID and the path to your authentication JSON key file.


#### **Q4: How does the data synchronization process work?**

Answer: The data synchronization process involves several steps such as converting data from CSV to JSON, correcting data formats, filtering data, and then loading the cleaned data into a specified BigQuery table.


#### **Q5: How can I contribute to this project?**

Answer: Contributions are welcome! You can contribute by submitting suggestions for improvement, reporting issues, or proposing pull requests with code modifications. Make sure to follow the project's contribution guidelines.


#### **Q6: Where can I find more information about this project?**

Answer: You can find more information about this project in the documentation available on the GitHub repository. For specific questions or assistance requests, you can contact the project owner via the provided email address in the documentation.

## More question
contact me :)