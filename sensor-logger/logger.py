#!/usr/bin/python3
import time
import os
from influx import InfluxDB
from bme280 import *

monitorHost = os.getenv("MONITOR_HOST")
if monitorHost == None:
    monitorHost = "influxdb"
hostName = os.getenv("HOST")
if hostName == None:
    hostName = "unknown"
pollStr = os.getenv("POLL")
poll = 30
if pollStr != None:
    poll = int(pollStr)
location = os.getenv("PHYSICAL_LOCATION")
degrees,hectopascals,humidity = readBME280All()
print("monitor host: " + monitorHost)
print("location: " + location)
print("degrees: " + str(degrees))
print("hectopascals: " + str(hectopascals))
print("humidity: " + str(humidity))

while True:
    degrees,hectopascals,humidity = readBME280All()
    
    client = InfluxDB('http://' + monitorHost + ':8086')
    client.create_database('environment')
    
    iso = time.ctime()
    
    client.write('environment', 'temperature', fields={'value': degrees}, tags={'location': location, 'host': hostName})
    client.write('environment', 'pressure', fields={'value': hectopascals}, tags={'location': location, 'host': hostName})
    client.write('environment', 'humidity', fields={'value': humidity}, tags={'location': location, 'host': hostName})
    
    time.sleep(poll)
