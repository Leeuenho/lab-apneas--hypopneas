# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:28:46 2021

@author: eunho
"""

import pandas as pd
import warnings
import numpy as np

warnings.filterwarnings('ignore')

fdir = 'D:/한림대학교/연구실/git_lab//'
fn = '1m_HRV_최종환_PRE_30s.csv'
file = fdir+fn

data = pd.read_csv(file)
hrv = data['HRV'].values


x = [0.0]*len(hrv)

for i in range (0, len(hrv)):
    if (i == 0):
        x[i] = hrv[i]
    else :
        x[i] = x[i-1] + hrv[i]
        
        
from scipy.interpolate import interp1d


#1024개 data로 interpolation
fl = interp1d(x, hrv, kind= 'linear')
xint = np.linspace(min(x), max(x), 5000)
yint = fl(xint)

        
        
t = x[len(x)-1] / 1000
n = len(yint)
fs = n/t



import pywt

import matplotlib.pyplot as plt
    

#dwt 최대 레벨 찾기
max_level = pywt.dwt_max_level(5000, 'db4')

#dwt 수행
coeff = pywt.wavedec(yint, 'db4', level = 9)


for i in range(len(coeff)):
    coeff[i] = abs(coeff[i]**2)


l9, l8h, l7h, l6h, l5h, l4h, l3h, l2h, lh, h = coeff



f = [0.0]*11

for i in range(0,10):
    f[i] = 2**(-i)

f1 = np.linspace(f[0], f[1], len(h))
f2 = np.linspace(f[1], f[2], len(lh))
f3 = np.linspace(f[2], f[3], len(l2h))
f4 = np.linspace(f[3], f[4], len(l3h))
f5 = np.linspace(f[4], f[5], len(l4h))
f6 = np.linspace(f[5], f[6], len(l5h))
f7 = np.linspace(f[6], f[7], len(l6h))
f8 = np.linspace(f[7], f[8], len(l7h))
f9 = np.linspace(f[8], f[9], len(l8h))
f10 = np.linspace(f[9], f[10], len(l9))




h = np.c_[h, f1]
lh = np.c_[lh, f2]
l2h = np.c_[l2h, f3]
l3h = np.c_[l3h, f4]
l4h = np.c_[l4h, f5]
l5h = np.c_[l5h, f6]
l6h = np.c_[l6h, f7]
l7h = np.c_[l7h, f8]
l8h = np.c_[l8h, f9]
l9 = np.c_[l9, f10]





lf = 0
hf = 0

for i in range(len(h)-1):
    if(h[i][1] >= 0.04 and h[i][1] <= 0.15):
        lf += h[i][0]
    elif(h[i][1] >= 0.15 and h[i][1] <= 0.4):
        hf += h[i][1]

for i in range(len(lh)):
    if(lh[i][1] >= 0.04 and lh[i][1] <= 0.15):
        lf += lh[i][0]
    elif(lh[i][1] >= 0.15 and lh[i][1] <= 0.4):
        hf += lh[i][0]

for i in range(len(l2h)):
    if(l2h[i][1] >= 0.04 and l2h[i][1] <= 0.15):
        lf += l2h[i][0]
    elif(l2h[i][1] >= 0.15 and l2h[i][1] <= 0.4):
        hf += l2h[i][0]
        
for i in range(len(l3h)):
    if(l3h[i][1] >= 0.04 and l3h[i][1] <= 0.15):
        lf += l3h[i][0]
    elif(l3h[i][1] >= 0.15 and l3h[i][1] <= 0.4):
        hf += l3h[i][0]
        
for i in range(len(l4h)):
    if(l4h[i][1] >= 0.04 and l4h[i][1] <= 0.15):
        lf += l4h[i][0]
    elif(l4h[i][1] >= 0.15 and l4h[i][1] <= 0.4):
        hf += l4h[i][0]
        
for i in range(len(l5h)):
    if(l5h[i][1] >= 0.04 and l5h[i][1] <= 0.15):
        lf += l5h[i][0]
    elif(l5h[i][1] >= 0.15 and l5h[i][1] <= 0.4):
        hf += l5h[i][0]       

for i in range(len(l6h)):
    if(l6h[i][1] >= 0.04 and l6h[i][1] <= 0.15):
        lf += l6h[i][0]
    elif(l6h[i][1] >= 0.15 and l6h[i][1] <= 0.4):
        hf += l6h[i][0]

for i in range(len(l7h)):
    if(l7h[i][1] >= 0.04 and l7h[i][1] <= 0.15):
        lf += l7h[i][0]
    elif(l7h[i][1] >= 0.15 and l7h[i][1] <= 0.4):
        hf += l7h[i][0]
        
for i in range(len(l8h)):
    if(l8h[i][1] >= 0.04 and l8h[i][1] <= 0.15):
        lf += l8h[i][0]
    elif(l8h[i][1] >= 0.15 and l8h[i][1] <= 0.4):
        hf += l8h[i][0]

for i in range(len(l9)):
    if(l9[i][1] >= 0.04 and l9[i][1] <= 0.15):
        lf += l9[i][0]
    elif(l9[i][1] >= 0.15 and l9[i][1] <= 0.4):
        hf += l9[i][0]
        

ln_lf = np.log(lf)
ln_hf = np.log(hf)
    
    
# plt.subplot(5,1,1)
# plt.plot(hrv)


# plt.subplot(5,1,2)
# plt.plot(ch)

# plt.subplot(5,1,3)
# plt.plot(clh)

# plt.subplot(5,1,4)
# plt.plot(cllh)

# plt.subplot(5,1,5)
# plt.plot(clll)




#----------------------복원

# hrv_res = pywt.waverec(coeff, 'sym4')

# plt.subplot(2,1,1)
# plt.plot(hrv)
# plt.subplot(2,1,2)
# plt.plot(hrv_res)
    
