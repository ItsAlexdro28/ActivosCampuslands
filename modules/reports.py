from tabulate import tabulate
import os
os.system('cls')
def listactivoscate1(data:dict):  
        listMonitor = []
        for keys, activo in data["Activos"].items():
            if activo["Tipo"] == "Monitor":
                nombre = activo["Tipo"]
                numero_serial = activo["NroSerial"]
                subLista = [keys, nombre, numero_serial]
                listMonitor.append(subLista)
        if listMonitor:
            print(tabulate(listMonitor, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
        else:
            print(f"No hay activos en la categoría ")

def listactivoscate2(data:dict):  
        listCpu = []
        for keys, activo in data["Activos"].items():
            if activo["Tipo"] == "Cpu":
                nombre = activo["Tipo"]
                numero_serial = activo["NroSerial"]
                subLista = [keys, nombre, numero_serial]
                listCpu.append(subLista)
        if listCpu:
            print(tabulate(listCpu, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
        else:
            print(f"No hay activos en la categoría ")            

def listactivoscate3(data:dict):  
        listTeclado = []
        for keys, activo in data["Activos"].items():
            if activo["Tipo"] == "Teclado":
                nombre = activo["Tipo"]
                numero_serial = activo["NroSerial"]
                subLista = [keys, nombre, numero_serial]
                listTeclado.append(subLista)
        if listTeclado:
            print(tabulate(listTeclado, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
        else:
            print(f"No hay activos en la categoría ")  

def listactivoscate4(data:dict):  
        listMouse = []
        for keys, activo in data["Activos"].items():
            if activo["Tipo"] == "Mouse":
                nombre = activo["Tipo"]
                numero_serial = activo["NroSerial"]
                subLista = [keys, nombre, numero_serial]
                listMouse.append(subLista)
        if listMouse:
            print(tabulate(listMouse, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
        else:
            print(f"No hay activos en la categoría ")      

# def                            
#     elif op == "2":
#         listaCPU = []
#         for codigo, activo in data_inventario["activos"].items():
#             if activo["tipo"] == "CPU":
#                 nombre = activo["nombre"]
#                 numero_serial = activo["numero_serial"]
#                 subLista = [codigo, nombre, numero_serial]
#                 listaCPU.append(subLista)
#         if listaCPU:
#             print(tabulate(listaCPU, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
#         else:
#             print(f"No hay activos en la categoría '{tipo}'.")
# listar activos o sea todos
# def listarActivos(data_inventario):

#     lista = []
#     for i in data_inventario["activos"]:
#         codigo = i
#         numero_serial = data_inventario["activos"][i]["numero_serial"]
#         nombre = data_inventario["activos"][i]["nombre"]
#         subLista = [codigo, nombre, numero_serial]
#         lista.append(subLista)
#     linesPorPage = 30
#     totalPag = (len(lista) - 1) // linesPorPage + 1
#     for idx in range(totalPag):
#         clear_screen()
#         subset_data = lista[idx * linesPorPage: (idx + 1) * linesPorPage]
#         print(tabulate(subset_data, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
#         print(f'Pagina {idx + 1} de {totalPag}')
#         pause_screen()
#         op = input('Si desea volver al menú, presione 0: ')
#         if op == "0":
#             clear_screen()
             