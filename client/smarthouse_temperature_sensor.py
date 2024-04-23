import logging
import threading
import time
import math
import requests
import json

from messaging import SensorMeasurement
import common


class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')

    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while True:

            temp = round(math.sin(time.time() / 10) * common.TEMP_RANGE, 1)

            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))

            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Sensor Client {self.did} starting")

        # TODO: START
        # send temperature to the cloud service with regular intervals
        while True:
            Value = self.measurement.value
            Timestamp = self.measurement.timestamp
            Unit = self.measurement.unit
 
            url = f"http://localhost:8000/smarthouse/sensor/{self.did}/current?timestamp={Timestamp}&value={Value}&unit={Unit}"

            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST",url,headers = headers)
           
            time.sleep(common.TEMPERATURE_SENSOR_CLIENT_SLEEP_TIME)

        logging.info(f"Client {self.did} finishing")

        # TODO: END

    def run(self):

        pass
        # TODO: START

        # create and start thread simulating physical temperature sensor
        thread3 = threading.Thread(target=self.simulator)
        thread3.start()

        # create and start thread sending temperature to the cloud service
        thread4 = threading.Thread(target=self.client)
        thread4.start()


        # TODO: END

