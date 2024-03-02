from tabulate import tabulate
import os

def activosDelete(data:dict):
    os.system('cls')
    titulo=[["ELIMINAR"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus que desea eliminar")
    if codCampus in data["Activos"]:
        activeToDelete = data["Activos"][codCampus]
        print("Detalles de Activo: ")
        for key, value in activeToDelete.items():
            print(f"{key}: {value}")
        confirmation = input("Estas seguro de eliminar este activo (s/N)? ")
        if confirmation.lower() == "s":
            del data["Activos"][codCampus]
            print(f"Activo '{codCampus}' Eliminado satisfactoriamente")
        else:
            print("Eliminacion Cancelada.")
    else:
        print(f"Activo con Codigo de campus '{codCampus}' no ha sido encontrado")
# Esta función permite a los usuarios eliminar un activo existente en función de su clave 'CodCampus'.
# Solicita al usuario que ingrese la clave 'CodCampus' del activo que desea eliminar.
# Si se encuentra el activo, muestra todos sus detalles.
# Luego, la función solicita al usuario que confirme la eliminación.
# Si el usuario confirma, la función elimina el activo del diccionario de datos.
# Finalmente, muestra un mensaje indicando si el activo se eliminó exitosamente o no.

def peopleDelete(data:dict):
    os.system('cls')
    titulo=[["ELIMINAR PERSONAL"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    idpersonal = input("Ingresa el ID de la persona de campus que desea eliminar")
    if idpersonal in data["Personal"]:
        peopleDelete = data["Personal"][idpersonal]
        print("Detalles de Personal: ")
        for key, value in peopleDelete.items():
            print(f"{key}: {value}")
        confirmation = input("Estas seguro de eliminar esta Persona (s/N)? ")
        if confirmation.lower() == "s":
            del data["Personal"][idpersonal]
            print(f"Personal '{idpersonal}' Eliminado satisfactoriamente")
        else:
            print("Eliminacion Cancelada.")
    else:
        print(f"Persona con id de campus '{idpersonal}' no ha sido encontrado")

def zonDelete(data:dict):
    os.system('cls')
    titulo=[["ELIMINAR ZONAS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    zonDelete = input("Ingresa la zona a eliminarnde campus que desea eliminar")
    if zonDelete in data["Zonas"]:
        zonDelete = data["Zonas"][zonDelete]
        print("Detalles de la zona: ")
        for key, value in zonDelete.items():
            print(f"{key}: {value}")
        confirmation = input("Estas seguro de eliminar esta Zona (s/N)? ")
        if confirmation.lower() == "s":
            del data["Zonas"][zonDelete]
            print(f"Zona '{zonDelete}' Eliminado satisfactoriamente")
        else:
            print("Eliminacion Cancelada.")
    else:
        print(f"Zona con  de campus '{zonDelete}' no ha sido encontrado")















        