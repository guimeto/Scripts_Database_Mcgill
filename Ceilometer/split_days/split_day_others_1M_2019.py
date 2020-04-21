# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:45:58 2020

@author: guillaume
"""

import pandas as pd
import datetime
import csv
from datetime import datetime,  timedelta


file1 = "/storage1/gault/CS135/2019/CS135_11_15_2019-11_18_2019.txt"

fichierIn = open(file1,"r", encoding='cp437') 
appended_data = []
for ligne in  fichierIn: 
    appended_data.append(ligne.split(",")) 
        
df = pd.DataFrame(appended_data) 

for  index, row in df.iterrows():
    try:
        df.loc[index][0] = pd.to_datetime(row[0], format='"%Y-%m-%d %I:%M:%S %p"')
    except:
        df.drop(index, inplace=True)
    
    
df.index = pd.to_datetime(df.index, format='%Y-%m-%d %H:%M:%S')  

df = df.set_index(0)

df_2019_11 = df['2019-11']

for day in df_2019_11.index.day.unique().tolist():
    tmp = df['2019-11-'+str(day)]
    tmp.index =  tmp.index.strftime('"%Y-%m-%d %I:%M:%S %p"')
    tmp.to_csv(tmp.to_csv('/storage1/gault/CS135/2019/CS135_11_'+str("%(num)02d" % {"num":int(day)})+'_2019_new.dat', header=False, sep = ',', quoting = csv.QUOTE_NONE, escapechar = ' '))
