# -*-coding:Latin-1 -*
###############################################################################################################################################################
# Nom : readFile()
# Autor : Guillaume Dueymes 
# Last update: 27/02/2020
# Description : Lit le fichier pointé par filename, extrait les données dans un tuple, regarde selon la date si le dossier  
# où stocker ces données existe, les crée au besoin, puis appelle ecrireFichier() en passant la liste de données à écrire et le path
# Arguments entrée : filename qui est le path du fichier à lire
# Arguments sortie : usefulData qui est une liste contenant toutes les données et informations (path) pour stocker les données convenablement
###############################################################################################################################################################
import pandas as pd

"""   
"TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version32.CR6 Feb 3rd.cr6","64318","IceAcc_Data"
 
	CR6Series_IceAcc_Data AllData[] 
	----------------------
    [0] :TIMESTAMP | Unit: [TS]
    [1] :RECORD | Unit: [RN]
    [2] :MainString | Unit: [nan]
    [3] :Frequency_Ice | Unit: [Hz]
    [4] :HeatingString | Unit: [nan]
    [5] :Ice_heater | Unit: [nan]
    [6] :LF1_Ice_Output | Unit: [nan]
    [7] :Ice_Inch | Unit: [nan]
    [8] :Ice_mm | Unit: [nan]
    ------------------------------------
    ------------------------------------       
	CR6Series_IceAcc_Data usefulData[] 
	----------------------
    [0] :TIMESTAMP | Unit: [TS]
    [6] :LF1_Ice_Output | Unit: [nan]      [char]
    [8] :Ice_mm | Unit: [nan]              [float64]
    [7] :Ice_Inch | Unit: [nan]            [float64]
    
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""
   
def read_CR6Series_IceAcc_Data(filename):
    CR6Series_IceAcc_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,6,7,8])     
    CR6Series_IceAcc_Data = CR6Series_IceAcc_Data.set_index('TIMESTAMP')
    CR6Series_IceAcc_Data.index = pd.to_datetime(CR6Series_IceAcc_Data.index)  
    return(CR6Series_IceAcc_Data)  
	
# Tips to print columns names and index    
#filename = 'CR6Series_IceAcc_Data.dat'   
#CR6Series_IceAcc_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(filename, sep=",", skiprows=[0])   
#for col in list(CR6Series_IceAcc_Data.columns.values):
#    print('['+str(CR6Series_IceAcc_Data.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )