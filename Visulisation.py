import folium
import json
import time
import webbrowser

# location of city as well as its co-ordinates to place markers
city_locations = {
    "london": {"lat": 51.5074, "lon": -0.1278},
    "newyork": {"lat": 40.7128, "lon": -74.0060},
    "tokyo": {"lat": 35.6895, "lon": 139.6917},
    "coventry": {"lat": 52.4068, "lon": -1.5197},
    "cardiff": {"lat": 51.4816, "lon": -3.1791},
    "edinburgh": {"lat": 55.9533, "lon": -3.1883},
    "dublin": {"lat": 53.3498, "lon": -6.2603},
    "birmingham": {"lat": 52.4862, "lon": -1.8904},
}

# the data is stored on this file when it is updated
DATA_FILE = "data.json"

# creating the map
def generate_map(data):
    m = folium.Map(location=[20, 0], zoom_start=2)
    for city, location in city_locations.items():
        if city in data:
            city_info = data[city]
            popup_text = f"""                               
            <b>{city.title()}</b><br>
            Temperature: {city_info['temperature']} °C<br>
            Humidity: {city_info['humidity']} %<br>
            CO2 Levels: {city_info['co2']} ppm<br>
            Air Quality: {city_info['airquality']}<br>
            """
            folium.Marker(
                location=[location["lat"], location["lon"]],
                popup=popup_text,
                icon=folium.Icon(color="red", icon="info-sign"),
            ).add_to(m)
    m.save("ClimateMap.html")
    print("Map updated: ClimateMap.html")


def visualize():
    while True:
        try:
            # reads data from the json file
            with open(DATA_FILE, "r") as file:
                city_data = json.load(file)
            # creates/generates the map
            generate_map(city_data)
            # opens the map in browser
            webbrowser.open("ClimateMap.html")
        except Exception as e:
            print(f"Error reading data: {e}")
        time.sleep(15)  # made to update every 15 seconds

# runs the visulisation part of the code
if __name__ == "__main__":
    visualize()
