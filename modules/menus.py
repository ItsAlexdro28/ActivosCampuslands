from tabulate import tabulate
import modules.add as add
import modules.edit as edit
import modules.delete as delete
import main as main 
import modules.importJson as imp
data = imp.readJson('data')

def menuPRINCIPAL(): 
<<<<<<< HEAD
    titulo=[["SISTEMA G&C DE INVENTARIO CAMPUSLANDS"]]
<<<<<<< HEAD
    print(tabulate(titulo,tablefmt="double_grid"))
=======
    print(tabulate(titulo,tablefmt="heavy grid"))
    print(titulo)
=======
    titulo=[["SISTEMA G&C DE INVENTARIO CAMPUSLANDS\n"]]
    print(tabulate(titulo,tablefmt="double_grid"))
>>>>>>> 3277f09be570148639293b467c42ca39d5e92a08
>>>>>>> refs/remotes/origin/main
    opciones = [["1.", "ACTIVOS"], ["2.", "PERSONAL "], ["3.", "ZONAS "], ["4.", "ASIGNACION DE ACTIVOS "], ["5.", "REPORTES"], ["6.", "MOVIMIENTOS DE ACTIVOS"],["7.", "SALIR"]]
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
        menuREPORTES()
    elif opcion == "6":
        menuMOVIMIENTOSDEACTIVOS()
    elif opcion == "7":
        ("Vuelva pronto!")
        exit()
    else:
      menuPRINCIPAL()

#OPCION 1
def menuACTIVOS(): 
    titulo=[["MENU ACTIVOS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "BUSCAR "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        add.activosAdd(data)
        imp.writeJson(data, 'data')
    elif opcion == "2":
        edit.activosEdit(data)
        imp.writeJson(data, 'data')
    elif opcion == "3":
        delete.activosDelete(data)
        imp.writeJson(data, 'data')
    elif opcion == "4":
        pass
    elif opcion == "5": 
        menuPRINCIPAL()
    else:
      menuACTIVOS()

#OPCION2 
def menuPERSONAL(): 
    titulo=[["MENU PERSONAL"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "BUSCAR "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        pass 
    elif opcion == "2":
        pass
    elif opcion == "3":
        delete.peopleDelete(data)
        imp.writeJson(data, 'data')
    elif opcion == "4":
        pass
    elif opcion == "5":   
        menuPRINCIPAL()
    else:
      menuPERSONAL()

#OPCION3
def menuZONAS(): 
    titulo=[["MENU ZONAS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", " Buscar"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
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
     menuZONAS()            

#OPCION4    
def menuASIGACTIVOS(): 
    titulo=[["ASIGNACION DE ACTIVOS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "CREAR ASIGNACION "], ["2.", "BUSCAR ASIGNACION "],["3.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="fancy_grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        pass 
    elif opcion == "2":
        pass
    elif opcion == "3":
        menuPRINCIPAL()
    else:
      menuASIGACTIVOS()
      
#OPCION5 
def menuREPORTES(): 
    titulo=[["REPORTES"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "LISTAR TODOS LOS ACTIVOS"], ["2.", "LISTAR ACTIVOS POR CATEGORIA"], ["3.", "LISTAR ACTIVOS DADOS DE BAJA POR DAÑOS "], ["4.", "LISTAR ACTIVOS Y ASIGNACION "], ["5.", "LISTAR HISTORIAL DE MOV. DE ACTIVO"], ["6.",  "REGRESAR AL MENU PRINCIPAL"]]
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
        pass
    elif opcion == "6":
        menuPRINCIPAL()
    else:
      menuREPORTES()

#OPCION5 
def menuMOVIMIENTOSDEACTIVOS(): 
    titulo=[["MOVIMIENTOS DE ACTIVOS"]]
    print(tabulate(titulo,tablefmt="double_grid"))
    opciones = [["1.", "RETORNO DE ACTIVO"], ["2.", "DAR DE BAJA ACTIVO"], ["3.", "CAMBIAR ASIGNACION DE ACTIVO"], ["4.", "ENVIAR A GARANTIA ACTIVO"], ["5.",  "REGRESAR AL MENU PRINCIPAL"]]
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





















































































































