# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:56:16 2020

@author: guillaume
"""
# -*-coding:Latin-1 -*
from bd_eos import bd_eos
import glob
import pandas as pd 

for f in glob.glob('/roddy/storage1/gault/LoggerData/Flux_AmeriFluxFormat/2020/02/*.dat'):   
    print(f)  
    #f = 'Flux_AmeriFluxFormat_01_06_2020.dat'
    cols = {"TIMESTAMP","FC", "LE", "ET", "H",                         
                        "G", "SG", "FETCH_MAX", "WD",
                        "WS", "PA", "SWC_1_1_1", "TS_1_1_1",
                        "TS_2_1_1", "ALB", "NETRAD", "SW_IN",
                        "SW_OUT", "LW_IN", "LW_OUT"}    
    Flux_Data = pd.read_csv(f, sep=",", skiprows=[0,2,3], usecols=lambda x: x in cols)    
    
    Flux_Data = Flux_Data.set_index('TIMESTAMP')
    Flux_Data.index = pd.to_datetime(Flux_Data.index)
    
    for i in range (0,len(Flux_Data)-1): 
            
            queryReleveMeteo = ("INSERT IGNORE INTO gault_fluxdata \
                               (date,\
                                FC, \
                                LE, \
                                ET, \
                                H, \
                                G, \
                                SG, \
                                FETCH_MAX, \
                                WD, \
                                WS, \
                                PA, \
                                SWC_1_1_1, \
                                TS_1_1_1, \
                                TS_2_1_1, \
                                ALB, \
                                NETRAD, \
                                SW_IN, \
                                SW_OUT, \
                                LW_IN, \
                                LW_OUT) VALUES('"+Flux_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                            "','"+str(Flux_Data.iloc[-i,0])+"','"+
                            str(Flux_Data.iloc[-i,1])+"','"+
                            str(Flux_Data.iloc[-i,2])+"','"+
                            str(Flux_Data.iloc[-i,3])+"','"+
                            str(Flux_Data.iloc[-i,4])+"','"+
                            str(Flux_Data.iloc[-i,5])+"','"+
                            str(Flux_Data.iloc[-i,6])+"','"+                           
                            str(Flux_Data.iloc[-i,7])+"','"+
                            str(Flux_Data.iloc[-i,8])+"','"+
                            str(Flux_Data.iloc[-i,9])+"','"+
                            str(Flux_Data.iloc[-i,10])+"','"+
                            str(Flux_Data.iloc[-i,11])+"','"+
                            str(Flux_Data.iloc[-i,12])+"','"+                        
                            str(Flux_Data.iloc[-i,13])+"','"+
                            str(Flux_Data.iloc[-i,14])+"','"+
                            str(Flux_Data.iloc[-i,15])+"','"+
                            str(Flux_Data.iloc[-i,16])+"','"+
                            str(Flux_Data.iloc[-i,17])+"','"+
                            str(Flux_Data.iloc[-i,18])+"') ON DUPLICATE KEY UPDATE \
                            FC = VALUES(FC), \
                            LE = VALUES(LE),\
                            ET = VALUES(ET), \
                            H  = VALUES(H), \
                            G  = VALUES(G), \
                            SG = VALUES(SG), \
                            FETCH_MAX = VALUES(FETCH_MAX), \
                            WD = VALUES(WD), \
                            WS = VALUES(WS),\
                            PA = VALUES(PA), \
                            SWC_1_1_1  = VALUES(SWC_1_1_1), \
                            TS_1_1_1  = VALUES(TS_1_1_1), \
                            TS_2_1_1 = VALUES(TS_2_1_1), \
                            ALB = VALUES(ALB), \
                            NETRAD  = VALUES(NETRAD), \
                            SW_IN  = VALUES(SW_IN), \
                            SW_OUT = VALUES(SW_OUT), \
                            LW_IN = VALUES(LW_IN), \
                            LW_OUT = VALUES(LW_OUT)")      
            print(queryReleveMeteo)
            bd_eos(queryReleveMeteo)
         
