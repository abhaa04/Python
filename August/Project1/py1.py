import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile of Indian states
india_map = gpd.read_file('India_State_Boundary.shp')

# Capital city data
capital_cities = {
    'Karnataka': ('Bengaluru', 12.9716, 77.5946),
    'Maharashtra': ('Mumbai', 19.0760, 72.8777),
    'Gujarat': ('Gandhinagar', 23.0222, 72.6141),
    'Punjab': ('Chandigarh', 30.7333, 76.7794),
    'Uttarakhand': ('Dehradun', 30.3165, 78.0292),
    'Tamil Nadu': ('Chennai', 13.0827, 80.2707),
    'Kerala': ('Thiruvananthapuram', 8.4870, 76.9350),
    'Uttar Pradesh': ('Lucknow', 26.8467, 80.9462)
}

# Extract capital city coordinates
capital_lats = [city[1] for city in capital_cities.values()]
capital_lons = [city[2] for city in capital_cities.values()]

# Create a GeoPandas GeoSeries of capital city points
capitals_gdf = gpd.GeoSeries(
    gpd.points_from_xy(capital_lons, capital_lats),
    crs='EPSG:4326'  # Assuming WGS84 coordinate system
)

# Plot the map
fig, ax = plt.subplots(figsize=(10, 8))
india_map.plot(ax=ax, color='lightgray', edgecolor='black')

# Plot capital cities
capitals_gdf.plot(ax=ax, color='red', markersize=50)

# Add labels for capital cities
for state, (capital, lat, lon) in capital_cities.items():
    ax.text(lon, lat, capital, fontsize=8, ha='center', va='center')

plt.title('Capital Cities of Selected Indian States')
plt.show()
