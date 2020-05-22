# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:56:16 2020

@author: guillaume
"""
# -*-coding:Latin-1 -*
from bd_eos import bd_eos
from read_CR6Series_CS725_6Hour_Data import read_CR6Series_CS725_6Hour_Data
        
### Path to read gault_transit data 
#CR6Series_CS725_6Hour = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_CS725_6Hour.dat' 
CR6Series_CS725_6Hour = '/roddy/storage1/gault_transit/CR6Series_CS725_6Hour.dat' 

### read useful data
CR6Series_CS725_6Hour_Data = read_CR6Series_CS725_6Hour_Data(CR6Series_CS725_6Hour)  


queryReleveMeteo = ("INSERT INTO gault_swe_6h (date,"
                        "CS725_SWE_K, CS725_SWE_K)"                      
                    "VALUES('"+CR6Series_CS725_6Hour_Data.index.strftime('%Y-%m-%d %H:%M:%S')[-1]+
                    "','"+str(CR6Series_CS725_6Hour_Data.iloc[-1,0])+"','"+str(CR6Series_CS725_6Hour_Data.iloc[-1,1])+
                    "')")

print(queryReleveMeteo)
bd_eos(queryReleveMeteo)


