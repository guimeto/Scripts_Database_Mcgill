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
    "TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version32.CR6 Feb 3rd.cr6","64318","Flux_AmeriFluxFormat"
	CR6Series_Flux_AmeriFluxFormat AllData[] 
	----------------------
    [0] :TIMESTAMP | Unit: [TS]                     [1] :RECORD | Unit: [RN]
    [2] :TIMESTAMP_START | Unit: [nan]              [3] :TIMESTAMP_END | Unit: [nan]
    [4] :CO2 | Unit: [umolCO2 mol-1]                [5] :CO2_SIGMA | Unit: [umolCO2 mol-1]
    [6] :H2O | Unit: [mmolH2O mol-1]                [7] :H2O_SIGMA | Unit: [mmolH2O mol-1]
    [8] :FC | Unit: [umolCO2 m-2 s-1]               [9] :FC_SSITC_TEST | Unit: [adimensional]
    [10] :LE | Unit: [W m-2]     b                 [11] :LE_SSITC_TEST | Unit: [adimensional]
    [12] :ET | Unit: [mm hour-1]                   [13] :ET_SSITC_TEST | Unit: [adimensional]
    [14] :H | Unit: [W m-2]                        [15] :H_SSITC_TEST | Unit: [adimensional]
    [16] :G | Unit: [W m-2]                        [17] :SG | Unit: [W m-2]
    [18] :FETCH_MAX | Unit: [m]                    [19] :FETCH_90 | Unit: [m]
    [20] :FETCH_55 | Unit: [m]                     [21] :FETCH_40 | Unit: [m]
    [22] :WD | Unit: [decimal degrees]             [23] :WS | Unit: [m s-1]
    [24] :WS_MAX | Unit: [m s-1]                   [25] :USTAR | Unit: [m s-1]
    [26] :ZL | Unit: [adimensional]                [27] :TAU | Unit: [kg m-1 s-2]
    [28] :TAU_SSITC_TEST | Unit: [adimensional]    [29] :MO_LENGTH | Unit: [m]
    [30] :U | Unit: [m s-1]                        [31] :U_SIGMA | Unit: [m s-1]
    [32] :V | Unit: [m s-1]                        [33] :V_SIGMA | Unit: [m s-1]
    [34] :W | Unit: [m s-1]                        [35] :W_SIGMA | Unit: [m s-1]
    [36] :PA | Unit: [kPa]                         [37] :TA_1_1_1 | Unit: [deg C]
    [38] :RH_1_1_1 | Unit: [%]                     [39] :T_DP_1_1_1 | Unit: [deg C]
    [40] :TA_2_1_1 | Unit: [deg C]                 [41] :RH_2_1_1 | Unit: [%]
    [42] :T_DP_2_1_1 | Unit: [deg C]               [43] :TA_3_1_1 | Unit: [deg C]
    [44] :RH_3_1_1 | Unit: [%]                     [45] :T_DP_3_1_1 | Unit: [deg C]
    [46] :VPD | Unit: [hPa]                        [47] :T_SONIC | Unit: [deg C]
    [48] :T_SONIC_SIGMA | Unit: [deg C]            [49] :PBLH | Unit: [m]
    [50] :SWC_1_1_1 | Unit: [%]                    [51] :TS_1_1_1 | Unit: [deg C]
    [52] :TS_2_1_1 | Unit: [deg C]                 [53] :ALB | Unit: [%]
    [54] :NETRAD | Unit: [W m-2]                   [55] :SW_IN | Unit: [W m-2]
    [56] :SW_OUT | Unit: [W m-2]                   [57] :LW_IN | Unit: [W m-2]
    [58] :LW_OUT | Unit: [W m-2]
    ------------------------------------
    ------------------------------------
	CR6Series_Flux_AmeriFluxFormat usefulData[] 
	----------------------
		[0]     Timestamp
		[55]	SW_IN
		[56]	SW_OUT
		[57]	LW_IN
		[58]	LW_OUT
		[23]	WS
		[22]	WD
		[51]	TS_1_1_1
		[52]	TS_2_1_1
		[50] 	SWC_1_1_1
		[36] 	PA
		[54]	NETRAD
		[53]	ALB
		[8]	    FC
		[16]	G
		[17]	SG
		[12]	ET
		[10]	LE
        [14]    H
		[18]    FETCH_MAX
        
	
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""    
def read_CR6Series_Flux_AmeriFluxFormat_Data(filename):
    CR6Series_Flux_AmeriFluxFormat  = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,8,10,12,14,16,17,18,22,23,36,50,51,52,53,54,55,56,57,58])     
    CR6Series_Flux_AmeriFluxFormat = CR6Series_Flux_AmeriFluxFormat.set_index('TIMESTAMP')
    CR6Series_Flux_AmeriFluxFormat.index = pd.to_datetime(CR6Series_Flux_AmeriFluxFormat.index)
    CR6Series_Flux_AmeriFluxFormat = CR6Series_Flux_AmeriFluxFormat.replace(['NAN'],[-999]) 
    return(CR6Series_Flux_AmeriFluxFormat)
# Tips to print columns names and index    
#file1 = 'K:/PROJETS/PROJET_Mcgill/Data_logger/Preparation_DataBase/data_brute/CR6Series_Flux_AmeriFluxFormat.dat'   
#CR6Series_Flux_AmeriFluxFormat  = pd.read_csv(file1, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(file1, sep=",", skiprows=[0])   
#for col in list(CR6Series_Flux_AmeriFluxFormat.columns.values):
#    print('['+str(CR6Series_Flux_AmeriFluxFormat.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )	
