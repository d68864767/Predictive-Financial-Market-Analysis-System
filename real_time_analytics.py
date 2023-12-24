```python
# Import necessary libraries
from google.cloud import pubsub_v1
from google.cloud import bigquery
import os
import pandas as pd

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize Pub/Sub client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path('your_project_id', 'your_subscription_id')

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# Function to process real-time data from Pub/Sub
def process_real_time_data(message):
    # Convert message data to string
    data = message.data.decode("utf-8")

    # Here, you would typically perform real-time analytics on the data
    # For the sake of simplicity, let's assume we just print the data
    print(f"Received data: {data}")

    # Acknowledge the message
    message.ack()

# Function to start real-time analytics
def start_real_time_analytics():
    # Subscribe to the Pub/Sub topic
    future = subscriber.subscribe(subscription_path, process_real_time_data)

    # Keep the main thread from exiting so the subscriber can process messages in the background
    try:
        future.result()
    except Exception as e:
        future.cancel()
        print(f"Subscription cancelled due to {e}.")

# Call the function to start real-time analytics
start_real_time_analytics()
```
