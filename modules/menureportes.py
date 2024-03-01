from tabulate import tabulate
import modules.menus as m

op="0"
def menuRep():
    # os.system('cls')
    titulo=[["MENU REPORTES"]]
    bandera= True
    global op 
    while op!="6":
        # os.system('cls')
        print(tabulate(titulo,tablefmt="double_grid"))
        opciones = [["1.","LISTAR TODOS LOS ACTIVOS: \n>>"],["2.","LISTAR ACTIVOS POR CATEGORIA: \n>> "],["3.","LISTAR ACTIVOS DADOS DE BAJA POR DAÑO: \n>>"],
                    ["4.","LISTAR ACTIVOS Y ASIGNACION:\n>>"],["5.","LISTAR HISTORIAL DE MOV. DE ACTIVO: \n>>"],["6.","REGRESAR AL MENU PRINCIPAL: \n>>"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        op=input()
        op=op.upper()
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
            m.menuPRINCIPAL()
        else:
            menuRep()
            print('Valor no encontrado\n')
        bandera=bool(input('Desea revisar otro reporte? enter(no) X(si)\n'))
   
      