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
"TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version34 May 7 2020.CR6","30372","TPS_3100_Data"

	----------------------
    
    [0] :TIMESTAMP | Unit: [TS]
    [1] :RECORD | Unit: [RN]
    [2] :RX | Unit: [nan]
    [3] :TPS_Wind_Spd_ms_Max | Unit: [nan]
    [4] :TPS_Baro_Press_mbar_Corrected | Unit: [mbar]
    [5] :TPS_Time_Sec | Unit: [nan]
    [6] :TPS_Precip_Rate_1minAvg_mmHr | Unit: [nan]
    [7] :TPS_Total_Accum_mm | Unit: [nan]
    [8] :TPS_Pwr_Sensor_W | Unit: [nan]
    [9] :TPS_Pwr_Ref_W | Unit: [nan]
    [10] :TPS_Amb_Temp_C | Unit: [nan]
    [11] :TPS_Enc_Temp_C | Unit: [nan]
    [12] :TPS_Wind_Spd_ms | Unit: [nan]
    [13] :TPS_Coll_Eff | Unit: [nan]
    [14] :TPS_Pwr_Offset_W | Unit: [nan]
    [15] :TPS_Pwr_OffsetRad_W | Unit: [nan]
    [16] :TPS_Raw_Precip_Rate_1minAvg_mmHr | Unit: [nan]
    [17] :TPS_Raw_Precip_Rate_5minAvg_mmHr | Unit: [nan]
    [18] :TPS_Solar_Rad_Wm2 | Unit: [nan]
    [19] :TPS_Net_Rad_Wm2 | Unit: [nan]
    [20] :TPS_Baro_Press_mbar | Unit: [nan]
    [21] :TPS_Air_Temp_C | Unit: [nan]
    [22] :TPS_RH_perc | Unit: [nan]	    
    ------------------------------------
    ------------------------------------       
	CR6Series_TPS_3100_Data usefulData[] 
	----------------------
    [0] :TIMESTAMP                             [float64]
    [16] :TPS_Raw_Precip_Rate_1minAvg_mmHr     [float64]
    [17] :TPS_Raw_Precip_Rate_5minAvg_mmHr     [float64]
    [12] :TPS_Wind_Spd_ms                      [float64]
    [21] :TPS_Air_Temp_C                       [float64]
    [7] :TPS_Total_Accum_mm                    [float64]
    [8] :TPS_Pwr_Sensor_W                      [float64]
    [9] :TPS_Pwr_Ref_W                         [float64]
    [4] :TPS_Baro_Press_mbar_Corrected | Unit: [mbar]
    
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""
    
def read_CR6Series_TPS_3100_Data(filename):   
    CR6Series_TPS_3100_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,16,17,12,21,7,8,9,4])     
    CR6Series_TPS_3100_Data = CR6Series_TPS_3100_Data.set_index('TIMESTAMP')
    CR6Series_TPS_3100_Data.index = pd.to_datetime(CR6Series_TPS_3100_Data.index)  
    
    try :
            CR6Series_TPS_3100_Data = CR6Series_TPS_3100_Data.replace(['NAN'],[-999]) 
    except:
            pass
        
    return(CR6Series_TPS_3100_Data)
    
## Tips to print columns names and index    
#filename = 'CR6Series_TPS_3100_Data.dat'   
#CR6Series_TPS_3100_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(filename, sep=",", skiprows=[0])   
#for col in list(CR6Series_TPS_3100_Data.columns.values):
#    print('['+str(CR6Series_TPS_3100_Data.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )
#    

	
