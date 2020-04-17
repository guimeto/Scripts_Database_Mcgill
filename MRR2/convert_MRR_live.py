# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:20:17 2019

@author: guillaume
Script permettant de faire la conversion des donnees du MRR2 au format Netcdf 
Le present code travaille aux 10minutes
"""
import core_original
from datetime import datetime, timedelta
import os
from os.path import exists

#now = datetime.now() -  timedelta(days=1)
now = datetime.utcnow()
year, month, day = now.year, now.month, now.day


path_ori = '/StationMeteo_01/radar/MRR2/RawSpectra/'
path =  '/StationMeteo_01/radar/MRR2/'

MRR2_file  = path_ori + str(year)+'{:02d}'.format(month)+'/'+'{:02d}'.format(month)+'{:02d}'.format(day)+'.raw'

rawData = core_original.mrrRawData(MRR2_file)
Proc0 = core_original.MrrZe(rawData)
Proc0.rawToSnow()  

pathout = path + 'RawSpectra_Netcdf/' + str(year)+'{:02d}'.format(month)+ '/'
if exists(pathout):
    pass
else:
    os.makedirs(pathout)

Proc0.writeNetCDF(pathout + 'UQAM_MRR2_'+str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)+'.nc',ncForm="NETCDF3_CLASSIC")

