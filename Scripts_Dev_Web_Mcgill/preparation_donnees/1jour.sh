#!/bin/bash
. /etc/profile
. ~/.profile  
module load python2
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/Create_current_Rose_data.py
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/create_data_CSV_alldata_UQAM.py
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/get_data_toradial_UQAM.py
