from tabulate import tabulate
import os
import modules.menus as menu
os.system('cls')
def listactivosall(data:dict):  
        listall = []
        for i in data["Activos"].items():
            codigo = i[0]
            numero_serial = data["Activos"][i[0]]["NroSerial"]
            nombre = data["Activos"][i[0]]["CodCampus"]
            subLista = [codigo, nombre, numero_serial]
            listall.append(subLista)
        if listall:
            print(tabulate(listall, headers=["Codcampus", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
            os.system('pause')
        else:
            print(f"No hay activos en la categoría ") 
        if listall:
            linesPorPage = 30
            totalPag = (len(listall) - 1) // linesPorPage + 1
            for idx in range(totalPag):
                os.system('cls')
                subset_data = listall[idx * linesPorPage: (idx + 1) * linesPorPage]
                print(tabulate(subset_data, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
                print(f'Pagina {idx + 1} de {totalPag}')
                os.system('pause')
                os.system('cls')
                op = input('Si desea volver al menú, presione 0: ')
                if op == "0":
                    os.system('cls')  
                    menu.menuRep()
        else:
                print(f"No hay activos aun.")
                os.system('pause')
                os.system('cls')

def listActivosCategoria(data:dict): 
    while True:
        os.system('cls')
        opcion=('1. EQUIPOS DE COMPUTO \n2. ELECTRODOMESTICOS \n3. JUEGOS\n4. REGRESAR A MENU REPORTES\n  ')
        print(opcion)
        #EQUIPOS DE COMPUTO
        op = input('>> ')
        if op == "1": 
            list_equipos = []
            for keys, activo in data["Activos"].items():
                if activo["Categoria"] == "Equipo de computo":
                    nombre = activo["CodCampus"]
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
                if activo["Categoria"] == "Electrodomesticos":
                    nombre = activo["CodCampus"]
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
            else:
                print(f"No hay activos en la categoría juegos.")
                os.system('pause')
                os.system('cls')        
            os.system('pause')  
        elif op == "4": 
            menu.menuRep()    

