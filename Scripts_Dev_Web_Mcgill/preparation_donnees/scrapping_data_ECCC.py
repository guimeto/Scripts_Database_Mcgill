#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:15:46 2019

@author: guillaume
"""
print('import librairies')


import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')
import requests
import pandas as pd
# Téléchargement de la page web
page = requests.get("https://meteo.gc.ca/city/pages/qc-147_metric_f.html")

print('On est dans le code !! ')

#Utilisation de BeautifulSoup pour analyser le code html
from bs4 import BeautifulSoup

print('On est toujours dans le code !! ')
# on va analyser le contenu précédent avec BeautifulSoup 
soup = BeautifulSoup(page.content,'html.parser')

conditions = soup.find(id="mainContent")
col1 = conditions.find_all(class_="dl-horizontal wxo-conds-col1")
today1 = col1[1]
#print(today1.prettify())
tmp1  = today1.select(".mrgn-bttm-0")
# print(tmp1)

short_desc = [tmp1[0].get_text()]
pression = [tmp1[1].get_text().replace('\n','')]
tendance =[ tmp1[3].get_text()]

col2 = conditions.find_all(class_="dl-horizontal wxo-conds-col2")
today2 = col2[1]
# print(today2.prettify())
tmp2  = today2.select(".mrgn-bttm-0")
# print(tmp2)

temperature = [tmp2[0].get_text().replace('\n','')]
rosee = [tmp2[2].get_text().replace('\n','')]
humidite = [tmp2[4].get_text().replace('\n','')]

col3 = conditions.find_all(class_="dl-horizontal wxo-conds-col3")
today3 = col3[1]
# print(today2.prettify())
tmp3  = today3.select(".mrgn-bttm-0")
# print(tmp3)

vent = [tmp3[0].get_text().replace('\n','')]
visibilite = [tmp3[2].get_text().replace('\n','')]

weather = pd.DataFrame({"short_desc": short_desc,
                        "pression":   pression,
                        "Tendance":   tendance,
                        "temperature": temperature,
                        "temperature_rosee":   rosee,
                        "humidite":   humidite,
                        "vent":   vent,
                        "visibilite":   visibilite,
                       })

print('Debut Sauvegarde!')

weather.to_csv("/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/current.csv", header = True, sep = ',',encoding='utf-8')
print('sauvegarde current')
period_tags = soup.find(id="mainContent")
row1 = period_tags.find_all(class_="div-row div-row1 div-row-head")

period_tags = soup.find(id="mainContent")
row1 = period_tags.find_all(class_="div-row div-row1 div-row-head")
periods = [pt.get_text().replace('\xa0', ' ').replace('\n','') for pt in row1]

period_tags = soup.find(id="mainContent")
row2 = period_tags.find_all(class_="div-row div-row2 div-row-data")


temperature_f = [pt.get_text().split('\n')[1][0:4] for pt in row2]

temperature_2=[]
for val in enumerate(temperature_f):
    temperature_2.append(val[1].split('C')[0] + 'C')
temperature_2

conditions_f = [pt.get_text().split('\n')[3] for pt in row2]

weather_f = pd.DataFrame({"Period": periods,
                       "temperature_f": temperature_2,
                       "conditions_f":conditions_f,
                       })
print('Fin du code')    

weather_f.to_csv("/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/forecast.csv", header = True, sep = ',',encoding='utf-8')
print('sauvegarde futur')
