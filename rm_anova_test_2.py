import matplotlib.font_manager as fm
font_path = 'C:/Windows/Fonts/gulim.ttc' #굴림폰트 사용

fontprop20=fm.FontProperties(fname=font_path,size=20)
fontprop14=fm.FontProperties(fname=font_path,size=14)
import warnings
warnings.filterwarnings('ignore') #실행시 경고문 무시

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.special import erf

#파일 경로 및 이름 지정
fdir=r"D:/한림대학교/연구실//" 
fn1="2021-06-23 (19-56-56)-HRV_for_anova.csv"  # 
test_fileList=fdir+fn1


col_list=["Id","NAME","LnHF","R_value","MemoCom","LnLF"] # column lists of excel file
cols=col_list[3]   # <- target data = R_value (LF/HF = 교감/부교감)
ID=col_list[0] # <- ID provides extracted information

subset=pd.read_csv(test_fileList,usecols=col_list) #csv파일 중에서 col_list해당만 로드

#30초 미만 pre
subset1=subset[subset["MemoCom"].str.contains('pre', case=False) & subset["MemoCom"].str.contains('30s미만',case=False)]
#30초미만 pos
subset2=subset[subset["MemoCom"].str.contains('pos', case=False) & subset["MemoCom"].str.contains('30s미만',case=False)]
#30초 이상 pre
subset3=subset[subset["MemoCom"].str.contains('pre', case=False) & subset["MemoCom"].str.contains('30s이상',case=False)]
#30초 이상 pos
subset4=subset[subset["MemoCom"].str.contains('pos', case=False) & subset["MemoCom"].str.contains('30s이상',case=False)]

#dataframe 정렬위한 준비
s1=list()
for i in range(len(subset1)):
    s1.append('pre1')
    
s2=list()
for i in range(len(subset2)):
    s2.append('post1')
s3=list()
for i in range(len(subset3)):
    s3.append('pre2')
s4=list()
for i in range(len(subset4)):
    s4.append('post2')
    
    
under30_1=list()
for i in range(len(subset1)):
    under30_1.append('Under 30 s')
under30_2=list()
for i in range(len(subset2)):
    under30_2.append('Under 30 s')
over30_3=list()
for i in range(len(subset3)):
    over30_3.append('Over 30 s')
over30_4=list()
for i in range(len(subset4)):
    over30_4.append('Over 30 s')

g1=list()
for i in range(len(subset1)):
    g1.append('pre')
g2=list()
for i in range(len(subset2)):
    g2.append('post')
g3=list()
for i in range(len(subset3)):
    g3.append('pre')
g4=list()
for i in range(len(subset4)):
    g4.append('post')
    
#data frame 정렬
sub1=pd.DataFrame({ID:subset1[ID].values, cols:subset1[cols].values, "Position":s1, "Group":g1,"Duration":under30_1})
sub2=pd.DataFrame({ID:subset1[ID].values, cols:subset2[cols].values, "Position":s2, "Group":g2,"Duration":under30_2})
sub3=pd.DataFrame({ID:subset1[ID].values, cols:subset3[cols].values, "Position":s3, "Group":g3,"Duration":over30_3})
sub4=pd.DataFrame({ID:subset1[ID].values, cols:subset4[cols].values, "Position":s4, "Group":g4,"Duration":over30_4})



#각 경우의 수의 data frame 병합
dataAdd = sub1.append([sub2,sub3,sub4],ignore_index=True)

import statsmodels.api as sm
from statsmodels.formula.api import ols

model_1 = ols('R_value ~ C(Duration) + C(Group) + C(Duration):C(Group)',dataAdd).fit()
anova_table = sm.stats.anova_lm(model_1)
print(cols)
print(anova_table,'\n')




import pingouin as pg
aov =pg.rm_anova(dv = "R_value", within=['Duration', 'Group'], subject = "Id", data = dataAdd)

print(aov, '\n')



from statsmodels.stats.anova import AnovaRM

anoc_2 = AnovaRM(dataAdd, 'R_value', 'Id', within = ['Duration', 'Group'])
res_2way = anoc_2.fit()


print(res_2way.anova_table)
