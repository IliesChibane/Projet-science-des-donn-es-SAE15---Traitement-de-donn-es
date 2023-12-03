import json
import urllib
import requests
import pandas as pd
import geopandas as gpd

def loadVelibInformation() :
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
  site = 'https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json'
  req = urllib.request.Request(site, headers=hdr)
  json_data = json.loads(urllib.request.urlopen(req).read()) 
  return(json_data)

def loadVelibStatus() :
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
  site = 'https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json'
  req = urllib.request.Request(site, headers=hdr)
  json_data = json.loads(urllib.request.urlopen(req).read())
  return(json_data)

def getVelibStations(json_data) :
  return json_data['data']['stations']

def exportToGeoDF(data_df) :
  geom = gpd.points_from_xy(data_df["lon"], data_df["lat"])
  data_geodf = gpd.GeoDataFrame(data_df, crs="EPSG:4326", geometry=geom)
  return data_geodf
