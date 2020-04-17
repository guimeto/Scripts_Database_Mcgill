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
"TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version32.CR6 Feb 3rd.cr6","64318","TPS_3100_Data"       
	CR6Series_TPS_3100_Data AllData[] 
	----------------------
    
	[0] :TIMESTAMP
    [1] :RECORD
    [2] :RX
    [3] :TPS_Time_Sec
    [4] :TPS_Precip_Rate_1minAvg_mmHr
    [5] :TPS_Total_Accum_mm
    [6] :TPS_Pwr_Sensor_W
    [7] :TPS_Pwr_Ref_W
    [8] :TPS_Amb_Temp_C
    [9] :TPS_Enc_Temp_C
    [10] :TPS_Wind_Spd_ms
    [11] :TPS_Coll_Eff
    [12] :TPS_Pwr_Offset_W
    [13] :TPS_Pwr_OffsetRad_W
    [14] :TPS_Raw_Precip_Rate_1minAvg_mmHr
    [15] :TPS_Raw_Precip_Rate_5minAvg_mmHr
    [16] :TPS_Solar_Rad_Wm2
    [17] :TPS_Net_Rad_Wm2
    [18] :TPS_Baro_Press_mbar
    [19] :TPS_Air_Temp_C
    [20] :TPS_RH_perc	    
    ------------------------------------
    ------------------------------------       
	CR6Series_TPS_3100_Data usefulData[] 
	----------------------
    [0] :TIMESTAMP                             [float64]
    [14] :TPS_Raw_Precip_Rate_1minAvg_mmHr     [float64]
    [15] :TPS_Raw_Precip_Rate_5minAvg_mmHr     [float64]
    [10] :TPS_Wind_Spd_ms                      [float64]
    [19] :TPS_Air_Temp_C                       [float64]
    [5] :TPS_Total_Accum_mm                    [float64]
    [6] :TPS_Pwr_Sensor_W                      [float64]
    [7] :TPS_Pwr_Ref_W                         [float64]
    
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""
    
def read_CR6Series_TPS_3100_Data(filename):   
    CR6Series_TPS_3100_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,14,15,10,19,5,6,7])     
    CR6Series_TPS_3100_Data = CR6Series_TPS_3100_Data.set_index('TIMESTAMP')
    CR6Series_TPS_3100_Data.index = pd.to_datetime(CR6Series_TPS_3100_Data.index)  
    return(CR6Series_TPS_3100_Data)
    
# Tips to print columns names and index    
#file1 = 'CR6Series_TPS_3100_Data.dat'   
#CR6Series_TPS_3100_Data  = pd.read_csv(file1, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(file1, sep=",", skiprows=[0])   
#for col in list(CR6Series_TPS_3100_Data.columns.values):
#    print('['+str(CR6Series_TPS_3100_Data.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )
#    

	
