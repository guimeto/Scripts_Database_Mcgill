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

query = ("select * from gault_metdata ORDER BY DATE DESC LIMIT 1;")

df = pd.read_sql_query(query, con=cnx)
df = df.set_index('DATE')

df.to_csv('./data/DATA_STATION_last.csv')

