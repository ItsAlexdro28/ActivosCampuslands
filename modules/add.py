def activosAdd(data:dict):
    try:
        new = {}
        hold = {}
        keys = ['CodTransaccion','NroFormulario','CodCampus','Marca','Categoria','Tipo','ValUnid','Proveedor','NroSerial','EmpresaResponsable','Estado']
        keysRead = ['Codigo de Transaccion','Numero de Formulario','Codigo Campus','Marca','Categoria','Tipo','ValUnid','Proveedor','Numero Serial','la Empresa Responsable','Estado']
        print('Añadir un nuevo activo')
        for i in range(len(keys)):
            if keys[i] == 'Marca':
                print('valores sugeridos: LG, COMPUMAX, LOGITECH, BENQ, ASUS, LENOVO, HP')
            elif keys[i] == 'Categoria':
                print('valores sugeridos: Equipo de computo, Electrodomestico, Juego')
            elif keys[i] == 'Tipo':
                print('valores sugeridos: Monitor, CPU, Teclado, Mouse, Aire Acondicionado, Portatil, Impresora')
            value = input(f'Valor para {keysRead[i]}')
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

    