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
            print("Deletion cancelled.")
    else:
        print(f"Activo con Codigo de campus '{codCampus}' no ha sido encontrado")
