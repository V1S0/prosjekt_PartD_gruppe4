import logging
import threading
from threading import Thread
import time
import requests

from messaging import ActuatorState
import common


class Actuator:

    def __init__(self, did):
        self.did = did
        self.state = ActuatorState('False')

    def simulator(self):

        logging.info(f"Actuator {self.did} starting")

        while True:

            logging.info(f"Actuator {self.did}: {self.state}")

            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Actuator Client {self.did} starting")

        # TODO: START
        # send request to cloud service with regular intervals and
        # set state of actuator according to the received response
        while True:
            response = requests.get(f"http://localhost:8000/smarthouse/actuator/{self.did}/current")
            
            noe = response.json()
            #state = eval(noe)
            bool1 = bool(noe)

            self.state = bool1

            time.sleep(common.LIGHTBULB_CLIENT_SLEEP_TIME)

        

        logging.info(f"Client {self.did} finishing")

        # TODO: END

    def run(self):

        pass
        # TODO: START

        # start thread simulating physical light bulb
        thread1 = threading.Thread(target=self.simulator)
        thread1.start()

        # start thread receiving state from the cloud
        thread2 = threading.Thread(target=self.client)
        thread2.start()


        # TODO: END


