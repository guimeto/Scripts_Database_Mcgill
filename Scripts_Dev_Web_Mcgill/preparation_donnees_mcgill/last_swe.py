import numpy as np
import mysql.connector
import datetime
import itertools
import pandas as pd

#ouverture de la connexion du serveur sql
#cnx = mysql.connector.connect(host = '192.168.0.22', database = 'stationuqam', user = 'dueymes', password = 'mysqlstation')
cnx = mysql.connector.connect(database = 'eos_mcgill_uqam', user = 'station', password = 'reli39,cao')


##### tavail en UTC pour la base de donnees
last_UTC = datetime.datetime.utcnow()
last_UTC = last_UTC.replace(second=0, microsecond=0)

lastdate = last_UTC.strftime("%Y-%m-%d %H:%M")+'%'

query = ("select * from gault_swe_6h ORDER BY DATE DESC LIMIT 1;")

df = pd.read_sql_query(query, con=cnx)
df = df.set_index('DATE')
df = df.round(3)
df.to_csv('/aos/home/gdueymes/tmp/prepare_data_website/Sentinel_1/data/station_last_swe.csv')

