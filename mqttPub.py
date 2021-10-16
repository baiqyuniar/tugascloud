# import paho.mqtt.client as mqtt

# client = mqtt.Client()  

# client.connect("localhost", 1884, 60)       #parameternya IPAddr, port, timeout


# while True:
#     payload = input("Masukkan angka: ")

#     print("Publishing message . . .")
#     client.publish("Angka", payload)
#     print("Message Published\n")


import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

mqttBroker ="192.168.1.7" 

client = mqtt.Client("Temperature")
client.connect(mqttBroker) 

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)