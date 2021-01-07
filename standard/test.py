#%% Import packages
import json
import numpy as np
import pandas as pd

#%% set-up dataframe
d = np.array([['sensor-1', 'off', (1,1), 1, 1],
                ['sensor-2', 'off', (3,1), 3, 1],
                ['sensor-3', 'on', (5,1), 5, 1],
                ['sensor-4', 'off', (7,1), 7, 1],
                ['sensor-5', 'off', (1,2), 1, 2],
                ['sensor-6', 'off', (4,2), 4, 2],
                ['sensor-7', 'off', (9,2), 7, 2]], dtype=object)
# Dataframe section
df = pd.DataFrame(data=d, columns=['SensorId', 'Status', 'Loc', 'x', 'y'])

#%% load in json
log = '{"data":{"sensor-1":"off","sensor-2":"on","sensor-3":"off","sensor-4":"off","sensor-5":"off","sensor-6":"off","sensor-7":"off"},"time":"time"}'
data = json.loads(log)

#%% update data
for i in len(data['data']):
    data['data']

df[df['SensorId'] == 'sensor-1'].index[0]


# %% times tuff
from datetime import datetime
print(datetime.now().time())

# %%
from datetime import datetime
sensorName = np.array(['Vent1', 'Vent2', 'Vent3', 'Vent4', 'Sensor1', 'Sensor2', 'Sensor3'])
sensorState = np.full(7, 'off')
sensorLoc = np.array([[1,1],[3,1],[5,1],[7,1],[1,2],[4,2],[7,2]])

timeStamp = datetime.now()
sensorTimestamp = np.full(7,timeStamp.time())
sensorDate = np.full(7,timeStamp.date())

df = np.vstack([sensorName, sensorState, sensorLoc[:,0], sensorLoc[:,1], sensorTimestamp, sensorDate])
# %% set-up dataframe
from datetime import datetime
import numpy as np
import pandas as pd

# Basic variables
sensorName = np.array(['Vent1', 'Vent2', 'Vent3', 'Vent4', 'Sensor1', 'Sensor2', 'Sensor3'])
sensorState = np.full(7, 'off')
sensorLoc = np.array([[1,1],[3,1],[5,1],[7,1],[1,2],[4,2],[7,2]])

# Time Stamp allocation
timeStamp = datetime.now()
sensorTimestamp = np.full(7,timeStamp.time())
sensorDate = np.full(7,timeStamp.date())

# Creation of data frame
d = np.vstack([sensorName, sensorState, sensorLoc[:,0], sensorLoc[:,1], sensorTimestamp, sensorDate])
columns = ['SensorId', 'State', 'x', 'y', 'TimeStamp', 'DateStamp']
df = pd.DataFrame(data=d, index= columns)
df = df.transpose()

# file location
dir_path = os.path.dirname(os.path.realpath(__file__))
fileName = "sensorStatus.csv"
fileLocName = os.path.join(dir_path, fileName)

df.to_csv(fileLocName)


# %%
df2 = pd.read_csv(fileLocName)

#%% Test corrupt data frame

# Basic variables
sensorName = np.array(['Vent1', 'Vent2', 'Vent3', 'Vent4', 'Sensor1', 'Sensor2', 'Sensor3'])
sensorState = np.full(7, 'off')
sensorLoc = np.array([[1,1],[3,1],[5,1],[7,1],[1,2],[4,2],[7,2]])

# Time Stamp allocation
timeStamp = datetime.now()
sensorTimestamp = np.full(7,timeStamp.time())
sensorDate = np.full(7,timeStamp.date())

# Creation of data frame
df = np.vstack([sensorName, sensorState, sensorLoc[:,0], sensorLoc[:,1], sensorTimestamp, sensorDate])
columns = ['SensorId', 'Status', 'x', 'y', 'TimeStamp', 'DateStamp']
df = pd.DataFrame(data=df, index=columns)
df = df.transpose()

df.to_csv()

# %% Update data

jsonMqttMsg = { 
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

for key, value in jsonMqttMsg['data'].items():
            df['State'][df[df['SensorId'] == key].index[0]] = value
            df['TimeStamp'][df[df['SensorId'] == key].index[0]] = jsonMqttMsg['dateTimeStamp']['time'] 
            df['DateStamp'][df[df['SensorId'] == key].index[0]] = jsonMqttMsg['dateTimeStamp']['date'] 

# %%

# %%
