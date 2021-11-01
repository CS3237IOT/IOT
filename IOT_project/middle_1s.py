import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import paho.mqtt.client as mqtt
import json
import joblib
from scipy.signal import find_peaks
from mqtt import Publisher




global arr
arr = []

global count
count = 0

thisdict = {
  "0.0": "idle",
  "1.0": "jumping jack",
  "2.0": "push-up",
  "3.0": "running",
  "4.0": "sit-up",
  "5.0": "walking"
}

#activities = ['idles', 'jumping jack', 'push-up', 'running', 'Sit-ups', 'walking']
global loaded_rf
global scaler



mqtt_pub = Publisher("sensor/data", "localhost", 1883)
mqttPeak_pub = Publisher("sensor_peak/data", "localhost", 1883)



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
        peak_data = recv_dict['peak']


    if count == int(1):
        #features = arr
        #transformed_data = scaler.transform([features])
        value = loaded_rf.predict([arr])
        print(value[0])
        print(thisdict[str(value[0])])
        activity = thisdict[str(value[0])]
        json_msg = {
            'type':'activity',
            'result': thisdict[str(value[0])]
        }
        mqtt_pub.publish(json.dumps(json_msg))


        if activity == 'push-up':
            threshold = 0.8 * max(peak_data)
            peaks, _ = find_peaks(peak_data, height=threshold)
            print(len(peaks))
            json_msg = {
            'type':'peak_pushup',
            'peak_count': len(peaks)
            }
            mqttPeak_pub.publish(json.dumps(json_msg))

        if activity == 'sit-up':
            threshold = 0.8 * max(peak_data)
            peaks, _ = find_peaks(peak_data, height=threshold)
            print(len(peaks))
            json_msg = {
            'type':'peak_situp',
            'peak_count': len(peaks)
            }
            mqttPeak_pub.publish(json.dumps(json_msg))

        if activity == 'jumping jack':
            threshold = 0.8 * max(peak_data)
            peaks, _ = find_peaks(peak_data, height=threshold)
            print(len(peaks))
            json_msg = {
            'type':'peak_jump',
            'peak_count': len(peaks)
            }
            mqttPeak_pub.publish(json.dumps(json_msg))
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
    #set up the MQTT publisher
    global loaded_rf
    global scaler
    loaded_rf = joblib.load("./random_forest.joblib")
    #scaler = joblib.load('scaler_data.joblib')
    setup("localhost")
    mqtt_pub.run()
    mqttPeak_pub.run()
    while True:
        pass

if __name__ == "__main__":
    main()

