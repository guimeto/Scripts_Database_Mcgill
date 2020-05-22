# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:15:46 2019

@author: guillaume
"""

import requests

# Téléchargement de la page web Sentinel 1 : Mont saint hilaire 
page = requests.get("https://meteo.gc.ca/city/pages/qc-92_metric_f.html")

#Utilisation de BeautifulSoup pour analyser le code html
from bs4 import BeautifulSoup
# on va analyser le contenu précédent avec BeautifulSoup 
soup = BeautifulSoup(page.content,'html.parser')
period_tags = soup.find(id="mainContent")

from urllib import request
row3 = period_tags.find_all(class_="div-row div-row2 div-row-data")
i = 0
for images in row3:
    s = images.find('img')
    f = open('/aos/home/gdueymes/tmp/prepare_data_website/Sentinel_1/data/' + str(i) + '.gif', 'wb')
    f.write(request.urlopen("https://meteo.gc.ca/weathericons/"+str(s)[str(s).find('gif')-3:(str(s).find('gif'))-1]+".gif").read())
    f.close() 
    i += 1 






