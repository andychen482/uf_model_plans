import json

def sort_json_file(input_filepath, output_filepath):
    try:
        # Read the JSON data from the input file
        with open(input_filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Check if the data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("JSON data is not a dictionary")
        
        # Create a new dictionary with the keys sorted
        sorted_data = {k: data[k] for k in sorted(data.keys())}
        
        # Write the sorted data to the output file
        with open(output_filepath, 'w', encoding='utf-8') as file:
            json.dump(sorted_data, file, ensure_ascii=False, indent=4)
        
        print(f"JSON data has been sorted and saved to {output_filepath}")
    
    except FileNotFoundError:
        print(f"File not found: {input_filepath}")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON data from file: {input_filepath}")
    except ValueError as e:
        print(e)

# Usage
sort_json_file('majors.json', 'sortedMajors.json')
