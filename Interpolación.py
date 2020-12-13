# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:58:21 2020

@author: Ivan
"""
import matplotlib.pyplot as plt

###########################################
### INTERPOLAR UN VALOR EN MEDIO DE DOS ###


#### DATOS DE LA FUNCION ###

x=[7,10,13,16,19]
fx=[14,21,28,30,28]

#### PUNTO EN DONDE DESEA INTERPOLAR #####

hora=11


### EXTRACCION DE DATOS ######
for i in range(4):
    if (x[i]<hora) and (hora<x[i+1]):
        xo=x[i]
        x1=x[i+1]
        fxo=fx[i]
        fx1=fx[i+1]

### Interpolacion
Inter=fxo+((fx1-fxo)/(x1-xo))*(hora-xo)
print(Inter)

#### GRÁFICA ####
    
plt.plot(x,fx,'o',label='Puntos')
plt.plot(hora,Inter,'o',color='red',label='Interpolación en '+str(hora))
plt.legend()