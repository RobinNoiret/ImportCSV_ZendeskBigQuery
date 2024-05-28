# Execution

## Execution steps

#### 1. Clean and CSV to JSON conversion:

- **Input:** CSV file (input.csv).
- **Output:** JSON file (JSON_data.json).
- **Process:** Calls clean_and_convert_csv_to_json() function to convert CSV to JSON.


#### 2. JSON to NDJSON conversion:

- **Input:** JSON file (JSON_data.json).
- **Output:** NDJSON file (NDJSON_data.json).
- **Process:** Calls convert_json_to_ndjson() function to convert JSON to NDJSON.


#### 3. Data Filtering:

- **Input:** NDJSON file (NDJSON_data.json).
- **Output:** Filtered JSON file (FILTERED_data.json).
- **Process:** Calls data_filtering() function to filter data based on column mappings.


#### 4. JSON to NDJSON conversion (Filtered):

- **Input:** Filtered JSON file (FILTERED_data.json).
- **Output:** NDJSON file (NDJSON_data2.json).
- **Process:** Calls convert_json_to_ndjson() function to convert filtered JSON to NDJSON.


#### 5. Date Format Correction:

- **Input:** Filtered NDJSON file (NDJSON_data2.json).
- **Output:** JSON file with corrected dates (DateCorrection.json).
- **Process:** Calls date_correction() function to correct date formats.


#### 6. Organization Name Correction:

- **Input:** JSON file with corrected dates (DateCorrection.json).
- **Output:** JSON file with filled organization names (OrgaName.json).
- **Process:** Calls fill_organization_name() function to populate missing organization names.


#### 7. Correct Tag Format:

- **Input:** JSON file with filled organization names (OrgaName.json).
- **Output:** Final JSON file with corrected tag format (Output.json).
- **Process:** Calls convert_tags_to_list() function to convert tags to list format.


#### 8. BigQuery Data Loading:

- **Input:** Final JSON file with corrected tag format (Output.json).
- **Process:**
-> Initializes the BigQuery client.
-> Verifies dataset and table existence.
-> Configures load job settings.
-> Loads JSON data into the BigQuery table.


#### 9. Completion Message:

Displays a success message upon successful data loading into the BigQuery table.


#### 10. Connection Closure:

Closes the connection to BigQuery after data loading is completed.