# fft-hue

Python script based on Fast Fourier Transform to dynamically animate your Philips Hue lights.
***
### How-to
1. Install dependencies `pip install requests pyaudio numpy`
2. Create an authenticated user for your Hue Bridge : [Philips' tutorial](https://www.developers.meethue.com/documentation/getting-started)
3. Add your devices/lights following this synthax (changing `/lights/1/state`)
```Python
r_1 = requests.put('http://' + hue_bridge_ip + '/api/' + user_id 
+'/lights/1/state', data='{"bri": ' + str(bri) +', "transitiontime" : 1, "hue": ' + hue +'}')
```
4. Run script `python fft_hue.py`
5. Make some noises
***
### Tweakings
Sound sensibility can be adjusted with the `activation_threshold` variable.

Modify `input_device_index` to choose the audio device streamed. Open a Python shell with `pyaudio.PyAudio().get_device_info_by_index(N)` to check your available devices.
***
### Dependencies
* [requests](http://docs.python-requests.org/en/master/) : HTTP Library *(send requests to Hue Bridge)*
* [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/) : Audio Library *(open audio streams)*
* [numpy](http://www.numpy.org/) : Scientific Library *(fft and data manipulation)*

