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
# Esta función permite a los usuarios eliminar un activo existente en función de su clave 'CodCampus'.
# Solicita al usuario que ingrese la clave 'CodCampus' del activo que desea eliminar.
# Si se encuentra el activo, muestra todos sus detalles.
# Luego, la función solicita al usuario que confirme la eliminación.
# Si el usuario confirma, la función elimina el activo del diccionario de datos.
# Finalmente, muestra un mensaje indicando si el activo se eliminó exitosamente o no.
