# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:50:41 2020

@author: guillaume
"""
# -*- coding: utf-8 -*-

from bd_eos import bd_eos
import glob
import pandas as pd 

for f in glob.glob('/roddy/storage1/gault/LoggerData/TPS_3100_Data/2020/05/*.dat'):   
    print(f)
    f = 'SR50A_Data_02_01_2020.dat'
    # ajout de TPS_Baro_Press_mbar_Corrected le 5 mai 2020
    cols = {"TIMESTAMP","SR50A_SnowDepth","SR50A_QualityVal"}   
    
    CR6Series_SR50A_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    CR6Series_SR50A_Data = CR6Series_SR50A_Data.set_index('TIMESTAMP')
    CR6Series_SR50A_Data.index = pd.to_datetime(CR6Series_SR50A_Data.index)
      
    for i in range (0,len(CR6Series_SR50A_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata \
                               (date,\
                                SR50A_SnowDepth, \
                                SR50A_QualityVal) VALUES('"+CR6Series_SR50A_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(CR6Series_SR50A_Data.iloc[-i,0])+"','"+
                            str(CR6Series_SR50A_Data.iloc[-i,1])+"') ON DUPLICATE KEY UPDATE \
                            SR50A_SnowDepth = VALUES(SR50A_SnowDepth), \
                            SR50A_QualityVal   = VALUES(SR50A_QualityVal)")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo)
  