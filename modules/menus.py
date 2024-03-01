from tabulate import tabulate
import os
import modules.add as add
import modules.edit as edit
import modules.delete as delete
import modules.search as search
import modules.assingnations as assg
import main as main 
import modules.importJson as imp
data = imp.readJson('data')
history = imp.readJson('history')

def menuPRINCIPAL():
    os.system('cls')
    titulo=[["SISTEMA G&C DE INVENTARIO CAMPUSLANDS"]]
    print(tabulate(titulo,tablefmt="heavy grid"))
    opciones = [["1.", "ACTIVOS"], ["2.", "PERSONAL "], ["3.", "ZONAS "], ["4.", "ASIGNACION DE ACTIVOS "],
                 ["5.", "REPORTES"], ["6.", "MOVIMIENTOS DE ACTIVOS"],["7.", "SALIR"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        menuACTIVOS()
    elif opcion == "2":
        menuPERSONAL()
    elif opcion == "3":
        menuZONAS()
    elif opcion == "4":
       menuASIGACTIVOS()
    elif opcion == "5":
        menuRep()
    elif opcion == "6":
        menuMOVIMIENTOSDEACTIVOS()
    elif opcion == "7":
        ("Vuelva pronto!")
        exit()
    else:
      menuPRINCIPAL()

#OPCION 1
def menuACTIVOS(): 
    os.system('cls')
    titulo=[["MENU ACTIVOS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "BUSCAR "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        add.addactivos(data)
        imp.writeJson(data, 'data')
    elif opcion == "2":
        edit.activosEdit(data)
        imp.writeJson(data, 'data')
    elif opcion == "3":
        delete.activosDelete(data)
        imp.writeJson(data, 'data')
    elif opcion == "4":
        search.activosSearch(data)
        imp.writeJson(data, 'data')
    elif opcion == "5": 
        menuPRINCIPAL()
    else:
      menuACTIVOS()

#OPCION2 
def menuPERSONAL(): 
    os.system('cls')
    titulo=[["MENU PERSONAL"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "BUSCAR "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        add.addpeople(data)
        imp.writeJson(data, 'data') 
    elif opcion == "2":
        edit.peopleEdit()
    elif opcion == "3":
        delete.peopleDelete(data)
        imp.writeJson(data, 'data')
    elif opcion == "4":
        search.personaSearch(data)
        imp.writeJson(data, 'data')
    elif opcion == "5":   
        menuPRINCIPAL()
    else:
      menuPERSONAL()

#OPCION3
def menuZONAS(): 
    os.system('cls')
    titulo=[["MENU ZONAS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", " Buscar"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        add.addzone(data)
        imp.writeJson(data, 'data') 
    elif opcion == "2":
        edit.zonaEdit(data)
        imp.writeJson(data, 'data')
    elif opcion == "3":
        delete.zonDelete(data)
        imp.writeJson(data, 'data')
    elif opcion == "4":
        search.zonaSearch(data)
        imp.writeJson(data, 'data')
    elif opcion == "5":
        menuPRINCIPAL()
    else:
     menuZONAS()            

#OPCION4    
def menuASIGACTIVOS(): 
    os.system('cls')
    titulo=[["ASIGNACION DE ACTIVOS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "CREAR ASIGNACION "], ["2.", "BUSCAR ASIGNACION "],["3.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        assg.newAssing(data)
        imp.writeJson(data, 'data')
    elif opcion == "2":
        search.asigSearch(data)
        imp.writeJson(data, 'data')
    elif opcion == "3":
        menuPRINCIPAL()
    else:
      menuASIGACTIVOS()
      
#OPCION5
def menuRep():
    os.system('cls')
    titulo=[["MENU REPORTES"]]
    bandera= True
    global op 
    while op!="6":
        os.system('cls')
        print(tabulate(titulo,tablefmt="double_grid"))
        opciones = [["1.","LISTAR TODOS LOS ACTIVOS: \n>>"],["2.","LISTAR ACTIVOS POR CATEGORIA: \n>> "],["3.","LISTAR ACTIVOS DADOS DE BAJA POR DAÑO: \n>>"],
                    ["4.","LISTAR ACTIVOS Y ASIGNACION:\n>>"],["5.","LISTAR HISTORIAL DE MOV. DE ACTIVO: \n>>"],["6.","REGRESAR AL MENU PRINCIPAL: \n>>"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        op=input("\n>> ")
        if op == "1":
            pass
        elif op == "2":
            pass      
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "5":
            pass
        elif op =="6":
            menuPRINCIPAL()
        else:
            menuRep()
            print('Valor no encontrado\n')
        bandera=bool(input('Desea revisar otro reporte? enter(no) X(si)\n'))
   

#OPCION5 
def menuMOVIMIENTOSDEACTIVOS(): 
    os.system('cls')
    titulo=[["MOVIMIENTOS DE ACTIVOS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "RETORNO DE ACTIVO"], ["2.", "DAR DE BAJA ACTIVO"], ["3.", "CAMBIAR ASIGNACION DE ACTIVO"],
                 ["4.", "ENVIAR A GARANTIA ACTIVO"], ["5.",  "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        menuPRINCIPAL()
    else:
     menuMOVIMIENTOSDEACTIVOS()





















































































































