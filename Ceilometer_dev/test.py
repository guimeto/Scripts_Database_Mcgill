# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:19:51 2020
 Script to plot CS135 data
@author: guillaume
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib
import matplotlib.colors as mcolors



fname0 = 'CS135.dat'
fnames = [fname0]

fichierIn = open(fname0,"r", encoding='cp437')
appended_data = []
for ligne in  fichierIn:
    appended_data.append(ligne.split(","))

df = pd.DataFrame(appended_data)

df = df[df.iloc[:,1].apply(lambda x: len(x)  > 1000)]

df = df.set_index(0)

raw_spectrum = []
for  index, row in df.iterrows():
    line_decimal = []
    for i in range(2048):
        back_scat = int(row[1][5*i:5*i+5],16)
        if back_scat>524287:
            back_scat += -1048576
        line_decimal.append(back_scat)                
    raw_spectrum.append(line_decimal)


raw_spectrum = pd.DataFrame(raw_spectrum)* 10**-8
raw_spectrum_log = np.log10(raw_spectrum)
raw_spectrum_log.index = pd.to_datetime(df.index, format='"%Y-%m-%d %I:%M:%S %p"') 

resam_df = raw_spectrum_log.resample('1min').mean()
resam_df_5min = raw_spectrum_log.resample('5min').mean()


colors = plt.cm.ocean(np.linspace(1,0,256))
# generating a smoothly-varying LinearSegmentedColormap
cmap = mcolors.LinearSegmentedColormap.from_list('colormap', colors)


fig, ax = plt.subplots(1, figsize=(10,2))
cst = ax.contourf(resam_df_5min.index[:], np.arange(2048)*5+100, resam_df_5min[:].T,100,cmap=cmap)

ax.set_xlabel('Time')
ax.set_ylabel('Height [m]')
# ax.set_xlim([datetime(year=2019,month=10,day=16,hour=3), datetime(year=2019,month=10,day=16,hour=9)])
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))

ax.set_ylim([0,6000])


cbZe=fig.colorbar(cst, ax=ax)
cbZe.set_label(r'[sr$^-1$ m$^-1$]')
cbZe.set_ticks([-7,-6,-5,-4])
cbZe.set_ticklabels([r'$10^{-7}$',r'$10^{-6}$',r'$10^{-5}$',r'$10^{-4}$'])
plt.tight_layout()

plt.savefig('CS135.png', format='png',bbox_to_anchor='tight' )

