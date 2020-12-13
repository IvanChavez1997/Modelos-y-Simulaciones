# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:19:48 2020

@author: Ivan
"""

##########IMPORTAR###############
##########LIBRERIAS##############
import numpy as np
import matplotlib.pyplot as plt

##########################################
### MODELO DE DOS MOVIMIENTOS FORZADOS ###
### Y LA SUPERPOSICION DE ESTOS #####

######DEFINIR FUNCIONES DEL MOVIMIENTO#########
def Amplitud(Fo,m,wf,wo,Y):
    su=(wf**2-wo**2)**2+(Y*wf)**2
    r=su**0.5
    A=Fo/(m*r)
    return A

def Ec_Forzado(t,A,fa,w):
    cos=np.cos(w*t+fa)
    sen=np.sin(w*t+fa)
    Xh=A*np.exp(-w*t)*sen
    Xp=A*cos
    Xf=Xh+Xp
    return Xf

###################################
    #INGRESO DE DATOS #
##################################
##########################
###MOVIMIENTO FORZADO 1 ###
#Fuerza 1
F1=15
#masa 1
m1=1
#frecuencia final 1
wf1=2
#frecuancia inicial
wo1=2.5
#fase 1
fs1=1

## NOTA: ambos movimiento tienen la misma frecuencia inicial
##########################
###MOVIMIENTO FORZADO 2 ###
#Fuerza 2
F2=10
#masa 2
m2=1
#Frecuencia final 2
wf2=3
#Fase 2
fs2=1

### GENERAMOS EL ARRAY DE TIEMPO PARA LA GRAFICA
t=np.linspace(-1,5,200)
v=[-0.5,5,-10,15]

####################################
####OBTENCION DE DATOS A GRAFICAR ##
####################################
A1=Amplitud(F1,m1,wf1,wo1,1)
A2=Amplitud(F2,m2,wf2,wo1,1)
y=Ec_Forzado(t,A1,fs1,2)
y2=Ec_Forzado(t,A2,fs2,2)
sup=y+y2

#################################
##########GRAFICAS##############
################################

fig=plt.figure(figsize=(8,7),tight_layout=True)
ax=fig.add_subplot(211,autoscale_on=True,title=
                   'Movimientos Forzados',xlim=(v[0],v[1]),
                   ylim=(v[2],v[3]),xlabel='Tiempo',ylabel='Amplitud',
                   ymargin=2)
ax.plot(t,y,'blue',label='Mov.Forzado 1')
ax.plot(t,y2,'red',label='Mov.Forzado 2')
ax.legend()
ax2=fig.add_subplot(212,autoscale_on=True,title=
                   'Superposición de Movimientos Forzados',xlim=(v[0],v[1]),
                   ylim=(v[2],v[3]),ymargin=2)
ax2.plot(t,sup,'orange')

