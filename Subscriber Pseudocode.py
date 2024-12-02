FUNCTION subscribe_data():
    INITIALIZE MQTT client

    DEFINE on_connect():
        PRINT "Connected to MQTT Broker."
        SUBSCRIBE to "environment/#"

    DEFINE on_message(topic, payload):
        PRINT "Received topic:", topic, "payload:", payload

        SPLIT topic by "/" INTO parts
        city = parts[1]
        sensor = parts[2]

        IF city EXISTS in city_data AND sensor EXISTS in city_data[city]:
            UPDATE city_data[city][sensor] = payload
            PRINT "Updated", sensor, "for", city, ":", city_data[city][sensor]
            CALL save_to_file(city_data)

    DEFINE save_to_file(data):
        TRY:
            OPEN "data.json" in write mode
            WRITE data to file in JSON format
            PRINT "Data saved to JSON."
        CATCH error:
            PRINT "Error saving to file:", error

    ASSIGN on_connect as the connect callback for the client
    ASSIGN on_message as the message callback for the client

    CONNECT client to <BROKER_ADDRESS> on port <PORT>
    ENTER loop_forever() to keep the client listening
