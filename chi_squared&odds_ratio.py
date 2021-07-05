# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:07:33 2021

@author: eunho
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n2_under = 10
n2_over = 16
n3_under = 20
n3_over = 17
r_under = 30
r_over = 14

import pandas as pd

#dataframe 만들기
idx = ['30s 이하', '30s 이상']
data = {'N2' : [n2_under, n2_over], "N3" : [n3_under, n3_over], "REM" : [r_under, r_over]}
sub = pd.DataFrame(data, index = idx)
print(sub)
#print(sub['N2'].sum())

#sub.loc['Total'] = (sub['N2'].sum() , sub['N3'].sum(), sub["REM"].sum())
#sub['Total'] = sub.apply(lambda row : sum([row['N2'], row['N3'], row['REM']]), axis =1)
#print(sub, "\n\n")

#N2 - N3 dataframe
s1 = sub[['N2', 'N3']]
print(s1)

#N2 - REM dataframe
s2 = sub[['N2', 'REM']]

#N3 - REM dataframe
s3 = sub[['N3', "REM"]]

#카이제곱검정
import scipy.stats

#chi2 = 검정 통계량, p = P_Value, dof = 자유도
chi2_1, p_1, dof_1, expected_1 = scipy.stats.chi2_contingency(s1)
chi2_2, p_2, dof_2, expected_2 = scipy.stats.chi2_contingency(s2)
chi2_3, p_3, dof_3, expected_3 = scipy.stats.chi2_contingency(s3)


#기대 값 : 무조건 0이상 & 가능한 5이상
print(expected_1, "\n")
print(expected_2, "\n")
print(expected_3, "\n")

print("N2와 N3 사이 카이제곱 값 : " ,chi2_1, "\n")
print("N2와 REM 사이 카이제곱 값 : " ,chi2_2, "\n")
print("N3와 REM 사이 카이제곱 값 : " ,chi2_3, "\n")

print("N2와 N3 사이 P값 : " ,p_1, "\n")
print("N2와 REM 사이 P값 : " ,p_2, "\n")
print("N3와 REM 사이 P값 : " ,p_3, "\n")

import numpy as np

r = np.array(s1.values.tolist())

print(r)

#N2 - N3 odds ratio

oR = r[0,0]*r[1,1]/r[0,1]*r[1,0]
log_OR = np.log(oR)

print(np.reciprocal(r))
se = np.sqrt(1/r[0,0]+1/r[1,0]+1/r[0,1]+1/r[1,1])

min_or = log_OR - 1.96*se
max_or = log_OR + 1.96*se

print(min_or , " ~ ", max_or)

