# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:56:16 2020

@author: guillaume
"""
# -*-coding:Latin-1 -*
from bd_eos import bd_eos
from read_CR6Series_Met_Data import read_CR6Series_Met_Data
from read_CR6Series_TPS_3100_Data import read_CR6Series_TPS_3100_Data
from read_CR6Series_SDMS40_Data import read_CR6Series_SDMS40_Data
from read_CR6Series_SR50A_Data import read_CR6Series_SR50A_Data
from read_CR6Series_IceAcc_Data import read_CR6Series_IceAcc_Data
from read_CR6Series_CS120A_Data import read_CR6Series_CS120A_Data

 
### Path to read gault_transit data 
Met_Data = '/roddy/storage1/gault_transit/CR6Series_Met_Data.dat' 
#Met_Data = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_Met_Data.dat'  
  
TPS_3100_Data = '/roddy/storage1/gault_transit/CR6Series_TPS_3100_Data.dat' 
#TPS_3100_Data = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_TPS_3100_Data.dat'

SDMS40_Data = '/roddy/storage1/gault_transit/CR6Series_SDMS40_Data.dat'
#SDMS40_Data = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_SDMS40_Data.dat'   

SR50A_Data = '/roddy/storage1/gault_transit/CR6Series_SR50A_Data.dat'
#SR50A_Data = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_SR50A_Data.dat'   

IceAcc_Data = '/roddy/storage1/gault_transit/CR6Series_IceAcc_Data.dat'   
#IceAcc_Data = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_IceAcc_Data.dat'   

CS120A_Data = '/roddy/storage1/gault_transit/CR6Series_CS120A_Data.dat'
#CS120A_Data = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_CS120A_Data.dat' 

### read useful data
Met_Data = read_CR6Series_Met_Data(Met_Data)  
TPS_3100_Data = read_CR6Series_TPS_3100_Data(TPS_3100_Data)  
SDMS40_Data = read_CR6Series_SDMS40_Data(SDMS40_Data)
SR50A_Data = read_CR6Series_SR50A_Data(SR50A_Data)
IceAcc_Data = read_CR6Series_IceAcc_Data(IceAcc_Data)
CS120A_Data = read_CR6Series_CS120A_Data(CS120A_Data)

for i in range(5,0,-1):
    queryReleveMeteo = ("INSERT INTO gault_metdata (date,"
                            "LWMDry_Tot, LWMCon_Tot, LWMWet_Tot, WS_ms, Mean_WindDir, WindDir_SD,  WS_ms_Max, WindDir_Max, CMP10_Solar_uWm2_Avg,"
                            "Temp1_Avg, Temp2_Avg, Temp3_Avg, Temp4_Avg, Temp5_Avg, Temp6_Avg, Temp7_Avg, Temp8_Avg,"
                            "RH1, RH2, RH3, RH4, RH5, RH6, RH7, RH8,"
                            "TPS_Total_Accum_mm, TPS_Pwr_Sensor_W, TPS_Pwr_Ref_W, TPS_Wind_Spd_ms, TPS_Raw_Precip_Rate_1minAvg_mmHr, TPS_Raw_Precip_Rate_5minAvg_mmHr, TPS_Air_Temp_C,"
                            "SDMS40_Depth_Avg,"
                            "SR50A_SnowDepth, SR50A_QualityVal,"
                            "LF1_Ice_Output, Ice_Inch, Ice_mm,"
                            "Visibilitystr)"                      
                        "VALUES('"+Met_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-i]+
                        "','"+str(Met_Data.iloc[-i,0])+"','"+str(Met_Data.iloc[-i,1])+"','"+str(Met_Data.iloc[-i,2])+"','"+str(Met_Data.iloc[-i,3])+"','"+str(Met_Data.iloc[-i,4])+"','"+str(Met_Data.iloc[-i,5])+"','"+str(Met_Data.iloc[-i,6])+"','"+str(Met_Data.iloc[-i,7])+"','"+str(Met_Data.iloc[-i,8])+
                        "','"+str(Met_Data.iloc[-i,9])+"','"+str(Met_Data.iloc[-i,10])+"','"+str(Met_Data.iloc[-i,11])+"','"+str(Met_Data.iloc[-i,12])+"','"+str(Met_Data.iloc[-i,13])+"','"+str(Met_Data.iloc[-i,14])+"','"+str(Met_Data.iloc[-i,15])+"','"+str(Met_Data.iloc[-i,16])+
                        "','"+str(Met_Data.iloc[-i,17])+"','"+str(Met_Data.iloc[-i,18])+"','"+str(Met_Data.iloc[-i,19])+"','"+str(Met_Data.iloc[-i,20])+"','"+str(Met_Data.iloc[-i,21])+"','"+str(Met_Data.iloc[-i,22])+"','"+str(Met_Data.iloc[-i,23])+"','"+str(Met_Data.iloc[-i,24])+
                        "','"+str(TPS_3100_Data.iloc[-i,0])+"','"+str(TPS_3100_Data.iloc[-i,1])+"','"+str(TPS_3100_Data.iloc[-i,2])+"','"+str(TPS_3100_Data.iloc[-i,3])+"','"+str(TPS_3100_Data.iloc[-i,4])+"','"+str(TPS_3100_Data.iloc[-i,5])+"','"+str(TPS_3100_Data.iloc[-i,6])+                  
                        "','"+str(SDMS40_Data.iloc[-i,0])+
                        "','"+str(SR50A_Data.iloc[-i,0])+"','"+str(SR50A_Data.iloc[-i,1])+
                        "','"+str(IceAcc_Data.iloc[-i,0])+"','"+str(IceAcc_Data.iloc[-i,1])+"','"+str(IceAcc_Data.iloc[-i,1])+
                        "','"+str(CS120A_Data.iloc[-i,0])+                   
                        "')")
    
    
    
    print(queryReleveMeteo)
    bd_eos(queryReleveMeteo)


