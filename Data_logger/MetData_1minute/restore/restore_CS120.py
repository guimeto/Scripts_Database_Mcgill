# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:50:41 2020

@author: guillaume
"""
# -*- coding: utf-8 -*-

from bd_eos import bd_eos
import glob
import pandas as pd 

for f in glob.glob('/roddy/storage1/gault/LoggerData/CS120A_Data/2020/05/*.dat'):   
    print(f)
    #f = 'CS120A_Data_02_01_2020.dat'
    cols = {"TIMESTAMP","Visibilitystr"}   
    
    CS120_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    CS120_Data = CS120_Data.set_index('TIMESTAMP')
    CS120_Data.index = pd.to_datetime(CS120_Data.index)
      
    for i in range (0,len(CS120_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata \
                               (date,\
                                Visibilitystr) VALUES('"+CS120_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(CS120_Data.iloc[-i,0])+"') ON DUPLICATE KEY UPDATE \
                            Visibilitystr = VALUES(Visibilitystr)")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo)
  