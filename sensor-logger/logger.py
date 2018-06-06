#!/usr/bin/python3
import time
import os
from influx import InfluxDB
from bme280 import *

while True:
    degrees,hectopascals,humidity = readBME280All()
    
    host_pi = os.getenv("HOSTNAME")
    client = InfluxDB('http://influxdb:8086')
    client.create_database('environment')
    
    iso = time.ctime()
    
    client.write('environment', 'temperature', fields={'value': degrees}, tags={'location': 'peveril'})
    client.write('environment', 'pressure', fields={'value': hectopascals}, tags={'location': 'peveril'})
    client.write('environment', 'humidity', fields={'value': humidity}, tags={'location': 'peveril'})
    
    time.sleep(30)
