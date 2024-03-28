import numpy as np
import math 
import matplotlib as mp
import matplotlib.pyplot as plt 

#P1)
#Valores de h y x
x = np.linspace((1-0.5610), (1+0.5610), 100).reshape((1,100))
h = np.logspace((10^-8), (10^-1), 18, base=10).reshape((18,1))

#Valores de la derivada según el enunciado de las funciones dadas
der_sen_x = (-np.sin(x+2*h)+ 8*np.sin(x+h)-8*np.sin(x-h)+np.sin(x-2*h))/(12*h)
der_log_x = (-np.log(x+2*h)+8*np.log(x+h)-8*np.log(x-h)+np.log(x-2*h))/(12*h)

#P2)
#Primero se calcula el valor de la derivada real
der_sen_real = (np.sin(x+h) - np.sin(x-h))/(2*h)
der_log_real = (np.log(x+h) - np.log(x-h))/(2*h)
#Luego se calcula la diferencia entre estos valores
dif_sen = der_sen_x - der_sen_real
dif_log = der_log_x - der_log_real

#P3)
#Se grafican las curvas de las diferencias calculadas en la parte 2
#graficamos para la diferencia de las derivadas del seno
#MODIFICAR LOS GRÁFICOS
plt.plot(np.fabs(dif_sen))
plt.xscale('log')
#graficamos para la diferencia de las derivadas del log
plt.plot(np.fabs(dif_log))
plt.xscale('log')


#P4)
#Generamos la curva promedio para cada gráfico

#Primero la del Seno
A = np.fabs(dif_sen.mean(1))
plt.plot(A, linewidth = 10)

#Luego la del Coseno
B = np.fabs(dif_log.mean(1))
plt.plot(B, linewidth = 10)

#P5) REPETIR EL GRAFICO CON NUMEROS DEL TIPO NP.FLOAT32