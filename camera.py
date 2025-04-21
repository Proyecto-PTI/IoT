import time
import os
import paho.mqtt.client as mqtt

def on_subscribe(client, userdata, mid, QoS):
    print("Broker granted the following QoS:" + str(QoS))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def on_connect(client, userdata, flags, reason_code):
    print("Tried to connect with result code" + str(reason_code))
    client.subscribe("door_command")



mqttClient = mqtt.Client()
mqttClient.on_message = on_message
mqttClient.on_subscribe = on_subscribe
mqttClient.on_connect = on_connect

mqttClient.connect("nattech.fib.upc.edu", 40402)
mqttClient.loop_start()

while True:
    os.system('fswebcam -r 1920x1080 --save ~/Documents/image.jpeg -q')

    time.sleep(1)

loop_end()
