import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import paho.mqtt.client as mqtt
import json
from datetime import datetime


today = datetime.today().strftime('%Y-%m-%d')

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        client.subscribe("sensor/data")
        client.subscribe("sensor_peak/data")

    else:
        print("Connection failed with code %d." %rc)

def on_message(client, userdata, msg):
    recv_dict = json.loads(msg.payload)
    if recv_dict['type'] == 'activity':
        value = recv_dict['result']
        ref = db.reference("date"+ "/" + today + "/" +'message')
        current_value = ref.get()
        if current_value != value:
            print("changed")
            ref.set(value)

    if recv_dict['type'] == 'peak_pushup':
        value = recv_dict['peak_count']
        ref = db.reference("date"+ "/" + today + "/" + 'pushup_count')
        current_value = ref.get()
        value = int(current_value) + int(value)
        print(value)
        ref.set(value)

    if recv_dict['type'] == 'peak_situp':
        value = recv_dict['peak_count']
        ref = db.reference("date"+ "/" + today + "/" + 'situp_count')
        current_value = ref.get()
        value = int(current_value) + int(value)
        print(value)
        ref.set(value)

    if recv_dict['type'] == 'peak_jump':
        value = recv_dict['peak_count']
        ref = db.reference("date" + "/" + today + "/" + 'jump_count')
        current_value = ref.get()
        value = int(current_value) + int(value)
        print(value)
        ref.set(value)

    if recv_dict['type'] == 'heat_injury':
        value1 = recv_dict['FL_temp']
        value1 = round(value1, 2)
        value2 = recv_dict['env_temp']
        value2 = round(value2, 2)
        value3 = recv_dict['env_humi']
        value3 = round(value3, 2)
        temp_text = "T: " + str(value2) + "C " + "H: " + str(value3)  + "% " + "Feels: " + str(value1) + "C"
        ref = db.reference("date" + "/" + today + "/" + 'temp')
        ref.set(temp_text)

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


