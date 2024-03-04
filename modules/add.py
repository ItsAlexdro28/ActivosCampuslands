from tabulate import tabulate
import modules.search as search
import os

def addactivos(data:dict):
    os.system('cls')
    try:
        new = {}
        hold = {}
        keys = ['CodTransaccion','NroFormulario','CodCampus','Marca','Categoria','Tipo','ValUnid','Proveedor','NroSerial','EmpresaResponsable']
        keysRead = ['Codigo de Transaccion','Numero de Formulario','Codigo Campus','Marca','Categoria','Tipo','Valor Unidad','Nombre del Proveedor','Numero Serial','la Empresa Responsable']
        titulo=[["AÑADIR ACTIVOS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        for i in range(len(keys)):
            if keys[i] == 'Marca':
                print('valores sugeridos: LG, COMPUMAX, LOGITECH, BENQ, ASUS, LENOVO, HP')
            elif keys[i] == 'Categoria':
                print('Elija la categoria de su activo: Equipo de computo, Electrodomestico, Juego')
            elif keys[i] == 'Tipo':
                print('Elija el tipo de activo: Monitor, CPU, Teclado, Mouse, Aire Acondicionado, Portatil, Impresora')
            value = input(f'Valor para {keysRead[i]}\n>>').upper()
            hold[keys[i]] = value
        hold['Estado'] = '0'
        hold['Historial'] = []
        new[hold['CodCampus']] = hold
        data['Activos'].update(new)
        os.system('pause') 
        return
    except ValueError as e:
        print(f"Error: El valor de la llave '{e}' no es valido.")
        os.system('pause')
        return

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
        os.system('pause')
        return
    except ValueError as e:
        print(f"Error: El valor de la llave '{e}' no es valido.")
        os.system('pause')
        return

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
        os.system('pause')
        return
    except ValueError as e:
        print(f"Error: El valor de la llave '{e}' no es valido.")
        os.system('pause')
        return

def addHistoryAssing(data:dict, history:dict):
    last = list(data['Asignacion'].keys())[-1]
    Responsable = input('Id de quien efectuo el movimiento? ')
    nroid = historyIndex(history, last['FechaAsignacion'], 1, Responsable, last)
    for i in range(len(data['Asignacion'][str(last)]['Activos'])):
        data['Activos'][str(i)]['Historial'].append(nroid)
        data['Activos'][str(i)]['Estado'] = '1'
    data['Asignacion'][str(last)]['HistorialId'] = nroid
    os.system('pause')
    return

def addHistoryState(data:dict, history:dict, activo:dict):
    Responsable = input('Id de quien efectuo el movimiento? ')
    fecha = input('Fecha del movimiento: ').upper()
    # 2 dado de baja / 3 garantia
    if activo['Estado'] == '2':
        nroid = nroid = historyIndex(history, fecha, 2, Responsable, 'NA')
    elif activo['Estado'] == '3':
        nroid = nroid = historyIndex(history, fecha, 3, Responsable, 'NA')     
    data['Activos'][activo['CodCampus']]['Historial'].append(nroid)
    os.system('pause')
    return

def historyIndex(history:dict, fecha, tipo, Responsable, id):
    addHistory = {}
    try:
         #sumar el ultimo id y hacer dict de historial
         history = list(history.keys())[-1]
         nroid = history+1
         newHistory = {
             'NroId':nroid,
             'Fecha':fecha,
             'TipoMov':tipo,
             'IdRespMov':Responsable,
             'IdAssing':id 
         }
         addHistory[nroid] = newHistory
         history.update(addHistory)
    except IndexError as i:
        #crear el id 0001
        x = 0
        nroid = x.zfill(3)
        newHistory = {
            'NroId':nroid,
            'Fecha':fecha,
            'TipoMov':tipo,
            'IdRespMov':Responsable,
            'IdAssing':id  
        }
        addHistory[nroid] = newHistory
        history.update(addHistory)
    return nroid