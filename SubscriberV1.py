import json
import paho.mqtt.client as mqtt

# MQTT Broker Configuration
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "environment/#"  # Subscribe to all environment data

# File to store real-time data
DATA_FILE = "data.json"

# Initialize data structure
city_data = {
    "london": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
    "newyork": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
    "tokyo": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
    "coventry": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
    "cardiff": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
    "edinburgh": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
    "dublin": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
    "birmingham": {"temperature": "N/A", "humidity": "N/A", "co2": "N/A", "airquality": "N/A"},
}

# Save data to JSON file
def save_to_file(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Updated data saved to {DATA_FILE}")

# Callback for MQTT connection
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(TOPIC)

# Callback for processing received messages
def on_message(client, userdata, msg):
    global city_data
    topic_parts = msg.topic.split("/")
    if len(topic_parts) == 3:
        _, city, sensor = topic_parts
        if city in city_data:
            city_data[city][sensor] = msg.payload.decode()
            print(f"Updated {sensor} for {city}: {city_data[city][sensor]}")
            save_to_file(city_data)

# Subscriber function
def subscribe_and_save():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    client.loop_forever()

# Run the subscriber
if __name__ == "__main__":
    subscribe_and_save()
