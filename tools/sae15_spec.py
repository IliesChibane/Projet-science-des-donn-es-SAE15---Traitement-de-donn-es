#################################################################################################
# FONCTIONS SPECIFIQUES
#------------------------------------------------------------------------------------------------
# Les fonctions à coder selon l'échancier donné dans le document SAE15-Présentation.ipynb
#################################################################################################

#------------------------------------------------------------------------------------------------
# importations des modules utiles
#
# attention : geopandas et contextily doivent être installés avant l'importation
# utiliser pour cela !pip install ... dans le Notebook principal
#
import pandas as pd             # pour la mise en forme, l'analyse et la publication
import datetime as dt           # pour la détermination de la date
import geopandas as gpd         # pour la spatialisation des données
import matplotlib.pyplot as plt # pour les graphes
import contextily as ctx        # pour l'utilisation de cartes géographiques

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des stands (en %)
def availableDocksRate(stations_df) :

  rate = (stations_df.groupby(['stationCode'])['numDocksAvailable'].sum() / (stations_df.groupby(['stationCode'])['numBikesAvailable'].sum() + stations_df.groupby(['stationCode'])['numDocksAvailable'].sum())).fillna(0) * 100
  rate = rate.to_dict()

  return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des vélos (en %)
def availableBikesRate(stations_df) :

  rate = (stations_df.groupby(['stationCode'])['numBikesAvailable'].sum() / (stations_df.groupby(['stationCode'])['numBikesAvailable'].sum() + stations_df.groupby(['stationCode'])['numDocksAvailable'].sum())).fillna(0) * 100
  rate = rate.to_dict()

  return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne la date la plus récente de la mise à jour des données dynamiques
def getLatestDate(stations_df) :

  date = stations_df['last_reported'].apply(lambda x: dt.datetime.fromtimestamp(x).strftime('%d-%m-%Y %H:%M:%S'))

  return date

#------------------------------------------------------------------------------------------------
# fonction qui retourne les mesures statistiques  d'une clé du DataFrame de stations
def stationStatistics(stations_df_key) :

  stats = dict()

  stats['mean'] = stations_df_key.mean()
  stats['count'] = stations_df_key.count()
  stats['std'] = stations_df_key.std()
  stats['min'] = stations_df_key.min()
  stats['max'] = stations_df_key.max()

  return stats

#------------------------------------------------------------------------------------------------
# fonction qui exporte au format HTML le DataFrame des mesures statistiques
def exportStatistics(stats_df, filename) :

  # votre code...

  return

#------------------------------------------------------------------------------------------------
# fonction qui affiche et exporte la carte des stations Vélibs géolocalisées
def exportCityMap(geo_stations, marker_size, marker_color, title, date=None, filename=None) :
  # figure et axes
  # votre code...

  # conversion des coordonnées dans le système approprié
  # votre code...
  
  # affichage en fonction des variables passées en argument
  # votre code...

  # effacement des axes gradués
  # votre code...

  # ajout du fond de carte correspondant aux coordonnées géographiques des stations
  # votre code...

  # affichage du titre avec la date de mise à jour
  # votre code...

  # sauvegarde de la carte sur le Drive
  # votre code...
  
  # affichage forçé
  # votre code...

  return 

