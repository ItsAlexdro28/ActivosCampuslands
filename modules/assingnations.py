from tabulate import tabulate
import modules.search as search
import os

def newAssing(data:dict):
    os.system('cls')
    new = {}
    titulo=[["AÑADIR ASIGNACIÓN"]]
    oldActivo = 000
    print(tabulate(titulo,tablefmt="double_grid"))
    try:
        NroAsignacion = int(input('Ingresa el numero de asignación:\n>> '))
        FechaAsignacion = input('Ingresa la fecha de asignación \n>>')
        tipo = int(input('Tipo de asignación: \n1. Personal \n2. Zona\n>>'))
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
            'Activos':[],
            'HistorialId':0
        }
        while True:
            try:
                activo = search.activosSearch(data, 1)
            except TypeError:
                print('La zona o persona no esta en la base de datos')
                return
            if activo['Estado'] == 2:
                print('El Activo esta dado de baja')
                return
            elif activo['Estado'] == 3:
                print('El Activo esta en garantia, necesitas actualizar su estado')
                return
            else:
                if not activo == oldActivo:
                    blueprint['Activos'].append(activo['CodCampus'])
            oldActivo = activo
            continueAsk = input('Deseas añadir otro activo SI(s) NO(n)')
            if continueAsk.lower() == "s":
                pass
            else:
                length = len(blueprint['Activos'])
                print(f'{length} activos añadidos satisfactoriamente')
                break
        new[NroAsignacion] = blueprint
        data['Asignacion'].update(new)
        os.system('pause')
        return
    except ValueError:
        print('El valor ingresado no es un numero')
        os.system('pause')
        return
    except TypeError:
        print('La zona o persona no esta en la base de datos')
        os.system('pause')
        return


