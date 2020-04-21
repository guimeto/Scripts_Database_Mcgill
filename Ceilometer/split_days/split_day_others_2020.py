# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:45:58 2020

@author: guillaume
"""

import pandas as pd
import datetime
import csv
from datetime import datetime,  timedelta


file1 = "/storage1/gault/CS135/CS13501_31_2020-02_01-2020.dat"

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

df_2020_01 = df['2020-01']
df_2020_02 = df['2020-02']

for day in df_2020_01.index.day.unique().tolist():
    tmp = df['2020-01-'+str(day)]
    tmp.index =  tmp.index.strftime('"%Y-%m-%d %I:%M:%S %p"')
    tmp.to_csv(tmp.to_csv('/storage1/gault/CS135/CS135_01_'+str("%(num)02d" % {"num":int(day)})+'_2020_new2.dat', header=False, sep = ',', quoting = csv.QUOTE_NONE, escapechar = ' '))




for day in df_2020_02.index.day.unique().tolist():
    tmp = df['2020-02-'+str(day)]
    tmp.index =  tmp.index.strftime('"%Y-%m-%d %I:%M:%S %p"')
    tmp.to_csv(tmp.to_csv('/storage1/gault/CS135/CS135_02_'+str("%(num)02d" % {"num":int(day)})+'_2020_new2.dat', header=False, sep = ',', quoting = csv.QUOTE_NONE, escapechar = ' '))
