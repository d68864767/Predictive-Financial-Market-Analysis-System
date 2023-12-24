```python
# Import necessary libraries
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import os

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize Cloud Natural Language API client
client = language_v1.LanguageServiceClient()

# Function to analyze sentiment of a text
def analyze_sentiment(text):
    # The text should be in a document
    document = language_v1.types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT,
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print(f"Text: {text}")
    print(f"Sentiment: score {sentiment.score}, magnitude {sentiment.magnitude}")

# Function to analyze sentiment of financial news
def analyze_financial_news():
    # Here, you would typically fetch your financial news from an API or a database
    # For the sake of simplicity, let's assume we have a list of financial news
    financial_news = ["news1", "news2", "news3"]

    # Analyze sentiment for each news
    for news in financial_news:
        analyze_sentiment(news)

# Call the function to start the sentiment analysis process
analyze_financial_news()
```
