```python
# Import necessary libraries
from google.cloud import pubsub_v1
from google.cloud import bigquery
import os

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('your_project_id', 'your_topic_id')

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# Function to ingest data from Pub/Sub into BigQuery
def ingest_data(data):
    # Convert data to string
    data = str(data)

    # Publish data to the Pub/Sub topic
    future = publisher.publish(topic_path, data)
    print(future.result())

    # Ingest data into BigQuery
    table_id = "your_project_id.your_dataset_id.your_table_id"
    rows_to_insert = [(data,)]
    errors = bigquery_client.insert_rows_json(table_id, rows_to_insert)

    # If errors are returned, print them
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")
    else:
        print("Rows inserted successfully.")

# Function to ingest financial data
def ingest_financial_data():
    # Here, you would typically fetch your financial data from an API or a database
    # For the sake of simplicity, let's assume we have a list of financial data
    financial_data = ["data1", "data2", "data3"]

    # Ingest each piece of data
    for data in financial_data:
        ingest_data(data)

# Call the function to start the data ingestion process
ingest_financial_data()
```
