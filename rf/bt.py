#!/usr/bin/env python

#
# WARNING: never rename file to "bluetooth.py" or this script will fail because of the import
# command, which will try to implementi itself and report an "AttributeError"
#


import bluetooth
import time
import sys
import requests
import ssl

bt = ['CC:20:E8:64:0A:7F', '34:4D:AA:AD:7F:C0']
# You can hardcode the desired device ID here as a string to skip the discovery stage
addr = "CC:20:E8:64:0A:7F"
varWaitTime = 10

# #################################################

ARG_DISPLAY=0
for arg in sys.argv:
        if arg == "-display":
                ARG_DISPLAY=1


if ARG_DISPLAY == 1:
	print "DEMO: Bluetooth Tag"
	print ""
	print "Ausgabe:"


def UpdateStatus(status):
#  try:
     	context = ssl._create_unverified_context()

     	url = open('/home/pi/circonus/ecg1_sensors_url.txt', 'r').read()
#    	print 'URL=%s' % url

     	import json
     	import urllib2

     	data = {
             'ECG1.bluetooth': 1
     	}

     	req = urllib2.Request(url)
	req.add_header('Content-Type', 'application/json')

  	response = urllib2.urlopen(req, json.dumps(data), context=context)
#  except:
#	pass
			
while True:
    # Try to gather information from the desired device.
    # We're using two different metrics (readable name and data services)
    # to reduce false negatives.
    state = bluetooth.lookup_name(addr, timeout=20)
    services = bluetooth.find_service(address=addr)
    # Flip the LED pin on or off depending on whether the device is nearby
    if state == None and services == []:
        if ARG_DISPLAY == 1:
        	print("No device detected in range...")
    else:
	if ARG_DISPLAY == 1:
        	print("Device detected!")
	UpdateStatus(1)
    # Arbitrary wait time
    time.sleep(varWaitTime)
