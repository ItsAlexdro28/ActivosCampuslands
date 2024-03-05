from tabulate import tabulate
from modules.importJson import readJson
import os
import modules.menus as menu
import modules.validacion as v
os.system('cls')
def listActivosall(data:dict):  
        listall = []
        for i in data["Activos"].items():
            codigo = i[0]
            numeroSerial = data["Activos"][i[0]]["NroSerial"]
            nombre = data["Activos"][i[0]]["CodCampus"]
            subLista = [codigo, nombre, numeroSerial]
            listall.append(subLista)
        if listall:
            print(tabulate(listall, headers=["Codcampus", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            os.system('pause')
        else:
            print(f"No hay activos en la categoría ") 
        if listall:
            # para mostrar solo cierta cantidad de informacion
            linesforPages = 30
            totalPag = (len(listall) - 1) // linesforPages + 1
            for idx in range(totalPag):
                os.system('cls')
                subset_data = listall[idx * linesforPages: (idx + 1) * linesforPages]
                print(tabulate(subset_data, headers=["Codcampus", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                print(f'Pagina {idx + 1} de {totalPag}')
                os.system('pause')
                os.system('cls')
                op = input('Si desea volver al menú, presione 0: ')
                if op == "0":
                    os.system('cls')  
                    menu.menuRep()
        else:
                print(f"No hay existencia de activos aun.")
                os.system('pause')
                os.system('cls')

def listActivoscategoria(data:dict): 
    while True:
        os.system('cls')
        opcion=('1. EQUIPOS DE COMPUTO \n2. ELECTRODOMESTICOS \n3. JUEGOS\n4. REGRESAR A MENU REPORTES\n  ')
        print(tabulate(opcion, tablefmt="fancy_grid"))
        #EQUIPOS DE COMPUTO
        op =v.validacionInt22()
        if op == "1": 
            list_equipos = []
            for keys, activo in data["Activos"].items():
                if activo["Categoria"] == "Equipo de computo":
                    nombre = activo["CodCampus"]
                    categoria = activo["Categoria"]
                    numeroSerial = activo["NroSerial"]
                    subLista = [keys, nombre,categoria, numeroSerial]
                    list_equipos.append(subLista)
            if list_equipos:
                linesforPages = 30
                totalPag = (len(list_equipos) - 1) // linesforPages + 1
                for idx in range(totalPag):
                    os.system('cls')
                    subset_data = list_equipos[idx * linesforPages: (idx + 1) * linesforPages]
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
                if activo["Categoria"] == "Electrodomesticos":
                    nombre = activo["CodCampus"]
                    categoria = activo["Categoria"]
                    numero_serial = activo["NroSerial"]
                    subLista = [keys, nombre,categoria, numero_serial]
                    list_electro.append(subLista)
            if list_electro:
                linesforPages = 30
                totalPag = (len(list_electro) - 1) // linesforPages + 1
                for idx in range(totalPag):
                    os.system('cls')
                    subset_data = list_electro[idx * linesforPages: (idx + 1) * linesforPages]
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
                print(f"No hay activos en la categoría electrodomesticos.")
                os.system('pause')
                os.system('cls')        
            os.system('pause')               
            
                #juegos
        elif op == "3":
            list_juegos = []
            for keys, activo in data["Activos"].items():
                if activo["Categoria"] == "Juegos":
                    nombre = activo["CodCampus"]
                    categoria = activo["Categoria"]
                    numero_serial = activo["NroSerial"]
                    subLista = [keys, nombre,categoria, numero_serial]
                    list_juegos.append(subLista)
            if list_juegos:
                linesforPages = 30
                totalPag = (len(list_juegos) - 1) // linesforPages + 1
                for idx in range(totalPag):
                    os.system('cls')
                    subset_data = list_juegos[idx * linesforPages: (idx + 1) * linesforPages]
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
                print(f"No hay activos en la categoría juegos.")
                os.system('pause')
                os.system('cls')        
            os.system('pause')  
        elif op == "4": 
            menu.menuRep()    

def listActivosdaño(data:dict):
    listbreak = []
    for codigo, activo in data["activos"].items():
        if activo["estado"] == "Dado de baja por daño":
            nombre = activo["CodCampus"]
            estado = activo["Estado"]
            numero_serial = activo["NroSerial"]
            subLista = [codigo, nombre, estado, numero_serial]
            listbreak.append(subLista)
    
    if listbreak:   #if list is not empty - print unallocated assets
        linesforPages = 30
        totalPag = (len(listbreak) - 1) // linesforPages + 1
        for idx in range(totalPag):
            os.system('cls')
            subset_data = listbreak[idx * linesforPages: (idx + 1) * linesforPages]
            print(tabulate(subset_data, headers=["CODIGO", "NOMBRE", "ESTADO", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            print(f'Pagina {idx + 1} de {totalPag}')
            os.system('pause')
            op = input('Si desea volver al menú, presione 0: ')
            if op == "0":
                os.system('cls')
                menu.menuRep()

    else:
        print("No hay activos con estado 'No asignado'")
        os.system('pause')
        os.system('cls')

def listActivos_asg(data:dict):
    lista = []
    for i in data["Activos"]:
        codigo = i
        numero_serial = data["Activos"][i]["NroSerial"]
        nombre = data["Activos"][i]["CodCampus"]
        asignacion = data["Activos"][i]["Asignacion"]
        subLista = [codigo, nombre,asignacion, numero_serial]
        lista.append(subLista)
    if lista:
        linesforPages = 30
        totalPag = (len(lista) - 1) // linesforPages + 1
        for idx in range(totalPag):
            os.system('cls')
            subset_data = lista[idx * linesforPages: (idx + 1) * linesforPages]
            print(tabulate(subset_data, headers=["CODIGO", "NOMBRE",  "ASIGNADO ","NUMERO SERIAL"], tablefmt="fancy_grid"))
            print(f'Pagina {idx + 1} de {totalPag}')
            os.system('pause')
            op = input('Si desea volver al menú, presione 0: ')
            if op == "0":
                os.system('cls')  
                menu.menuRep()
    else:
            print(f"No hay existencia activos aun.")
            os.system('pause')
            os.system('cls')        

def listHist(data:dict):
    listah = []
    data = readJson("data/history.json",{})
    for codigo, activo in data:
        # Obtener el historial de movimientos del activo
        historial = activo.get("Historial", {})  # Obtener el historial de movimientos del activo
        for historial, movimiento in historial.items():
            fecha = movimiento.get("fecha")
            encargado = movimiento.get("encargado")
            tipoMov = movimiento.get("tipoMov")
            listah.append([historial, fecha, encargado, tipoMov])

    if listah:
        linesforPages = 30
        totalPag = (len(listah) - 1) // linesforPages + 1
        for idx in range(totalPag):
            os.system('cls')
            subset_data = listah[idx * linesforPages: (idx + 1) * linesforPages]
            print(tabulate(subset_data, headers=["Nro. HISTORIAL", "FECHA", "ENCARGADO", "TIPO DE MOVIMIENTO"], tablefmt="fancy_grid"))
            print(f'Pagina {idx + 1} de {totalPag}')
            os.system('pause')
            op = input('Si desea volver al menú, presione 0: ')
            if op == "0":
                os.system('cls')  
                menu.menuRep()
    else:
        print(f"No hay historial de movimientos disponibles.")
        os.system('pause')
        os.system('cls')            
        