#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:57:38 2019

@author: tony
"""
from scipy import stats
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
import os
from os import listdir
from datetime import datetime
from datetime import datetime, timedelta, date, time
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors
from scipy.stats import norm

###################################################################
#Vamos a hacer de 3.9 a 4.7 para que 4.3 este centrado (que es la posicion 16)
###################################################################
x_Total_por_Anio=[]
'''
pathdatos='/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/'
Lista_Nombres=sorted(os.listdir(pathdatos))
Datos_2012=np.load(pathdatos+str(Lista_Nombres[0]))[0,:,14:19]
Datos_2012=np.load(pathdatos+str(Lista_Nombres[1]))[0,:,14:19]
Datos_2012=np.load(pathdatos+str(Lista_Nombres[2]))[0,:,14:19]
Datos_2012=np.load(pathdatos+str(Lista_Nombres[3]))[0,:,14:19]
Datos_2012=np.load(pathdatos+str(Lista_Nombres[4]))[0,:,14:19]
Datos_2012=np.load(pathdatos+str(Lista_Nombres[5]))[0,:,14:19]
Datos_2012=np.load(pathdatos+str(Lista_Nombres[6]))[0,:,14:19]

Datos_1=[]
aux=[]
for i in range(5):
    aux=Datos_2012[:,i]
    Datos_1.append(np.log10(aux[~np.isnan(aux)]))

#######################
#Bines para el flujo
#######################
Inicio=2.0
Fin=7.0
bines=np.linspace(Inicio,Fin,num=11)

#######################
a,b=np.histogram(Datos_1[0],bins=bines)
c,d=np.histogram(Datos_1[1],bins=bines)
e,f=np.histogram(Datos_1[2],bins=bines)
g,h=np.histogram(Datos_1[3],bins=bines)
i,j=np.histogram(Datos_1[4],bins=bines)

Sumatoria_2018=a+c+e+g+i
Sumatoria_Total=Sumatoria_2018+Sumatoria_2017+Sumatoria_2016+Sumatoria_2015+Sumatoria_2014+Sumatoria_2013+Sumatoria_2012
np.save('Sumatoria_Total.npy',Sumatoria_Total)
np.save('bines.npy',bines)
'''
Bines=np.load('bines.npy')
Sumatoria_Total=np.load('Sumatoria_Total.npy')

#####################
#No se que hacer con esto
#####################
#Fiteado
mu, std = norm.fit(np.log10(Sumatoria_Total))
#############
#OJO CON ESTO
bines=Bines[1:len(Bines)]
#############
fig, axs = plt.subplots(constrained_layout=True)
fig.set_size_inches(12,10)
plt.bar(bines,Sumatoria_Total,width=0.8,align='center')
plt.xlabel('log$_{10}$(Monthly Mean Flux)',fontsize=24)
plt.tick_params(axis='x',labelsize=20)
plt.ylabel('Frecuency',fontsize=24)
plt.tick_params(axis='y',labelsize=20)
plt.text(1.65, 800000, r'$\mathcal{N}(\mu = 5.27 , \sigma =0.74)$', fontsize=30)
ax2 = axs.twinx()
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
ax2.axes.get_yaxis().set_visible(False)
plt.savefig('histograma_zona_gris.pdf', format='pdf')
plt.show()
