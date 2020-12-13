# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:39:19 2020

@author: Ivan
"""

import numpy as np
import matplotlib.pyplot as plt

########################################
### PROGRAMA QUE ANALIZA EL COMPORTAMIENTO DE LA AMPLITUD
### Y LA FASE EN UN MOVIMIENTO OSCILATORIO FORZADO

### DEFINIMOS LAS ECUACIONES DEL MOVIMIENTO OSCILATORIO FORZADO
def Amplitud(Fo,m,wf,wo,Y):
    su=(wf**2-wo**2)**2+(Y*wf)**2
    r=su**0.5
    A=Fo/(m*r)
    return A

def fase(wf,wo,Y):
    div=((Y*wf)/(wf**2-wo**2))
    return div

### GENERAMOS LOS DATOS PARA LA GRAFICA
n=10
ni=-n
wf=np.linspace(ni,10,200)
v=[0,n,-5,5]
v2=[0,n,0,15]

### INTRODUCIMOS LAS VARIABLES DEL MOVIMEINTO
### fUERZA EXTERNA
F1=20
# MASA DEL OBJETO
m1=1
# FRECUENCIA INICIAL
wo1=2
# k DEL RESORTE
Y1=1

### OBTENEMOS LOS DATOS A GRAFICAR ##
y=Amplitud(F1,m1,wf,wo1,Y1)
y2=fase(wf,wo1,Y1)

### GRAFICA
plt.figure(figsize=(10,15))
plt.subplot(2,1,1)
plt.axis(v2)
plt.plot(wf,y)
plt.grid()
plt.xlabel('Frecuencia Angular W')
plt.ylabel('Amplitud')
plt.title('Comportamiento de la Amplitud y la Fase con respecto a la Frecuencia Angular')
plt.subplot(2,1,2)
plt.axis(v)
plt.plot(wf,y2)
plt.xlabel('Frecuencia Angular W')
plt.ylabel(r'Tan ([$\phi$])')
plt.grid()