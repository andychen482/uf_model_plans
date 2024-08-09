import json

# Replace 'path/to/your/jsonfile.json' with the actual path to your JSON file
with open('sortedMajors.json', 'r') as file:
    data = json.load(file)

# Append "#modelsemesterplantext" to the end of each value in a key-value pair
for key in data:
    if isinstance(data[key], str):
        data[key] += "#modelsemesterplantext"

# Save the modified data back to the JSON file
# Replace 'path/to/your/jsonfile.json' with the actual path to your JSON file
with open('majorsWithPlan.json', 'w') as file:
    json.dump(data, file, indent=4)

print("The '#modelsemesterplantext' has been appended to each value in the JSON file.")
