# Documentation for Zendesk to BigQuery Sync

## 1. check_dataset(dataset_ref, client)

- Purpose: Checks for the existence of a dataset in Google BigQuery.
- Parameters:
-> dataset_ref: Reference to the dataset to be checked.
-> client: Google BigQuery client object for making API calls.
- Functionality:
Attempts to retrieve the specified dataset using client.get_dataset(dataset_ref).
If the dataset exists, it prints a success message.
If the dataset does not exist, it prints an error message and exits the program.
- Usage:
Before performing operations on a dataset, it ensures that the dataset exists in BigQuery.

## 2. check_table(table_ref, client)

- Purpose: Checks for the existence of a table in Google BigQuery.
- Parameters:
-> table_ref: Reference to the table to be checked.
-> client: Google BigQuery client object for making API calls.
- Functionality:
Attempts to retrieve the specified table using client.get_table(table_ref).
If the table exists, it prints a success message.
If the table does not exist, it prints an error message indicating the need to create a table schema.
- Usage:
Verifies the presence of the destination table before loading data into it.

## 3. clean_and_convert_csv_to_json(csv_Inputfile_path, json_file_path, delimiter=',')

- Purpose: Converts a CSV file to a JSON file while cleaning the data.
- Parameters:
-> csv_Inputfile_path: Path to the input CSV file.
-> json_file_path: Path to save the output JSON file.
- delimiter: Delimiter used in the CSV file (default is comma ,).
- Functionality:
Reads the CSV file and cleans each row.
Writes the cleaned data to a JSON file.
- Usage:
Preprocessing step to convert raw CSV data into a clean JSON format for further processing.

## 4. convert_json_to_ndjson(input_file_path, output_file_path)

- Purpose: Converts a JSON file to NDJSON format (Newline Delimited JSON).
- Parameters:
-> input_file_path: Path to the input JSON file.
-> output_file_path: Path to save the output NDJSON file.
- Functionality:
Reads the input JSON file.
Writes each JSON record as a single line in the output file.
- Usage:
Prepares the data in NDJSON format for efficient loading into BigQuery.


## 5. data_filtering(input_file_path, filtered_output_file_path, column_mapping)

- Purpose: Filters data from a JSON file based on specified column mappings.
- Parameters:
-> input_file_path: Path to the input JSON file.
-> filtered_output_file_path: Path to save the filtered output JSON file.
-> column_mapping: Dictionary mapping file columns to BigQuery columns.
- Functionality:
Reads each JSON record, maps specified columns, and creates filtered data.
Writes the filtered data to a new JSON file.
- Usage:
Selectively extracts and transforms data to match the schema of the destination table in BigQuery.


## 6. date_correction(input_file, output_file)

- Purpose: Corrects the date format in a JSON file.
- Parameters:
-> input_file: Path to the input JSON file.
-> output_file: Path to save the output JSON file with corrected dates.
- Functionality:
Reads each JSON record, checks and corrects the date format if necessary.
- Usage:
Ensures consistency in date formatting for compatibility with BigQuery date fields.


## 7. fill_organization_name(input_file, output_file)

- Purpose: Populates missing organization names using organization IDs.
- Parameters:
-> input_file: Path to the input JSON file.
-> output_file: Path to save the output JSON file with filled organization names.
- Functionality:
Reads each JSON record, checks for missing organization names, and fills them using organization IDs.
- Usage:
Enhances data completeness by providing organization names where missing.


## 8. convert_tags_to_list(input_file, output_file)

- Purpose: Converts tags from string to list format in a JSON file.
- Parameters:
-> input_file: Path to the input JSON file.
-> output_file: Path to save the output JSON file with tags converted to list format.
- Functionality:
Reads each JSON record, converts tag strings to lists if necessary.
- Usage:
Standardizes the format of tags for better handling and querying in BigQuery.
