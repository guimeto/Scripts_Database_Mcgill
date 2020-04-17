#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:21:48 2018

@author: UQAM
"""
from netCDF4 import Dataset
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

now = datetime.utcnow()
year, month, day = now.year, now.month, now.day
#=============================================================================
#...Read the MRR data
path = '/StationMeteo_01/radar/MRR2/RawSpectra_Netcdf/' + str(year)+'{:02d}'.format(month)+ '/'

filename = path + 'UQAM_MRR2_'+str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)+'.nc' 
nc = Dataset(filename)

#... To plot the MRR timeseries
height       = nc.variables['height'][:]
height_2D = np.rot90(height)
height_1D = pd.DataFrame(height_2D[:,0], columns=['height'])
readtime     = nc.variables['time'][:] 

x_unstag = np.tile(readtime, (31, 1))
for i in range(x_unstag.shape[0]):
    t = x_unstag[i,:]
    t_mrr = pd.to_datetime(t,unit='s')
t_mrr = pd.DataFrame(t_mrr[:], columns=['Date'])
t_mrr.index = t_mrr['Date'] 

#t_mrr_10min = t_mrr.iloc[::60]     # selection des données instantannées aux 10 minutes
# Pour travailler aux 5 minutes 
t_mrr_5min = t_mrr.iloc[::30]     # selection des données instantannées aux 5 minutes

#=======================Travail sur une journéée complète========================================
#... Reflectivity
reflectivity = nc.variables['Ze'][:]
ones = np.ones(reflectivity.shape)
reflectivity_2D = pd.DataFrame(np.rot90(reflectivity))
#reflectivity_2D_10min = reflectivity_2D.iloc[:,::60].round(2) # selection des données instantannées aux 10 minutes

# Pour travailler aux 5 minutes sur la journée complète 
reflectivity_2D_5min = reflectivity_2D.iloc[:,::30].round(2) # selection des données instantannées aux 5 minutes
#reflectivity_2D_5min = reflectivity_2D.rolling(window=30,axis=1).mean().iloc[:,::30]

##... Doppler velocity
Dopplervel = nc.variables['W'][:]
Dopplervel_2D = pd.DataFrame(np.rot90(Dopplervel))
#Dopplervel_2D_10min = Dopplervel_2D.iloc[:,::60].round(2)     # selection des données instantannées aux 10 minutes

# Pour travailler aux 5 minutes sur la journée complete
Dopplervel_2D_5min = Dopplervel_2D.iloc[:,::30].round(2)     # selection des données instantannées aux 5 minutes
#Dopplervel_2D_5min = Dopplervel_2D.rolling(window=30,axis=1).mean().iloc[:,::30]

#df_Doppler = pd.concat([Dopplervel_2D_10min, height_1D], axis=1)
df_Doppler = pd.concat([Dopplervel_2D_5min, height_1D], axis=1)
df_Doppler.set_index('height', inplace=True) 
Dopmin = df_Doppler.min().min()
Dopmax = df_Doppler.max().max() 


#df_reflectivity_2D = pd.concat([reflectivity_2D_10min, height_1D], axis=1)
df_reflectivity_2D = pd.concat([reflectivity_2D_5min, height_1D], axis=1)
df_reflectivity_2D.set_index('height', inplace=True) 
refmin = df_reflectivity_2D.min().min()
refmax = df_reflectivity_2D.max().max() 
# preparation du csv pour highchat
Vect=np.arange(31, 0, -1)

Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []

colnum = df_Doppler.shape[1]
for k in range(colnum):
    Col1.append(df_Doppler.iloc[:,k])
    Col2.append(Vect)
    Col3.append(np.ones(31)*k)
    Col4.append(Dopmin)
    Col5.append(Dopmax)
    
   # Col3.append( [start.strftime("%H:%M")]*32)
   # start=start+timedelta(minutes=10)
   
flattened_list1 = [y for x in Col1 for y in x]
flattened_list2 = [y for x in Col2 for y in x]
flattened_list3 = [y for x in Col3 for y in x]

resultDoppler = pd.DataFrame([flattened_list3, flattened_list2, flattened_list1,Col4,Col5]).replace(np.nan,0).T
resultDoppler.to_csv('/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/resultDoppler.csv') 

# preparation du csv pour highchat
Vect=np.arange(31, 0, -1)

Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []

colnum = df_reflectivity_2D.shape[1]
for k in range(colnum):
    Col1.append(df_reflectivity_2D.iloc[:,k])
    Col2.append(Vect)
    Col3.append(np.ones(31)*k)
    Col4.append(refmin)
    Col5.append(refmax)
    
flattened_list1 = [y for x in Col1 for y in x]
flattened_list2 = [y for x in Col2 for y in x]
flattened_list3 = [y for x in Col3 for y in x]




resultreflectivity_2D = pd.DataFrame([flattened_list3, flattened_list2, flattened_list1,Col4,Col5]).replace(np.nan,0).T
resultreflectivity_2D.to_csv('/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/resultreflectivity_2D.csv') 


#=======================Travail sur 10 minutes avec pas de temps de 10s ========================================
#... Reflectivity
reflectivity = nc.variables['Ze'][:]
ones = np.ones(reflectivity.shape)
reflectivity_2D = pd.DataFrame(np.rot90(reflectivity))

# Pour travailler sur les 30 dernieres minutes 
reflectivity_2D_last = reflectivity_2D[reflectivity_2D.columns[-180:]].copy()
##... Doppler velocity
Dopplervel = nc.variables['W'][:]
Dopplervel_2D = pd.DataFrame(np.rot90(Dopplervel))

# Pour travailler sur les 30 dernieres minutes
Dopplervel_2D_last = Dopplervel_2D[Dopplervel_2D.columns[-180:]].copy()

#df_Doppler = pd.concat([Dopplervel_2D_10min, height_1D], axis=1)
df_Doppler = pd.concat([Dopplervel_2D_last, height_1D], axis=1)
df_Doppler.set_index('height', inplace=True) 
Dopmin = df_Doppler.min().min()
Dopmax = df_Doppler.max().max() 

df_reflectivity_2D = pd.concat([reflectivity_2D_last, height_1D], axis=1)
df_reflectivity_2D.set_index('height', inplace=True) 
refmin = df_reflectivity_2D.min().min()
refmax = df_reflectivity_2D.max().max() 
# preparation du csv pour highchat
Vect=np.arange(31, 0, -1)

Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []

colnum = df_Doppler.shape[1]
for k in range(colnum):
    Col1.append(df_Doppler.iloc[:,k])
    Col2.append(Vect)
    Col3.append(np.ones(31)*k)
    Col4.append(Dopmin)
    Col5.append(Dopmax)
    
   # Col3.append( [start.strftime("%H:%M")]*32)
   # start=start+timedelta(minutes=10)
   
flattened_list1 = [y for x in Col1 for y in x]
flattened_list2 = [y for x in Col2 for y in x]
flattened_list3 = [y for x in Col3 for y in x]

resultDoppler = pd.DataFrame([flattened_list3, flattened_list2, flattened_list1,Col4,Col5]).replace(np.nan,0).T
resultDoppler.to_csv('/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/resultDoppler_30min.csv') 

# preparation du csv pour highchat
Vect=np.arange(31, 0, -1)

Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []

colnum = df_reflectivity_2D.shape[1]
for k in range(colnum):
    Col1.append(df_reflectivity_2D.iloc[:,k])
    Col2.append(Vect)
    Col3.append(np.ones(31)*k)
    Col4.append(refmin)
    Col5.append(refmax)
    
flattened_list1 = [y for x in Col1 for y in x]
flattened_list2 = [y for x in Col2 for y in x]
flattened_list3 = [y for x in Col3 for y in x]




resultreflectivity_2D = pd.DataFrame([flattened_list3, flattened_list2, flattened_list1,Col4,Col5]).replace(np.nan,0).T
resultreflectivity_2D.to_csv('/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/resultreflectivity_2D_30min.csv') 






