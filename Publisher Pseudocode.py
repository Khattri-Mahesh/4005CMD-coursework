FUNCTION publish_data():
    INITIALIZE MQTT client
    CONNECT to broker at <BROKER_ADDRESS> on port <PORT>

    DEFINE list_of_cities = ["london", "cardiff", ...]
    DEFINE sensors = ["temperature", "co2", "humidity", "air quality"]

    WHILE True:
        FOR city IN list_of_cities:
            FOR sensor IN sensors:
                IF sensor == "temperature":
                    value = RANDOM number between -10 and 40
                ELSE IF sensor == "humidity":
                    value = RANDOM number between 30 and 90
                ELSE IF sensor == "co2":
                    value = RANDOM integer between 300 and 500
                ELSE IF sensor == "air quality":
                    value = RANDOM choice of ["Good", "Moderate", "Poor"]

                topic = "environment/" + city + "/" + sensor
                PUBLISH value to topic
                PRINT "Published:", value, "to topic:", topic

            WAIT 1 seconds