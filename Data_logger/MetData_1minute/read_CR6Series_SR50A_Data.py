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
"TOA5","CR6Series","CR6","10158","CR6.Std.09.02 CR6-WIFI.04.00.01","CPU:McGill_University_Program_Version34 May 7 2020.CR6","30372","SR50A_Data"
	----------------------
    [0] :TIMESTAMP | Unit: [TS]
    [1] :RECORD | Unit: [RN]
    [2] :SR50A_SnowDepth | Unit: [m]
    [3] :SR50ASort | Unit: [nan]
    [4] :SR50A_QualityVal | Unit: [nan]
	
    ------------------------------------
    ------------------------------------       
	CR6Series_SR50A_Data usefulData[] 
	----------------------
    [0] :TIMESTAMP | Unit: [TS]
    [2] :SR50A_SnowDepth | Unit: [m]     [float64]
    [4] :SR50A_QualityVal | Unit: [nan]  [int64] 
    
	#"Explicit is better than Implicit" The Zen of Python 2nd aphorism
	"""
#    
def read_CR6Series_SR50A_Data(filename):
	#Ouverture du fichier csv précédemment créé et extraction des données dans un tuple
    CR6Series_SR50A_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3], usecols=[0,2,4])     
    CR6Series_SR50A_Data = CR6Series_SR50A_Data.set_index('TIMESTAMP')
    CR6Series_SR50A_Data.index = pd.to_datetime(CR6Series_SR50A_Data.index)
    try :
            CR6Series_SR50A_Data = CR6Series_SR50A_Data.replace(['NAN'],[-999]) 
    except:
            pass
        
    return(CR6Series_SR50A_Data)   

		
# Tips to print columns names and index    
#filename = 'CR6Series_SR50A_Data.dat'   
#CR6Series_SR50A_Data  = pd.read_csv(filename, sep=",", skiprows=[0,2,3]) 
#headers = pd.read_csv(filename, sep=",", skiprows=[0])   
#for col in list(CR6Series_SR50A_Data.columns.values):
#    print('['+str(CR6Series_SR50A_Data.columns.get_loc(col))+'] :' + col + ' | Unit: [' +str(headers.iloc[0][col])+']' )