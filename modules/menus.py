from tabulate import tabulate
import modules.add as add
import main as main 
titulo = """
        +**********************+
        |       OPCIONES       |
        +**********************+
        """
def menuprincipal(): 
    print(titulo)
    opciones = [["1.", "ACTIVOS"], ["2.", "PERSONAL "], ["3.", "ZONAS "], ["4.", "ASIGNACION DE ACTIVOS "], ["5.", "REPORTES"], ["6.", "MOVIMIENTOS DE ACTIVOS"],["7.", "SALIR"]]
    print(tabulate(opciones, tablefmt="grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
        menuactivos()
    elif opcion == "2":
        menupersonal()
    elif opcion == "3":
        menuZONAS()
    elif opcion == "4":
        menuasigactivos()
    elif opcion == "5":
        menuREPORTES()
    elif opcion == "6":
        menuMOVIMIENTOSDEACTIVOS()
    elif opcion == "7":
        ("Vuelva pronto!")
        exit()
    else:
      menuprincipal()

#OPCION 1
tituloACTIVOS = """
        +**********************+
        |       ACTIVOS        |
        +**********************+
        """
def menuactivos(): 
    print(tituloACTIVOS)
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "ASIGNACION DE ACTIVOS "], ["5.", "SALIR"]]
    print(tabulate(opciones, tablefmt="grid"))
    opcion = input("\n>> ")
    
    if opcion == "1":
       add.activosAdd(main.data)
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        input("\n>>Volver al menu principal (Presione ENTER)") 
        menuprincipal()
    else:
      menuactivos()

#OPCION2 
tituloPERSONAL = """
        +**********************+
        |       PERSONAL       |
        +**********************+
        """
def menupersonal(): 
    print(tituloPERSONAL)
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "BUSCAR "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="grid"))
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
        input("\n>>Volver al menu principal (Presione ENTER)")   
        menuprincipal()
    else:
      menupersonal()

#OPCION3
tituloZONAS = """
        +**********************+
        |       ZONAS          |
        +**********************+
        """
def menuZONAS(): 
    print(tituloZONAS)
    opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", " Buscar"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="grid"))
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
        input("\n>>Volver al menu principal (Presione ENTER)") 
        menuprincipal()
    else:
     menuZONAS()            

#OPCION4    
tituloASIGNACTIVOS = """
        +**********************************+
        |       ASIGNACION DE ACTIVOS      |
        +**********************************+ 
        """
def menuasigactivos(): 
    print(tituloASIGNACTIVOS)
    opciones = [["1.", "CREAR ASIGNACION "], ["2.", "BUSCAR ASIGNACION "], ["3.", "ELIMINAR "], ["4.", "ASIGNACION DE ACTIVOS "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="grid"))
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
        input("\n>>Volver al menu principal (Presione ENTER)") 
        menuprincipal()
    else:
      menuasigactivos()
      
#OPCION5 
tituloREPORTES = """
        +**********************+
        |       REPORTES       |
        +**********************+
        """
def menuREPORTES(): 
    print(tituloREPORTES)
    opciones = [["1.", "LISTAR TODOS LOS ACTIVOS"], ["2.", "LISTAR ACTIVOS POR CATEGORIA"], ["3.", "LISTAR ACTIVOS DADOS DE BAJA POR DAÑOS "], ["4.", "LISTAR ACTIVOS Y ASIGNACION "], ["5.", "LISTAR HISTORIAL DE MOV. DE ACTIVO"], ["6.",  "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="grid"))
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
        pass
    elif opcion == "7":
     input("\n>>Volver al menu principal (Presione ENTER)") 
     menuprincipal()
    else:
      menuREPORTES()


#OPCION5 
tituloMOVIMIENTOSDEACTIVOS = """
        +******************************+
        |    MOVIMIENTOS DE ACTIVOS    |
        +******************************+
        """
def menuMOVIMIENTOSDEACTIVOS(): 
    print(tituloMOVIMIENTOSDEACTIVOS)
    opciones = [["1.", "LISTAR TODOS LOS ACTIVOS"], ["2.", "LISTAR ACTIVOS POR CATEGORIA"], ["3.", "LISTAR ACTIVOS DADOS DE BAJA POR DAÑOS "], ["4.", "LISTAR ACTIVOS Y ASIGNACION "], ["5.",  "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(opciones, tablefmt="grid"))
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
        pass
    elif opcion == "7":
        input("\n>>Volver al menu principal (Presione ENTER)")   
        menuprincipal()
    else:
     menuMOVIMIENTOSDEACTIVOS()

menuprincipal()



















































































































