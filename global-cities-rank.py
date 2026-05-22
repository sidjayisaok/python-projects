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
    'City': ['New York City','Los Angeles','Toronto','Chicago','San Francisco','Montreal','Boston','Washington DC','Dallas','Miami','Houston','Atlanta','Vancouver','Denver','Philadelphia','Seattle','Calgary','San Jose','Tampa','Minneapolis','San Diego','Detroit','Austin','Charlotte','Saint Louis','Phoenix','Orlando','Baltimore','Ottawa','Nashville','Cleveland','Kansas City','Milwaukee','Salt Lake City','Columbus','Sacramento','Edmonton'],
    'State': ['NY','CA','ON','IL','CA','QC','MA','DC','TX','FL','TX','GA','BC','CO','PA','WA','AB','CA','FL','MN','CA','MI','TX','NC','MO','AZ','FL','MD','ON','TN','OH','MO','WI','UT','OH','CA','AB'],
    'Country': ['United States','United States','Canada','United States','United States','Canada','United States','United States','United States','United States','United States','United States','Canada','United States','United States','United States','Canada','United States','United States','United States','United States','United States','United States','United States','United States','United States','United States','United States','Canada','United States','United States','United States','United States','United States','United States','United States','Canada'],
    'Global_Rank': ['Alpha++','Alpha','Alpha','Alpha','Alpha-','Beta+','Alpha-','Alpha-','Beta+','Beta+','Alpha-','Beta+','Beta-','Beta-','Beta-','Beta-','Beta','Gamma','Gamma','Gamma+','Gamma+','Gamma','Gamma+','Gamma-','Gamma-','Sufficient','Sufficient','Gamma-','Sufficient','Gamma','Gamma-','Sufficient','Sufficient','Sufficient','Sufficient','Sufficient','Sufficient']
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

# Convert your GeoDataFrame to Web Mercator (required for basemap tiles)
gdf_web = gdf.to_crs(epsg=3857)

fig, ax = plt.subplots(figsize=(14, 8))

color_map = {
    'Alpha++': 'red',
    'Alpha': 'orange',
    'Alpha-': 'gold',
    'Beta+': 'green',
    'Beta': 'cyan',
    'Beta-': 'blue',
    'Gamma+': 'purple',
    'Gamma': 'pink',
    'Gamma-': 'brown',
    'Sufficient': 'gray'
}

gdf_web.plot(
    ax=ax,
    c=gdf_web['Global_Rank'].map(color_map),
    markersize=70,
    edgecolor='black',
    linewidth=1,
    legend=True
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
