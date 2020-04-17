# -*-coding:Latin-1 -*
###############################################################################################################################################################
# Nom : readFile()
# Autor : Guillaume Dueymes 
# Last update: 16/04/2020
# Description : Lit le fichier pointé par filename, extrait les données dans un tuple, regarde selon la date si le dossier  
# où stocker ces données existe, les crée au besoin, puis appelle ecrireFichier() en passant la liste de données à écrire et le path
# Arguments entrée : filename qui est le path du fichier à lire
# Arguments sortie : usefulData qui est une liste contenant toutes les données et informations (path) pour stocker les données convenablement
###############################################################################################################################################################
import pandas as pd
"""
    "TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version32.CR6 Feb 3rd.cr6","64318","Met_Data"
    CR6Series_Met_data AllData[] 
	----------------------
    [0] :TIMESTAMP | Unit: [TS]                    [1] :RECORD | Unit: [RN]
    [2] :LWMDry_Tot | Unit: [Minutes]              [3] :LWMCon_Tot | Unit: [Minutes]
    [4] :LWMWet_Tot | Unit: [Minutes]              [5] :Current_Avg | Unit: [Amps_rms]
    [6] :Current_Max | Unit: [Amps_rms]            [7] :Frequency | Unit: [Hz]
    [8] :WS_ms | Unit: [meters/second]             [9] :Mean_WindDir | Unit: [Deg]
    [10] :WindDir_SD | Unit: [Deg]                [11] :CMP10_Solar_uWm2_Avg | Unit: [uW/mÂ²]
    [12] :CMP10_Solar_uWm2_Std | Unit: [uW/mÂ²]   [13] :Temp1_Avg | Unit: [DegC]
    [14] :Temp2_Avg | Unit: [DegC]                [15] :Temp3_Avg | Unit: [DegC]
    [16] :Temp4_Avg | Unit: [DegC]                [17] :Temp5_Avg | Unit: [DegC]
    [18] :Temp6_Avg | Unit: [DegC]                [19] :Temp7_Avg | Unit: [DegC]
    [20] :Temp8_Avg | Unit: [DegC]                [21] :RH1 | Unit: [%]
    [22] :RH2 | Unit: [%]                         [23] :RH3 | Unit: [%]
    [24] :RH4 | Unit: [%]                         [25] :RH5 | Unit: [%]
    [26] :RH6 | Unit: [%]                         [27] :RH7 | Unit: [%]
    [28] :RH8 | Unit: [%]
    
    [0] :TIMESTAMP | Unit: [TS]
    [1] :RECORD | Unit: [RN]
    [2] :LWMDry_Tot | Unit: [Minutes]
    [3] :LWMCon_Tot | Unit: [Minutes]
    [4] :LWMWet_Tot | Unit: [Minutes]
    [5] :Current_Avg | Unit: [Amps_rms]
    [6] :Current_Max | Unit: [Amps_rms]
    [7] :Frequency | Unit: [Hz]
    [8] :WS_ms | Unit: [meters/second]
    [9] :Mean_WindDir | Unit: [Deg]
    [10] :WindDir_SD | Unit: [Deg]
    [11] :WS_ms_Max | Unit: [meters/second]
    [12] :WindDir_Max | Unit: [Degrees]
    [13] :CMP10_Solar_uWm2_Avg | Unit: [uW/mÂ²]
    [14] :CMP10_Solar_uWm2_Std | Unit: [uW/mÂ²]
    [15] :Temp1_Avg | Unit: [DegC]
    [16] :Temp2_Avg | Unit: [DegC]
    [17] :Temp3_Avg | Unit: [DegC]
    [18] :Temp4_Avg | Unit: [DegC]
    [19] :Temp5_Avg | Unit: [DegC]
    [20] :Temp6_Avg | Unit: [DegC]
    [21] :Temp7_Avg | Unit: [DegC]
    [22] :Temp8_Avg | Unit: [DegC]
    [23] :RH1 | Unit: [%]
    [24] :RH2 | Unit: [%]
    [25] :RH3 | Unit: [%]
    [26] :RH4 | Unit: [%]
    [27] :RH5 | Unit: [%]
    [28] :RH6 | Unit: [%]
    [29] :RH7 | Unit: [%]
    [30] :RH8 | Unit: [%]
    ------------------------------------
    ------------------------------------
	CR6Series_Met_data usefulData[] 
	----------------------
		 [0]     Timestamp
		 [15] :Temp1_Avg | Unit: [DegC]
         [16] :Temp2_Avg | Unit: [DegC]
         [17] :Temp3_Avg | Unit: [DegC]
         [18] :Temp4_Avg | Unit: [DegC]
         [19] :Temp5_Avg | Unit: [DegC]
         [20] :Temp6_Avg | Unit: [DegC]
         [21] :Temp7_Avg | Unit: [DegC]
         [22] :Temp8_Avg | Unit: [DegC]
         [23] :RH1 | Unit: [%]
         [24] :RH2 | Unit: [%]
         [25] :RH3 | Unit: [%]
         [26] :RH4 | Unit: [%]
         [27] :RH5 | Unit: [%]
         [28] :RH6 | Unit: [%]
         [29] :RH7 | Unit: [%]
         [30] :RH8 | Unit: [%]
		 [13] :CMP10_Solar_uWm2_Avg | Unit: [uW/mÂ²]
         [8] :WS_ms | Unit: [meters/second]
         [9] :Mean_WindDir | Unit: [Deg]
		 [10] :WindDir_SD | Unit: [Deg]
         [11] :WS_ms_Max | Unit: [meters/second]
         [12] :WindDir_Max | Unit: [Degrees]
	     [2] :LWMDry_Tot | Unit: [Minutes]
         [3] :LWMCon_Tot | Unit: [Minutes]
         [4] :LWMWet_Tot | Unit: [Minutes]
        
	
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""
#filename = 'CR6Series_Met_data.dat'    
def read_CR6Series_Met_Data(filename):
        CR6Series_Met_data = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,13,8,9,10,11,12,2,3,4])
        CR6Series_Met_data = CR6Series_Met_data.set_index('TIMESTAMP')
        CR6Series_Met_data.index = pd.to_datetime(CR6Series_Met_data.index) 
        CR6Series_Met_data = CR6Series_Met_data.replace(['NAN'],[-999]) 
        return(CR6Series_Met_data)

		

# Tips to print columns names and index    
#file1 = 'CR6Series_Met_data.dat'   
#CR6Series_Met_data  = pd.read_csv(file1, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(file1, sep=",", skiprows=[0])   
#for col in list(CR6Series_Met_data.columns.values):
#    print('['+str(CR6Series_Met_data.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )     