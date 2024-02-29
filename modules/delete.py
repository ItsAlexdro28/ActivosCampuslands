def activosDelete(data:dict):
    codCampus = input("Ingresa el valor del Codigo de campus para eliminar")
    if codCampus in data["Activos"]:
        activeToDelete = data["Activos"][codCampus]
        print("Detalles de Activo: ")
        for key, value in activeToDelete.items():
            print(f"{key}: {value}")
        confirmation = input("Estas seguro de eliminar este activo (s/N)? ")
        if confirmation.lower() == "s":
            del data["Activos"][codCampus]
            print(f"Activo '{codCampus}' Eliminado satisfactoriamente")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Activo con Codigo de campus '{codCampus}' no ha sido encontrado")
