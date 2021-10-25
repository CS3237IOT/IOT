import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import paho.mqtt.client as mqtt
import json
import joblib

global arr
arr = []

global count
count = 0

thisdict = {
  "0": "idle",
  "1": "jumping jack",
  "2": "push-up",
  "3": "running",
  "4": "sit-up",
  "5": "walking"
}

#activities = ['idles', 'jumping jack', 'push-up', 'running', 'Sit-ups', 'walking']
global loaded_rf
global scaler


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        client.subscribe("sensor1/data")
        client.subscribe("sensor2/data")
    else:
        print("Connection failed with code %d." %rc)


def on_message(client, userdata, msg):
    global count
    global arr
    recv_dict = json.loads(msg.payload)
    sensor = recv_dict['sensor']
    print(recv_dict)

    if sensor == int(1) and count==0:
        value1 = recv_dict['payload']
        arr = arr + value1
        count = count + sensor

    if count == int(1):
        #load ML model here
        features = arr
        transformed_data = scaler.transform([features])
        value = loaded_rf.predict(transformed_data)
        print(transformed_data)
        print(value[0])
        print(thisdict[str(value[0])])


        #
        #
        # json_msg = {
        #     'result': thisdict[str(value[0])]
        # }
        #
        #
        # print(json_msg)
        # #mqtt publish
        # mqtt_pub.publish(json.dumps(json_msg))
        arr.clear()
        count = 0


def setup(hostname):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(hostname)
    client.loop_start()
    return client

def main():
    global loaded_rf
    global scaler
    loaded_rf = joblib.load("./random_forest.joblib")
    scaler = joblib.load('scaler_data.joblib')
    setup("localhost")
    while True:
        pass

if __name__ == "__main__":
    main()

