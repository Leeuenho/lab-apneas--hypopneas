# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:00:54 2021

@author: eunho
"""
import warnings
warnings.filterwarnings('ignore')

import pandas as pd

#파일 이름 및 경로
fdir = 'D:/한림대학교/연구실/git_lab//'
fn = '2021-06-28 (12-36-47)-HRV_10samples.csv'

file = fdir + fn

#필요 data 정리
col_list=["Id","NAME","LnHF","LnLF", "R_value","MemoCom"] 
col_HF = col_list[2]
col_LF = col_list[3]
col_R = col_list[4]

col_ID = col_list[0]

#필요 data만 file에서 추출
subjects = pd.read_csv(file, usecols = col_list)

#30초 미만 pre
#case = 대소문자 구분
subject1 = subjects[subjects["MemoCom"].str.contains('pre', case=False) & subjects['MemoCom'].str.contains('30s미만', case = False)]

#30초 미만 post
subject2 = subjects[subjects["MemoCom"].str.contains('pos', case=False) & subjects['MemoCom'].str.contains('30s미만', case = False)]

#30초 이상 pre
subject3 = subjects[subjects["MemoCom"].str.contains('pre', case=False) & subjects['MemoCom'].str.contains('30s이상', case = False)]

#30초 이상 post
subject4 = subjects[subjects["MemoCom"].str.contains('pos', case=False) & subjects['MemoCom'].str.contains('30s이상', case = False)]

s1=list()
for i in range(len(subject1)):
    s1.append('pre1')
    
s2=list()
for i in range(len(subject2)):
    s2.append('post1')
s3=list()
for i in range(len(subject3)):
    s3.append('pre2')
s4=list()
for i in range(len(subject4)):
    s4.append('post2')
    
    
under30_1=list()
for i in range(len(subject1)):
    under30_1.append('Under 30 s')
under30_2=list()
for i in range(len(subject2)):
    under30_2.append('Under 30 s')
over30_3=list()
for i in range(len(subject3)):
    over30_3.append('Over 30 s')
over30_4=list()
for i in range(len(subject4)):
    over30_4.append('Over 30 s')

g1=list()
for i in range(len(subject1)):
    g1.append('pre')
g2=list()
for i in range(len(subject2)):
    g2.append('post')
g3=list()
for i in range(len(subject3)):
    g3.append('pre')
g4=list()
for i in range(len(subject4)):
    g4.append('post')
    

s_1 = pd.DataFrame({col_ID:subject1[col_ID].values, col_HF:subject1[col_HF].values, col_LF:subject1[col_LF].values, col_R:subject1[col_R].values, "Group":g1, "Duration" : under30_1})
s_2 = pd.DataFrame({col_ID:subject2[col_ID].values, col_HF:subject2[col_HF].values, col_LF:subject2[col_LF].values, col_R:subject2[col_R].values, "Group":g2, "Duration" : under30_2})
s_3 = pd.DataFrame({col_ID:subject3[col_ID].values, col_HF:subject3[col_HF].values, col_LF:subject3[col_LF].values, col_R:subject3[col_R].values, "Group":g3, "Duration" : over30_3})
s_4 = pd.DataFrame({col_ID:subject4[col_ID].values, col_HF:subject4[col_HF].values, col_LF:subject4[col_LF].values, col_R:subject4[col_R].values, "Group":g4, "Duration" : over30_4})

dataAdd = s_1.append([s_2, s_3, s_4], ignore_index = True)

import pingouin as pg
from statsmodels.stats.anova import AnovaRM

#LF : 교감신경
av1_LF = AnovaRM(dataAdd, 'LnLF', 'Id', within=['Duration', 'Group'])
res1_LF = av1_LF.fit()
print(res1_LF)

#LF : 교감신경
av_LF = pg.rm_anova(dv = "LnLF", within=['Duration', 'Group'], subject='Id', data = dataAdd)
print(av_LF)

#HF : 부교감신경
av_HF = pg.rm_anova(dv = "LnHF", within=['Duration', 'Group'], subject='Id', data = dataAdd)
print(av_HF)

#LF : 교감신경
av_R = pg.rm_anova(dv = "R_value", within=['Duration', 'Group'], subject='Id', data = dataAdd)
print(av_R)