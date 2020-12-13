# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:00:43 2020

@author: Ivan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

###### MOVIMIENTO ONDULATORIO ####
#### SIMULACION DE LA PROPAACION DE PULSOS ###

### INGRESAMOS LOS DATOS PQUE DESCRIBEN EL MOVIMIENTO
### VELOCIDADES
V1=1
V2=1
V3=1
### AMIPLITUDES
A1=1
A2=2
A3=3

### CREAMOS LA FIGURA SOBRE LA QUE TRABAJAREMOS ###
fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(311,ylim=(0,3.2),xlim=(0,10))
ax2 = fig.add_subplot(312,ylim=(0,3.2),xlim=(0,10))
ax3 = fig.add_subplot(313,ylim=(0,3.2),xlim=(0,10))

### GENERAMOS EL ARREGLO DE TIEMPO Y LAS LINEAS DE LAS FUNCIONES
t=np.arange(0,10,0.01)
line1, =ax1.plot(t,A1/(1+(t/V1)**2))
line2, =ax2.plot(t,A2/(1+(t/V2)**2))
line3, =ax3.plot(t,A3/(1+(t/V3)**2))

### CREAMOS LA FUNCION QUE GENERA LOS FRAMES ###
def animate(i):
    line1.set_ydata(A1/(1+(t/V1-i/50)**2))
    line2.set_ydata(A2/(1+(t/V2-i/50)**2))
    line3.set_ydata(A3/(1+(t/V3-i/50)**2))
    return line1,line2,line3

### GENERAMOS LA ANIMACION
ani = animation.FuncAnimation(
    fig, animate, blit=True, interval=10,repeat=True,frames=500)
plt.show()