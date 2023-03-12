continuar=True
while continuar==True:
    print "\nsolo integrales de la forma:"
    print "\nI( x^n  sen(ax) dx ) o I( x^n cos(ax) dx )"
    n=input("\nn:")
    print "\nseno o coseno?"
    print "\n1)seno\n2)coseno"
    funcionT=input("\n:")
    if funcionT==1:
        print "\nI ( x^",n," sen(ax) dx )="
    else:
        print "\nI ( x^",n," cos(ax) dx )="

    def fact(num):
        if num>1:
            resultado = num*fact(num-1)
        else:
            resultado = 1
        return resultado
    
    if funcionT==1:
        numerador=""
        cont=n
        cambio=1
        signo=0
        fx=2
        while cont >=0:
            if cambio == 1:
                if signo == 0:
                    numerador=numerador+"-"
                    signo = 1
                    cambio = 0
                else:
                    numerador=numerador+"+"
                    signo = 0
                    cambio = 0
            else:
                if signo == 0:
                    numerador=numerador+"-"
                    cambio = cambio + 1
                else:
                    numerador=numerador+"+"
                    cambio = cambio + 1

            termino = str(fact(n)/fact(cont))+" a^"+str(cont)+" x^"+str(cont)
            numerador=numerador+termino

            if fx == 2:
                numerador=numerador+" cos(ax)"
                fx=1
            else:
                numerador=numerador+" sen(ax)"
                fx=2

            cont = cont - 1
        resultado = "( "+ numerador + " )" + "/ a^"+str(n+1)

    if funcionT==2:
        numerador=""
        cont=n
        cambio=0
        signo=1
        fx=1
        while cont >=0:
            if cambio == 1:
                if signo == 0:
                    numerador=numerador+"-"
                    signo = 1
                    cambio = 0
                else:
                    numerador=numerador+"+"
                    signo = 0
                    cambio = 0
            else:
                if signo == 0:
                    numerador=numerador+"-"
                    cambio = cambio + 1
                else:
                    numerador=numerador+"+"
                    cambio = cambio + 1

            termino = str(fact(n)/fact(cont))+" a^"+str(cont)+" x^"+str(cont)
            numerador=numerador+termino

            if fx == 2:
                numerador=numerador+" cos(ax)"
                fx=1
            else:
                numerador=numerador+" sen(ax)"
                fx=2

            cont = cont - 1
        resultado = "( "+ numerador + " )" + "/ a^"+str(n+1)

    print "\n"+resultado
            
    c=raw_input("\ncontinuar? (S/N) :")
    if c == "S" or c == "s":
        continuar=True
    else:
        continuar=False

