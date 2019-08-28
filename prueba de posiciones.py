#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:06:32 2018

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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from spacepy import coordinates as coord
from spacepy.time import Ticktock



pathdatos='/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Documents/TESIS/vanallen/2012/'
Lista_Nombres=os.listdir(pathdatos)
t_REPT=[]
L=[]
Fesa=[]
pos=[]
for i in range(int(len(Lista_Nombres))):
    filename= pathdatos + str(Lista_Nombres[i])
    cdf_file_REPT=pycdf.CDF(filename)
    t_REPT_1=cdf_file_REPT['Epoch'].copy()
    t_REPT.append(t_REPT_1)
    L1=cdf_file_REPT['L'].copy()
    L.append(L1)
    Fesa_1=cdf_file_REPT['FESA'].copy()
    Fesa_1=Fesa_1[:,0]
    Fesa.append(Fesa_1)
    pos_1=cdf_file_REPT['Position'].copy()
    pos.append(pos_1)

h=np.empty(len(Fesa),dtype=float)
for j in range(len(Fesa)):
    k=len(Fesa[j])
    h[j]=k
aux=int(np.sum(h))

Fesa_Pegados=np.empty(int(np.sum(h)),dtype=float)
L_Pegados=np.empty(int(np.sum(h)),dtype=float)
t_Pegados=np.empty(int(np.sum(h)),dtype=datetime)

cvals = coord.Coords(pos_1, 'GEO', 'car')
cvals.ticks = Ticktock(t_REPT_1[:], 'ISO') 
newcoordinates = cvals.convert('GSE', 'car')

####GEO#########
fig, ax = plt.subplots(constrained_layout=True)
ax.plot(cvals.x,cvals.y)
circle1=plt.Circle((0, 0), 6371, color='blue')
ax.add_artist(circle1)
ax.set_ylim([-40000,40000])
ax.set_xlim([-40000,40000])
ax.set_title('Orbita de las Sondas Van Allen \n en sistema GEO',fontsize=18)
ax.set_xlabel('Distancia (km)')
ax.set_ylabel('Distancia (km)')
plt.show()
#######GSE (XY)##########################
fig, ax = plt.subplots(constrained_layout=True)
ax.plot(newcoordinates.x,newcoordinates.y)
circle1=plt.Circle((0, 0), 6371, color='blue')
ax.add_artist(circle1)
ax.set_ylim([-40000,40000])
ax.set_xlim([-40000,40000])
ax.set_title('Orbita de las Sondas Van Allen \n en sistema GSE',fontsize=18)
ax.set_xlabel('Distancia eje X(km)')
ax.set_ylabel('Distancia eje Y(km)')
plt.show()

###########GSE (XZ)########################
fig, ax = plt.subplots(constrained_layout=True)
ax.plot(newcoordinates.x,newcoordinates.z)
circle1=plt.Circle((0, 0), 6371, color='blue')
ax.add_artist(circle1)
ax.set_ylim([-40000,40000])
ax.set_xlim([-40000,40000])
ax.set_title('Orbita de las Sondas Van Allen \n en sistema GSE',fontsize=18)
ax.set_xlabel('Distancia eje X(km)')
ax.set_ylabel('Distancia eje Z(km)')
plt.show()


# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 6371 * np.outer(np.cos(u), np.sin(v))
y = 6371 * np.outer(np.sin(u), np.sin(v))
z = 6371 * np.outer(np.ones(np.size(u)), np.cos(v))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(newcoordinates.x, newcoordinates.y,newcoordinates.z)
# Plot the surface
ax.plot_surface(x, y, z, color='b')
ax.set_title(r'Orbita de las Sondas Van Allen en sistema GSE en proyección 3D')
ax.set_xlabel('Distancia (km)')
ax.set_ylabel('Distancia (km)')
ax.set_zlabel('Distancia (km)')
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(cvals.x, cvals.y,cvals.z)
# Plot the surface
ax.plot_surface(x, y, z, color='b')
ax.set_title(r'Orbita de las Sondas Van Allen en sistema GEO en proyección 3D')
ax.set_xlabel('Distancia (km)')
ax.set_ylabel('Distancia (km)')
ax.set_zlabel('Distancia (km)')
plt.show()

