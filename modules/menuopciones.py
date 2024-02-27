from tabulate import tabulate

titulo = """
        +**********************+
        |       OPCIONES       |
        +**********************+
        """


def menuopciones(): 
    print(titulo)
    opciones = [["1.", "ACTIVOS"], ["2.", "PERSONAL "], ["3.", "ZONAS "], ["4.", "ASIGNACION DE ACTIVOS "], ["5.", "REPORTES"], ["6.", "MOVIMIENTOS DE ACTIVOS"],["7.", "Salir"]]
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
        ("Vuelva pronto!")
    else:
      menuopciones()

menuopciones() 





