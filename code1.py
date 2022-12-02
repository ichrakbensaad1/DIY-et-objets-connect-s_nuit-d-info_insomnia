import RPi.GPIO as GPIO
import Adafruit_DHT
import pyrebase



config = {
  "apiKey": "AIzaSyBV_7FjcQe4TjqrVV1BdLADCslSPA5rTe8",
  "firebase_auth":"LrzS2FydknmOY65fejqjd9BUHiHcYJ5B5EsR47H5",
  "authDomain": "defi-7826c.firebaseapp.com",
  "databaseURL":"https://defi-7826c-default-rtdb.firebaseio.com",
  "projectId": "defi-7826c",
  "storageBucket": "defi-7826c.appspot.com",
  "messagingSenderId": "523137281756",
  "appId": "1:523137281756:web:575a9ba70dcc3232238e19",
  "measurementId": "G-F9YC8RWQNF"
};


#Setsensortype:OptionsareDHT11,DHT22orAM2302
sensor=Adafruit_DHT.DHT11
#Setsensortype:OptionsareDHT11,DHT22orAM2302
sensor=Adafruit_DHT.DHT11
#Adafruit_DHTusestheBCMmodebydefault
#SetGPIOsensorisconnectedt
gpio = 4
#Useread_retrymethod.Thiswillretryupto15timesto#getasensorreading(waiting2secondsbetweeneachretry).
humidity,temperature =Adafruit_DHT.read_retry(sensor,gpio)
firebase =  pyrebase.initialize_app(config)

    
#ReadingtheDHT11isverysensitivetotimingsandoccasionally#thePimightfailtogetavalidreading.Socheckifreadingsarevalid.
if humidity is not None and temperature is not None:
    
    print('Temp={0:0.1f}*CHumidity={1:0.1f}%'.format(temperature,humidity))
else:
    print('Failedtogetreading.Tryagain!')
data= {"temp":temperature, "humidity":humidity}
db=firebase.database()
results= db.child("users").push(data)

        
