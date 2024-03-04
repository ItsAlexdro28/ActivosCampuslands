from tabulate import tabulate
import os

def activosSearch(data:dict, state) :
    os.system('cls')
    titulo=[["BUSCAR"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    codCampus = input("Ingresa el valor del Codigo de campus ").upper()
    if codCampus in data["Activos"]:
        activeToSearch = data["Activos"][codCampus]
        if state == 1:
            return(activeToSearch)
        if state == 2:
            print("Detalles de Activo: ")
            for key, value in activeToSearch.items():
                print(f"{key}: {value}")
        os.system('pause')
        return
    else:
        print(f"Activo con Codigo de campus '{codCampus}' no ha sido encontrado")
        os.system('pause')
        return
# Esta función permite a los usuarios mostrarle los archivos de un activo existente en función de su clave 'CodCampus'.
# Solicita al usuario que ingrese la clave 'CodCampus' del activo que desea detallar.
# Si se encuentra el activo, muestra todos sus detalles.
# Si no encuentra el activo, le dice al usuario
        
def personaSearch(data:dict, state) :
    os.system('cls')
    titulo=[["BUSCAR PERSONA"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    idPersonal = input("Ingresa el numero de identificacion del personal ")
    if idPersonal in data["Personal"]:
        personalToSearch = data["Personal"][idPersonal]
        if state == 1:
            return(personalToSearch)
        if state == 2:
            print("Detalles de Activo: ")
            for key, value in personalToSearch.items():
                print(f"{key}: {value}")
        os.system('pause')
        return
    else:
        print(f"Personal con identificacion '{idPersonal}' no ha sido encontrado")
        os.system('pause')
        return

def zonaSearch(data:dict, state) :
    os.system('cls')
    titulo=[["BUSCAR ZONA "]]
    print(tabulate(titulo,tablefmt="double_grid"))
    zoneName = input("Ingresa el nombre de la zona ").upper()
    if zoneName in data["Zonas"]:
        zonaToSearch = data["Zonas"][zoneName]
        if state == 1:
            return(zonaToSearch)
        if state == 2:
            print("Detalles de Activo: ")
            for key, value in zonaToSearch.items():
                print(f"{key}: {value}")
        os.system('pause')
        return
    else:
        print(f"La zona '{zoneName}' no ha sido encontrada")
        os.system('pause')
        return


def asigSearch(data:dict, state) :
    os.system("cls")
    titulo=[["BUSCAR ASIGNACION"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    asigNro = input("Ingresa el Nro. de la asignacion ")
    if asigNro in data["Asignacion"].keys():
        asigSearch = data["Asignacion"][asigNro]
        if state == 1:
            return(asigSearch)
        if state == 2:
            print("Detalles de la asignacion: ")
            for key, value in asigSearch.items():
                print(f"{key}: {value}")
        os.system('pause')
        return
    else:
        print(f"La asignacion con Nro.'{asigNro}' no ha sido encontrada")
        os.system('pause')
        return