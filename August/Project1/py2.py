import folium
import pandas as pd

# Sample data (replace with your actual data)
data = pd.DataFrame({
    'state': ['Karnataka', 'Maharashtra', 'Gujarat', 'Punjab'],
    'capital': ['Bengaluru', 'Mumbai', 'Gandhinagar', 'Chandigarh'],
    'lat': [12.9716, 19.0760, 23.0222, 30.7333],
    'lon': [77.5946, 72.8777, 72.6141, 76.7794]
})

# Create a base map
m = folium.Map(location=[20, 78], zoom_start=5)

# Add markers for capital cities
for index, row in data.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['capital']).add_to(m)

# Display the map
# Save the map as an HTML file
m.save('map.html')
