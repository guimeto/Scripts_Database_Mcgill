import numpy as np
import mysql.connector
import datetime
import itertools
import pandas as pd

#ouverture de la connexion du serveur sql
cnx = mysql.connector.connect(host = '192.168.0.22', database = 'stationuqam', user = 'dueymes', password = 'mysqlstation')
#132.208.147.66
############## Partie a modififer 
station='Station_UQAM'
##### tavail en UTC pour la base de donnees
end_UTC=datetime.datetime.utcnow()
end_local=datetime.datetime.now()
##### definition des pas de temps requetes pour chaque variable
query1 = ("select temperature from ReleveMeteo where date between %s and %s")
query2 = ("select humidite from ReleveMeteo where date between %s and %s")
query3 = ("select pression from ReleveMeteo where date between %s and %s")
query4 = ("select date from ReleveMeteo where date between %s and %s")
query5 = ("select directionVent from ReleveMeteo where date between %s and %s")
query6 = ("select vitesseVent from ReleveMeteo where date  between %s and %s")

#####   definition des champs 
temp_data=np.zeros(1,'float')
temp_data[:] = np.NAN
humi_data=np.zeros(1,"float")
humi_data[:] = np.NAN
press_data=np.zeros(1,"float")
press_data[:] = np.NAN
vect_U=np.zeros(10,"float")
vect_U[:] = np.NAN
vect_V=np.zeros(10,"float")
vect_V[:] = np.NAN

mean_dir=np.zeros(1,"float")
mean_dir[:] = np.NAN
mean_mod=np.zeros(1,"float")
mean_mod[:] = np.NAN

#####  DEBUT DE LA BOUCLE HORAIRE   
incr=end_UTC
i=0
#### travail sur le vent
# # # # # # # # # on travaille sur les 10 dernieres  minutes pou le vent
last = incr - datetime.timedelta(minutes=10)
cursor = cnx.cursor ()
cursor.execute (query5,(last,incr))
dirwind = cursor.fetchall()    
cursor.close () 

cursor = cnx.cursor ()
cursor.execute (query6,(last,incr))
mod = cursor.fetchall()    
cursor.close ()
ws=list(itertools.chain.from_iterable(mod))
wd=list(itertools.chain.from_iterable(dirwind))
mean_dir[i]=round(np.mean(wd))
mean_mod[i]=round(np.mean(ws)*3.6)

#### travail sur la temperature
last = incr - datetime.timedelta(minutes=5)
cursor = cnx.cursor ()
cursor.execute (query1,(last,incr))
data1 = cursor.fetchall()
temp_data[i] = round(np.mean(data1[-1]),1)
cursor.close ()

#### travail sur l humidite
last = incr - datetime.timedelta(minutes=5)
cursor = cnx.cursor ()
cursor.execute (query2,(last,incr))
data2 = cursor.fetchall() 
humi_data[i] = round(np.mean(data2[-1]))  
cursor.close ()

#### travail sur la pression
last = incr - datetime.timedelta(minutes=5)
cursor = cnx.cursor ()
cursor.execute (query3,(last,incr))
data3 = cursor.fetchall() 
corr_data3=np.mean(data3[-1])*np.exp((0.08/(29.3*np.mean(data1[-1]))))    #### correction de la pression par l equation hypsometrique: station a 80m 
press_data[i] = round(corr_data3)   
cursor.close ()

Time=  end_local.strftime("%H-%M")

df = pd.DataFrame({'Temps':Time, 'pressure': press_data,'Temperature': temp_data,'Humidite': humi_data,'Dir_wind':  mean_dir,'Mod_wind':   mean_mod}, columns = ['Temps','pressure', 'Temperature','Humidite','Dir_wind','Mod_wind'])   
df.to_csv('/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/UQAM_DATA_STATION_last.csv')

