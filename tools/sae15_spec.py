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

  html = stats_df.to_html() 
    
  # write html to file 
  text_file = open(filename, "w") 
  text_file.write(html) 
  text_file.close() 

  return

#------------------------------------------------------------------------------------------------
# fonction qui affiche et exporte la carte des stations Vélibs géolocalisées
def exportCityMap(geo_stations, marker_size, marker_color, title, date=None, filename=None) :
  # figure et axes
  f, axes = plt.subplots(1, figsize=(15,15))

  # conversion des coordonnées dans le système approprié
  geo_data_with_map = geo_stations.to_crs(epsg=3857)
  
  # affichage en fonction des variables passées en argument
  geo_data_with_map.plot(marker_size, markersize=3*marker_size, cmap=marker_color, ax=axes)

  # effacement des axes gradués
  axes.set_axis_off()

  # ajout du fond de carte correspondant aux coordonnées géographiques des stations
  ctx.add_basemap(axes)

  # affichage du titre avec la date de mise à jour
  plt.title(title + " dernière mise à jour " + str(date))

  # sauvegarde de la carte sur le Drive
  plt.savefig(filename)
  
  # affichage forçé
  plt.show()

  return

