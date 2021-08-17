# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:34:28 2021

@author: eunho
"""

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

fdir = 'D:/한림대학교/연구실/git_lab//'
fn1 = '1m_HRV_최종환_PRE_30s.csv'
fn2 = '1m_HRV_최종환_PRE_30s_1.csv'

file1 = fdir+fn1
file2 = fdir+fn2

data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

hr = data1['HRV'].values

x = [0.0] * len(hr)

for i in range(0, len(hr)):
    if(i == 0):
        x[i] = hr[i]
    else:
        x[i] = x[i-1] + hr[i]
        


time = data2['Time'].values[-1]
a = time.split(':')
a = list(map(int, a))
s = a[0]*3600 + a[1]*60 + a[2]
n = len(hr)
fs = n/s
t = 1/fs
fd = fs/n
f = (np.arange(n)) * fd
f = f[range(int(n/2))]



import pywt
import matplotlib.pyplot as plt

fc = pywt.centrfrq('gaus1')
scale = fc/f
scale[0] = 0

for i in range(1, len(scale)):
    scale[i-1] = scale[i]

coef, freqs = pywt.cwt(hr, scale,  'gaus1')


# interpolation 번짐효과 none을 하면 번짐효과가 없다.
# vmin vmax colorbar의 최소값과 최대값을 조정. 
# 만약 vmax = 1, vmin = -1 >>>> 1보다 큰값은 1의, -1보다 작은값은 -1의 색을 따른다.

plt.imshow(abs(coef), extent=[0, 1, 0.45, 0], interpolation = 'none', cmap='bone', 
           aspect = 'auto', vmax = abs(coef).max(), vmin = -abs(coef).max())


plt.gca().invert_yaxis()





