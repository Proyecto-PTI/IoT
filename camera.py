import time
import os
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def on_subscribe(client, userdata, mid, QoS):
    print("Broker granted the following QoS:" + str(QoS))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if (msg.topic == "door_command" and str(msg.payload) == "b'Open'"):
        p.ChangeDutyCycle(10)
        print("detected command")
        time.sleep(10)
        p.ChangeDutyCycle(6)

def on_connect(client, userdata, flags, reason_code):
    print("Tried to connect with result code" + str(reason_code))
    client.subscribe("door_command")

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(16, True)
p = GPIO.PWM(18, 50)
p.start(0)
p.ChangeDutyCycle(6)

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
