# %% Subscriber
import paho.mqtt.client as mqtt

broker = "localhost"
topics = [("topic1",1),("topic2",1),("topic3",1)] 

client = mqtt.Client()
client.connect(broker, 1883)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
        client.subscribe(topics)

    else:
        print("Bad connection Returned code=", rc)

def on_message(client, userdata, message):
    print(message.payload.decode())


client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()


# %%
