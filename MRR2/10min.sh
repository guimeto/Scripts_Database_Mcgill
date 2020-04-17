#!/bin/bash
. /etc/profile
. ~/.profile  
module load python2
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees_MRR/convert_MRR_live.py
python /NFS2_RESCUE2/stationuqam/programmes/preparation_donnees_MRR/MRR2_Netcdf_to_heatmap.py
module unload python2
