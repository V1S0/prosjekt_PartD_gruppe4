import tkinter as tk
from tkinter import ttk

import logging
import requests
import json
from messaging import SensorMeasurement





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
 
    uuid = did

    response = requests.get(f"http://localhost:8000/smarthouse/sensor/{uuid}/current")
    print(response.json())
    noe = response.json()
    #temp = noe.get_temperature()
    temp = noe[1]
    
    sensor_measurement = SensorMeasurement(init_value=temp)

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


