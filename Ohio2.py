# -*- coding: utf-8 -*-

import numpy as np
import writeToImage as WI
from scipy.io.wavfile import read as ReadWAV



def GetFFT(Sample, SamplingFrequency, SampleDurationSec):
        
    SamplingPeriod = 1 / SamplingFrequency
    SignalLength = int(SamplingFrequency * SampleDurationSec)
    
    #init
    Time =      np.linspace(0, SignalLength - 1, SignalLength)
    Signal =    np.linspace(0, SignalLength - 1, SignalLength)
    Freq =      np.linspace(0, SignalLength - 1, SignalLength)
    
    for i in range(0, SignalLength):
        Time[i] = Time[i] * SamplingPeriod
        Signal[i] = Sample[i]
        Freq[i] = i
        
    FFT = np.fft.fft(Signal)    
        
    P2 = np.linspace(0, SignalLength - 1, SignalLength)
    for i in range(0, SignalLength):
        P2[i] = abs(FFT[i] / SignalLength);   
        
    P1 = np.linspace(0, SignalLength - 1, SignalLength / 2)
    for i in range(0, int(SignalLength / 2)):
        P1[i] = P2[i] * 2
        
    return P1


def GetSlice(Audio, Start, Duration, SampleRate):

    Return = np.linspace(1, 1, Duration * SampleRate)
    for i in range(0, int(Duration * SampleRate)):
        Return[i] = Audio[int(Start * SampleRate + i)]
        
    return Return


def Normalize(Sample, length, outLength = 480):
    
    Peak = 0;
    for i in range(0, length):
        if (Sample[i] > Peak):
            Peak = Sample[i]
    
    Return = np.linspace(1, 1, outLength)        
    for i in range(0, outLength):
        Return[i] = 0
        for ii in range(int(i * (length / outLength)), int((i + 1) * (length / outLength))):
            if (Sample[ii] > Return[i]):
                Return[i] = Sample[ii]
        Return[i] = Return[i] / Peak;

    return Return


def GetSliceMap(Filename):
    
    SampleFreq = 44100
    RawData = ReadWAV(Filename)
    RawAudio = RawData[1]
    Audio = RawAudio[:, 1] 
    AudioLengthSec = int(len(Audio) / SampleFreq)
    
    Return = [[0 for x in range(AudioLengthSec)] for x in range(480)] 
    for i in range(0, AudioLengthSec):
        Slice = GetSlice(Audio, i, 1, SampleFreq) 
        FFT = GetFFT(Slice, SampleFreq, 1)
        Normalized = Normalize(FFT, len(FFT))
        for ii in range(0, len(Normalized)):
            Return[ii][i] = Normalized[len(Normalized) - ii - 1]
    
    return Return
        
        




SliceMap = GetSliceMap('foo.wav')
print("finished slice")
WI.WriteToImage(SliceMap)


print('Finished')
        








     