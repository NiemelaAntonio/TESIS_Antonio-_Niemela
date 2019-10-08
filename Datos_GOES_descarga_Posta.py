#import numpy as np
import requests
from datetime import datetime, timedelta
#########################################################################
#Bajo las cosas y armo el datetime
#########################################################################

url='https://services.swpc.noaa.gov/text/goes-particle-flux-primary.txt'
r = requests.get(url)
filename='/home/tonyto94/DATOS_GOES_15.txt'
f = open(filename, 'w')
f.write(r.content.decode('utf-8'))
f.close()

with open(filename) as file:
    file_num=file.read().splitlines()
    Ult_Linea=(file_num[26:len(file_num)])

Prueba=[]
for i in range(len(Ult_Linea)):
    Prueba.append(Ult_Linea[i].split())
Anio_descarga=[]
Mes_descarga=[]
Dia_descarga=[]
Hora_descarga=[]
H_descarga=[]
Minuto_descarga=[]
E08Mev_descarga=[]
E2Mev_descarga=[]
for j in range(len(Prueba)):
    Anio_descarga.append(Prueba[j][0])
    Mes_descarga.append(Prueba[j][1])
    Dia_descarga.append(Prueba[j][2])
    Hora_descarga.append(Prueba[j][3])
    E08Mev_descarga.append(Prueba[j][12])
    E2Mev_descarga.append(Prueba[j][13])

for i in range(len(Hora_descarga)):
    H_str=str(Hora_descarga[i])
    H_descarga.append(H_str[0:2])
    Minuto_descarga.append(H_str[2:4])
Fecha_descarga=[]
for i in range(len(Hora_descarga)):
    Aux='%s/%s/%s %s:%s'%(Dia_descarga[i], Mes_descarga[i], Anio_descarga[i], H_descarga[i], Minuto_descarga[i])
    Fecha_descarga.append(Aux)
Date_descarga = [datetime.strptime(x,'%d/%m/%Y %H:%M') for x in Fecha_descarga]

#########################################################################
#Agarro el archivo de los datos y lo abro y armo el datetime
#########################################################################
filename1='/home/tonyto94/Datos_3_dias.txt'
with open(filename1) as file:
    file_num=file.read().splitlines()
    Archivo=(file_num[:])
Prueba1=[]  
for i in range(len(Archivo)):
    Prueba1.append(Archivo[i].split())
Anio_Archivo=[]
Mes_Archivo=[]
Dia_Archivo=[]
Hora_Archivo=[]
Minuto_Archivo=[]
H_Archivo=[]
E08Mev_Archivo=[]
E2Mev_Archivo=[]
for j in range(len(Prueba1)):
    Anio_Archivo.append(Prueba1[j][0])
    Mes_Archivo.append(Prueba1[j][1])
    Dia_Archivo.append(Prueba1[j][2])
    Hora_Archivo.append(Prueba1[j][3])
    E08Mev_Archivo.append(Prueba1[j][4])
    E2Mev_Archivo.append(Prueba1[j][5])
for i in range(len(Anio_Archivo)):
    H_str=str(Hora_Archivo[i])
    H_Archivo.append(H_str[0:2])
    Minuto_Archivo.append(H_str[2:4])
Fecha_Archivo=[]
for i in range(len(Anio_Archivo)):
    Aux='%s/%s/%s %s:%s'%(Dia_Archivo[i], Mes_Archivo[i], Anio_Archivo[i], H_Archivo[i], Minuto_Archivo[i])
    Fecha_Archivo.append(Aux)
del(Aux)
Date_Archivo = [datetime.strptime(x,'%d/%m/%Y %H:%M') for x in Fecha_Archivo]

#########################################################################
#Busco a partir de cuando la diferencia es de 5 min o mas con el último
#Del archivo
#########################################################################
Diferencia_Descarga_Archivo=[]
#np.empty(len(Date_descarga),dtype=timedelta)
for i in range(len(Date_descarga)):
    Diferencia_Descarga_Archivo.append(Date_descarga[i]-Date_Archivo[len(Date_Archivo)-1])
    #print(Diferencia_Descarga_Archivo[i])
    #print(i)
a=timedelta(minutes=4)
Anio_Memoria=[]
Mes_Memoria=[]
Dia_Memoria=[]
Hora_Memoria=[]
Minuto_Memoria=[]
E08Mev_Memoria=[]
E2Mev_Memoria=[]
for i in range(len(Diferencia_Descarga_Archivo)):
    if Diferencia_Descarga_Archivo[i]>a:
        Anio_Memoria.append(Anio_descarga[i])
        Mes_Memoria.append(Mes_descarga[i])
        Dia_Memoria.append(Dia_descarga[i])
        Hora_Memoria.append(Hora_descarga[i])
        Minuto_Memoria.append(Minuto_descarga[i])
        E08Mev_Memoria.append(E08Mev_descarga[i])
        E2Mev_Memoria.append(E2Mev_descarga[i])
        

                    
filename1='/home/tonyto94/Datos_3_dias.txt'
f1 = open(filename1, 'a+')
for i in range(len(Anio_Memoria)):
    f1.write('%s %s %s %s %s %s\n'%(Anio_Memoria[i],Mes_Memoria[i],Dia_Memoria[i],Hora_Memoria[i],E08Mev_Memoria[i],E2Mev_Memoria[i]))
f1.close()
#############################################################################
#Se que es ineficiente, porque cierro y vuelvo a abrir el mismo archivo
#pero funciona
############################################################################

filename1='/home/tonyto94/Datos_3_dias.txt'
with open(filename1) as file:
    file_num=file.read().splitlines()
    Archivo=(file_num[:])
Prueba1=[]  
for i in range(len(Archivo)):
    Prueba1.append(Archivo[i].split())
Anio_Archivo=[]
Mes_Archivo=[]
Dia_Archivo=[]
Hora_Archivo=[]
Minuto_Archivo=[]
H_Archivo=[]
E08Mev_Archivo=[]
E2Mev_Archivo=[]
for j in range(len(Prueba1)):
    Anio_Archivo.append(Prueba1[j][0])
    Mes_Archivo.append(Prueba1[j][1])
    Dia_Archivo.append(Prueba1[j][2])
    Hora_Archivo.append(Prueba1[j][3])
    E08Mev_Archivo.append(Prueba1[j][4])
    E2Mev_Archivo.append(Prueba1[j][5])
for i in range(len(Anio_Archivo)):
    H_str=str(Hora_Archivo[i])
    H_Archivo.append(H_str[0:2])
    Minuto_Archivo.append(H_str[2:4])
Fecha_Archivo=[]
for i in range(len(Anio_Archivo)):
    Aux='%s/%s/%s %s:%s'%(Dia_Archivo[i], Mes_Archivo[i], Anio_Archivo[i], H_Archivo[i], Minuto_Archivo[i])
    Fecha_Archivo.append(Aux)
del(Aux)
Date_Archivo = [datetime.strptime(x,'%d/%m/%Y %H:%M') for x in Fecha_Archivo]


Diferencia_con_el_primero=[]
for i in range(len(Date_Archivo)):
    Diferencia_con_el_primero.append(Date_Archivo[i]-Date_Archivo[len(Date_Archivo)-1])
SieteDias=timedelta(days=-7)
for i in range(len(Diferencia_con_el_primero)):
    if Diferencia_con_el_primero[i]<SieteDias:
        print(i)
        Mes_Archivo.pop(i)
        Anio_Archivo.pop(i)
        Dia_Archivo.pop(i)
        Hora_Archivo.pop(i)
        E08Mev_Archivo.pop(i)
        E2Mev_Archivo.pop(i)


filename1='/home/tonyto94/Datos_3_dias.txt'
f1 = open(filename1, 'w')
for i in range(len(Anio_Archivo)-1):
    f1.write('%s %s %s %s %s %s\n'%(Anio_Archivo[i],Mes_Archivo[i],Dia_Archivo[i],Hora_Archivo[i],E08Mev_Archivo[i],E2Mev_Archivo[i]))
f1.close()
