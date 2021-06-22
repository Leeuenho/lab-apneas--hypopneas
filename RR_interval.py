#!/usr/bin/env python
# coding: utf-8

# # 변수선언, 파일 불러오기

# In[ ]:



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks
from scipy.interpolate import interp1d

subset = pd.read_csv("D:/한림대학교/연구실/EKG_data.csv", encoding='UTF-8') #csv파일 불러오기

subset1 = subset['pre1'].values
subset2 = subset['post1'].values
subset3 = subset['pre2'].values
subset4 = subset['post2'].values


# # Pre1
# 
# ## pre1 피크 값

# In[11]:


pre1_peaks, properties = find_peaks(subset1,height=200)
print("pre1_peaks",pre1_peaks)
plt.plot(subset1)
plt.plot(pre1_peaks,subset1[pre1_peaks],"x")
print("pre1_peaks_height", properties['peak_heights'])


# ## pre1 RR interval

# In[13]:


pre1_RR_interval= list()
for i in range(len(pre1_peaks)-1):
    #RR interval 구하기 10초에 2000개 data, 1초 기준으로 보려면 1/200 = 0.005 /단위 : ms, 따라서 *5
    k = (int(pre1_peaks[i+1])-int(pre1_peaks[i]))*5
    pre1_RR_interval.append(k) 
print("pre1_RR_interval",pre1_RR_interval)
plt.plot(pre1_RR_interval,"x") #x모형으로 점 출력 
plt.grid()


# ## pre1 interpolation

# In[14]:


pre1_result = list()
x1 = (len(pre1_RR_interval))-1 #데이터 간격
print("x1 : ", x1)
for i in range(30): #30개 data로 맞추기
    index = (x1/30)*i #점이 찍힐 위치 
    y1 = pre1_RR_interval[int(index)]+ ((pre1_RR_interval[int(index)+1]-pre1_RR_interval[int(index)])*(index-int(index))) #이전 위치 + 거리*비율
    pre1_result.append(y1)
print(pre1_result)
plt.plot(pre1_result,'x')
plt.grid()


# # Post1
# 
# ## post1 피크 값

# In[15]:


post1_peaks, _ = find_peaks(subset2,height=200)
print("post1_peaks",post1_peaks)
plt.plot(subset2)
plt.plot(post1_peaks,subset2[post1_peaks],"x")


# ## post1 RR interval

# In[16]:


post1_RR_interval= list()
for i in range(len(post1_peaks)-1):
    k = (int(post1_peaks[i+1])-int(post1_peaks[i]))*5
    post1_RR_interval.append(k)
print("post1_RR_interval",post1_RR_interval)
plt.plot(post1_RR_interval,"x")
plt.grid()


# ## post1 interpolation

# In[17]:


post1_result = list()
x2 = (len(post1_RR_interval))-1 #데이터 간격
for i in range(30):
    index = (x2/30)*i
    y1 = post1_RR_interval[int(index)]+ ((post1_RR_interval[int(index)+1]-post1_RR_interval[int(index)])*(index-int(index)))
    post1_result.append(y1)

print(post1_result)
plt.plot(post1_result,'x')
plt.grid()


# ## under 30s

# In[18]:


under_30s = pre1_result + post1_result
x_range = range(-30,30) #under 30s
plt.plot(x_range,under_30s,'x')
plt.grid()


# # pre2
# 
# ## pre2 피크 값

# In[19]:


pre2_peaks, _ = find_peaks(subset3,height=200)
print("pre2_peaks",pre2_peaks)
plt.plot(subset3)
plt.plot(pre2_peaks,subset3[pre2_peaks],"x")


# ## pre2 RR insterval

# In[20]:


pre2_RR_interval= list()
for i in range(len(pre2_peaks)-1):
    k = (int(pre2_peaks[i+1])-int(pre2_peaks[i]))*5
    pre2_RR_interval.append(k)
print("pre2_RR_interval",pre2_RR_interval)
plt.plot(pre2_RR_interval,"x")
plt.grid()


# ## pre2 interpolation

# In[21]:


print(pre2_RR_interval)
pre2_result = list()
x3 = (len(pre2_RR_interval))-1 #데이터 간격
for i in range(30):
    index = (x3/30)*i
    y1 = pre2_RR_interval[int(index)]+ ((pre2_RR_interval[int(index)+1]-pre2_RR_interval[int(index)])*(index-int(index)))
    pre2_result.append(y1)

print(pre2_result)
plt.plot(pre2_result,'x')
plt.grid()


# # post2
# 
# 
# ## post2 피크 값

# In[22]:


post2_peaks, _ = find_peaks(subset4,height=200)
print("post2_peaks",post2_peaks)
plt.plot(subset4)
plt.plot(post2_peaks,subset4[post2_peaks],"x")


# ## post2 RR interval

# In[23]:


post2_RR_interval= list()
for i in range(len(post2_peaks)-1):
    k = (int(post2_peaks[i+1])-int(post2_peaks[i]))*5
    post2_RR_interval.append(k)
print("post2_RR_interval",post2_RR_interval)
plt.plot(post2_RR_interval,"x")
plt.grid()


# ## post2 interpolation

# In[24]:


print(post2_RR_interval)
post2_result = list()
x4 = (len(post2_RR_interval))-1 #데이터 간격
for i in range(30):
    index = (x4/30)*i
    y1 = post2_RR_interval[int(index)]+ ((post2_RR_interval[int(index)+1]-post2_RR_interval[int(index)])*(index-int(index)))
    post2_result.append(y1)

print(post2_result)
plt.plot(post2_result,'x')
plt.grid()


# ## over 30s

# In[26]:


over_30s = pre2_result + post2_result

plt.plot(x_range,over_30s,"x")
plt.grid()


# In[ ]:





# In[ ]:




