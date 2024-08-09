import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def download_table_from_url(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with the specified class name
        table = soup.find('table', class_='sc_plangrid')
        
        # Check if the table is found
        if not table:
            print("No table found with the specified class name.")
            return None

        # Read the table into a pandas DataFrame
        df = pd.read_html(str(table))[0]

        # Replace NaN values with None
        df = df.replace({np.nan: None})

        return df

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage. Error: {e}")
    except Exception as e:
        print(f"An error occurred. Error: {e}")

# Load the JSON file
with open('majorsWithPlan.json', 'r') as file:
    data = json.load(file)

output = {}

for key in data:
    if isinstance(data[key], str):
        print(key, data[key])
        url = data[key]
        df = download_table_from_url(url)
        if df is None:
            continue
        output[key] = df.to_dict(orient='records')  # Convert DataFrame to dictionary

# Save the dictionary data to a JSON file
with open('fullTables.json', 'w') as file:
    json.dump(output, file, indent=4)
