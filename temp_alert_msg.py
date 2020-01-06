import Conf
from boltiot import Sms, Bolt
import json, time

minimum_limit = 300
maximum_limit = 600  


mybolt = Bolt(Conf.API_KEY, Conf.DEVICE_ID)
sms = Sms(Conf.SID, Conf.AUTH_TOKEN, Conf.TO_NUMBER, Conf.FROM_NUMBER)


while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is " +str(sensor_value))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e: 
        print ("Error: ")
        print (e)
    time.sleep(10)