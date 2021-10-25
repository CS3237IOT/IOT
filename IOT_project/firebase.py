import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        client.subscribe("sensor/data")
    else:
        print("Connection failed with code %d." %rc)


def on_message(client, userdata, msg):
    recv_dict = json.loads(msg.payload)
    value = recv_dict['result']
    ref = db.reference('message')
    current_value = ref.get()
    if current_value != value:
        print("changed")
        ref.set(value)

def setup(hostname):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(hostname)
    client.loop_start()
    return client


def main():
    setup("localhost")
    while True:
        pass

if __name__ == "__main__":
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('firebase-adminsdk.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nusiot-4b3c2-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    main()


