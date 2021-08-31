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
        
        
        
# t = x[len(x)-1] / 1000
# n = len(hrv)
# fs = n/t
# f = (np.arange(n)) * fs
# f = f[range(int(n/2))]


data[0] = hrv

import pywt

import matplotlib.pyplot as plt
    

coeff = pywt.wavedec(hrv, 'db4', level = 18)

cl18, cl17h, cl16h, cl15h, cl14h, cl13h, cl12h, cl11h, cl10h, cl9h, cl8h, cl7h, cl6h, cl5h, cl4h, cl3h, cl2h, clh, ch = coeff

f = pywt.scale2frequency('db4', 18)







# 18 = 0.39/ 5 = 0.14/ 2 = 0.35

lf = 0
hf = 0

for i in range(len(coeff)):
    abs(coeff[i]**2)


for i in range(len(coeff)):
    if (i>=5 & i<=17):
        for k in range(len(coeff[i])):
            lf += coeff[i][k]
            
            
for i in range(len(coeff)):
    if (i>=1 & i<=5):
        for k in range(len(coeff[i])):
            hf += coeff[i][k]


    
    
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
    
