#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:21:48 2018

@author: UQAM
"""
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.dates import DateFormatter, date2num
import matplotlib
import datetime

#=============================================================================
#... create the figure
#....................................
fig=plt.figure(figsize=(7,9))
#... reflectivity 
ax1=fig.add_axes([0.13,0.83,0.85,0.13])
ax1.set_title('(a) Reflectivity', fontsize = 10) 
#... Doppler velocity
ax2=fig.add_axes([0.13,0.62,0.85,0.13])
ax2.set_title('(b) Doppler velocity', fontsize = 10) 
##... Temperature
#ax3=fig.add_axes([0.13,0.44,0.68,0.1])
#ax3.set_title('(c) Temperature', fontsize = 10) 
##... Wind speed
#ax4=fig.add_axes([0.13,0.26,0.68,0.1])
#ax4.set_title('(d) Wind speed', fontsize = 10) 
##... accumulated precipitation
#ax5=fig.add_axes([0.13,0.08,0.68,0.1])
#ax5.set_title('(e) Accumulated precipitation', fontsize = 10) 
##... snow depth
#ax6=fig.add_axes([0.13,0.04,0.68,0.08])
#ax6.set_title('(f) Snow depth', fontsize = 10) 
#=============================================================================
#=============================================================================
#...Read the MRR data
#... read the netcdf file after QC
filename = './Gault_MRR2_20200401.nc'
nc = Dataset(filename)

#... To plot the MRR timeseries
height       = nc.variables['height'][:]
height_2D = np.rot90(height)

readtime     = nc.variables['time'][:] 
x_unstag = np.tile(readtime, (31, 1))

#... colors number for the colormap
nb_couleur = 256
    
#=============================================================================
#... Reflectivity
reflectivity = nc.variables['Ze'][:]
ones = np.ones(reflectivity.shape)
reflectivity_2D = np.rot90(reflectivity)

for i in range(x_unstag.shape[0]):
    t = x_unstag[i,:]
    t = pd.to_datetime(t,unit='s')
    t = np.array(t)
    if i == 0:
        temps = t.reshape(1,t.shape[0])
    else:
        temps = np.append(temps,t.reshape(1,t.shape[0]),axis=0)

  
plotCF = ax1.contourf(temps,height_2D,reflectivity_2D)
level = np.linspace(-15, 46, nb_couleur)
label_colormap = 'Ze [dBz]'
cbZe=plt.colorbar(plotCF,ax=ax1)
cbZe.set_label(label_colormap,size=10)
cbZe.set_ticks([-15, 0, 15, 30, 45])
cbZe.ax.tick_params(labelsize=10)
 
ax1.set_ylim(0,1000)
ax1.set_ylabel("Height \n AGL [km]",size=10)
ax1.tick_params(axis='both',labelsize=10)
ax1.set_xticklabels([])
#ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m-%d %H:%M')) #to plot with the date with day/time
ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))


##... Doppler velocity
Dopplervel = nc.variables['W'][:]
Dopplervel_2D = np.rot90(Dopplervel)

for i in range(x_unstag.shape[0]):
    t = x_unstag[i,:]
    t_mrr = pd.to_datetime(t,unit='s')
    t = np.array(t_mrr)
    if i == 0:
        temps = t.reshape(1,t.shape[0])
    else:
        temps = np.append(temps,t.reshape(1,t.shape[0]),axis=0)

str_time = str(t_mrr[0].year)+'-'+str(t_mrr[0].month)+'-'+str(t_mrr[0].day)
str_time_1 = str_time
t1 = pd.Timestamp(str_time)
str_time = str(t_mrr[-1].year)+'-'+str(t_mrr[-1].month)+'-'+str(t_mrr[-1].day)
t2 = pd.Timestamp(str_time)

level = np.linspace(-4., 4., nb_couleur)
cmap = plt.get_cmap('bwr')    
plotCF = ax2.contourf(temps,height_2D,Dopplervel_2D,level,cmap=cmap,extend="both")

label_colormap = 'W [m/s]'
cbZe=plt.colorbar(plotCF,ax=ax2)
cbZe.set_label(label_colormap,size=10)
cbZe.set_ticks([-4, -2., 0, 2, 4])
cbZe.ax.tick_params(labelsize=10)
 
ax2.set_ylim(0,1000)
ax2.set_ylabel("Height \n AGL [km]",size=10)
ax2.tick_params(axis='both',labelsize=10)
ax2.set_xticklabels([])
#ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m-%d %H:%M')) #to plot with the date with day/time
ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))

##=============================================================================
##=============================================================================
##...Read Met data
#metdata = "./metdata_Aug-Nov_2018.csv"
#data = pd.read_csv(metdata,sep = ',',index_col=False) #,names = ['Year',
##                     'Month','Day','Hour','Minute','Second','temp1','temp2','type'],
##                     converters={'Year': str, 'Month': str,'Day': str,
##                                 'Hour': str,'Minute': str,'Second': str,})
###
#time_metdata = pd.to_datetime(data['Timestamp (MST)']).values
#limMRR = ax2.get_xlim()
#tick2 = ax2.get_xticks()
#data.index = time_metdata
#data_daily = data[t1:t2]
#time_daily = data_daily.index
##=============================================================================
##... air temperature
#temperature = data_daily['Air Temp (degC)']
#
#ax3.plot(time_daily,temperature,'k', label = "T")
#ax3.set_xlim(limMRR)
#ax3.set_xticks(tick2)
#ax3.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
#ax3.set_ylabel("Temp \n [degC]",size=10)
#
##=============================================================================
##... wind speed
#windspeed = data_daily['Wind Speed at 10m (m/s)']
#
#ax4.plot(time_daily,windspeed,'k', label = "U")
#limMRR = ax2.get_xlim()
#ax4.set_xlim(limMRR)
#tick2 = ax2.get_xticks()
#ax4.set_xticks(tick2)
#ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
#ax4.set_ylabel("Wind \n speed \n [m/s]",size=10)
#
##=============================================================================
##... Accumultaed precipitation
#accpcpn = data_daily['Weighing Precip Gauge VW123 (mm)']
#accpcpn_daily = accpcpn-accpcpn[0]
#ax5.plot(time_daily,accpcpn_daily,'k', label = "AC")
#
##accpcpn_cor = data_daily['Weighing Precip Gauge VW123 Corrected (mm)']
##accpcpn_cor_daily = accpcpn_cor-accpcpn_cor[0]
##ax5.plot(time_daily,accpcpn_cor_daily,'b', label = "AC_cor")
#
#limMRR = ax2.get_xlim()
#ax5.set_xlim(limMRR)
#tick2 = ax2.get_xticks()
#ax5.set_xticks(tick2)
#ax5.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
#ax5.set_ylabel("Acc \n pcpn [mm]",size=10)
#
#ax5.set_xlabel("Time (MST) starting on "+str_time_1,size=10)


#uncomment to plot snow depth or any other variable
#we would need to modify the number/size of plots
##=============================================================================
##... Accumultaed precipitation
#snowdepth = data_daily['Snow Depth (m)']
#
#snowdepth_daily = snowdepth-snowdepth[0]
#
#ax6.plot(time_daily,snowdepth_daily,'k', label = "SD")
#limMRR = ax2.get_xlim()
#ax6.set_xlim(limMRR)
#tick2 = ax2.get_xticks()
#ax6.set_xticks(tick2)
#ax6.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
#ax6.set_ylabel("Snow \n Depth [m]",size=10)

#save the figure
fig.savefig('MRR_metdata_'+str_time_1+'.pdf')