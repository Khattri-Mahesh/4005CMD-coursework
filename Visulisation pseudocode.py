FUNCTION generate_map():
    WHILE True:
        TRY:
            OPEN "data.json" in read mode
            READ data into city_data dictionary

            INITIALIZE map centered at [latitude, longitude] with zoom level

            FOR city, location IN city_locations:
                latitude = location["lat"]
                longitude = location["lon"]

                RETRIEVE city_data[city] as data
                FORMAT popup_text:
                    "City: city
                    Temperature: data['temperature'] °C
                    Humidity: data['humidity'] %
                    CO2 Levels: data['co2'] ppm
                    Air Quality: data['airquality']"

                ADD marker to map at [latitude, longitude] with popup_text

            SAVE map to "real_time_map.html"
            PRINT "Map updated and saved."

            OPEN "real_time_map.html" in browser
        CATCH error:
            PRINT "Error generating map:", error

        WAIT 15 seconds  # Refresh map periodically