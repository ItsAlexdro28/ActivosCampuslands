from tabulate import tabulate
import os
os.system('cls')
def listactivosall(data:dict):  
        listall = []
        for keys, activo in data["Activos"].items():
            if activo["Codcampus"] == "Activos":
                nombre = activo["Tipo"]
                numero_serial = activo["NroSerial"]
                subLista = [keys, nombre, numero_serial]
                listall.append(subLista)
        if listall:
            print(tabulate(listall, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            os.system('pause')
        else:
            print(f"No hay activos en la categoría ") 

def listActivosCategoria(data:dict): 
    while True:
        os.system('cls')
        opcion=('1. Equipos de computo \n2. Electrodomesticos \n3. Juegos ')
        print(opcion)
        #EQUIPOS DE COMPUTO
        op = input('>> ')
        if op == "1": 
            list_equipos = []
            for keys, activo in data["Activos"].items():
                if activo["Categoria"] == "Equipo computo":
                    nombre = activo["Nombre"]
                    categoria = activo["Categoria"]
                    numero_serial = activo["NroSerial"]
                    subLista = [keys, nombre,categoria, numero_serial]
                    list_equipos.append(subLista)
            if list_equipos:
                linesPorPage = 30
                totalPag = (len(list_equipos) - 1) // linesPorPage + 1
                for idx in range(totalPag):
                    os.system('cls')
                    subset_data = list_equipos[idx * linesPorPage: (idx + 1) * linesPorPage]
                    print(tabulate(subset_data, headers=["CODIGO", "NOMBRE","CATEGORIA", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                    print(f'Pagina {idx + 1} de {totalPag}')
                    os.system('pause')
                    op = input('Si desea volver al menú, presione 0: ')
                    os.system('cls')
                    if op == "0":
                        os.system('cls')
                        break  
                    print(opcion)
            else:
                print(f"No hay activos en la categoría equipos de computo.")
                os.system('pause')
                os.system('cls')        
            os.system('pause')
            #Electrodomesticos
        elif op == "2":
            list_electro = []
            for keys, activo in data["Activos"].items():
                if activo["Categoria"] == "Electrodomestico":
                    nombre = activo["Nombre"]
                    categoria = activo["Categoria"]
                    numero_serial = activo["NroSerial"]
                    subLista = [keys, nombre,categoria, numero_serial]
                    list_electro.append(subLista)
            if list_electro:
                linesPorPage = 30
                totalPag = (len(list_electro) - 1) // linesPorPage + 1
                for idx in range(totalPag):
                    os.system('cls')
                    subset_data = list_electro[idx * linesPorPage: (idx + 1) * linesPorPage]
                    print(tabulate(subset_data, headers=["CODIGO", "NOMBRE","CATEGORIA", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                    print(f'Pagina {idx + 1} de {totalPag}')
                    os.system('pause')
                    op = input('Si desea volver al menú, presione 0: ')
                    os.system('cls')
                    if op == "0":
                        os.system('cls')
                        break  
                    print(opcion)        
            
                #juegos
        elif op == "3":
            list_juegos = []
            for keys, activo in data["Activos"].items():
                if activo["Categoria"] == "Juegos":
                    nombre = activo["Nombre"]
                    categoria = activo["Categoria"]
                    numero_serial = activo["NroSerial"]
                    subLista = [keys, nombre,categoria, numero_serial]
                    list_juegos.append(subLista)
            if list_juegos:
                linesPorPage = 30
                totalPag = (len(list_juegos) - 1) // linesPorPage + 1
                for idx in range(totalPag):
                    os.system('cls')
                    subset_data = list_juegos[idx * linesPorPage: (idx + 1) * linesPorPage]
                    print(tabulate(subset_data, headers=["CODIGO", "NOMBRE","CATEGORIA", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                    print(f'Pagina {idx + 1} de {totalPag}')
                    os.system('pause')
                    op = input('Si desea volver al menú, presione 0: ')
                    os.system('cls')
                    if op == "0":
                        os.system('cls')
                        break  
                    print(opcion) 
