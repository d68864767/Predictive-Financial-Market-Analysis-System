```python
# Import necessary libraries
import os

# Import modules from other files
from data_ingestion import ingest_financial_data
from data_processing import process_data
from ml_model import prepare_data, train_model, predict
from sentiment_analysis import analyze_sentiment
from real_time_analytics import real_time_analytics
from dashboard import run_dashboard

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

def main():
    # Ingest financial data
    ingest_financial_data()

    # Process the ingested data
    processed_data = process_data()

    # Prepare the data for model training
    train_features, train_labels, test_features, test_labels = prepare_data(processed_data)

    # Train the machine learning model
    model = train_model(train_features, train_labels)

    # Make predictions using the trained model
    predictions = predict(model, test_features)

    # Analyze sentiment of financial news
    sentiment_scores = analyze_sentiment("Sample financial news text")

    # Run real-time analytics
    real_time_analytics()

    # Run the investment dashboard
    run_dashboard(predictions, sentiment_scores)

if __name__ == "__main__":
    main()
```
