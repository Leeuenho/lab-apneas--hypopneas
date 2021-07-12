#김남철/2019 /1m

import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

fdir = 'D:/한림대학교/연구실/git_lab//'
fn = '1m_HRV.csv'
file = fdir+fn
data = pd.read_csv(file, encoding = "UTF-8")

#HRV 값 가져오기
hrv = data['HRV'].values

#hrv 구하기
y = 60000/hrv
    
#시간 값 가져오기
time = data['time'].values


x_s = list()
x_ms = list()

#시간 중 s값만 추출
for i in time:
    x_s.append( i[6]+i[7])
    
#시간 중 ms값 추출    
for i in time :
    x_ms.append(i[9]+i[10]+i[11])

#시간 = s단위로 정리
xx = list()
for i in range(0, len(x_s)):
    xx.append(x_s[i]+'.'+x_ms[i])

#### time을 바로 float으로 바꾸기위해 x = [float(i) for i in xx] 이용할 경우
####  could not convert string to float: '02:02:00:259' 에러 발생하여 위와같은 방법을 사용
####  time이라는 dataframe을 바로 interp1d에 입력할 경우 에러 발생

x1 = list()
x1 = [float(i) for i in xx]
x = pd.DataFrame(x1)


#선형보간법 
fl = interp1d(x[0],y, kind= 'linear')
xint = np.linspace(x[0].min(), x[0].max(), 1024)
yint = fl(xint)

plt.plot(x[0],y)
plt.plot(xint, yint, 'x')

plt.show()


# N = number of samples

# n = current sample

# k = current frequency, where k∈[0,N−1]

# xn = the sine value at sample n

# Xk = The DFT which include information of both amplitude and phase


#dft 함수 정의

def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    
    X = np.dot(e, x)
    
    return X



X = dft(yint)

N = len(X)

n = np.arange(N)
T = N/60
freq = n/T 
plt.figure(figsize = (8, 6))
plt.stem(freq, abs(X), 'b', \
         markerfmt=" ", basefmt="-b")