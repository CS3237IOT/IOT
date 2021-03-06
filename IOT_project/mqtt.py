import paho.mqtt.client as mqtt


class Subscriber:
    def __init__(self, topic, ip, port):
        self.MQTT_DATA = None
        self.client = mqtt.Client()
        self.topic = topic
        self.ip = ip
        self.port = port


    def on_connect(self, client, userdata, flags,rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(self.topic)

    def on_message(self, msg):
        self.MQTT_DATA = str(msg.payload.decode('ascii'))


    def getData(self):
        return self.MQTT_DATA

    def run(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        print("Connecting")
        self.client.connect(self.ip, self.port)
        # #self.client.tls_set("ca.pem", "client.crt", "client.key")



class Publisher:
    def __init__(self, topic, ip, port):
        self.client = mqtt.Client()
        self.topic = topic
        self.ip = ip
        self.port = port

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    def publish(self, data):
        print("Sending messsage")
        self.client.publish(self.topic, data)

    def run(self):
        self.client.on_connect = self.on_connect
        print("Connecting")
        self.client.connect(self.ip, self.port)

