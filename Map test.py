import folium
import webbrowser

#  a map generated around the co-ordinates
center_coordinates = [0, -0]
my_map = folium.Map(location=center_coordinates, zoom_start=4)


# adding markers test

folium.Marker(
    location=[51, -0],  # london co ordinates
    popup="London",
    icon=folium.Icon(color="red", icon="sign")
).add_to(my_map)




# save map in a html file
map_file = "map.html"
my_map.save(map_file)


#opens map in browser
webbrowser.open(map_file)
