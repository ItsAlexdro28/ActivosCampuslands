import csv
import json
data = {
    'Personal': {},
    'Zonas': {},
    'Asignacion': {},
    'Activos':{}
}

DIR = 'data/'
with open(DIR+'data.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    key_column_index = 2
    for row in reader:
        key = row[key_column_index]
        row_dict = {}
        for i, value in enumerate(row):
            if value == '[]':
                value = []
            row_dict[headers[i]] = value
        data['Activos'][key] = row_dict
#itera en cada fila, asigna el valor de acurdo al primer valor de la columna y agrega con identificacion 'CodCampus'

def readJson(filename):
    try:
        with open(DIR+filename+'.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Invalid JSON format in file '{filename}'.")
    
def writeJson(data, filename):
    try:
        with open(DIR+filename+'.json', 'w') as f:
            json.dump(data, f, indent=4) 
    except IOError as e:
        raise IOError(f"Error writing to file '{filename}': {e}")

writeJson(data, 'data')  
