# -*- coding: utf-8 -*-

import string 

### FUNCIONES #####

### CONTEO DE REPETICIONES DEL CARACTER ###
def contar_Caracter(texto,carac):
    return texto.count(carac)
### GENERA UNA LISTA CON LOS CARACTERES ####
def Generar_caracteres():
    carac=[]
    abc=string.ascii_uppercase
    for letra in abc:
        carac.append(letra)
    carac.append('Ã‘')
    carac.append(',')
    carac.append(':')
    carac.append(' ')
    return carac
### GENERA UNA LISTA CON EL CONTEO DE CARACTERES ###
def Generar_Conteo(texto,carac):
    conteo=[]
    for letra in carac:
        cont=contar_Caracter(texto,letra)
        conteo.append(cont)
    return conteo

### ORDENA LA LISTA DE CARACTERES ###
def Ordenar(carac,conteo):
    New_carac=[]
    for i in range(len(conteo)):
        mayor=max(conteo)
        pos_may=conteo.index(mayor)
        New_carac.append(carac[pos_may])
        conteo[pos_may]=-1
    return New_carac

### Generar el diccionarios ###
def Generar_Dic(New):
    Diccionario={}
    for i in range(len(New)):
        Diccionario[New[i]]=i+1
    Diccionario2={}
    for i in range(len(New)):
        Diccionario2[i+1]=New[i]
    Diccionarios=[Diccionario,Diccionario2]
    return Diccionarios

def Codificar_Archivo():
    carac=Generar_caracteres()
    text=open('TEXTO.txt','r')
    texto=text.read()
    text.close()
    conteo=Generar_Conteo(texto,carac)
    New_carac=Ordenar(carac,conteo)
    Dic=Generar_Dic(New_carac)[0]
    cad=''
    for letra in texto:
        if letra=='Ã':
            cad2='1'*Dic['Ã‘']
        elif letra=='‘':
            cad2=''
        elif letra=='\n':
            cad=''
        else:
            cad2='1'*Dic[letra]
        cad=cad+cad2
        cad=cad+'0'
    text=open('TEXTO_Codificado.txt','w')
    text.write(cad)
    return

def Decodificar_Archivo():
    carac=Generar_caracteres()
    text=open('TEXTO.txt','r')
    texto=text.read()
    text.close()
    conteo=Generar_Conteo(texto,carac)
    New_carac=Ordenar(carac,conteo)
    Dic=Generar_Dic(New_carac)[1]
    text=open('TEXTO_Codificado.txt','r')
    texto=text.read()
    cad=''
    cont=0
    for cifra in texto:
        if cifra=='1':
            cont=cont+1
        else:
            if cont==0:
                cad=cad+''
            else:
                cad=cad+Dic[cont]
            cont=0
    text=open('TEXTO_Decodificado.txt','w')
    text.write(cad)
    text.close()
    return 

print('Programa que codifica y decodifica un texto')
print('Que acción desea realizar:')
print('1.Codificar el archivo')
print('2.Decodificar el archivo')
op=input('Digite la opcion: ')
if op=='1':
    print('Usted ha escogido la opción para codificar el texto')
    Codificar_Archivo()
    print('El texto codificado se ha generado con exito.')
elif op=='2':
    print('Usted ha escogido la opción para decodificar el texto')
    Decodificar_Archivo()
    print('El texto se ha decodificado con éxito.')
else:
    print('Esa opción no existe')


        






    
    
    
    
    
    
    