# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:02:20 2021

@author: pixee
"""

#Risk ratio
n2_under = [0,0,0,0,1,1,0,0,1, 1]
n2_over = [1,1,1,0,0,1,1,0,1,0]
n3_under = [1,1,1,1,0,0,1,1,0,0]
n3_over = [0,1,0,0,0,1,1,0,0,1]
r_under = [1,1,1,0,0,0,0,0,0,1]
r_over = [0,1,1,0,0,0,1,0,1,0]

import pandas as pd

df = pd.DataFrame()
df['n2_under'] = [0,0,0,0,1,1,0,0,1, 1]
df['n2_over'] =  [1,1,1,0,0,1,1,0,1,0]

from zepid import RiskRatio

rr = RiskRatio()
rr.fit(df, exposure = "n2_under", outcome = "n2_over")

print(rr.results)
