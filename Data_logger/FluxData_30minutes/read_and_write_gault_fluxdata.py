# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:56:16 2020

@author: guillaume
"""
# -*-coding:Latin-1 -*
from bd_eos import bd_eos
from read_CR6Series_Flux_AmeriFluxFormat_Data import read_CR6Series_Flux_AmeriFluxFormat_Data
        
### Path to read gault_transit data 
#Flux_Data = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_Flux_AmeriFluxFormat.dat' 
#FFlux_Data = '/roddy/storage1/gault_transit/CR6Series_Flux_AmeriFluxFormat.dat' 
Flux_Data = '/roddy/storage1/gault_transit/CR6Series_Flux_AmeriFluxFormat.dat'
### read useful data
Flux_Data = read_CR6Series_Flux_AmeriFluxFormat_Data(Flux_Data)  



queryReleveMeteo = ("INSERT INTO gault_fluxdata (date,"
                        "FC, LE, ET, H,"                         
                        "G, SG, FETCH_MAX, WD,"
                        "WS, PA, SWC_1_1_1, TS_1_1_1,"
                        "TS_2_1_1, ALB, NETRAD, SW_IN,"
                        "SW_OUT, LW_IN, LW_OUT)" 
                     
                    "VALUES('"+Flux_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-1]+
                    "','"+str(Flux_Data.iloc[-1,0])+"','"+str(Flux_Data.iloc[-1,1])+"','"+str(Flux_Data.iloc[-1,2])+"','"+str(Flux_Data.iloc[-1,3])+
                    "','"+str(Flux_Data.iloc[-1,4])+"','"+str(Flux_Data.iloc[-1,5])+"','"+str(Flux_Data.iloc[-1,6])+"','"+str(Flux_Data.iloc[-1,7])+                    
                    "','"+str(Flux_Data.iloc[-1,8])+"','"+str(Flux_Data.iloc[-1,9])+"','"+str(Flux_Data.iloc[-1,10])+"','"+str(Flux_Data.iloc[-1,11])+                   
                    "','"+str(Flux_Data.iloc[-1,12])+"','"+str(Flux_Data.iloc[-1,13])+"','"+str(Flux_Data.iloc[-1,14])+"','"+str(Flux_Data.iloc[-1,15])+                    
                    "','"+str(Flux_Data.iloc[-1,16])+"','"+str(Flux_Data.iloc[-1,17])+"','"+str(Flux_Data.iloc[-1,18])+
                    "')")


print(queryReleveMeteo)
bd_eos(queryReleveMeteo)


