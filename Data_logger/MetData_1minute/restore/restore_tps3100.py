# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:46:44 2020

@author: guillaume
"""
# -*-coding:Latin-1 -*
from bd_eos import bd_eos
import glob
import pandas as pd 

for f in glob.glob('/storage1/gault/LoggerData/TPS_3100_Data/2020/01/*.dat'):   
    print(f)  
    # f = './restore/TPS_3100_Data_02_28_2020.dat' 
    
    cols = {"TIMESTAMP","TPS_Raw_Precip_Rate_1minAvg_mmHr","TPS_Raw_Precip_Rate_5minAvg_mmHr", "TPS_Wind_Spd_ms", "TPS_Air_Temp_C", "TPS_Total_Accum_mm", 
                 "TPS_Pwr_Sensor_W",  "TPS_Pwr_Ref_W", "TPS_Baro_Press_mbar_Corrected"}   
    
    TPS_3100_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    TPS_3100_Data = TPS_3100_Data.set_index('TIMESTAMP')
    TPS_3100_Data.index = pd.to_datetime(TPS_3100_Data.index)
    
    try:
   
        for i in range (0,len(TPS_3100_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata (date,"
                                "TPS_Total_Accum_mm, TPS_Pwr_Sensor_W, TPS_Pwr_Ref_W, TPS_Wind_Spd_ms, TPS_Raw_Precip_Rate_1minAvg_mmHr, TPS_Raw_Precip_Rate_5minAvg_mmHr, TPS_Air_Temp_C,TPS_Baro_Press_mbar_Corrected)"    
                       
                            "VALUES('"+TPS_3100_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(TPS_3100_Data.iloc[-i,1])+"','"+str(TPS_3100_Data.iloc[-i,2])+"','"+str(TPS_3100_Data.iloc[-i,3])+"','"+str(TPS_3100_Data.iloc[-i,4])+"','"+str(TPS_3100_Data.iloc[-i,5])+"','"+str(TPS_3100_Data.iloc[-i,6])+"','"+str(TPS_3100_Data.iloc[-i,7])+"','"+str(TPS_3100_Data.iloc[-i,0])+"')")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo)
            
    # pas de ['TPS_Baro_Press_mbar_Corrected', 'WS_ms_Max']        
    except: 
 
        for i in range (0,len(TPS_3100_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata (date,"
                                "TPS_Total_Accum_mm, TPS_Pwr_Sensor_W, TPS_Pwr_Ref_W, TPS_Wind_Spd_ms, TPS_Raw_Precip_Rate_1minAvg_mmHr, TPS_Raw_Precip_Rate_5minAvg_mmHr, TPS_Air_Temp_C)"  
                       
                            "VALUES('"+TPS_3100_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(TPS_3100_Data.iloc[-i,0])+"','"+str(TPS_3100_Data.iloc[-i,1])+"','"+str(TPS_3100_Data.iloc[-i,2])+"','"+str(TPS_3100_Data.iloc[-i,3])+"','"+str(TPS_3100_Data.iloc[-i,4])+"','"+str(TPS_3100_Data.iloc[-i,5])+"','"+str(TPS_3100_Data.iloc[-i,6])+"')")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo) 
         

