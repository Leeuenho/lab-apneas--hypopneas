# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:51:34 2021

@author: eunho
"""

import numpy as np
import matplotlib.pyplot as plt
# n = 100 #한 파장당 지점 개수
# fs = 200 
# t = 1/fs
# x = np.linspace(0.0, n*t, n, endpoint = False)  #np.linspace(시작, 종료, 간격) endpoint = 마지막 값을 포함할지 여부

# y = np.sin(10*2*np.pi*x)
# plt.plot(y)


f = 10
fs = 200
t = 1/fs
n = fs*2


x = np.linspace(0, n*t, n, endpoint = False)
y = np.sin(f*2*np.pi*x)

import matplotlib.pyplot as plt

plt.plot(y)

from scipy.fft import fft, fftfreq

from scipy import fftpack

X = fftpack.fft(y)
freqs = fftpack.fftfreq(len(y)) * fs

fig, ax = plt.subplots()
ax.stem(freqs, np.abs(X))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(-fs / 10, fs / 10)
ax.set_ylim(-5, 110)