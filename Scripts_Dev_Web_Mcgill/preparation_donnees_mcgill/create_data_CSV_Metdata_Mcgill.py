import numpy as np
import mysql.connector
import datetime
from datetime import date
from datetime import timedelta as td
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

##############
now = datetime.datetime.now()
yearf = now.year
monthf = now.month

yeari = (now - td(days = 7)).year
monthi = (now - td(days = 7)).month # on remonte de 1 semaines
day_start= (now - td(days = 7)).day

day_end = pd.date_range('{}-{}'.format(yearf, monthf), periods=1, freq='M').day.tolist()[0]

## calcul du nombre d heures pour passer en UTC 
test_local=datetime.datetime.now()
test_utc=datetime.datetime.utcnow()
test_local=test_local.replace(minute=0, second=0, microsecond=0)
test_utc=test_utc.replace(minute=0, second=0, microsecond=0)

delta_h=(test_utc-test_local).total_seconds()/3600  # 3600 secondes dans 1 heure

start_local = datetime.datetime(yeari,monthi,day_start)
end_local=datetime.datetime(yearf,monthf,day_end)

start_utc=start_local+td(hours=delta_h)
end_utc=end_local+td(hours=delta_h)

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own

#cnx = mysql.connector.connect(host = '192.168.0.22', database = 'eos_mcgill_uqam', user = 'station', password = 'reli39,cao')
cnx = mysql.connector.connect(database = 'eos_mcgill_uqam', user = 'station', password = 'reli39,cao')

startdate = start_utc.strftime("%Y-%m-%d")+'%'
enddate   = end_utc.strftime("%Y-%m-%d")+'%'

#query = ("select Date, Temp1_Avg, Temp2_Avg, Temp3_Avg, Temp4_Avg, Temp5_Avg, Temp6_Avg, Temp7_Avg, RH1, RH2, RH3, RH4, RH5, RH6, RH7 from gault_metdata where Date BETWEEN %(mindate)s AND %(maxdate)s")
query = ("select * from gault_metdata where Date BETWEEN %(mindate)s AND %(maxdate)s")
df = pd.read_sql_query(query, con=cnx, params={'mindate': startdate, 'maxdate': enddate})
   
df = df.set_index('DATE')
df = df.resample('15Min').mean()
df = df.round(2)
df = df.replace(-999, np.nan)
df.to_csv('/aos/home/gdueymes/tmp/prepare_data_website/Sentinel_1/data/station_Metdata.csv')

