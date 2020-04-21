# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:19:51 2020
 Script to plot CS135 data
@author: guillaume
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.dates import DateFormatter, DayLocator, HourLocator

fname0 = 'CS135_ok.dat'

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
resam_df_5min = raw_spectrum_log.resample('5min').mean()

colors = plt.cm.jet(np.linspace(1,0,256))
# generating a smoothly-varying LinearSegmentedColormap
cmap = mcolors.LinearSegmentedColormap.from_list('colormap', colors)

fig, ax = plt.subplots(1, figsize=(15,8))
#cst = ax.contourf(resam_df_5min.index[:], np.arange(2048)*5+100, resam_df_5min[:].T,100,cmap=cmap)

cst = ax.contourf(raw_spectrum_log.index[:], np.arange(2048)*5+100, raw_spectrum_log[:].T,100,cmap=cmap)

ax.set_xlabel('Time')
ax.set_ylabel('Height [m]')
#ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
# format the x tick marks
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

ax.xaxis.set_minor_formatter(DateFormatter('\n%d %b'))

ax.xaxis.set_major_locator(HourLocator(interval=1))
ax.xaxis.set_minor_locator(DayLocator())

ax.set_ylim([0,6000])

cbZe=fig.colorbar(cst, ax=ax)
cbZe.set_label(r'[sr$^-1$ m$^-1$]')
cbZe.set_ticks([-7,-6,-5,-4])
cbZe.set_ticklabels([r'$10^{-7}$',r'$10^{-6}$',r'$10^{-5}$',r'$10^{-4}$'])
plt.tight_layout()

plt.savefig('CS135_ok.png', format='png',bbox_to_anchor='tight' )


