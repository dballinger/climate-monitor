#!/usr/bin/python


from bme280 import *
degrees,hectopascals,humidity = readBME280All()
print(degrees)
print(hectopascals)
print(humidity)

