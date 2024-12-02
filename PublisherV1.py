import time
import random
import paho.mqtt.client as mqtt

# configuring the broker and the port
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_PREFIX = "environment"

# creating a list of cities and the sensor/topics
cities = ["london","newyork","tokyo", "coventry", "birmingham", "dublin", "edinburgh", "cardiff"]
sensors = ["temperature", "humidity", "co2", "airquality"]


def simulated_data(sensor):
    if sensor == "temperature":
        return round(random.uniform(-10, 40), 2)  # temperature in celcius -10 40 to make it a more believable temp
    elif sensor == "humidity":
        return round(random.uniform(30, 90), 2)  # humidity in %
    elif sensor == "co2":
        return random.randint(300, 500)  # the ppm in the co2 levels
    elif sensor == "airquality":
        return random.choice(["Good", "Moderate", "Poor"]) # returns a random airquality as their is no way to measure it for the time being with my resources

# publisher function
def publish_data():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    print("Connected to MQTT Broker. Publishing data...")   # this function is trying to make a connection with the broker and send the data through

    while True:
        for city in cities:
            for sensor in sensors:
                value = simulated_data(sensor)
                topic = f"{TOPIC_PREFIX}/{city}/{sensor}"
                client.publish(topic, value)        # publishing the data to the broker
                print(f"Published: {value} to topic: {topic}")
                time.sleep(1)  # this line makes it seem like its real-time data as its constantly updated/repeated after a short period


if __name__ == "__main__":  # its running the publisher
    publish_data()
