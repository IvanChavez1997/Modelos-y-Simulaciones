# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:42:56 2020

@author: Ivan Chavez
"""

import numpy as np
import matplotlib.pyplot as plt
import math as math
from sympy.abc import x
from sympy.integrals import integrate
from sympy import cos,pi,sin

#######################################
### Serie de Fourier de una función ###
# Gráfica de los n primeros términos ##

### Defino mis funciones

def Obtener_Periodo(Inf,Sup):
    if Inf<Sup:
        P=Sup
    elif Lim_inf==Lim_sup:
        print('Error: No existe periodo')
    else:
        print('Error: El límite inferior es mayor al superior')
    return P

##############################################
#### Ingreso de Datos ####
##########################

# n términos de la serie
n=8

#DEFINE LA FUNCIÓN NUEVAMENTE PARA LA GRAFICA
def funcion(x):
    num=x**2-x+2
    return num

# DEFINE LA FUNCION PARA EL CALCULO DE LA INTEGRAL
# LA MISMA FUNCIÓN QUE DIJITASTE ANTERIORMENTE
fun=x**2-x+2

# Limites de integración
Lim_inf=-1
Lim_sup=1

##############################################

P=Obtener_Periodo(Lim_inf, Lim_sup)

# Calculamos la constante a0
a0=integrate(fun,(x,-P,P))/P

#Definimos las funciones de las integrales y hallamos los coeficientes
Coef_a=[]
Coef_b=[]
for ni in range(n):
    ni=ni+1
    Coef_ai=integrate(fun*(cos((ni*pi/P)*x)),(x,-P,P))/P
    Coef_bi=integrate(fun*(sin((ni*pi/P)*x)),(x,-P,P))/P
    Coef_a.append(Coef_ai)
    Coef_b.append(Coef_bi)

#Generamos los arreglos para las graficas
x=np.linspace(Lim_inf,Lim_sup,100)
y=np.zeros(100)+a0/2
yi=[]
N=range(n)
#GENERAMOS LA GRAFICA
fig=plt.figure(figsize=(8,12),tight_layout=True)
ax1=fig.add_subplot(211,autoscale_on=True,title='Las '+ str(n)+" funciones trigonométricas que se superponen")
ax2=fig.add_subplot(212,autoscale_on=True,title="Aproximación de Fourier con n="+str(n)+' términos')
line=ax1.plot(x,y)
#Se calcula y suma cada término de la serie
#También se genera cada gráfica
for j in range(len(Coef_a)):
    ai=Coef_a[j]
    bi=Coef_b[j]
    j=j+1
    for i in x:
        val=ai*math.cos((j*math.pi/P)*i)+bi*math.sin((j*math.pi/P)*i)
        yi.append(val)
    y=y+yi
    line=ax1.plot(x,yi)
    yi=[]
ax2.plot(x,funcion(x),'--')   
ax2.plot(x,y)
plt.show()

