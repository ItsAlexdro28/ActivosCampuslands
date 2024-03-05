def validacionInt():
    try:
        x=int(input('>>'))
        if x<0:
            print('Solo positivos')
            return validacionInt()
        else:
            return x
    except ValueError:
        print('Solo numeros, ingrese nuevamente')
        return validacionInt()

def validacionKeyNew(data:dict,tipo):
    try:
        x=input('>>').upper()
        data[tipo][x]
        print('LLave ya existente')
        return validacionKeyNew(data,tipo)
    except KeyError:
        return x
    
def validacionInt2():
    try:
        x=int(input('>>'))
        if x<0:
            print('Solo positivos')
            return validacionInt()
        else:
            return str(x)
    except ValueError:
        print('Solo numeros, ingrese nuevamente')
        return validacionInt2()
    
def validacionKeyNew2(data:dict,tipo):
    try:
        x=int(input('>>'))
        data[tipo][x]
        print('LLave ya existente')
        return validacionKeyNew2(data,tipo)
    except ValueError:
        print('Solo numeros')
        return validacionKeyNew2(data,tipo)
    except KeyError:
        return x
    