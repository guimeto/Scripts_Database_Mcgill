#!/bin/bash
. /etc/profile
. ~/.profile  
module load python2
source activate soup
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/last_value.py
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/scrapping_data_ECCC.py
source deactivate soup
module unload python2 

module load python3
source activate soup 
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/scrapping_gif_ECCC.py
source deactivate soup
module unload python3

#!scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/parsivel.png dueymes@docker-01.scta.uqam.ca:/var/www/html/stationuqam_uqam_ca_docker/www/stationuqam/uqam/static/documentation/img/
#!scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.csv dueymes@docker-01.scta.uqam.ca:/var/www/html/stationuqam_uqam_ca_docker/www/stationuqam/uqam/static/shared/data/
#!scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.json dueymes@docker-01.scta.uqam.ca:/var/www/html/stationuqam_uqam_ca_docker/www/stationuqam/uqam/static/shared/data/


#!scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.csv dueymes@docker-01.scta.uqam.ca:/var/www/html/uqam_station_docker/uqam_station_website/staticfiles/
#!scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.gif dueymes@docker-01.scta.uqam.ca:/var/www/html/uqam_station_docker/uqam_station_website/staticfiles/
#!scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.png dueymes@docker-01.scta.uqam.ca:/var/www/html/uqam_station_docker/uqam_station_website/staticfiles/

#Pour les png et gifs
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.png dueymes@web2.infra-pk.uqam.ca:/var/www/html/station.escer.uqam.ca/resources/images/
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.gif dueymes@web2.infra-pk.uqam.ca:/var/www/html/station.escer.uqam.ca/resources/images/

#Pour toutes les données csv json
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.csv dueymes@web2.infra-pk.uqam.ca:/var/www/html/station.escer.uqam.ca/resources/data/
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.json dueymes@web2.infra-pk.uqam.ca:/var/www/html/station.escer.uqam.ca/resources/data/

#Pour les png et gifs
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.png /StationMeteo_01/web2_VRSI/images/
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.gif /StationMeteo_01/web2_VRSI/images/

#Pour toutes les données csv json
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.csv /StationMeteo_01/web2_VRSI/data/
scp -r /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/data/*.json /StationMeteo_01/web2_VRSI/data/

