import json
import urllib
import requests
import pandas as pd
import geopandas as gpd

def loadVelibInformation() :
  json_data = json.loads(urllib.request.urlopen('https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json').read()) 
  return(json_data)

def loadVelibStatus() :
  json_data = json.loads(urllib.request.urlopen('https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json').read())
  return(json_data)

def getVelibStations(json_data) :
  return json_data['data']['stations']

def exportToGeoDF(data_df) :
  geom = gpd.points_from_xy(data_df["lon"], data_df["lat"])
  data_geodf = gpd.GeoDataFrame(data_df, crs="EPSG:4326", geometry=geom)
  return data_geodf
