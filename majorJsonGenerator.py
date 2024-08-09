import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json

# Load and parse the XML file
with open('filtered_sitemap.xml', 'r', encoding='us-ascii') as file:
    xml_data = file.read()
    root = ET.fromstring(xml_data)

# Initialize an empty dictionary to store the results
result_dict = {}

# Loop through each URL in the XML file
for url in root.findall(".//loc"):
    url_text = url.text
    response = requests.get(url_text)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the text in the HTML element with class "page-title"
    page_title = soup.find(class_='page-title')
    
    # If the "page-title" class exists, add it to the dictionary with the URL as the value
    if page_title:
        result_dict[page_title.get_text()] = url_text

# Write the resulting dictionary to a JSON file
with open('majors.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_dict, json_file, ensure_ascii=False, indent=4)
