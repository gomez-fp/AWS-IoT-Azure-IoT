import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

#CONNECTION_STRING = "HostName=Device-IoT.azure-devices.net;DeviceId=Raspberry_IoT2;SharedAccessKey=9SGwuMVVPvB78caDOLu4YL271LPpTCzDXxVlusM6doY="
CONNECTION_STRING = "HostName=pi-iot.azure-devices.net;DeviceId=iot-device-01;SharedAccessKey=00XzDP8iL3PvFdAsGWTiJyKep/h/WEq8LR9hEfGgdO0="

# Define the JSON message to send to IoT Hub.
TEMPERATURE = 20.0
HUMIDITY = 60
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Build the message with simulated telemetry values.
            temperature = TEMPERATURE + (random.random() * 15)
            humidity = HUMIDITY + (random.random() * 20)
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
            message = Message(msg_txt_formatted)

            # Send the message.
            #print( "Sending message: {}".format(message) )
            message = "hola mundo"
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()