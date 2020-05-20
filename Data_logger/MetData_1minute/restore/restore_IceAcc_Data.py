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
    #f = 'IceAcc_Data_01_31_2020.dat'
    # ajout de TPS_Baro_Press_mbar_Corrected le 5 mai 2020
    cols = {"TIMESTAMP","LF1_Ice_Output", "Ice_Inch", "Ice_mm"}   
    
    IceAcc_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    IceAcc_Data = IceAcc_Data.set_index('TIMESTAMP')
    IceAcc_Data.index = pd.to_datetime(IceAcc_Data.index)
      
    for i in range (0,len(IceAcc_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata \
                               (date,\
                                LF1_Ice_Output, \
                                Ice_Inch, \
                                Ice_mm) VALUES('"+IceAcc_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(IceAcc_Data.iloc[-i,0])+"','"+
                            str(IceAcc_Data.iloc[-i,1])+"','"+
                            str(IceAcc_Data.iloc[-i,2])+"') ON DUPLICATE KEY UPDATE \
                            LF1_Ice_Output = VALUES(LF1_Ice_Output), \
                            Ice_Inch   = VALUES(Ice_Inch),\
                            Ice_mm      = VALUES(Ice_mm)")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo)
  