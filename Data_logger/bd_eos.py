# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:32:03 2020
function to connect on eos_mcgill_uqam database
@author: guillaume
"""
import mysql.connector
def bd_eos(releveMeteoQuery):
        cnx = mysql.connector.connect(user ='root', 
                                      database = 'eos_mcgill_uqam', 
                                      password = 'uq2012am')
        
#Création d'un curseur et exécution de la requête SQL passée en paramètre
        cursor = cnx.cursor ()
        cursor.execute(releveMeteoQuery)
        cnx.commit()
        cursor.close ()

