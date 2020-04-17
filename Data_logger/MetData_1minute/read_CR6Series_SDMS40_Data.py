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
   "TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version32.CR6 Feb 3rd.cr6","64318","SDMS40_Data"    
	CR6Series_SDMS40_Data AllData[] 
	----------------------    
    [0] :TIMESTAMP | Unit: [TS]                                     [1] :RECORD | Unit: [RN]
    [2] :SDMS40_Depth_Avg | Unit: [mm]                              [3] :SDMS40_Board_Temperature | Unit: [Deg C]
    [4] :SDMS40_Heater_Low_Threshold_Temperature | Unit: [Deg C]    [5] :SDMS40_Laser_Temperature | Unit: [Deg C]
    [6] :SDMS40_Depth_Points(1) | Unit: [mm]                        [7] :SDMS40_Depth_Points(2) | Unit: [mm]
    [8] :SDMS40_Depth_Points(3) | Unit: [mm]                        [9] :SDMS40_Depth_Points(4) | Unit: [mm]
    [10] :SDMS40_Depth_Points(5) | Unit: [mm]                       [11] :SDMS40_Depth_Points(6) | Unit: [mm]
    [12] :SDMS40_Depth_Points(7) | Unit: [mm]                       [13] :SDMS40_Depth_Points(8) | Unit: [mm]
    [14] :SDMS40_Depth_Points(9) | Unit: [mm]                       [15] :SDMS40_Depth_Points(10) | Unit: [mm]
    [16] :SDMS40_Depth_Points(11) | Unit: [mm]                      [17] :SDMS40_Depth_Points(12) | Unit: [mm]
    [18] :SDMS40_Depth_Points(13) | Unit: [mm]                      [19] :SDMS40_Depth_Points(14) | Unit: [mm]
    [20] :SDMS40_Depth_Points(15) | Unit: [mm]                      [21] :SDMS40_Depth_Points(16) | Unit: [mm]
    [22] :SDMS40_Depth_Points(17) | Unit: [mm]                      [23] :SDMS40_Depth_Points(18) | Unit: [mm]
    [24] :SDMS40_Depth_Points(19) | Unit: [mm]                      [25] :SDMS40_Depth_Points(20) | Unit: [mm]
    [26] :SDMS40_Depth_Points(21) | Unit: [mm]                      [27] :SDMS40_Depth_Points(22) | Unit: [mm]
    [28] :SDMS40_Depth_Points(23) | Unit: [mm]                      [29] :SDMS40_Depth_Points(24) | Unit: [mm]
    [30] :SDMS40_Depth_Points(25) | Unit: [mm]                      [31] :SDMS40_Depth_Points(26) | Unit: [mm]
    [32] :SDMS40_Depth_Points(27) | Unit: [mm]                      [33] :SDMS40_Depth_Points(28) | Unit: [mm]
    [34] :SDMS40_Depth_Points(29) | Unit: [mm]                      [35] :SDMS40_Depth_Points(30) | Unit: [mm]
    [36] :SDMS40_Depth_Points(31) | Unit: [mm]                      [37] :SDMS40_Depth_Points(32) | Unit: [mm]
    [38] :SDMS40_Depth_Points(33) | Unit: [mm]                      [39] :SDMS40_Depth_Points(34) | Unit: [mm]
    [40] :SDMS40_Depth_Points(35) | Unit: [mm]                      [41] :SDMS40_Depth_Points(36) | Unit: [mm]
    [42] :SDMS40_Distance_Points(1) | Unit: [mm]                    [43] :SDMS40_Distance_Points(2) | Unit: [mm]
    [44] :SDMS40_Distance_Points(3) | Unit: [mm]                    [45] :SDMS40_Distance_Points(4) | Unit: [mm]
    [46] :SDMS40_Distance_Points(5) | Unit: [mm]                    [47] :SDMS40_Distance_Points(6) | Unit: [mm]
    [48] :SDMS40_Distance_Points(7) | Unit: [mm]                    [49] :SDMS40_Distance_Points(8) | Unit: [mm]
    [50] :SDMS40_Distance_Points(9) | Unit: [mm]                    [51] :SDMS40_Distance_Points(10) | Unit: [mm]
    [52] :SDMS40_Distance_Points(11) | Unit: [mm]                   [53] :SDMS40_Distance_Points(12) | Unit: [mm]
    [54] :SDMS40_Distance_Points(13) | Unit: [mm]                   [55] :SDMS40_Distance_Points(14) | Unit: [mm]
    [56] :SDMS40_Distance_Points(15) | Unit: [mm]                   [57] :SDMS40_Distance_Points(16) | Unit: [mm]
    [58] :SDMS40_Distance_Points(17) | Unit: [mm]                   [59] :SDMS40_Distance_Points(18) | Unit: [mm]
    [60] :SDMS40_Distance_Points(19) | Unit: [mm]                   [61] :SDMS40_Distance_Points(20) | Unit: [mm]
    [62] :SDMS40_Distance_Points(21) | Unit: [mm]                   [63] :SDMS40_Distance_Points(22) | Unit: [mm]
    [64] :SDMS40_Distance_Points(23) | Unit: [mm]                   [65] :SDMS40_Distance_Points(24) | Unit: [mm]
    [66] :SDMS40_Distance_Points(25) | Unit: [mm]                   [67] :SDMS40_Distance_Points(26) | Unit: [mm]
    [68] :SDMS40_Distance_Points(27) | Unit: [mm]                   [69] :SDMS40_Distance_Points(28) | Unit: [mm]
    [70] :SDMS40_Distance_Points(29) | Unit: [mm]                   [71] :SDMS40_Distance_Points(30) | Unit: [mm]
    [72] :SDMS40_Distance_Points(31) | Unit: [mm]                   [73] :SDMS40_Distance_Points(32) | Unit: [mm]
    [74] :SDMS40_Distance_Points(33) | Unit: [mm]                   [75] :SDMS40_Distance_Points(34) | Unit: [mm]
    [76] :SDMS40_Distance_Points(35) | Unit: [mm]                   [77] :SDMS40_Distance_Points(36) | Unit: [mm]

    ------------------------------------
    ------------------------------------       
	CR6Series_SDMS40_Data usefulData[] 
	----------------------
    [0] :TIMESTAMP
    [2] :SDMS40_Depth_Avg  [int64]   
    
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""
## Tips to print columns names and index    
#file1 = 'CR6Series_SDMS40_Data.dat'   
#CR6Series_SDMS40_Data  = pd.read_csv(file1, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(file1, sep=",", skiprows=[0])   
#for col in list(CR6Series_SDMS40_Data.columns.values):
#    print('['+str(CR6Series_SDMS40_Data.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )
#
#    
    
def read_CR6Series_SDMS40_Data(filename):
	#Ouverture du fichier csv précédemment créé et extraction des données dans un tuple
    CR6Series_SDMS40_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,2])     
    CR6Series_SDMS40_Data = CR6Series_SDMS40_Data.set_index('TIMESTAMP')
    CR6Series_SDMS40_Data.index = pd.to_datetime(CR6Series_SDMS40_Data.index)  
    return(CR6Series_SDMS40_Data)
	
