# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:20:17 2019

@author: guillaume
"""
import core_original
from calendar import monthrange
import os
from os.path import exists

list_mon = [1]
year = 2020
path_ori = '/storage1/gault/mrr_data/RawSpectra/'
path = '/storage1/gault/mrr_data/'

for month in list_mon:
    if month == 1:
        for day in range(24,29):

            MRR2_file  = path_ori + str(year)+'{:02d}'.format(month)+'/'+'{:02d}'.format(month)+'{:02d}'.format(day)+'.raw'
            rawData = core_original.mrrRawData(MRR2_file)
            Proc0 = core_original.MrrZe(rawData)
            Proc0.rawToSnow()
            pathout = path + 'RawSpectra_Netcdf/' + str(year)+'{:02d}'.format(month) + '/'
            if exists(pathout):
                pass
            else:
                os.makedirs(pathout)

            Proc0.writeNetCDF(pathout + 'Gault_MRR2_'+str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)+'.nc',ncForm="NETCDF3_CLASSIC")
            print("%d/%d/2019 ---- conversion OK ---- " % (day, month) )
           
    else:

        for day in range(1,monthrange(year, month)[1]+1):
            MRR2_file    = path_ori + str(year)+'{:02d}'.format(month)+'/'+'{:02d}'.format(month)+'{:02d}'.format(day)+'.raw'

            rawData = core_original.mrrRawData(MRR2_file)
            Proc0 = core_original.MrrZe(rawData)
            Proc0.rawToSnow()  

            pathout = path + 'RawSpectra_Netcdf/' + str(year)+'{:02d}'.format(month)+ '/'
            if exists(pathout):
                pass
            else:
                os.makedirs(pathout)

            Proc0.writeNetCDF(pathout + 'Gault_MRR2_'+str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)+'.nc',ncForm="NETCDF3_CLASSIC")
            print("%d/%d/2019 ---- conversion OK ---- " % (day, month) )
