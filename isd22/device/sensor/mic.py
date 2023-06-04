# International Sensor Development Project
# Hochschule Osnabrück University of Applied Sciences, Germany & Metropolia University of Applied Sciences, Finland
# 2022-2023

import pyaudio
import math
import struct

class Mic:

    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.selectDevice()
        self.setup()

    def selectDevice(self):
        # reference https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone
        for i in range(self.audio.get_device_count()):
            if "USB" in self.audio.get_device_info_by_index(i).get('name'):
                self.index = i
    
    def setup(self):
        # reference https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone
        # reference https://stackoverflow.com/questions/70502339/how-would-i-find-the-current-decibel-level-and-set-it-as-a-variable
        self.audioStream = self.audio.open(format=pyaudio.paInt16,rate=int(self.audio.get_device_info_by_index(self.index).get('defaultSampleRate')),input_device_index=self.index,input=True,channels=1,frames_per_buffer=2048)
    
    def read(self):
        audioData = self.audioStream.read(2048, exception_on_overflow=False)
        db = self.calculateDecibels(self.calculateRMS(audioData))
        return round(float(db),2)

    def calculateRMS(self, audioData):
        # reference https://stackoverflow.com/questions/25868428/pyaudio-how-to-check-volume
        count = len(audioData)/2
        format="%dh"%(count)
        shorts=struct.unpack(format,audioData)
        sumSq = 0.0
        for samp in shorts:
            n = samp * (1.0/32768)
            sumSq += n*n
        return math.sqrt(sumSq/count)
    
    def calculateDecibels(self, rms):
        # reference https://stackoverflow.com/questions/25868428/pyaudio-how-to-check-volume
        # reference https://stackoverflow.com/questions/70502339/how-would-i-find-the-current-decibel-level-and-set-it-as-a-variable
        return 20*math.log10(rms)

    def close(self):
        self.audioStream.stop_stream()
        self.audioStream.close()


