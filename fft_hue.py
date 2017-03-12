#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import pyaudio
import numpy as np
import requests
import time

LOW_BRI = 0
MAX_BRI = 254
MAX_HUE = 65534

chunk = 2**10
rate = 22050
fft_selection_filter = 12
hue_cycle_speed = 500
activation_threshold = 10000
run_time = 10 #in sec
user_id = 'your_dev_id'
hue_bridge_ip = '192.168.0.XX'

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=chunk, input_device_index=0)

previous_bri = LOW_BRI
for i_data_blocks in range(run_time*rate/chunk):
    data = np.fromstring(stream.read(chunk),dtype=np.int16)
    fft = np.fft.fft(data)
    hue = str((i_data_blocks*hue_cycle_speed)%MAX_HUE)
    bri = int(np.absolute(np.average(fft[0:fft_selection_filter])))
    if bri < activation_threshold:
        bri = LOW_BRI
    else:
        bri = MAX_BRI
    if bri != previous_bri:
        r_1 = requests.put('http://' + hue_bridge_ip + '/api/' + user_id +'/lights/1/state',
            data='{"bri": ' + str(bri) +', "transitiontime" : 1, "hue": ' + hue +'}')
        r_2 = requests.put('http://' + hue_bridge_ip + '/api/' + user_id +'/lights/2/state',
            data='{"bri": ' + str(bri) +', "transitiontime" : 1, "hue": ' + hue +'}')
        if bri:
            print("--High")
        else:
            print("-Low")
    previous_bri = bri
stream.stop_stream()
stream.close()
p.terminate()
