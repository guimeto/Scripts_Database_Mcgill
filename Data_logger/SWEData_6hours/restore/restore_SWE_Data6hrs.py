# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:50:41 2020

@author: guillaume
"""
# -*- coding: utf-8 -*-

from bd_eos import bd_eos
import glob
import pandas as pd 

for f in glob.glob('/roddy/storage1/gault/LoggerData/CS725_6Hour/2020/05/*.dat'):   
    print(f)
    #f = 'CS725_6Hour_01_07_2020.dat'

    cols = {"TIMESTAMP","CS725_SWE_K", "CS725_SWE_TL"}   
    
    swe_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    swe_Data = swe_Data.set_index('TIMESTAMP')
    swe_Data.index = pd.to_datetime(swe_Data.index)
      
    for i in range (0,len(swe_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_swe_6h \
                               (date,\
                                CS725_SWE_K, \
                                CS725_SWE_TL) VALUES('"+swe_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(swe_Data.iloc[-i,0])+"','"+
                            str(swe_Data.iloc[-i,1])+"') ON DUPLICATE KEY UPDATE \
                            CS725_SWE_K = VALUES(CS725_SWE_K), \
                            CS725_SWE_TL   = VALUES(CS725_SWE_TL)")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo)
  