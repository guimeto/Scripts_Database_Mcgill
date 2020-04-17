# -*-coding:Latin-1 -*
###############################################################################################################################################################
# Nom : read_CR6Series_CS120A()
# Autor : Guillaume Dueymes 
# Last update: 27/02/2020
# Description : Lit le fichier pointé par filename, extrait les données dans un tuple, regarde selon la date si le dossier  
# où stocker ces données existe, les crée au besoin, puis appelle ecrireFichier() en passant la liste de données à écrire et le path
# Arguments entrée : filename qui est le path du fichier à lire
# Arguments sortie : usefulData qui est une liste contenant toutes les données et informations (path) pour stocker les données convenablement
###############################################################################################################################################################
import pandas as pd

"""   
"TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version32.CR6 Feb 3rd.cr6","64318","CS120A_Data"
   
	CR6Series_CS120A_Data AllData[] 
	----------------------
    [0] :TIMESTAMP | Unit: [TS]
    [1] :RECORD | Unit: [RN]
    [2] :Message_ID | Unit: [nan]
    [3] :Sensor_ID | Unit: [nan]
    [4] :System_status | Unit: [nan]
    [5] :Interval_time | Unit: [nan]
    [6] :Visibilitystr | Unit: [nan]
    [7] :VisibilityUnits | Unit: [nan]
    [8] :Averaging_duration | Unit: [nan]
    [9] :User_alarm_1 | Unit: [nan]
    [10] :User_alarm_2 | Unit: [nan]
    [11] :Emitter_failure | Unit: [nan]
    [12] :Emitter_lens_dirty | Unit: [nan]
    [13] :Emitter_temp_error | Unit: [nan]
    [14] :Detector_lens_dirty | Unit: [nan]
    [15] :Detector_temp_error | Unit: [nan]
    [16] :Detector_saturated | Unit: [nan]
    [17] :Hood_temp_error | Unit: [nan]
    [18] :Signature_error | Unit: [nan]
    [19] :Flash_read_error | Unit: [nan]
    [20] :Flash_write_error | Unit: [nan]
    [21] :checksumrx | Unit: [nan]
    ------------------------------------
    ------------------------------------       
	CR6Series_CS120A_Data usefulData[] 
	----------------------
    [0] :TIMESTAMP | Unit: [TS]
    [6] :Visibilitystr | Unit: [nan]
    
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""
def read_CR6Series_CS120A_Data(filename):

    CR6Series_CS120A_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,6])     
    CR6Series_CS120A_Data = CR6Series_CS120A_Data.set_index('TIMESTAMP')
    CR6Series_CS120A_Data.index = pd.to_datetime(CR6Series_CS120A_Data.index)          
    return(CR6Series_CS120A_Data)
        
# Tips to print columns names and index    
#file1 = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_CS120A_Data.dat'   
#CR6Series_CS120A_Data  = pd.read_csv(file1, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(file1, sep=",", skiprows=[0])   
#for col in list(CR6Series_CS120A_Data.columns.values):
#    print('['+str(CR6Series_CS120A_Data.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )
#    

		
	
