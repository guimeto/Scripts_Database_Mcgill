# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:19:51 2020
 Script to plot CS135 data
@author: guillaume
"""
import numpy as np
import pandas as pd
from netCDF4 import Dataset
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as md
import seaborn as sns
import xarray as xr

now = datetime.now()
year, month, day, hour = now.year, now.month, now.day, now.hour


fname0 = '/storage1/gault_transit/CS135/CS135.dat'
fnames = [fname0]

fichierIn = open(fname0,"r", encoding='cp437')
appended_data = []
for ligne in  fichierIn:
    appended_data.append(ligne.split(","))

df = pd.DataFrame(appended_data)
df = df[~df.iloc[:,1].isnull()] 

df = df[df.iloc[:,1].apply(lambda x: len(x)  > 1000)]
df = df.set_index(0)
for i in df.index:
    if len(i) == 12:
        df.rename(index={i:'"' + i.replace('"','')+ ' 12:00:00 AM"'},inplace=True)   

raw_spectrum = []
for  index, row in df.iterrows():
    line_decimal = [int(i,16) for i in map(''.join, zip(*[iter(row[1])]*5))]
    raw_spectrum.append(line_decimal)
    
raw_spectrum = pd.DataFrame(raw_spectrum)
raw_spectrum[raw_spectrum>524287]+= -1048576
raw_spectrum_log = np.log10(raw_spectrum* 10**-8)
raw_spectrum_log.index = pd.to_datetime(df.index, format='"%Y-%m-%d %I:%M:%S %p"') 

#instantiate NetCDF output
dataset = Dataset('CS135_'+str(month)+'_'+str(day)+'_'+str(hour)+'.nc', "w", format="NETCDF4_CLASSIC")

# Create the time dimension - with unlimited length
time_dim = dataset.createDimension("time", None)

# Create the time variable
base_time = np.datetime64('1970-01-01T00:00:00')
#timeoffsets = (raw_spectrum_log.index - base_time).total_seconds().get_values()

timeoffsets = (raw_spectrum_log.index - base_time).total_seconds()
timeoffsets = [float(np_float) for np_float in timeoffsets]

time_units = "seconds since " + base_time.astype(datetime).strftime('%Y-%m-%d %I:%M:%S %p')
time_var = dataset.createVariable("time", np.float64, ("time",))
time_var.units = time_units
time_var.fill_value = np.nan
time_var.standard_name = "time"
time_var.calendar = "standard"
time_var[:] = timeoffsets[:]


#Create the altitude dimension
altitude_dim = dataset.createDimension("altitude", len(raw_spectrum_log.columns))

altitude_var = dataset.createVariable("altitude", np.float32, ("altitude",))
altitude_var.units = 'm'
altitude_var.standard_name = 'altitude'
altitude_var.long_name = 'Geometric height above geoid (WGS84)'
altitude_var.axis = 'Z'
altitude_var[:] = np.arange(2048)*5+100

#dataset.processing_software_url = subprocess.check_output(["git", "remote", "-v"]).split()[1] # get the git repository URL
#dataset.processing_software_version = subprocess.check_output(['git','rev-parse', '--short', 'HEAD']).strip() #record the Git revision
dataset.time_coverage_start = raw_spectrum_log.index[0].strftime('%Y-%m-%d %I:%M:%S %p')
dataset.time_coverage_end = raw_spectrum_log.index[-1].strftime('%Y-%m-%d %I:%M:%S %p')

backscatter = dataset.createVariable('backscatter_coefficient', 'float32', ('time','altitude'))
backscatter.units = 'm-1 sr-1'
backscatter.standard_name = 'attenuated_aerosol_backscatter_coefficient'
backscatter.long_name = 'Attenuated Aerosol Backscatter Coefficient'
backscatter.fill_value = -1.00e20
backscatter[:] = raw_spectrum_log.values
dataset.setncattr('Conventions',"CF-1.6, NCAS-AMF-1.0")
dataset.close()

'''Does a quick-and-dirty plot for testing purposes'''

var = xr.open_dataset('CS135_'+str(month)+'_'+str(day)+'_'+str(hour)+'.nc')
fig=plt.figure(figsize=(22,12), frameon=True)  
varT = var.transpose()
varT.backscatter_coefficient.plot()
plt.savefig('./CS135_'+str(hour)+'.png', bbox_inches='tight', pad_inches=0.1)



