import numpy as np
import math 
import matplotlib as mp
import matplotlib.pyplot as plt 

x = np.linspace((1-0.5610), (1+0.5610), 100).reshape((100,1))
h = np.logspace((10^-8), (10^-1), 18, base=10).reshape((1,18))
#Esta es la derivación que se nos presenta para disminuir el error
#Para seno
sen_x = (-np.sin(x+2*h)+ 8*np.sin(x+h)-8*np.sin(x-h)+np.sin(x-2*h))/(12*h)
log_x = (-np.log(x+2*h)+8*np.log(x+h)-8*np.log(x-h)+np.log(x-2*h))/(12*h)

print(sen_x)
print((sen_x.shape))
#usar 100 x para cada h
