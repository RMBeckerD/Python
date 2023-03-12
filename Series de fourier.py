# -*- coding: cp1252 -*-
#BLOQUE DE DEFINICIONES

#IMPORTACION DE MODULOS

#Libreria math que utilizaremos para representar graficamente la señal analoga mediante funciones trigonometricas
import math
#La libreria matplotlib la usaremos para graficar la funcion de la señal en la salida del programa.
import matplotlib.pyplot as funcionGrafica

#DEF CONSTANTES
#se define la constante pi para poder ser usada mas adelante en las funciones trigonometricas
PI=math.pi

#DEF FUNCIONES



#BLOQUE PRINCIPAL
#ENTRADA
L=input("Ingrese el limite de la serie(restriccion de dominio):")
n=input("Ingrese la cantidad de terminos para aproximar la funcion:")
#Indicar constantes de la serie
a0=1
an=1
bn=1
#PROCESAMIENTO
funcionGrafica.plot(1,1)


#SALIDA
#llama a la función para crear el archivo de texto
funcionGrafica.show()

