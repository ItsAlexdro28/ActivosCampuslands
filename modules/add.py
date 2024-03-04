from tabulate import tabulate
import modules.search as search
import os

def addactivos(data:dict):
    os.system('cls')
    try:
        new = {}
        hold = {}
        keys = ['CodTransaccion','NroFormulario','CodCampus','Marca','Categoria','Tipo','ValUnid','Proveedor','NroSerial','EmpresaResponsable','Estado']
        keysRead = ['Codigo de Transaccion','Numero de Formulario','Codigo Campus','Marca','Categoria','Tipo','ValUnid','Proveedor','Numero Serial','la Empresa Responsable','Estado']
        titulo=[["AÑADIR ACTIVOS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        for i in range(len(keys)):
            if keys[i] == 'Marca':
                print('valores sugeridos: LG, COMPUMAX, LOGITECH, BENQ, ASUS, LENOVO, HP')
            elif keys[i] == 'Categoria':
                print('Elija la categoria de su activo: Equipo de computo, Electrodomestico, Juego')
            elif keys[i] == 'Tipo':
                print('Elija el tipo de activo: Monitor, CPU, Teclado, Mouse, Aire Acondicionado, Portatil, Impresora')
            value = input(f'Valor para {keysRead[i]}\n>>')
            hold[keys[i]] = value
        hold['Historial'] = []
        new[hold['CodCampus']] = hold
        data['Activos'].update(new) 
    except ValueError as e:
        print(f"Error: El valor de la llave '{e}' no es valido.")

# la funcion tiene dos diccionarios, uno para poner todos los datos ingresados por el usuario y otro para poder añadirlo a la base de datos
# la funcion "for" itera por todos los valores de 'keys' siendo los nombres de las llaves para asignar en el diccionarios
# por cada llave se asignara el valor que ingrese el usuario al diccionario 'hold'
# cuando termine el "for" se agregaran los datos a el diccionario 'new' con la llave del codigo campus para identificarlo
# cuando pregunte por 'marca, categoria y tipo' imprimira valores sugeridos segun los requerimientos del cliente
# el historial no se pregunta porque no hay record del activo hasta ahora, y se añade la lista donde luego estaran las identificaciones de activo
def addpeople(data:dict):
    try:
        os.system('cls')
        hold2={}
        titulo=[["AÑADIR PERSONAS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        id=input('Ingrese id:\n>>').upper()
        nombre=input('Ingrese un nombre:\n>>').upper()
        email=input('Ingrese un email:\n>>').upper()
        telefono=input('Ingrese un telfono:\n>>').upper()
        celular=input('Ingrese un celular:\n>>').upper()
        people={
            "Nombre":nombre,
            "Id":id,
            "Email":email,
            "Telefono":telefono,
            "Celular":celular
        }
        hold2[people[id]]=people
        data['Personal'].update(hold2)
    except ValueError as e:
        print(f"Error: El valor de la llave '{e}' no es valido.")

def addzone(data:dict):
    try:
        os.system('cls')
        hold3={}
        titulo=[["AÑADIR ZONAS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        nrozona=input('Ingrese el nro zona:\n>>').upper()
        nombrezona=input('Ingrese el nombre de la zona:\n>>').upper()
        totalcapacidad=input('Ingrese la capacidad de la zona:\n>>').upper()
        zon={
            "NroZona":nrozona,
            "NombreZona":nombrezona,
            "totalCapacidad":totalcapacidad
        }
        hold3[zon[nombrezona]]=zon
        data['Zonas'].update(hold3)
    except ValueError as e:
        print(f"Error: El valor de la llave '{e}' no es valido.")

def addHistoryAssing(data:dict, history:dict):
     last = list(data['Asignacion'].keys())[-1]
     Responsable = input('Id de quien efectuo el movimiento? ')
     addHistory = {}
     try:
         #sumar el ultimo id y hacer dict de historial
         history = list(history.keys())[-1]
         nroid = history+1
         fecha = last['FechaAsignacion']
         newHistory = {
             'NroId':nroid,
             'Fecha':fecha,
             'TipoMov':1,
             'IdRespMov':Responsable 
         }
         addHistory[nroid] = newHistory
         history.update(addHistory)
     except IndexError as i:
         #crear el id 0001
         x = 0
         nroid = x.zfill(3)
         fecha = last['FechaAsignacion']
         newHistory = {
             'NroId':nroid,
             'Fecha':fecha,
             'TipoMov':1,
             'IdRespMov':Responsable 
         }
         addHistory[nroid] = newHistory
         history.update(addHistory)
     for i in range(len(data['Asignacion'][last]['Activos'])):
         data['Activos'][i]['Historial'].append(nroid)

        


    

    