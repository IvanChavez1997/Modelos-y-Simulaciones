"""
Created on Thu Jun 18 02:49:58 2020
@author: Ivan Chavez, Emi Altamirano, Christhian Varzallo
"""
#%matplotlib auto
#%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.image import NonUniformImage
from matplotlib import colors

###########################################################
### ESTE ES UNA SIMULACION QUE HICE ##
### PARA MI CLASE DE TERMODINÁMICA ###
### DONDE SE REALIZA UN MODELADO DE UN SECADOR SOLAR QUE TIENE
### FORMA RECTANGULAR Y UTILIZANDO LA ENERGÍA INCIDENTE DEL SOL
### PUEDE ELEVAR SU TEMPERATURA EN EL INTERIOR DE LA CAMARA
###########################################################

################################
##### FUNCIONES QUE DESCRIBEN EL MODELO################
################################
#Coeficiente de perdidas
def Coef_Perdidas(Ka,Aef):
    Up=1.06+Ka*(50+(54/Aef))
    return Up
#Energia Absorvida
def En_Absorvida(I,at):
    return I*at
#Temperatura media de la placa
def Tem_Placa(h,A,Tmin,Q):
    masa=h*A
    T=Tmin + (Q/(masa*1010))
    return T
#Area efectiva
def Area_efectiva(l,a):
    return l*a

### FUNCIÓN PARA EL COLOR DE CADA BARRA SEGÚN LA TEMPERATURA
def Bar_Color(T_Flujo):
    if T_Flujo<6: clr='navy'
    elif T_Flujo>5  and T_Flujo<11: clr='indigo'
    elif T_Flujo>10 and T_Flujo<16: clr='purple'
    elif T_Flujo>15 and T_Flujo<21: clr='orchid'
    elif T_Flujo>20 and T_Flujo<26: clr='hotpink'
    elif T_Flujo>25 and T_Flujo<31: clr='orange'
    elif T_Flujo>30 and T_Flujo<36: clr='gold'
    else : clr='yellow'
    return clr

###########################################
### FUNCIÓN PRINCIPAL QUE DESCRIBE EL MODELO DEL SECADOR SOLAR
def modelo(K,l,a,h):
################################
########## DATOS ###############
################################
    #Coeficiente de pérdidas
    U=Coef_Perdidas(K,Area_efectiva(l,a))
    #Absorvancia-transmitancia ideal
    at=1
    #Temperaturas del ambiente
    Ts=np.array([11.8,11.7,11.5,11.2,11.1,10.7,10.6,10.5,10.3,
                 10.1,10.5,11.1,12.8,13.6,14.2,14.6,17.6,17.6,
                 17.6,17.7,16.8,15.6,14.1,12.8])
    Tmin=np.amin(Ts)
    n=Ts.size
    #Radiaciones
    Is=np.array([0,0,0,0,0,0,0,39,173,396,385,363,632,1085,
                 1184,490,496,318,122,13,11,10,9,0])
    #tiempo
    ts=np.arange(0,n+1,1)
    
    ################################
    #### Modelo Colector Solar #####
    ################################
    # Arreglo de potencias
    Ps=np.arange(0,n+1,1)
    Qs=np.arange(0,n+1,1)
    TsFlujo=np.arange(0,n+1,1)
    # Calculo de Potencia y Calor
    # A cada hora
    Qs[0]=0
    for i in range(Ts.size):
        P=Area_efectiva(l,a)*(En_Absorvida(Is[i],at)-U*(Tem_Placa(h,Area_efectiva(l,a),Tmin,Qs[i])-Ts[i]))
        Ps[i+1]=P
        Qs[i+1]=Qs[i]+P
        TsFlujo[i]=Qs[i+1]/(990*Area_efectiva(l,a)*h)+Tmin
    datos=np.array([ts,Ps,Qs,Ts,TsFlujo,n])
    return datos

    ################################
    # Modelo Temperatura de Flujo ##
    ################################

    # Calculo de temperatura en el flujo #
### ESTA FUNCIÓN CREA UNA MATRIZ BIDIMENSIONAL CON EL VALOR DE LA
### TEMPERATURA EN CADA PARTE DENTRO DE LA CAMARA DE ABSORCIÓN DE CALOR
### LUEGO ESTOS DATOS DE TEMPERATURA SON REPRESENTADOS CON DIFERENTES
### COLORES PARA UNA MEJOR OBSERVACIÓN DE COMO FLUYE EL CALOR DENTRO
### DE LA CAMARA.
def Graf_Flujo(Vf,K,l,a,h,H):
    #Matriz del Marco
    Mx=int(l/0.05)
    LadoMx=np.arange(1,Mx+1,1)
    My=int (a/0.05)+1
    LadoMy=np.arange(1,My+1,1)
    M=np.ones([My,Mx])
    #Extraigo los datos
    mod=modelo(K,l,a,h)
    Qs=mod[2]
    TsFlujo=mod[4]
    Hi=H
    Tmin=TsFlujo[Hi-2]
    QsAn=Qs[Hi-1:Hi+3]
    #Calor en cada celda
    Qi=QsAn[0]/(Mx*My)
    #Incremento de T
    Tadd=Qi/(Vf)
    Tper=((K*Qi)/h)
    #Primera columna con Tmin
    for i in range(My):
        M[i,0]=Tmin
    #print(M)
    #Tfinal en cada celda
    for j in range(int(My/2)+1):
        for i in range(1,Mx):
            M[j,i]=M[j,i-1]+Tadd
            M[My-1-j,i]=M[j,i]
        M[j]=M[j]-(Tper*(int(My/2)-j))
        M[My-1-j]=M[j]        
    #print(M)
    #grafico del flujo
    fig, axs = plt.subplots(figsize=(10,5))
    im = NonUniformImage(axs, interpolation='bilinear', extent=(-4,4,-4,4),
                     cmap='plasma')
    im.set_data(LadoMx, LadoMy, M)
    axs.images.append(im)
    axs.set_xlim(0, Mx-1)
    axs.set_ylim(0, My-1)
    axs.set_title('Temperatura del Flujo de Aire dentro del Colector (con K='+str(K)+")",fontsize=14)
    axs.set_xlabel('Longitud (x0.05m)')
    axs.set_ylabel('Ancho (x0.05m)')

#    print(tsAn,QsAn,TsAn,TsFlujoAn)
################################
#### Graficas del modelado #####
################################

#######################################33
### PEDIMOS AL USUARIO QUE INGRESE ALGUNOS DATOS
# Longitud
l=float(input('Ingrese la longitud de la placa en metros: '))
# Ancho
a=float(input('Ingrese el ancho de la placa en metros: '))   
#Altura
h=float(input('Ingrese la altura de la placa en metros: '))
#Constante con aislante
print(' Ingrese la constante térmica del modelo:')
K=float(input('El modelo solo puede tomar valores en el intervalo [0,2.5]:'))

### GENERAMOS EL MODELO Y EXTRAEMOS LOS RESPECTIVOS ARREGLOS
mod=modelo(K,l,a,h)
ts=mod[0]
Ps=mod[1]
Qs=mod[2]
Ts=mod[3]
TsFlujo=mod[4]
n=mod[5]
### CREAMOS LOS VALORES MAXIMOS Y MINIMOS DE LA BARRA
norm = colors.Normalize(vmin=0, vmax=35)
### GENERAMOS LA FIGURA DONDE TRABAJAREMOS
fig, Graficas=plt.subplots(3,1,figsize=(9,15),constrained_layout=True)
fig.suptitle('Modelado de un Secador Solar', fontsize=16)
fig.colorbar(cm.ScalarMappable(norm=norm, cmap='plasma'), ax=Graficas, 
                 orientation='horizontal', fraction=.1)
### GRAFICAMOS EN CADA SUBPLOT CON LOS CORRESPONDIENTES ARREGLOS
    #Grafica Tiempo vs Potencia
Graficas[0].plot(ts,Ps)
Graficas[0].plot(ts,Ps,marker='o',linestyle='none')
Graficas[0].set_title('Potencia efectiva')
Graficas[0].set_ylabel('Pefectiva(w)')
Graficas[0].set_xlabel('Tiempo(h)')
Graficas[0].grid()
#Graficas[0].set(ylim=(-500,1800))
    #Grafica Tiempo vs Calor
Graficas[1].plot(ts,Qs)
Graficas[1].plot(ts,Qs,marker='^',linestyle='none',markeredgecolor='black',
            markerfacecolor='black')
Graficas[1].set_title('Calor en el colector')
Graficas[1].set_ylabel('Calor (J)')
Graficas[1].set_xlabel('Tiempo(h)')
Graficas[1].grid()
#Graficas[1].set(ylim=(0,8000))
    #Grafica Tiempo vs Temperatura del flujo
for i in range (n):
        color=Bar_Color(TsFlujo[i])
        Graficas[2].bar(ts[i],TsFlujo[i],color=color)
Graficas[2].set_title('Temperatura en el colector')
Graficas[2].set_ylabel('Temperatura(C)')
Graficas[2].set_xlabel('Tiempo(h)')
Graficas[2].grid()
#Graficas[2].set(ylim=(0,40))
Graf_Flujo(0.5,K,l,a,h,10)
















