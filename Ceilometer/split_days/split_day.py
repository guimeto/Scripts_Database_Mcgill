import pandas as pd
import datetime
import csv
from datetime import datetime,  timedelta


file1 = "/storage1/gault/CS135/CS135_01_22_2020-01_25_2020.dat"
days_to_select = ['22','23','24','25']

fichierIn = open(file1,"r", encoding='cp437') 
appended_data = []
for ligne in  fichierIn: 
    appended_data.append(ligne.split(",")) 
        
df = pd.DataFrame(appended_data) 
df[2].fillna(value='', inplace=True)
df = df.set_index(0)
df.index = pd.to_datetime(df.index, format='"%Y-%m-%d %I:%M:%S %p"')    

for day in days_to_select:
    tmp = df['2020-01-'+day]
    tmp.index =  tmp.index.strftime('"%Y-%m-%d %I:%M:%S %p"')
    tmp = tmp.drop(tmp.columns[1], axis=1)
    tmp.to_csv(tmp.to_csv('CS135_01_'+str("%(num)02d" % {"num":int(day)})+'_2020_new.dat', header=False, sep = ',', quoting = csv.QUOTE_NONE, escapechar = ' '))
