#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:24:21 2019

@author: tony
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
nc=Dataset('g15_epead_e13ew_1m_20120801_20120831_science_v1.0.0.nc','r')
for i in nc.variables:
    print(i)
a=nc.variables
print(a)

E2West_Cor_Flux=nc.variables['E2W_COR_FLUX'][:]
Time_Tag=nc.variables['time_tag'][:]

plt.plot(Time_Tag,E2West_Cor_Flux)