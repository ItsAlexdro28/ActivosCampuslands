import csv
import json
data = {}
with open('data/data.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    key_column_index = 2
    for row in reader:
        key = row[key_column_index]
        row_dict = {}
        for i, value in enumerate(row):
            row_dict[headers[i]] = value
        data[key] = row_dict

with open('data/data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)  

print(f"Data saved to data/data.json")
