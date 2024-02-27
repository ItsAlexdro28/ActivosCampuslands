from csv import reader
data = []
with open('', 'r') as file:
    lector = reader(file)
    for row in lector:
        data.append(row[0].split(';'))
print(data)