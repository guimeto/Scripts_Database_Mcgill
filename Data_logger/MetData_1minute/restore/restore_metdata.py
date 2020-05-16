# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:56:16 2020

@author: guillaume
"""
# -*-coding:Latin-1 -*
from bd_eos import bd_eos
import glob
import pandas as pd 

for f in glob.glob('/roddy/storage1/gault/LoggerData/Met_Data/2020/01/*.dat'):   
    print(f)  
#    f = 'Met_Data_05_07_2020.dat'
    cols = {"TIMESTAMP","LWMDry_Tot","LWMCon_Tot", "LWMWet_Tot", "WS_ms", "Mean_WindDir", 
                 "WindDir_SD",  "WS_ms_Max", "WindDir_Max", "CMP10_Solar_uWm2_Avg",
                 "Temp1_Avg", "Temp2_Avg", "Temp3_Avg", "Temp4_Avg", "Temp5_Avg", "Temp6_Avg", "Temp7_Avg", 
                 "Temp8_Avg", "RH1", "RH2", "RH3", "RH4", "RH5", "RH6", "RH7", "RH8"}    
    Met_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    Met_Data = Met_Data.set_index('TIMESTAMP')
    Met_Data.index = pd.to_datetime(Met_Data.index)
    
    try:
   
        for i in range (0,len(Met_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata (date,"
                                "LWMDry_Tot, LWMCon_Tot, LWMWet_Tot, WS_ms, Mean_WindDir, WindDir_SD,  WS_ms_Max, WindDir_Max, CMP10_Solar_uWm2_Avg,"
                                "Temp1_Avg, Temp2_Avg, Temp3_Avg, Temp4_Avg, Temp5_Avg, Temp6_Avg, Temp7_Avg, Temp8_Avg,"
                                "RH1, RH2, RH3, RH4, RH5, RH6, RH7, RH8)"   
                       
                            "VALUES('"+Met_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(Met_Data.iloc[-i,0])+"','"+str(Met_Data.iloc[-i,1])+"','"+str(Met_Data.iloc[-i,2])+"','"+str(Met_Data.iloc[-i,3])+"','"+str(Met_Data.iloc[-i,4])+"','"+str(Met_Data.iloc[-i,5])+"','"+str(Met_Data.iloc[-i,6])+"','"+str(Met_Data.iloc[-i,7])+"','"+str(Met_Data.iloc[-i,8])+
                            "','"+str(Met_Data.iloc[-i,9])+"','"+str(Met_Data.iloc[-i,10])+"','"+str(Met_Data.iloc[-i,11])+"','"+str(Met_Data.iloc[-i,12])+"','"+str(Met_Data.iloc[-i,13])+"','"+str(Met_Data.iloc[-i,14])+"','"+str(Met_Data.iloc[-i,15])+"','"+str(Met_Data.iloc[-i,16])+
                            "','"+str(Met_Data.iloc[-i,17])+"','"+str(Met_Data.iloc[-i,18])+"','"+str(Met_Data.iloc[-i,19])+"','"+str(Met_Data.iloc[-i,20])+"','"+str(Met_Data.iloc[-i,21])+"','"+str(Met_Data.iloc[-i,22])+"','"+str(Met_Data.iloc[-i,23])+"','"+str(Met_Data.iloc[-i,24])+
    
                            "')")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo)
            
    # pas de ['WindDir_Max', 'WS_ms_Max']        
    except: 
 
        for i in range (0,len(Met_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_metdata (date,"
                                "LWMDry_Tot, LWMCon_Tot, LWMWet_Tot, WS_ms, Mean_WindDir, WindDir_SD, CMP10_Solar_uWm2_Avg,"
                                "Temp1_Avg, Temp2_Avg, Temp3_Avg, Temp4_Avg, Temp5_Avg, Temp6_Avg, Temp7_Avg, Temp8_Avg,"
                                "RH1, RH2, RH3, RH4, RH5, RH6, RH7, RH8)"   
                       
                            "VALUES('"+Met_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(Met_Data.iloc[-i,0])+"','"+str(Met_Data.iloc[-i,1])+"','"+str(Met_Data.iloc[-i,2])+"','"+str(Met_Data.iloc[-i,3])+"','"+str(Met_Data.iloc[-i,4])+"','"+str(Met_Data.iloc[-i,5])+"','"+str(Met_Data.iloc[-i,6])+
                            "','"+str(Met_Data.iloc[-i,7])+"','"+str(Met_Data.iloc[-i,8])+"','"+str(Met_Data.iloc[-i,9])+"','"+str(Met_Data.iloc[-i,10])+"','"+str(Met_Data.iloc[-i,11])+"','"+str(Met_Data.iloc[-i,12])+"','"+str(Met_Data.iloc[-i,13])+"','"+str(Met_Data.iloc[-i,14])+
                            "','"+str(Met_Data.iloc[-i,15])+"','"+str(Met_Data.iloc[-i,16])+"','"+str(Met_Data.iloc[-i,17])+"','"+str(Met_Data.iloc[-i,18])+"','"+str(Met_Data.iloc[-i,19])+"','"+str(Met_Data.iloc[-i,20])+"','"+str(Met_Data.iloc[-i,21])+"','"+str(Met_Data.iloc[-i,22])+
    
                            "')")
        
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo) 
         
