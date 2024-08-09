# Decode Unicode characters in a JSON file

data = open('fullTables.json', 'r').read()

with open('fullTables2.json', 'w') as f:
    f.write(data.encode().decode('unicode_escape'))