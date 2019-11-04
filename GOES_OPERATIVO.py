#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:24:21 2019

@author: tony
"""

import numpy as np
from datetime import datetime, timedelta, date, time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

data = pd.read_csv('/home/tony/Datos_3_dias.txt', sep=",", header=None)

Anio=data[0]
Mes=data[1]
Dia=data[2]
Hora=data[3]
Minuto=[]
H=[]
for i in range(len(data[3])):
    H_str=str(Hora[i])
    H.append(H_str[0:2])
    Minuto.append(H_str[2:4])



Fecha=[]
for i in range(len(data)):
    Aux='%s/%s/%s %s:%s'%(Dia[i], Mes[i], Anio[i], H[i], Minuto[i])
    Fecha.append(Aux)
Date = [datetime.strptime(x,'%d/%m/%Y %H:%M') for x in Fecha]


E08Mev=data[4]
E2Mev=data[5]
E08Mev=np.ma.masked_where(E08Mev[:] == -1.00e+05, E08Mev[:])
E2Mev=np.ma.masked_where(E2Mev[:] == -1.00e+05, E2Mev[:])

year = mdates.DayLocator(interval=1)
months = mdates.HourLocator(interval=6)
yearFmt = mdates.DateFormatter('%Y/%m/%d')
fig, ax = plt.subplots()
ax.plot(Date,E2Mev,'r')
ax.plot(Date,E08Mev,'b')
# format the ticks
ax.xaxis.set_major_locator(year)
ax.xaxis.set_major_formatter(yearFmt)
#ax.xaxis.set_minor_locator(months)
#ax.set_xlim(Tiempo_Posta[0], Tiempo_Posta[len(Tiempo_Posta)-1])
ax.set_yscale('log')
ax.set_ylim((10**-1),(10**7))
plt.legend(['GOES-15 >= 2 MeV','GOES-15 >= 0,8 MeV'],loc='best')
fig.autofmt_xdate()
ax.grid(b=None, which='major', axis='both')
ax.set_xlabel('Fecha (Año/Mes/Día)')
ax.set_ylabel('Partículas $cm^{-2}s^{-1}sr^{-1}$')
#plt.title('Flujo de electrones con E>0.8MeV para sensor Este de GOES 2018',loc='center')
plt.show()

