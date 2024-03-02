from tabulate import tabulate
import modules.search as search
import os

def newAssing(data:dict):
    os.system('cls')
    new = {}
    titulo=[["AÑADIR ASIGNACIÓN"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    try:
        NroAsignacion = int(input('Ingresa el numero de asignación '))
        FechaAsignacion = input('Ingresa la fecha de asignación ')
        tipo = int('Tipo de asignación: \n1. Personal \n2. Zona')
    except ValueError:
        print('El valor ingresado no es un numero')
        return
    if tipo == 1:
        tipo = 'Personal'
        Asignado = search.personaSearch(data, 1)['Id']
    elif tipo == 2:
        tipo = 'Zona'
        Asignado = search.zonaSearch(data, 1)['NombreZona']
    blueprint = {
        'NroAsignacion':NroAsignacion,
        'FechaAsignacion':FechaAsignacion,
        'Tipo':tipo,
        'Asignado':Asignado,
        'Activos':[]
    }
    while True:
        activo = search.activosSearch(data, 1)
        if activo['Estado'] == 2:
            print('El Activo esta dado de baja')
        elif activo['Estado'] == 3:
            print('El Activo esta en garantia, necesotas actualizar su estado')
        else:
            blueprint['Activos'].append(activo['CodCampus'])
        continueAsk = input('Deseas añadir otro activo')
        if continueAsk.lower() == "s":
            pass
        else:
            print(f'{len(blueprint['Activos'])} activos añadidos satisfactoriamente')
            break
    new[NroAsignacion] = blueprint
    data['Asignacion'].update(new)

