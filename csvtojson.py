import csv
import json

csv_file = 'profiles1.csv'
json_file = 'data.json'

data = []

# Read the CSV file with the specified encoding
with open(csv_file, 'r', encoding='utf-8-sig') as file:
    csv_data = csv.DictReader(file)
    
    # Convert each row into a dictionary and add it to the data list
    for row in csv_data:
        data.append(row)

# Write the data to the JSON file
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
