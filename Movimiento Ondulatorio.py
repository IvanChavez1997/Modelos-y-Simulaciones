# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:58:54 2020

@author: Ivan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


####### SIMULACIÓN DE MOVIMIENTO ONDULATORIO ####

### CREAMOS LA GRAFICA CON TRES SUBGRAFICAS###
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(311,autoscale_on=True,title="Q=Asen(wt)")
ax2 = fig.add_subplot(312,autoscale_on=True,title="Q=Asen(kx)")
ax3 = fig.add_subplot(313,autoscale_on=True,title="Q=Asen(kx+wt)")

### INGRESAMOS LOS DATOS DEL MOVIMIENTO ##
#AMPLITUD
A= 5
#FRECUENCIA ANGULAR
w= 5
#NUMERO DE ONDA
k= 3

### GENERAMOS LOS ARREGLOS DETIEMPO Y POSICION ##
t= np.arange(0, 2*np.pi, 0.01)
x= np.arange(0, 2*np.pi, 0.01)

### GENERAMOS LAS TRES LINEAS QUE DESCRIBEN UN CASO DIFERENTE ###
### K=0
line1, = ax1.plot(t, A*np.sin(w*t))
### w=0
line2, = ax2.plot(x, A*np.sin(k*x))
### k Y w DIFERENTE DE CERO
line3, = ax3.plot(t, A*np.sin(w*t+k*t))

###DEFINIMOS NUESTRA FUNCIÓN PARA LOS FRAMES ###
def animate(i):
    line1.set_ydata(A*np.sin(w*t+i/50))  # update the data.
    line2.set_ydata(A*np.sin(k*x+i/50))
    line3.set_ydata(A*np.sin(w*t+k*t+i/50))
    return line1, line2 , line3

### CREAMOS LA ANIMACIÓN ###
ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=bool, repeat_delay=25)

plt.show()