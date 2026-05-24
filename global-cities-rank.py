import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import contextily as ctx
import matplotlib.patches as mpatches
import pandas as pd
from dotenv import load_dotenv
from shapely.geometry import Point
from geopy.geocoders import GoogleV3
import time
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

matplotlib.use("Agg")

df = pd.DataFrame({
   "City":["New York City","Los Angeles","Toronto","Chicago","San Francisco","Montreal","Boston","Washington DC","Dallas","Miami","Houston","Atlanta","Vancouver","Denver","Philadelphia","Seattle","Calgary","San Jose","Tampa","Minneapolis","San Diego","Detroit","Austin","Charlotte","Saint Louis","Baltimore","Nashville","Cleveland"],
   "State":["NY","CA","ON","IL","CA","QC","MA","DC","TX","FL","TX","GA","BC","CO","PA","WA","AB","CA","FL","MN","CA","MI","TX","NC","MO","MD","TN","OH"],
   "Country":["United States","United States","Canada","United States","United States","Canada","United States","United States","United States","United States","United States","United States","Canada","United States","United States","United States","Canada","United States","United States","United States","United States","United States","United States","United States","United States","United States","United States","United States"],
   "Global_Rank":["Alpha++","Alpha","Alpha","Alpha","Alpha-","Beta+","Alpha-","Alpha-","Beta+","Beta+","Alpha-","Beta+","Beta-","Beta-","Beta-","Beta-","Beta","Gamma","Gamma","Gamma+","Gamma+","Gamma","Gamma+","Gamma-","Gamma-","Gamma-","Gamma","Gamma-"],
   "Population":[8336817,3898747,2794356,2746388,873965,1762949,675647,689545,1304379,442241,2304580,498715,662248,715522,1603797,737015,1306784,1013240,384959,429954,1386932,639111,964177,874579,301578,585708,689447,372624]
})

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
df['Global_Rank'] = df['Global_Rank'].str.strip()

gdf = gpd.GeoDataFrame(df, geometry='coordinates', crs="EPSG:4326")
gdf.head()
print(gdf.head())
gdf_web = gdf.to_crs(epsg=3857)

fig, ax = plt.subplots(figsize=(14, 8))

color_map = {
    'Alpha++': '#08306B',
    'Alpha':   '#08519C',
    'Alpha-':  '#2171B5',
    'Beta+':   '#4292C6',
    'Beta':    '#6BAED6',
    'Beta-':   '#9ECAE1',
    'Gamma+':  '#C6DBEF',
    'Gamma':   '#DEEBF7',
    'Gamma-':  '#F7FBFF'
}

# Normalize population to a reasonable size range
min_size = 20
max_size = 800

pop_min = gdf_web['Population'].min()
pop_max = gdf_web['Population'].max()

gdf_web['marker_size'] = (
    (gdf_web['Population'] - pop_min) / (pop_max - pop_min)
) * (max_size - min_size) + min_size

gdf_web.plot(
    ax=ax,
    c=gdf_web['Global_Rank'].map(color_map),
    markersize=gdf_web['marker_size'],
    edgecolor='black',
    linewidth=1
)

print(gdf_web['Global_Rank'].dtype)
print(gdf_web['Global_Rank'].unique())

legend_handles = [
    mpatches.Patch(color=color_map[label], label=label)
    for label in color_map.keys()
]

ax.legend(
    handles=legend_handles,
    title="Global Rank",
    loc="lower right",
    frameon=True,
    facecolor="white",
    edgecolor="black"
)

# Add basemap tiles
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# Clean up axes
ax.set_axis_off()

# Save the final image
plt.savefig("global_cities_map.png", dpi=300, bbox_inches='tight')
