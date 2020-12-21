import paho.mqtt.client as mqtt 

client = mqtt.Client("Python1")
client.connect(host="localhost",port=1883)
client.publish("topic1", "message2")