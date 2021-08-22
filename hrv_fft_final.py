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
fn1 = '1m_HRV_최종환_PRE_30s.csv'

file1 = fdir+fn1
data1 = pd.read_csv(file1, encoding = "UTF-8")


#HRV 값 가져오기 (RR interval)
hrv = data1['HRV'].values


#x축 설정(시간)
x = [0.0]*75

for i in range(0, (len(hrv))) :
    if (i == 0):
        x[i] = hrv[i]
    else:
        x[i] = np.add(x[i-1], hrv[i])


import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np


#1024개 data로 interpolation
fl = interp1d(x, hrv, kind= 'linear')
xint = np.linspace(min(x), max(x), 1024)
yint = fl(xint)

# plt.plot(x, hrv)
# plt.plot(xint, yint, 'x')

# plt.show()



#n과 주파수 선언


s = x[len(x)-1]/1000
n = 1024
fs = n/s
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
# dc_rm = yy - np.mean(yy)
#dc_rm = detrend(dc_rm) 


# detred
# signal의 값 (point) 아래에 stem(DC) 값 존재
# 그것을 제거하는 함수
# 대부분의 신호 처리에서 사용하나 HRV에서는 거의 제거 안하는 편

#fft
X = fftpack.fft(yy)
X[0] = 0
X[1] = 0
X[2] = 0
X[3] = 0


freqs = fftpack.fftfreq(len(yy)) * fs


# fig, ax = plt.subplots()
# ax.stem(freqs, np.abs(X))
# ax.set_xlabel('Frequency in Hertz [Hz]')
# ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
# ax.set_xlim(0, fs / 20)
# ax.set_ylim(0, 10000)

#-----------------------------------------
# #dc 주파수인 0Hz 제거
# dc_rm = yint - np.mean(yint)
# #dc_rm = detrend(dc_rm)

# #fft
# Y = np.fft.fft(dc_rm)/n  >>>>> 자동으로 detred 
# Y = Y[range(int(n/2))]


# fig,ax = plt.subplots()
# ax.stem(f, np.abs(Y))
# ax.set_xlim(0, fs/20)

#---------------------------------------------------
lf_sum = 0
hf_sum = 0

######################### 원 데이터 : lf : 6.1 / hf : 4.1

################# lf: 6.22 / hf : 5.4
################# X 값 이용
for i in range(0, len(X)):
    if (X[i] >= 1 and X[i] <9):
        lf_sum += X[i]
    elif (X[i] >= 9 and X[i] < 23):
        hf_sum += X[i]
    else:
        continue;


################# lf : 7.6 / hf : 4.7
################# 주파수에 따른 X 값
# for i in range (0, len(freqs)):
#     if (freqs[i] >= 0.04 and freqs[i] < 0.14):
#         lf_sum += X[i]
#     elif (freqs[i] >= 0.14 and freqs[i] < 0.4) :
#         hf_sum += X[i]
#     else : 
#         continue
    

lf = np.log(lf_sum)

hf = np.log(hf_sum)








