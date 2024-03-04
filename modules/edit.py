from tabulate import tabulate
import os
def activosEdit(data:dict):
    os.system('cls')
    titulo=[["EDITAR ACTIVOS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus para editar")
    #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
    keysRead = ['Codigo de Transaccion','Numero de Formulario','Codigo Campus','Marca','Categoria','Tipo','ValUnid','Proveedor','Numero Serial','la Empresa Responsable','Estado']
    if codCampus in data['Activos']:
        activeToEdit = data['Activos'][codCampus]
        print("Detalles de Activo:")
        for i, (key, value) in enumerate(activeToEdit.items()):
            if key != 'Historial':  # Saltar el historial
                print(f"{i+1}. {keysRead[i]}: {value}")
        try:
            indexToEdit = int(input("Ingrese el numero de identificacion del valor que desea editar (-1 para cancelar o 0 para editarlos todos): "))
        except ValueError:
            print("Invalid input. Escriba un entero.")
            return #VOLVER AL MENU PRINCIPAL
        if indexToEdit == 0:
                # Edit todos los valores
                for key, value in activeToEdit.items():
                    x = 0
                    if key != 'Historial':  # Saltar el historial
                        newValue = input(f"Ingresa el nuevo valor para '{keysRead[x]}': ")
                        activeToEdit[key] = newValue
                    x += 1
                print(f"Activo '{codCampus}' fue editado satisfactoriamente.")
                return
        if indexToEdit == -1:
            print("Cancelado")
            return

        if 0 < indexToEdit < len(list(activeToEdit.items())):
            keyToEdit, _ = list(activeToEdit.items())[indexToEdit-1]  # Extraer llave
            keyToPrint, _ = list(keysRead[indexToEdit-1])
            newValue = input(f"Ingresa el nuevo valor para '{keyToPrint}': ")
            activeToEdit[keyToEdit] = newValue
            print(f"Activo '{activeToEdit}' Actualizado.")
            return
        else:
            print(f"Index invalido: {indexToEdit}. Ingresa un valor valido entre -1 y {len(indexToEdit) - 1}.")
          
    else:
        print(f"Activo con Codigo de campus '{indexToEdit}' no ha sido encontrado.")

# Esta función permite a los usuarios editar los detalles de un activo existente en función de su clave 'CodCampus'.
# Solicita al usuario que ingrese la clave 'CodCampus' del activo que desea editar.
# Si se encuentra el activo, muestra todos sus detalles con números de índice que comienzan desde 1.
# Luego, el usuario puede elegir el índice del valor que desea editar o ingresar 0 para editar todos los valores.
# Para cada valor que se va a editar, se le solicita al usuario que ingrese el nuevo valor.
# Luego, la función actualiza los detalles del activo en el diccionario de datos.
# Finalmente muestra un mensaje indicando si el activo se actualizó exitosamente o no.

def peopleEdit(data:dict):
    os.system('cls')
    titulo=[["EDITAR PERSONAL"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    id = input("Ingresa el id de la persona para editar")
    #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
    info = ['Nombre','Id','Email','Telefono','Celular']
    if id in data['Personal']:
        peopleToEdit = data['Personal'][id]
        print("Detalles del personal:")
        for i, (key, value) in enumerate(peopleToEdit.items()):
            if key != 'Historial':  # Saltar el historial
                print(f"{i+1}. {info[i]}: {value}")
        try:
            indexToEdit = int(input("Ingrese el numero de identificacion del valor que desea editar (-1 para cancelar o 0 para editarlos todos): "))
        except ValueError:
            print("Invalid input. Escriba un entero.")
            return #VOLVER AL MENU PRINCIPAL
        if indexToEdit == 0:
                # Edit todos los valores
                for key, value in peopleToEdit.items():
                    x = 0
                    if key != 'Historial':  # Saltar el historial
                        newValue = input(f"Ingresa el nuevo valor para '{info[x]}': ")
                        peopleToEdit[key] = newValue
                    x += 1
                print(f"El personal con id #'{id}' fue editado satisfactoriamente.")
                return
        if indexToEdit == -1:
            print("Cancelado")
            return

        if 0 < indexToEdit < len(list(peopleToEdit.items())):
            keyToEdit, _ = list(peopleToEdit.items())[indexToEdit-1]  # Extraer llave
            keyToPrint, _ = list(info[indexToEdit-1])
            newValue = input(f"Ingresa el nuevo valor para '{keyToPrint}': ")
            peopleToEdit[keyToEdit] = newValue
            print(f"Activo '{peopleToEdit}' Actualizado.")
            return
        else:
            print(f"Index invalido: {indexToEdit}. Ingresa un valor valido entre -1 y {len(indexToEdit) - 1}.")
          
    else:
        print(f"El personal con id#{id} '{indexToEdit}' no ha sido encontrado.")

def zonaEdit(data:dict):
    os.system('cls')
    titulo=[["EDITAR ZONAS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    nombre= input("Ingrese el nombre de la zona para editar")
    #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
    info2 = ['NroZona','NombreZona','totalCapacidad']
    if nombre in data['Zonas']:      
        zoneToEdit = data['Zonas'][nombre]
        print("Detalles de la zona:")
        for i, (key, value) in enumerate(zoneToEdit.items()):
            if key != 'Historial':  # Saltar el historial
                print(f"{i+1}. {info2[i]}: {value}")
        try:
            indexToEdit = int(input("Ingrese el numero de identificacion del valor que desea editar (-1 para cancelar o 0 para editarlos todos): "))
        except ValueError:
            print("Invalid input. Escriba un entero.")
            return #VOLVER AL MENU PRINCIPAL
        if indexToEdit == 0:
                # Edit todos los valores
                for key, value in zoneToEdit.items():
                    x = 0
                    if key != 'Historial':  # Saltar el historial
                        newValue = input(f"Ingresa el nuevo valor para '{info2[x]}': ")
                        zoneToEdit[key] = newValue
                    x += 1
                print(f"La zona '{nombre}' fue editada satisfactoriamente.")
                return
        if indexToEdit == -1:
            print("Cancelado")
            return

        if 0 < indexToEdit < len(list(zoneToEdit.items())):
            keyToEdit, _ = list(zoneToEdit.items())[indexToEdit-1]  # Extraer llave
            keyToPrint, _ = list(info2[indexToEdit-1])
            newValue = input(f"Ingresa el nuevo valor para '{keyToPrint}': ")
            zoneToEdit[keyToEdit] = newValue
            print(f"Zona '{zoneToEdit}' Actualizada.")
            return
        else:
            print(f"Index invalido: {indexToEdit}. Ingresa un valor valido entre -1 y {len(indexToEdit) - 1}.")
          
    else:
        print(f"La zona '{indexToEdit}' no ha sido encontrada.")

def estadoEdit(data:dict, estado):
    os.system('cls')
    titulo=[["EDITAR ESTADO DE ACTIVO"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus para editar")
    #LISTA DE LLAVES PARA QUE EL USUARIO LO LEA MAS BONITO
    if codCampus in data['Activos']:
        activeToEdit = data['Activos'][str(codCampus)]
        activeToEdit['Estado'] = str(estado)
        if estado == 2:
            print(f"Activo '{activeToEdit}' actualizado a 'dado de baja por daño' ") 
        elif estado == 3:
            print(f"Activo '{activeToEdit}' actualizado a 'reparacion por garantia' ")   
    return(data['Activos'][str(codCampus)])   

def returnEdit(data:dict, history:dict):
    os.system('cls')
    titulo=[["RETORNAR ACTIVO"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus para editar")
    if codCampus in data['Activos']:
        ultHistorial = data['Activos'][str(codCampus)]['Historial'][-1]
        ultAssing = history[str(ultHistorial)]['IdAssing']
        data['Assignaciones'][str(ultAssing)].remove(codCampus)
        data['Activos'][str(codCampus)]['Estado'] = '0'

def activeAssingEdit(data:dict, history:dict):
    os.system('cls')
    titulo=[["CAMBIAR ASIGNACION ACTIVO"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus para editar")
    if codCampus in data['Activos']:
        ultHistorial = data['Activos'][str(codCampus)]['Historial'][-1]
        ultAssing = history[str(ultHistorial)]['IdAssing']
        data['Asignaciones'][str(ultAssing)].remove(codCampus)
    newAssing = input("Ingresa el numero de asignacion para agregar cambiar el activo ")
    data['Asignaciones'][str(newAssing)]['Activos'].append(codCampus)


