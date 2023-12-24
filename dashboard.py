```python
# Import necessary libraries
from google.cloud import bigquery
from flask import Flask, render_template
import os
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# Initialize Flask app
app = Flask(__name__)

# Function to fetch data from BigQuery
def fetch_data():
    # Define the SQL query
    sql_query = """
    SELECT *
    FROM `your_project_id.your_dataset_id.your_table_id`
    """

    # Execute the query and get the result as a pandas DataFrame
    df = bigquery_client.query(sql_query).to_dataframe()

    return df

# Function to create a Plotly figure
def create_figure(df):
    # Create a line chart with market data
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['price'], mode='lines', name='Price'))

    # Add title and labels
    fig.update_layout(title='Market Data', xaxis_title='Date', yaxis_title='Price')

    return fig

# Route for the dashboard
@app.route('/')
def dashboard():
    # Fetch data
    df = fetch_data()

    # Create figure
    fig = create_figure(df)

    # Convert the figure to HTML
    plot_html = fig.to_html(full_html=False)

    # Render the dashboard template with the plot
    return render_template('dashboard.html', plot_html=plot_html)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
