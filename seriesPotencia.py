cont=1
while cont == 1:
    i=0
    n=input("ingrese limite sumatoria:")
    x=input("ingrese valor de x:")
    
    def fact(a):
        if a>1:
            resultado = a*fact(a-1)
        else:
            resultado = 1
        return resultado
    sumatoria=0
    while i<=n:
        sumatoria = sumatoria + ((x**i/(fact(i)*1.0)))
        i=i+1
    print "e^",x,"=",sumatoria
    cont=input("desea continuar? (1=si ; 0=no):")
