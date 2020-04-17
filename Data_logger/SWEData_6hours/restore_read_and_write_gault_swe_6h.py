# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:56:16 2020

@author: guillaume
"""
# -*-coding:Latin-1 -*
from bd_eos import bd_eos
from read_CR6Series_CS725_6Hour_Data import read_CR6Series_CS725_6Hour_Data
import glob

for f in glob.glob('/storage1/gault/LoggerData/CS725_6Hour/2019/CR6Series_CS725_6Hour*.dat'):   
    print(f)       
   
    ### read useful data
    CR6Series_CS725_6Hour_Data = read_CR6Series_CS725_6Hour_Data(f)  
    
    for i in range (0,len(CR6Series_CS725_6Hour_Data)-1): 
        
        queryReleveMeteo = ("INSERT INTO gault_swe_6h (date,"
                                    "CS725_SWE_K, CS725_SWE_TL)"                      
                                    "VALUES('"+CR6Series_CS725_6Hour_Data.index.strftime('%Y-%m-%d %H:%M:%S')[i]+
                                    "','"+str(CR6Series_CS725_6Hour_Data.iloc[i,0])+"','"+str(CR6Series_CS725_6Hour_Data.iloc[i,1])+
                            "')")
    
        print(queryReleveMeteo)
        bd_eos(queryReleveMeteo)


