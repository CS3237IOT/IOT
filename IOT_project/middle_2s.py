import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import paho.mqtt.client as mqtt
import json
import joblib
import  numpy as np
from mqtt import Publisher


mqtt_pub = Publisher("sensor/data", "localhost", 1883)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        client.subscribe("sensor2/data")
    else:
        print("Connection failed with code %d." %rc)


def on_message(client, userdata, msg):

    recv_dict = json.loads(msg.payload)
    temp = np.array(recv_dict['payload'][0]).reshape(-1, 1)
    RH = np.array(recv_dict['payload'][1]).reshape(-1, 1)

    data = np.concatenate((temp, RH), axis = 1)
    env_humi = loaded_RH.predict(data)
    env_temp = loaded_Temp.predict(data)
    tempF= env_temp[0][0]*1.8+32
    data2 = np.concatenate(
        (
        np.array(tempF).reshape(-1,1),
        np.array(env_humi[0][0]).reshape(-1,1),
        )
        ,axis = 1)

    feelikeF = loaded_HI.predict(data2)
    feellikeC = (feelikeF[0][0]-32)/1.8
    json_msg = {
            'type': 'heat_injury',
            'env_temp':env_temp[0][0],
            'env_humi':env_humi[0][0],
            "FL_temp": feellikeC
    }
    mqtt_pub.publish(json.dumps(json_msg))


def setup(hostname):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(hostname)
    client.loop_start()
    return client

def main():
    global loaded_RH
    global loaded_Temp
    global loaded_HI
    loaded_RH = joblib.load("./Predict_env_humi.pkl")
    loaded_Temp = joblib.load("./Predict_env_temp.pkl")
    loaded_HI = joblib.load('./Predict_Heat_Injury.pkl')
    setup("localhost")
    mqtt_pub.run()
    while True:
        pass
if __name__ == "__main__":
    main()

