# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:25:23 2020

@author: guillaume
"""
# -*- coding: utf-8 -*-

from bd_eos import bd_eos
import glob
import pandas as pd 

for f in glob.glob('/roddy/storage1/gault/LoggerData/TPS_3100_Data/2020/05/*.dat'):   
    print(f)
    f = 'SDMS40_Data_01_28_2020.dat'
    # ajout de TPS_Baro_Press_mbar_Corrected le 5 mai 2020
    cols = {"TIMESTAMP","SDMS40_Depth_Avg"}   
    
    CR6Series_SDMS40_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    CR6Series_SDMS40_Data = CR6Series_SDMS40_Data.set_index('TIMESTAMP')
    CR6Series_SDMS40_Data.index = pd.to_datetime(CR6Series_SDMS40_Data.index)
      
    for i in range (0,len(CR6Series_SDMS40_Data)-1): 
        
        queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata \
                           (date,\
                            SDMS40_Depth_Avg) VALUES('"+CR6Series_SDMS40_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                        "','"+str(CR6Series_SDMS40_Data.iloc[-i,0])+"') ON DUPLICATE KEY UPDATE \
                        SDMS40_Depth_Avg = VALUES(SDMS40_Depth_Avg)")  
        print(queryReleveMeteo)
        bd_eos(queryReleveMeteo)
  
