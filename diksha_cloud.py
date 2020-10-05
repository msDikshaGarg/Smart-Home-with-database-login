import serial
import time
import pyrebase
import matplotlib as plt
from drawnow import *

value_time=[]
value_read=[]
config = {
    "apiKey": "AIzaSyDhI9M8P6yXayigbm8sGk_JvDH2lP-m_1s",
    "authDomain": "dikshaiot-79cdd.firebaseapp.com",
    "databaseURL": "https://dikshaiot-79cdd.firebaseio.com",
    "projectId": "dikshaiot-79cdd",
    "storageBucket": "dikshaiot-79cdd.appspot.com",
    "messagingSenderId": "486388324579"
}
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
plt.show()
firebase = pyrebase.initialize_app(config)
db = firebase.database()
#time_cc=int(time.time())
#obj = {"timestamp":time_cc,"reading":200}
#db.child("waterlevel").push(obj)
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    rdata = ser.readline().decode('utf-8')
    print(rdata)
    rdata=rdata.strip()
    rintd=int(rdata)
    value_read.append(rintd)
    time_cc=int(time.time())
    value_time.append(time_cc)
    plt.plot(value_time, value_read)
    plt.show()
    obj = {"timestamp":time_cc,"reading":rintd}
    db.child("motor").push(obj)

