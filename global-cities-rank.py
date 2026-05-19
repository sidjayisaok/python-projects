import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point
from geopy.geocoders import Nominatim

df =  pd.DataFrame({
    'City': ['New York City','Los Angeles','Toronto','Chicago','San Francisco','Montreal','Boston','Washington DC','Dallas','Miami','Houston','Atlanta','Vancouver','Denver','Philadelphia','Seattle','Calgary','San Jose','Tampa','Minneapolis','San Diego','Detroit','Austin','Charlotte','Saint Louis','Phoenix','Orlando','Baltimore','Ottawa','Nashville','Cleveland','Kansas City','Milwaukee','Salt Lake City','Columbus','Sacramento','Edmonton'],
    'State': ['NY','CA','ON','IL','CA','QC','MA','DC','TX','FL','TX','GA','BC','CO','PA','WA','AB','CA','FL','MN','CA','MI','TX','NC','MO','AZ','FL','MD','ON','TN','OH','MO','WI','UT','OH','CA','AB'],
    'Country': ['United States','United States','Canada','United States','United States','Canada','United States','United States','United States','United States','United States','United States','Canada','United States','United States','United States','Canada','United States','United States','United States','United States','United States','United States','United States','United States','United States','United States','United States','Canada','United States','United States','United States','United States','United States','United States','United States','Canada'],
    'Rank': ['Alpha ++','Alpha','Alpha','Alpha','Alpha -','Alpha -','Alpha -','Beta +','Beta +','Beta +','Beta +','Beta +','Beta +','Beta','Beta','Beta','Beta -','Beta -','Beta -','Beta -','Beta -','Beta -','Beta -','Gamma +','Gamma +','Gamma +','Gamma +','Gamma +','Gamma','Gamma','Gamma -','Gamma -','Gamma -','Gamma -','Gamma -','Gamma -','Gamma -']
})

geolocator = Nominatim(user_agent="global-cities-rank")

long = []
lat = []
coordinates = []

for coordinates in df["City"]:
    lat += [geolocator.geocode(coordinates).latitude]
    long += [geolocator.geocode(coordinates).longitude]
    
df['latitude'] = lat
df['longitude'] = long
df['coordinates'] = list(zip(lat,long))
df['coordinates'] = df['coordinates'].apply(Point)

gdf = gpd.GeoDataFrame(df, geometry="Coordinates")
gdf.head()

# print('gdf is : ', type(gdf))
# print('\ngdf column : ', gdf.geometry.name)



