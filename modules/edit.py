from tabulate import tabulate
import os
import modules.menus as m
def activosEdit(data:dict):
    try:
        os.system('cls')
        titulo=[["EDITAR ACTIVOS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        codCampus = input("Ingresa el valor del Codigo de campus para editar \n>> ").upper()
        #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
        keysRead = ['Codigo de Transaccion','Numero de Formulario','Codigo Campus','Marca','Categoria','Tipo','ValUnid','Proveedor','Numero Serial','la Empresa Responsable','Estado']
        if codCampus in data['Activos']:
            activeToEdit = data['Activos'][codCampus]
            print("Detalles de Activo:\n>> ")
            for i, (key, value) in enumerate(activeToEdit.items()):
                if key != 'Historial':  # Saltar el historial
                    print(f"{i+1}. {keysRead[i]}: {value}")
            try:
                indexToEdit = int(input("Ingrese el numero de identificacion del valor que desea editar (-1 para cancelar o 0 para editarlos todos):\n>> "))
            except ValueError:
                print("Invalid input. Escriba un entero.\n>> ")
                os.system('pause')
                m.menuPRINCIPAL() 
                #VOLVER AL MENU PRINCIPAL
            if indexToEdit == 0:
                    # Edit todos los valores
                    x = 0
                    for key, value in activeToEdit.items():
                        if key != 'Historial':  # Saltar el historial
                            newValue = input(f"Ingresa el nuevo valor para '{str(keysRead[x])}':\n>> ")
                            activeToEdit[key] = newValue
                        x += 1
                    print(f"Activo '{codCampus}' fue editado satisfactoriamente.\n>> ")
                    os.system('pause')
                    return
            if indexToEdit == -1:
                print("Cancelado")
                os.system('pause')
                return

            if 0 < indexToEdit < len(list(activeToEdit.items())):
                keyToEdit = list(activeToEdit.keys())[indexToEdit-1]  # Extraer llave
                newValue = input(f"Ingresa el nuevo valor para '{keyToEdit}'\n>>")
                if keyToEdit == 'CodCampus':
                    data["Activos"][newValue] = data["Activos"][codCampus]
                    del data["Activos"][codCampus]
                else:
                    activeToEdit[keyToEdit] = newValue
                activeToEdit[keyToEdit] = newValue
                print(f"Activo '{activeToEdit['CodCampus']}' Actualizado.")
                os.system('pause')
                return
            else:
                print(f"Index invalido: {indexToEdit}. Ingresa un valor valido entre -1 y {len(indexToEdit) - 1}.\n>> ")
                os.system('pause')
                m.menuPRINCIPAL() 
            
        else:
            print(f"Activo con Codigo de campus '{indexToEdit}' no ha sido encontrado. \n>> ")
            os.system('pause')
            m.menuPRINCIPAL() 
    except UnboundLocalError as i:
        print('El valor ingresado no es valido\n>>' )
        os.system('pause')

# Esta función permite a los usuarios editar los detalles de un activo existente en función de su clave 'CodCampus'.
# Solicita al usuario que ingrese la clave 'CodCampus' del activo que desea editar.
# Si se encuentra el activo, muestra todos sus detalles con números de índice que comienzan desde 1.
# Luego, el usuario puede elegir el índice del valor que desea editar o ingresar 0 para editar todos los valores.
# Para cada valor que se va a editar, se le solicita al usuario que ingrese el nuevo valor.
# Luego, la función actualiza los detalles del activo en el diccionario de datos.
# Finalmente muestra un mensaje indicando si el activo se actualizó exitosamente o no.

def peopleEdit(data:dict):
    try:
        os.system('cls')
        titulo=[["EDITAR PERSONAL"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        id = input("Ingresa el id de la persona para editar \n>> ").upper()
        #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
        info = ['Nombre','Id','Email','Telefono','Celular']
        if id in data['Personal']:
            peopleToEdit = data['Personal'][id]
            print("Detalles del personal:")
            for i, (key, value) in enumerate(peopleToEdit.items()):
                if key != 'Historial':  # Saltar el historial
                    print(f"{i+1}. {info[i]}: {value}")
            try:
                indexToEdit = int(input("Ingrese el numero de identificacion del valor que desea editar (-1 para cancelar o 0 para editarlos todos): \n>> "))
            except ValueError:
                print("Invalid input. Escriba un entero.\n>> ")
                return #VOLVER AL MENU PRINCIPAL
            
            if indexToEdit == 0:
                    # Edit todos los valores
                    x = 0
                    for key, value in peopleToEdit.items():
                        newValue = input(f"Ingresa el nuevo valor para '{info[x]}'\n>>")
                        peopleToEdit[key] = newValue
                        x += 1
                    print(f"El personal con id #'{id}' fue editado satisfactoriamente.\n>> ")
                    os.system('pause')
                    return
            if indexToEdit == -1:
                print("Cancelado")
                os.system('pause')
                return

            if 0 < indexToEdit < len(list(peopleToEdit.items())):
                keyToEdit = list(peopleToEdit.keys())[indexToEdit-1]  # Extraer llave
                newValue = input(f"Ingresa el nuevo valor para '{keyToEdit}'\n>>")
                if keyToEdit == 'Id':
                    data["Personal"][newValue] = data["Personal"][id]
                    del data["Personal"][id]
                else:
                    peopleToEdit[keyToEdit] = newValue
                peopleToEdit[keyToEdit] = newValue
                print(f"Personal '{peopleToEdit['Id']}' Actualizado.")
                os.system('pause')
                return
            else:
                print(f"Index invalido: {indexToEdit}. Ingresa un valor valido entre -1 y {len(indexToEdit) - 1}.\n>> ")
                os.system('pause')
                return
            
        else:
            print(f"El personal con id#{id} '{indexToEdit}' no ha sido encontrado.\n>> ")
            os.system('pause')
            return
    except UnboundLocalError as i:
        print('El valor ingresado no es valido\n>> ')
        os.system('pause')

def zonaEdit(data:dict):
    try:
        os.system('cls')
        titulo=[["EDITAR ZONAS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        nombre = input("Ingrese el nombre de la zona para editar").upper()
        #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
        info2 = ['NroZona','NombreZona','totalCapacidad']
        if nombre in data['Zonas']:      
            zoneToEdit = data['Zonas'][nombre]
            print("Detalles de la zona:")
            for i, (key, value) in enumerate(zoneToEdit.items()):
                if key != 'Historial':  # Saltar el historial
                    print(f"{i+1}. {info2[i]}: {value}")
            try:
                indexToEdit = int(input("Ingrese el numero de identificacion del valor que desea editar (-1 para cancelar o 0 para editarlos todos):\n>>  "))
            except ValueError:
                print("Invalid input. Escriba un entero.")
                return #VOLVER AL MENU PRINCIPAL       
            if indexToEdit == 0:
                    # Edit todos los valores
                    x = 0
                    for key, value in zoneToEdit.items():
                        newValue = input(f"Ingresa el nuevo valor para '{info2[x]}'\n>>")
                        zoneToEdit[key] = newValue
                        x += 1
                    print(f"Zona '{nombre}' fue editada satisfactoriamente.")
                    os.system('pause')
                    return
            if indexToEdit == -1:
                print("Cancelado")
                os.system('pause')
                return

            if 0 < indexToEdit < len(list(zoneToEdit.items())):
                keyToEdit = list(zoneToEdit.keys())[indexToEdit-1]  # Extraer llave
                newValue = input(f"Ingresa el nuevo valor para '{keyToEdit}'\n>>")
                if keyToEdit == 'NombreZona':
                    data["Zonas"][newValue] = data["Zonas"][nombre]
                    del data["Zonas"][nombre]
                else:
                    zoneToEdit[keyToEdit] = newValue
                zoneToEdit[keyToEdit] = newValue
                print(f"Zona '{zoneToEdit['NombreZona']}' Actualizada.")
                os.system('pause')
                return
            else:
                print(f"Index invalido: {indexToEdit}. Ingresa un valor valido entre -1 y {len(indexToEdit) - 1}.\n>> ")
                os.system('pause')
                return
            
        else:
            print(f"La zona '{indexToEdit}' no ha sido encontrada.\n>> ")
            os.system('pause')
            return
    except UnboundLocalError as i:
        print('El valor ingresado no es valido\n>> ')
        os.system('pause')

def estadoEdit(data:dict, estado):
    os.system('cls')
    titulo=[["EDITAR ESTADO DE ACTIVO"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus para editar\n>> ").upper()
    #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
    if codCampus in data['Activos']:
        activeToEdit = data['Activos'][str(codCampus)]
        activeToEdit['Estado'] = str(estado)
        if estado == 2:
            print(f"Activo '{activeToEdit}' actualizado a 'dado de baja por daño'\n>>  ")
            os.system('pause') 
        elif estado == 3:
            print(f"Activo '{activeToEdit}' actualizado a 'reparacion por garantia'\n>>  ")
            os.system('pause')   
    return(data['Activos'][str(codCampus)])   

def returnEdit(data:dict, history:dict):
    os.system('cls')
    titulo=[["RETORNAR ACTIVO"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus para editar\n>> ").upper()
    if codCampus in data['Activos']:
        ultHistorial = data['Activos'][str(codCampus)]['Historial'][-1]
        ultAssing = history[str(ultHistorial)]['IdAssing']
        data['Assignaciones'][str(ultAssing)].remove(codCampus)
        data['Activos'][str(codCampus)]['Estado'] = '0'
    return(data['Activos'][str(codCampus)])

def activeAssingEdit(data:dict, history:dict):
    os.system('cls')
    titulo=[["CAMBIAR ASIGNACION ACTIVO"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus para editar\n>> ").upper()
    if codCampus in data['Activos']:
        ultHistorial = data['Activos'][str(codCampus)]['Historial'][-1]
        ultAssing = history[str(ultHistorial)]['IdAssing']
        data['Asignaciones'][str(ultAssing)].remove(codCampus)
    newAssing = input("Ingresa el numero de asignacion para agregar cambiar el activo\n>>  ")
    data['Asignaciones'][str(newAssing)]['Activos'].append(codCampus)
    return


