#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:43:35 2018

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
L=[]
L_star=[]
for i in range(int(len(Lista_Nombres))):
    filename= pathdatos + str(Lista_Nombres[i])
    cdf_file_REPT=pycdf.CDF(filename)
    L1_star=cdf_file_REPT['L_star'].copy()
    L1=cdf_file_REPT['L'].copy()
    L.append(L1)
    L_star.append(L1_star)
    
    
    
h=np.empty(len(L),dtype=float)
for j in range(len(L)):
    k=len(L[j])
    h[j]=k
L_Pegados=np.empty(int(np.sum(h)),dtype=float)
L_star_Pegados=np.empty(int(np.sum(h)),dtype=float)
Delta_h=np.empty(len(h),dtype=float)
for i in range(len(h)):
    if i==0:
        Delta_h[i]=h[i]
    else:
        Delta_h[i]=h[i]+Delta_h[i-1]
        
for i in range(len(L)):
    if i==0:
        L_Pegados[0:int(Delta_h[0])]=L[0]
        L_star_Pegados[0:int(Delta_h[0])]=L_star[0]
        
    else:
        L_Pegados[int(Delta_h[i-1]):int(Delta_h[i])]=L[i]
        L_star_Pegados[int(Delta_h[i-1]):int(Delta_h[i])]=L_star[i]

x=L_Pegados
y=L_star_Pegados
plt.scatter(x,y)
plt.xlabel('L')
plt.ylabel('L_Star')
plt.xlim(-0.5,10)
plt.ylim(-0.5,10)
    
    
    
    
    