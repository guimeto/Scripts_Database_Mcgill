#!/bin/bash
#echo $PATH
. /etc/profile
. ~/.profile  
module load python2
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/Create_CSV_today.py
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees/Create_heatmap.py
