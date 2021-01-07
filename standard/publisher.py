#%% Full set
import paho.mqtt.client as mqtt 
from datetime import datetime
import json

# Connection details
client = mqtt.Client("Python1")
client.connect(host="localhost",port=1883)

# Get time of message creation
timeStamp = datetime.now()

# This MQTT message sends a list of all sensor states
data = { 
    "ver" : "full", 
    "data" : {
        "Vent1":"off",
        "Vent2":"off",
        "Vent3":"off",
        "Vent4":"off",
        "Sensor1":"off",
        "Sensor2":"off",
        "Sensor3":"off"
    },
    "dateTimeStamp" :{
        "time" : "{}".format(timeStamp.time()),
        "date" : "{}".format(timeStamp.date())
    } 
}
log = json.dumps(data)
#log = '{"ver":"Full",data":{"Vent1":"off","Vent2":"on","Vent3":"off","Vent4":"off","Sensor1":"off","Sensor2":"off","Sensor3":"off"},"timeStampe":{"time":"{}","date":"{}"}'.format()

client.publish("LRI_resin_arrival/Topic1", log)
#%% Single sensor
import paho.mqtt.client as mqtt 
from datetime import datetime
import json

# Connection details
client = mqtt.Client("Python1")
client.connect(host="localhost",port=1883)

# Message variables
topic= 'Sensor1'
value= 'on'
timeStamp = datetime.now()

data = { 
    "ver" : "single", 
    "data" : {
        "{}".format(topic):"{}".format(value),
    },
    "dateTimeStamp" :{
        "time" : "{}".format(timeStamp.time()),
        "date" : "{}".format(timeStamp.date())
    } 
}
log = json.dumps(data)

client.publish("topic1", log)
# %%
