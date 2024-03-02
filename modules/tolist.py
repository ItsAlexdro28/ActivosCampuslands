from tabulate import tabulate
import os
# os.system('cls')


# def listActivosCategoria(data_inventario, tipo):
#     op = input('Si desea volver al menú, presione 0: ')
#     if op == "1":
#         listaMonitor = []
#         for codigo, activo in data_inventario["activos"].items():
#             if activo["tipo"] == "Monitor":
#                 nombre = activo["nombre"]
#                 numero_serial = activo["numero_serial"]
#                 subLista = [codigo, nombre, numero_serial]
#                 listaMonitor.append(subLista)
#         if listaMonitor:
#             print(tabulate(listaMonitor, headers=["CODIGO", "NOMBRE", "NUMERO SERIAL"], tablefmt="fancy_grid"))
#         else:
#             print(f"No hay activos en la categoría '{tipo}'.")
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
#             reports_menu()