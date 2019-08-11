#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:38:59 2018

@author: tonyto94
"""

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
for i in range(int(len(Lista_Nombres)/105)):
    filename= pathdatos + str(Lista_Nombres[i])
    cdf_file_REPT=pycdf.CDF(filename)
    t_REPT_1=cdf_file_REPT['Epoch'].copy()
    t_REPT.append(t_REPT_1)
    L1=cdf_file_REPT['L_star'].copy()
    L.append(L1)
    Fesa_1=cdf_file_REPT['FESA'].copy()
    Fesa_1=Fesa_1[:,0]
    Fesa.append(Fesa_1)
    
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




x=t_Pegados
y=ma.masked_less(L_Pegados,-1)
y=L_Pegados
plt.scatter(x,y)

z=Fesa_Pegados
xyz=[]
xyz=np.array([x,y,z])

xyz[2,:]=np.log10(z)
fig,ax=plt.subplots()
marker_size=15
plt.scatter(xyz[0,:], xyz[1,:], marker_size, c=np.log10(z))
plt.title("FESA (spin averaged electron flux) vs. L")
t_min=t_Pegados[0]
t_max=t_Pegados[len(t_Pegados)-1]
fig.autofmt_xdate()
ax.set_xlim([t_min, t_max])
plt.xlabel("Tiempo")
plt.ylabel("L-Shell")
cbar= plt.colorbar()
cbar.set_label("Flujo log10(FESA)", labelpad=+1)
plt.show()
