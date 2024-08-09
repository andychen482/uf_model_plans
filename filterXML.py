import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('sitemap.xml')
root = tree.getroot()

# Define the unwanted substrings
unwanted_substrings = ["UCT", ".pdf", "UFO", ".html"]

# Find and remove URLs containing unwanted substrings
namespace = {'ns': root.tag.split('}')[0][1:]}
for url in root.findall('ns:url', namespaces=namespace):
    loc = url.find('ns:loc', namespaces=namespace)
    if loc is not None and any(substring in loc.text for substring in unwanted_substrings):
        root.remove(url)

# Remove namespaces
for elem in root.iter():
    if '}' in elem.tag:
        elem.tag = elem.tag.split('}', 1)[1]

# Save the modified XML tree back to the file
tree.write('filtered_sitemap.xml', xml_declaration=True, method='xml')
