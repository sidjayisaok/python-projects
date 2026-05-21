import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point
from geopy.geocoders import GoogleV3
import time
import os

matplotlib.use("Agg")

df = pd.DataFrame({
    'City': ['New York City','Los Angeles','Toronto','Chicago','San Francisco','Montreal','Boston','Washington DC','Dallas','Miami','Houston','Atlanta','Vancouver','Denver','Philadelphia','Seattle','Calgary','San Jose','Tampa','Minneapolis','San Diego','Detroit','Austin','Charlotte','Saint Louis','Phoenix','Orlando','Baltimore','Ottawa','Nashville','Cleveland','Kansas City','Milwaukee','Salt Lake City','Columbus','Sacramento','Edmonton'],
    'State': ['NY','CA','ON','IL','CA','QC','MA','DC','TX','FL','TX','GA','BC','CO','PA','WA','AB','CA','FL','MN','CA','MI','TX','NC','MO','AZ','FL','MD','ON','TN','OH','MO','WI','UT','OH','CA','AB'],
    'Country': ['United States','United States','Canada','United States','United States','Canada','United States','United States','United States','United States','United States','United States','Canada','United States','United States','United States','Canada','United States','United States','United States','United States','United States','United States','United States','United States','United States','United States','United States','Canada','United States','United States','United States','United States','United States','United States','United States','Canada']
})

API_KEY = os.getenv("GOOGLE_API_KEY")

geolocator = GoogleV3(api_key=API_KEY, timeout=10)

lat = []
lon = []

for i, row in df.iterrows():
    query = f"{row['City']}, {row['State']}, {row['Country']}"
    location = geolocator.geocode(query)

    lat.append(location.latitude)
    lon.append(location.longitude)

df['latitude'] = lat
df['longitude'] = lon
df['coordinates'] = df.apply(lambda r: Point(r['longitude'], r['latitude']), axis=1)

gdf = gpd.GeoDataFrame(df, geometry='coordinates')
gdf.head()
print(gdf.head())

# Load world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot world map
world.plot(ax=ax, color='lightgray', edgecolor='white')

# Plot your cities
gdf.plot(ax=ax, color='red', markersize=50)

# Save output
plt.savefig("global_cities_map.png", dpi=300, bbox_inches='tight')
