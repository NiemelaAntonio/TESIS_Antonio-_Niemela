#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:44:01 2019

@author: tony
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

pathdatos='/media/tony/TOSHIBAEXT/TESIS/vanallen/'
Lista_Nombres=os.listdir(pathdatos)
L=[]
L_star=[]
pos=[]
for i in range(int(len(Lista_Nombres)/500)):
    filename= pathdatos + str(Lista_Nombres[i])
    cdf_file_REPT=pycdf.CDF(filename)
    L1=cdf_file_REPT['L'].copy()
    L1_star=cdf_file_REPT['L_star'].copy()
    L.append(L1)
    L_star.append(L1_star)
    pos_1=cdf_file_REPT['Position'].copy()
    pos.append(pos_1)
    
#aca los pego uno al lado del otro
 
h=np.empty(len(L),dtype=float)
for j in range(len(L)):
    k=len(L[j])
    h[j]=k
L_Pegados=np.empty(int(np.sum(h)),dtype=float)
L_star_Pegados=np.empty(int(np.sum(h)),dtype=float)
Delta_h=np.empty(len(h),dtype=float)
pos_pegados=np.empty(((int(np.sum(h))),3),dtype=float)
for i in range(len(h)):
    if i==0:
        Delta_h[i]=h[i]
    else:
        Delta_h[i]=h[i]+Delta_h[i-1]
        
for i in range(len(L)):
    if i==0:
        L_Pegados[0:int(Delta_h[0])]=L[0]
        L_star_Pegados[0:int(Delta_h[0])]=L_star[0]
        pos_pegados[0:int(Delta_h[0]),:]=pos[0]
        
    else:
        L_Pegados[int(Delta_h[i-1]):int(Delta_h[i])]=L[i]
        L_star_Pegados[int(Delta_h[i-1]):int(Delta_h[i])]=L_star[i]
        pos_pegados[int(Delta_h[i-1]):int(Delta_h[i]),:]=pos[i]
        
R=np.empty_like(L_Pegados)
for i in range(len(L_Pegados)):
    R[i]=(pos_pegados[i,0]**2+pos_pegados[i,1]**2+pos_pegados[i,2]**2)**(1/2)

#Me quedo con los puntos entre el minimo y 1000km de radio.
    
    
R=np.empty_like(L_Pegados)
R_1000km=[]
R_2000km=[]
for i in range(len(L_Pegados)):
    R[i]=(pos_pegados[i,0]**2+pos_pegados[i,1]**2+pos_pegados[i,2]**2)**(1/2)-6371
    if R[i]<1000:
        R_1000km.append(R[i])
    if R[i]<2000:
        R_2000km.append(R[i])
print('fracción de datos entre min(r) y 1000km es:',len(R_1000km)/len(R))
print('fracción de datos entre min(r) y 2000km es:',len(R_2000km)/len(R))