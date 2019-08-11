#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:14:57 2019

@author: tony
"""


from scipy import stats
from spacepy import pycdf
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
from datetime import datetime, timedelta, date, time
import numpy as np
import numpy.ma as ma
from collections import defaultdict
import spacepy.toolbox as tb
import spacepy.time as spt
import spacepy.radbelt as sprb
from spacepy import radbelt
import spacepy.pycdf as cdf
import os
from os import listdir
from datetime import datetime
from datetime import datetime, timedelta, date, time
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors


pathdatos='/home/tonyto94/Documents/TESIS/vanallen/'
Lista_Nombres=sorted(os.listdir(pathdatos))
t_REPT=[]
L=[]
Fesa=[]
Lista_Nombres_2012=Lista_Nombres[0:121]
Lista_Nombres_2013=Lista_Nombres[121:485]
Lista_Nombres_2014=Lista_Nombres[485:850]
Lista_Nombres_2015=Lista_Nombres[850:1214]
Lista_Nombres_2016=Lista_Nombres[1214:1580]
Lista_Nombres_2017=Lista_Nombres[1580:1945]
Lista_Nombres_2018=Lista_Nombres[1945:len(Lista_Nombres)]

for i in range(int(len(Lista_Nombres_2018))):
    filename= pathdatos + str(Lista_Nombres_2018[i])
    cdf_file_REPT=pycdf.CDF(filename)
    t_REPT_1=cdf_file_REPT['Epoch'].copy()
    t_REPT.append(t_REPT_1)
    L1=cdf_file_REPT['L_star'].copy()
    L.append(L1)
    Fesa_1=cdf_file_REPT['FESA'].copy()
    Fesa_1=Fesa_1[:,0]
    Fesa.append(Fesa_1)
FESA_label=cdf_file_REPT['FESA_LABL_1'].copy()   
#pego los fesa uno al lado del otro
h=np.empty(len(Fesa),dtype=float)
for j in range(len(Fesa)):
    k=len(Fesa[j])
    h[j]=k
aux=int(np.sum(h))

Fesa_Pegados=np.empty(int(np.sum(h)),dtype=float)
L_Pegados=np.empty(int(np.sum(h)),dtype=float)
t_Pegados=np.empty(int(np.sum(h)),dtype=datetime)


Delta_h=np.empty(len(h),dtype=float)
for i in range(len(h)):
    if i==0:
        Delta_h[i]=h[i]
    else:
        Delta_h[i]=h[i]+Delta_h[i-1]

for i in range(len(Fesa)):
    if i==0:
        Fesa_Pegados[0:int(Delta_h[0])]=Fesa[0]
        L_Pegados[0:int(Delta_h[0])]=L[0]
        t_Pegados[0:int(Delta_h[0])]=t_REPT[0]
        
    else:
        Fesa_Pegados[int(Delta_h[i-1]):int(Delta_h[i])]=Fesa[i]
        L_Pegados[int(Delta_h[i-1]):int(Delta_h[i])]=L[i]
        t_Pegados[int(Delta_h[i-1]):int(Delta_h[i])]=t_REPT[i]
        
#Ahora hago la lista de los bines de L
L_bineado=np.linspace(1,7,31)
L_por_bines=np.empty((len(L_Pegados),len(L_bineado),3))
L_por_bines[:,:,:]=np.NaN
#tiempo_por_bines=[[]]*len(L_bineado)
for i in range(len(L_Pegados)):
    for j in range(len(L_bineado)-1):    
        if L_bineado[j]<=L_Pegados[i]<L_bineado[j+1]:
            L_por_bines[i,j,0]=L_Pegados[i]
            L_por_bines[i,j,1]=Fesa_Pegados[i]
            #L_por_bines[i,j,2]=t_Pegados[i]
            break
            
#Ahora veo las medias por bin

L_medio_por_bin=np.empty_like(L_bineado)            
for i in range(len(L_medio_por_bin)):
    L_medio_por_bin[i]=np.nanmean(L_por_bines[:,i,1])
"""
#acá lo de adentro de L_Guardados es el L medio por bin separados
#por anios
#L_Guardados=[]
L_Guardados.append(L_medio_por_bin)
"""
#Calculo la media de las medias
MEDIA_bineado=np.empty_like(L_bineado)


for j in range(len(L_bineado)):
    aux=[]
    for i in range(len(L_Guardados)):
        aux.append(L_Guardados[i][j])
        MEDIA_bineado[j]=np.nanmean(aux)
        



#Ploteo para ver que pinta tiene
plt.plot(L_bineado,MEDIA_bineado)
plt.yscale('symlog')
plt.title('Grafico de Flujo Medio (unidades) vs. L')
plt.xlabel('L')
plt.ylabel('Flujo promedio (Unidades)')
plt.legend(loc = 'best')
plt.xticks(L_bineado,rotation=90)
plt.show()