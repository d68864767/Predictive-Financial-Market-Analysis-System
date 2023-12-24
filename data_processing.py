```python
# Import necessary libraries
from google.cloud import bigquery
import os
import pandas as pd

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# Function to clean and normalize data
def clean_and_normalize_data(data):
    # Here, you would typically perform operations to clean and normalize your data
    # For the sake of simplicity, let's assume we just convert all strings to lowercase
    cleaned_data = [d.lower() for d in data]
    return cleaned_data

# Function to analyze data
def analyze_data(data):
    # Here, you would typically perform complex data analysis
    # For the sake of simplicity, let's assume we just calculate the average length of the strings
    average_length = sum(len(d) for d in data) / len(data)
    return average_length

# Function to process data from BigQuery
def process_data():
    # Define the SQL query
    sql_query = """
    SELECT *
    FROM `your_project_id.your_dataset_id.your_table_id`
    """

    # Execute the query and get the result as a pandas DataFrame
    df = bigquery_client.query(sql_query).to_dataframe()

    # Convert the DataFrame to a list of strings
    data = df.values.tolist()

    # Clean and normalize the data
    cleaned_data = clean_and_normalize_data(data)

    # Analyze the data
    analysis_result = analyze_data(cleaned_data)

    print(f"Analysis result: {analysis_result}")

# Call the function to start the data processing process
process_data()
```
