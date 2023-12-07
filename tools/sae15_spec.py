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
    # Calcul du taux de disponibilité pour chaque station
    rate = (stations_df.groupby(['stationCode'])['numDocksAvailable'].sum() / 
            (stations_df.groupby(['stationCode'])['numBikesAvailable'].sum() + 
             stations_df.groupby(['stationCode'])['numDocksAvailable'].sum())).fillna(0) * 100
    
    # Conversion du résultat en dictionnaire
    rate = rate.to_dict()

    # Retourne le dictionnaire de taux de disponibilité des stands
    return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des vélos (en %)
def availableBikesRate(stations_df):
    # Calcul du taux de disponibilité de vélos pour chaque station
    rate = (stations_df.groupby(['stationCode'])['numBikesAvailable'].sum() / 
            (stations_df.groupby(['stationCode'])['numBikesAvailable'].sum() + 
             stations_df.groupby(['stationCode'])['numDocksAvailable'].sum())).fillna(0) * 100
    
    # Conversion du résultat en dictionnaire
    rate = rate.to_dict()

    # Retourne le dictionnaire de taux de disponibilité des vélos
    return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne la date la plus récente de la mise à jour des données dynamiques
def getLatestDate(stations_df) :
    # Extraction et formatage de la date la plus récente des rapports des stations
    date = stations_df['last_reported'].apply(lambda x: dt.datetime.fromtimestamp(x).strftime('%d-%m-%Y %H:%M:%S'))

    # Retourne la série de dates formatées
    return date

#------------------------------------------------------------------------------------------------
# fonction qui retourne les mesures statistiques  d'une clé du DataFrame de stations
def stationStatistics(stations_df_key):
    # Initialisation d'un dictionnaire pour stocker les mesures statistiques
    stats = dict()

    # Calcul des mesures statistiques
    stats['mean'] = stations_df_key.mean()
    stats['count'] = stations_df_key.count()
    stats['std'] = stations_df_key.std()
    stats['min'] = stations_df_key.min()
    stats['max'] = stations_df_key.max()

    # Retourne le dictionnaire de mesures statistiques
    return stats

#------------------------------------------------------------------------------------------------
# fonction qui exporte au format HTML le DataFrame des mesures statistiques
def exportStatistics(stats_df, filename):
    # Convertit le DataFrame en une représentation HTML
    html = stats_df.to_html()

    # Écrit le HTML dans un fichier
    with open(filename, "w") as text_file:
        text_file.write(html)

    # Aucune valeur n'est retournée, le fichier est écrit directement sur le disque.
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

