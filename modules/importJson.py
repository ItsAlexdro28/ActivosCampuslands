import csv
import json
data = {
    'Personal': {},
    'Zonas': {},
    'Asignacion': {},
    'Activos':{}
}
history = {}

DIR = 'data/'
def addCsv():
    with open(DIR+'data.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        #PARA QUE EL IDENTIFICADOR POR ACTIVO SEA EL CODIGO
        keyColumnIndex = 2
        for row in reader:
            key = row[keyColumnIndex]
            row_dict = {}
            for i, value in enumerate(row):
                if value == '[]':
                    value = []
                row_dict[headers[i]] = value
            data['Activos'][key] = row_dict
    return
#itera en cada fila, asigna el valor de acurdo al primer valor de la columna y agrega con identificacion 'CodCampus'

def readJson(filename):
    try:
        with open(DIR+filename+'.json', 'r') as rd:
            return json.load(rd)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Invalid JSON format in file '{filename}'.")
    return
    
def writeJson(data, filename):
    try:
        with open(DIR+filename+'.json', 'w') as wr:
            json.dump(data, wr, indent=4) 
    except IOError as e:
        raise IOError(f"Error writing to file '{filename}': {e}")
    return

addCsv()
writeJson(data, 'data')




