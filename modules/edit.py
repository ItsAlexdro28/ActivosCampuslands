def activosEdit(data:dict):
    codCampus = input("Ingresa el valor del Codigo de campus para editar")
    keysRead = ['Codigo de Transaccion','Numero de Formulario','Codigo Campus','Marca','Categoria','Tipo','ValUnid','Proveedor','Numero Serial','la Empresa Responsable','Estado']
    if codCampus in data['Activos']:
        activeToEdit = data['Activos'][codCampus]
        print("Detalles de Activo:")
        for i, (key, value) in enumerate(activeToEdit.items()):
            if key != 'Historial':  # Saltar el historial
                print(f"{i+1}. {keysRead[i]}: {value}")
        try:
            indexToEdit = int(input("Ingrese el numero de identificacion del valor que desea editar (-1 para cancelar o 0 para editarlos todos): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return
        if indexToEdit == 0:
                # Edit todos los valores
                for key, value in activeToEdit.items():
                    x = 0
                    if key != 'Historial':  # Saltar el historial
                        newValue = input(f"Ingresa el nuevo valor para '{keysRead[x]}': ")
                        activeToEdit[key] = newValue
                    x += 1
                print(f"Activo '{codCampus}' Editado satisfactoriamente.")
                return
        if indexToEdit == -1:
            print("Cancelado")
            return

        if 0 < indexToEdit < len(list(activeToEdit.items())):
            keyToEdit, _ = list(activeToEdit.items())[indexToEdit-1]  # Extraer llave
            keyToPrint, _ = list(keysRead[indexToEdit-1])
            newValue = input(f"Ingresa el nuevo valor para '{keyToPrint}': ")
            activeToEdit[keyToEdit] = newValue
            print(f"Activo '{activeToEdit}' Actualizado.")
            return
        else:
            print(f"Index invalido: {indexToEdit}. Ingresa un valor valido entre -1 y {len(indexToEdit) - 1}.")
            activosEdit(data)
    else:
        print(f"Activo con Codigo de campus '{indexToEdit}' no ha sido encontrado.")
        activosEdit(data)

# Esta función permite a los usuarios editar los detalles de un activo existente en función de su clave 'CodCampus'.
# Solicita al usuario que ingrese la clave 'CodCampus' del activo que desea editar.
# Si se encuentra el activo, muestra todos sus detalles con números de índice que comienzan desde 1.
# Luego, el usuario puede elegir el índice del valor que desea editar o ingresar 0 para editar todos los valores.
# Para cada valor que se va a editar, se le solicita al usuario que ingrese el nuevo valor.
# Luego, la función actualiza los detalles del activo en el diccionario de datos.
# Finalmente muestra un mensaje indicando si el activo se actualizó exitosamente o no.

