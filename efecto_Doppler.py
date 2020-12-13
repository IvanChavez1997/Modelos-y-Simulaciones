# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:46:24 2020

@author: Ivan Chavez
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#########################
#### SIMULACION DEL #####
#### EFECTO DOPPLER #####
#########################
### Ingreso de Datos ####
#########################

### POSICION FINAL ###
def dar_pos_final():
    pos=100
    return pos

### VELOCIDAD DE ONDA ###
def dar_velocidad():    
    v=350
    return v

### VELOCIDAD DE PARTICULA ###
def dar_velocidad_part():
    vp=300
    return vp

def dar_Amplitud():
    A=2
    return A

### CREAMOS LA GRAFICA ###
fig= plt.figure(figsize=(20,10))
### NUMERO DE LINEAS QUE REPRESENTARAN LAS ONDAS GENERADAS ###
num_lineas=300
### EXTRAEMOS LOS DATOS ###
y_lim=dar_velocidad_part()/4
x_lim_inf=-dar_velocidad_part()+dar_pos_final()
x_lim_sup=dar_pos_final()

###CREAMOS EL EJE DE COORDENADAS DONDE TRABAJARA LA SIMULACION
an1=fig.add_subplot(111,autoscale_on=True,title="Simulación del efecto Doppler",
                    ylim=(-y_lim,y_lim),xlim=(x_lim_inf,x_lim_sup))

### GENERAMOS LOS DATOS NECESARIOS PARA LA ANIMACION
lineas=[]
ang=np.linspace(0,2*np.pi,100)
pos=dar_pos_final()
for k in range(num_lineas):
    ### SE GENERA CADA ONDA ###
    linea, = an1.plot(np.cos(ang)+pos,np.sin(ang),'white')
    lineas.append(linea)
    
    ### CREAMOS UNA FUNCION PARA CADA FRAME DE CADA LINEA ###
    def animate(i):
        R=-num_lineas*dar_Amplitud()
        pos=dar_pos_final()
        for r in range(num_lineas):
            ### LAS LINEAS CAMBIAN SU POSICION DE ORIGEN 
            ### SIMULANDO QUE LA PARTICULA SE MUEVE
            lineas[r].set_ydata((R+i*(dar_velocidad()/350))*np.sin(ang))
            lineas[r].set_xdata((R+i*(dar_velocidad()/350))*np.cos(ang)+pos)
            ### EL RADIO DE LAS ONDAS AUMENTA SIMULANDO QUE SE PROPAGAN
            R=R+dar_Amplitud()
            ### hACEMOS UN CAMBIO DE COLOR PARA IDENTIFICAR LA POSICION
            val=lineas[r].get_ydata()[1]
            pos=pos-dar_velocidad_part()/350
            if val>0.6:
                lineas[r].set_color('blue')
            elif (val>0) & (val<0.4):
                lineas[r].set_color('red')
            elif (val>0.4)& (val<0.6):
                lineas[r].set_color('white')
        return
    pos=pos-dar_velocidad_part()/350
  
### GENERAMOS LA SIMULACION PARA CADA LINEA
    ani = animation.FuncAnimation(
        fig, animate, blit=False, interval=1)
plt.show()