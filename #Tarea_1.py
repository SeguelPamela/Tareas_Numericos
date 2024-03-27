import numpy as np
import math 
import matplotlib as mp
import matplotlib.pyplot as plt 

#P1)
#Valores de h y x
x = np.linspace((1-0.5610), (1+0.5610), 100).reshape((100,1))
h = np.logspace((10^-8), (10^-1), 18, base=10).reshape((1,18))
#Valores de la derivada de las funciones dadas
sen_x = (-np.sin(x+2*h)+ 8*np.sin(x+h)-8*np.sin(x-h)+np.sin(x-2*h))/(12*h)
log_x = (-np.log(x+2*h)+8*np.log(x+h)-8*np.log(x-h)+np.log(x-2*h))/(12*h)

#P2)
#Para ambas funciones clacule la diferencia entre los valores
#de la derivada estimados en la parte anterior con el valor real de la derivada
#CUANDO HABLA DE LA DERIVADA REAL SE REFIERE A LA DERIVADA Q VIMOS EN CLASES O A LA DERIVADA OFICIAL ONDA NP.DERIVADA O ALGO ASI???
#No hay q usar otra formulita
#Para la del seno es coseno
#Para la del log es 1/(xln(10))
