# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:41:25 2021

@author: eunho
"""

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

fdir = 'D:/한림대학교/연구실/git_lab//'
fn = '1m_HRV_최종환_PRE_30s.csv'

file = fdir+fn
data = pd.read_csv(file, encoding = "UTF-8")

#HRV 값 가져오기
hrv = data['HRV'].values


#소수점 2까지 hrv 구하기
y = [0.0]*75
for i in range(0, (len(hrv))):
    y[i] = round((60000/hrv[i]),2)

#x축 설정
x = [0.0]*75

for i in range(0, (len(hrv))) :
   if (i == 0):
       x[i] = y[i]
   else:
        x[i] = np.add(x[i-1],y[i])

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np


#1024개 data로 interpolation
fl = interp1d(x,y, kind= 'linear')
xint = np.linspace(min(x), max(x), 1024)
yint = fl(xint)

plt.plot(x,y)
plt.plot(xint, yint, 'x')

plt.show()



#n과 주파수 선언
n = 1024
s = 60
fs = n/s
t = 1/fs
fd = fs/n
f = (np.arange(n)) * fd
f = f[range(int(n/2))]

#hanning window 선언
win = np.hanning(1024)
win = win.tolist()

#data * window
yy = win*yint   


from scipy.fft import fft, fftfreq
from scipy import fftpack
from scipy.signal import detrend

#dc 주파수인 0Hz 제거
dc_rm = yint - np.mean(yint)
dc_rm = detrend(dc_rm)

#fft
X = fftpack.fft(dc_rm)
freqs = fftpack.fftfreq(len(dc_rm)) * fs


fig, ax = plt.subplots()
ax.stem(freqs, np.abs(X))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(0, fs / 20)

#-----------------------------------------
#dc 주파수인 0Hz 제거
dc_rm = yint - np.mean(yint)
dc_rm = detrend(dc_rm)

#fft
Y = np.fft.fft(dc_rm)/n
Y = Y[range(int(n/2))]


fig,ax = plt.subplots()
ax.stem(f, np.abs(Y))
ax.set_xlim(0, fs/10)

