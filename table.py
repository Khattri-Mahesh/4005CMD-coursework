import pandas as pd
import json

# loads city data from the json file
with open("data.json", "r") as file:
    city_data = json.load(file)

# converts information into a data frame
data = []
for city, params in city_data.items():
    data.append([
        city.title(),
        params.get("temperature", "N/A"),
        params.get("humidity", "N/A"),
        params.get("co2", "N/A"),
        params.get("airquality", "N/A")
    ])

columns = ["City", "Temperature (°C)", "Humidity (%)", "CO2 Levels (ppm)", "Air Quality"]
df = pd.DataFrame(data, columns=columns)

# shows the table
print ("here is the table of results")
print(df)


