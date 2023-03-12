#DEF FUNCIONES
#Funcion que invierte el rut
def invertirRut(rut):
    #ENTRADA:rut
    rutInvertido=""
    for digito in rut:
        rutInvertido=digito+rutInvertido
    #SALIDA:rutInvertido
    return rutInvertido

def obtenerDigito(rutInvertido):
    suma=0
    serie=2
    for numero in rutInvertido:
        suma=suma+int(numero)*serie
        if serie==7: serie=1
        serie+=1
    resto=suma%11
    resultado=11-resto
    if resultado==11:
        resultado=0
    elif resultado==10:
        resultado="k"
    else:
        resultado=resultado
    return resultado
    
#BLOQUE PRINCIPAL
#ENTRADA
rut=raw_input("Ingrese su rut de la forma 12345678-9:\n")
#PROCESAMIENTO
rutSinDigito=rut[:-2]
digito=rut[-1]
while not rutSinDigito.isdigit() or not digito.isdigit() and digito!="k" or rut[-2] != "-":
    rut=raw_input("Ingrese su rut de la forma 12345678-9:\n")
    rutSinDigito=rut[:-2]
    digito=rut[-1]
rutInvertido=invertirRut(rutSinDigito)
digitoObtenido=obtenerDigito(rutInvertido)
#SALIDA
if str(digito)==str(digitoObtenido):
    print "El rut",rut,"es valido"
else:
    print "El rut",rut,"es invalido"
a=input("...")
