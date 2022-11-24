import RPi.GPIO as GPIO
import time
import ast
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

#inicialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
mensaje = ""

def customCallback(client, userdata, message):
    global mensaje
    mensaje = message.payload
    my_json = mensaje.decode('utf8')
    mydata = ast.literal_eval(my_json)
    print(mydata)
    return mensaje,
    
#AWS IoT certificaciones para la coneccion
myMQTTClient = AWSIoTMQTTClient("myClientID")
myMQTTClient.configureEndpoint("a1gpptc672aj5e-ats.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/pi02/Gauges/Cer_aws-iot/AmazonRoot_CA1.pem",
                                  "/home/pi02/Gauges/Cer_aws-iot/e8b6e32aef1db82d8a37c5fcf01b4dcc06599fd1fc1c89a8f97794a2af071617-private.pem.key",
                                  "/home/pi02/Gauges/Cer_aws-iot/e8b6e32aef1db82d8a37c5fcf01b4dcc06599fd1fc1c89a8f97794a2af071617-certificate.pem.crt")

# myMQTTClient.configureCredentials("/home/pi02/Gauges/Cer_aws-iot/AmazonRootCA1.pem",
#                                   "/home/pi02/Gauges/Cer_aws-iot/8e664e2cdc22eabfcf436849dab7115172fe668611a5f929c82d3b8356768c2a-private.pem.key",
#                                   "/home/pi02/Gauges/Cer_aws-iot/8e664e2cdc22eabfcf436849dab7115172fe668611a5f929c82d3b8356768c2a-certificate.pem.crt")


myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)

myMQTTClient.connect()
#myMQTTClient.publish("esp32/pub","connected", 0)
#myMQTTClient.subscribe("esp32/pub", 1, customCallback)


while True:
#     dato = "hola mundo"
#     myMQTTClient.publish("esp32/pub", dato, 0)
#     print("se mando el datooo")
# ##    if myMQTTClient.connect():
#     try:
#         print(myMQTTClient.connect())
#     except:
#         print("error")
    
    myMQTTClient.subscribe("met/co", 1, customCallback)
#     mensajeNuevo = mensajeNuevo.lstrip("b'")
#    print(mensaje)
    
    
    time.sleep(2)


