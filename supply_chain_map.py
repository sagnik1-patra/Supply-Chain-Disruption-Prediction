import folium

# Example coordinates (you can replace these with user inputs or geocoding)
location_name = "Singapore"
latitude = 1.3521
longitude = 103.8198

# Create a Folium map with Stamen Terrain tiles and required attribution
m = folium.Map(
    location=[latitude, longitude],
    zoom_start=6,
    tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
)

# Add a marker for the location
folium.Marker(
    location=[latitude, longitude],
    popup=f"Supply Chain Hub: {location_name}",
    tooltip="Click for info",
    icon=folium.Icon(color='green')
).add_to(m)

# Save the map as HTML file
m.save("supply_chain_map.html")

print("✅ Map has been saved as 'supply_chain_map.html'. Open it in a browser to view.")
