import numpy as np
import mysql.connector
import datetime
from datetime import date
from datetime import timedelta as td
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


##############
yeari=2019
monthi=7
now = datetime.datetime.now()
yearf = 2019
monthf = 9

day_start=1
day_end = pd.date_range('{}-{}'.format(yearf, monthf), periods=1, freq='M').day.tolist()[0]

name = '20190701-20190901'

d0 = date(2019, 7, 1)
d1 = date(yearf, monthf, day_end)
delta = d1 - d0
nb_days = delta.days+1

## calcul du nombre d heures pour passer en UTC 
test_local=datetime.datetime.now()
test_utc=datetime.datetime.utcnow()
test_local=test_local.replace(minute=0, second=0, microsecond=0)
test_utc=test_utc.replace(minute=0, second=0, microsecond=0)
delta_h=(test_utc-test_local).total_seconds()/3600  # 3600 secondes dans 1 heure

start_local=datetime.datetime(yeari,monthi,day_start)
end_local=datetime.datetime(yearf,monthf,day_end)

start_utc=start_local+td(hours=delta_h)
end_utc=end_local+td(hours=delta_h)


# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
cnx = mysql.connector.connect(host = '192.168.0.22', database = 'stationuqam', user = 'dueymes', password = 'mysqlstation')
#192.168.0.22
# prepare a cursor object using cursor() method
cursor = cnx.cursor ()
query = ("select temperature from ReleveMeteo where temperature between -50 and 45 and date between %s and %s")

query2 = ("select humidite from ReleveMeteo where date  between %s and %s")
query3 = ("select pyranometreUP from ReleveMeteo where date  between %s and %s")
query4 = ("select pyranometreDW from ReleveMeteo where  date between %s and %s")
query5 = ("select pyregeometreUP from ReleveMeteo where date between %s and %s")
query6 = ("select pyregeometreDW from ReleveMeteo where  date between %s and %s")

t_data=np.zeros(nb_days)

h_data=np.zeros(nb_days)
py_up=np.zeros(nb_days)
py_dw=np.zeros(nb_days)
pg_up=np.zeros(nb_days)
pg_dw=np.zeros(nb_days)

t_data[:] = np.NAN

h_data[:] = np.NAN
py_up[:] = np.NAN
py_dw[:] = np.NAN
pg_up[:] = np.NAN
pg_dw[:] = np.NAN

incr=start_utc 
i=0
while incr <= end_utc:
  last = incr -datetime.timedelta(days=1)

  cursor.execute (query,(last,incr))
  if not cursor.rowcount:
#          print "No results found"
          i=i+1       
  else:
#          print "Results found"
          data = cursor.fetchall() 
          if len(data) == 0:
            t_data[i]=np.NAN
          else:
            mean = np.nanmean(data, axis=0)
            sd = np.nanstd(data, axis=0)     
            final_list = [x for x in data if (x > mean - 2 * sd)]
            final_list = [x for x in final_list if (x < mean + 2 * sd)] 
            if len(final_list) == 0:
              t_data[i]=np.NAN
            else:
              t_data[i]=round(np.mean(final_list),1)
            
  incr=incr + datetime.timedelta(days=1)
  i=i+1

incr=start_utc 
i=0
while incr <= end_utc:
  last = incr -datetime.timedelta(days=1)
#   print  incr
#   print  last

  cursor.execute (query2,(last,incr))
  data2 = cursor.fetchall()    
  h_data[i]=round(np.mean(data2))  

  cursor.execute (query3,(last,incr))
  data3 = cursor.fetchall()    
  py_up[i]=round(np.mean(data3)) 

  cursor.execute (query4,(last,incr))
  data4 = cursor.fetchall()    
  py_dw[i]=round(np.mean(data4))

  cursor.execute (query5,(last,incr))
  data5 = cursor.fetchall()    
  pg_up[i]=round(np.mean(data5))

  cursor.execute (query6,(last,incr))
  data6 = cursor.fetchall()    
  pg_dw[i]=round(np.mean(data6))

  incr=incr + datetime.timedelta(days=1)
  i=i+1

cursor.close ()


TIME=[]
for i in range(0,nb_days,1):
    start=(start_local+td(days=i)).strftime("%y-%m-%d_%H")
    TIME.append(start)

df = pd.DataFrame({'Date': TIME, 'Temperature moyenne': t_data, 'Humidite moyenne': h_data,'pyranometreUP': py_up, 'pyranometreDW':  py_dw,'pyregeometreUP': pg_up,'pyregeometreDW': pg_dw }, columns = ['Date','Temperature moyenne','Humidite moyenne', 'pyranometreUP', 'pyranometreDW','pyregeometreUP','pyregeometreDW']) 
df = df.set_index('Date')   
df.to_csv('/NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/UQAM_DATA_STATION_'+name+'.csv')

