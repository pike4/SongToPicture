# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:35:00 2015

@author: Continuum

Main method. 
"""
import numpy as np

import writeToImage as WI
from scipy.io.wavfile import read
from scipy import misc
import matplotlib.pyplot as plt
from PIL import Image



# read audio samples
input_data = read("foo.wav")
audio = input_data[1]
## plot the first 1024 samples
sample = audio[111000:111050]
#plt.plot(np.fft.fft(sample))

#1
#plt.plot(sample)
WI.WriteToImage(sample)
#plt.show()



#t = np.arange(256)
#sp = np.fft.fft(np.sin(t))
#freq = np.fft.fftfreq(t.shape[-1])
#plt.plot(freq, sp.real, freq, sp.imag)
#plt.show()
