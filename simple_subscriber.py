import paho.mqtt.client as mqtt_client
import time

BROKER = 'localhost'
MQTT_TOPIC = 'testing'

def UNUSED(x):
    return x

def on_message(client, userdata, message):
    UNUSED(client)
    UNUSED(userdata)
    print(str(message.payload.decode("utf-8")))


is_connected = False
client = mqtt_client.Client()
client.on_message = on_message
client.connect(BROKER)
client.loop_start()
client.subscribe(MQTT_TOPIC)

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()

# %%