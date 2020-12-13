# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 01:36:31 2020

@author: Ivan
"""
import matplotlib.pyplot as plt
import numpy as np

#### NOTA #####
# Este programa es un generador de campos para EDO´s básicas
# Puede generar campos de ecuaciones de primer orden y primer grado

### ECUACIÓN DIFERENCIAL QUE GENERA EN CAMPO ###
def funcion(x,y):
    EDO=3*y +x
    return EDO

### CREAMOS LOS ARREGLOS ###
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)

### REALIZAMOS UNA MALLA DE DATOS ###
X,Y=np.meshgrid(x,y)
### LONGITUD DE LAS LINEAS DE CAMPO ##
U=5
### GENERA LA DIRECCIÓN DE LAS LÍNEAS
V=funcion(X,Y)

### GRAFICA ###
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111,title='Campo direccional de una EDO')
q = ax.quiver(X, Y, U, V, scale=250)
plt.show()