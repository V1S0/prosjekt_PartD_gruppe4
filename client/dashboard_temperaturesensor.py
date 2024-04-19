import tkinter as tk
from tkinter import ttk

import logging
import requests

from messaging import SensorMeasurement
import common

import smarthouse.api.py


#husk husk
#source .venv/bin/activate
#uvicorn smarthouse.api:app --reload
#cd client/
#python dashboard.py

#cd ..

#http://127.0.0.1:8000/docs


def refresh_btn_cmd(temp_widget, did):

    logging.info("Temperature refresh")

    # TODO: START
    # send request to cloud service to obtain current temperature
 
    response = get_current_sensor_measurement("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e")
    value = response.value

    # replace statement below with measurement from response
    #sensor_measurement = SensorMeasurement(init_value="-273.15")
    
    sensor_measurement = SensorMeasurement(init_value=value)

    # TODO: END

    # update the text field in the user interface
    temp_widget['state'] = 'normal' # to allow text to be changed
    temp_widget.delete(1.0, 'end')
    temp_widget.insert(1.0, sensor_measurement.value)
    temp_widget['state'] = 'disabled'


def init_temperature_sensor(container, did):

    ts_lf = ttk.LabelFrame(container, text=f'Temperature sensor [{did}]')

    ts_lf.grid(column=0, row=1, padx=20, pady=20, sticky=tk.W)

    temp = tk.Text(ts_lf, height=1, width=10)
    temp.insert(1.0, 'None')
    temp['state'] = 'disabled'

    temp.grid(column=0, row=0, padx=20, pady=20)

    refresh_button = ttk.Button(ts_lf, text='Refresh',
                                command=lambda: refresh_btn_cmd(temp, did))

    refresh_button.grid(column=1, row=0, padx=20, pady=20)


