import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import paho.mqtt.client as mqtt
import json
from datetime import datetime


today = datetime.today().strftime('%Y-%m-%d')

def setup(hostname):


    ref = db.reference("/")
    ref.set(
    {
        "date": {
        "2021-11-12": {
            "pushup_count": 10,
            "situp_count": 40,
            "jump_count": 36,
            "message": "idle"
        },
            "2021-11-13": {
            "pushup_count": 15,
            "situp_count": 40,
            "jump_count": 30,
            "message": "idle"
        },
            "2021-11-14": {
            "pushup_count": 20,
            "situp_count": 30,
            "jump_count": 1,
            "message": "idle"
        },
            "2021-11-15": {
            "pushup_count": 25,
            "situp_count": 30,
            "jump_count": 36,
            "message": "idle"
       },
            "2021-11-16": {
            "pushup_count": 245,
            "situp_count": 33,
            "jump_count": 36,
            "message": "idle"
       },

        "2021-11-17": {
            "pushup_count": 35,
            "situp_count": 30,
            "jump_count": 31,
            "message": "idle"
       },
        "2021-11-18": {
            "pushup_count": 35,
            "situp_count": 40,
            "jump_count": 36,
            "message": "idle",

       },
            "2021-11-19": {
            "pushup_count": 35,
            "situp_count": 40,
            "jump_count": 36,
            "message": "idle",
            "temp": "T: 23.22C H: 60.54% Feels: 25.32C"

       }
    }
})




def main():
    setup("localhost")


if __name__ == "__main__":
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('firebase-adminsdk.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nusiot-4b3c2-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    main()
