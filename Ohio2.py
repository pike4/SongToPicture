# -*- coding: utf-8 -*-

import numpy as np
from scipy.io.wavfile import read as ReadWAV
import writeToImage as WI



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


def FillFreqBins(Sample, length, outLength = 480):
    
    Peak = 0;
    for i in range(0, length):
        if (Sample[i] > Peak):
            Peak = Sample[i]
            
    #BaseNormalized = LoadNormilizationData('Baseline.txt')
    
    Return = np.linspace(1, 1, outLength)        
    for i in range(0, outLength):
        Return[i] = 0
        for ii in range(int(i * (length / outLength)), int((i + 1) * (length / outLength))):
            if (Sample[ii] > Return[i]):
                Return[i] = Sample[ii]
        #Return[i] = Return[i] / Peak #abs((Return[i] - (BaseNormalized[i] * Peak)) / Peak);

    return Return
    
    
def PerFreqNorm(Sample):

    Return = [[0 for x in range(0, len(Sample))] for x in range(0, len(Sample[0]))] 

    # Find peak across rows and normalize to peak
    for i in range(0, 480):
        Peak = 0
        for ii in range(0, int(AudioLengthSec / SliceDuration)):
            if (Return[i][ii] > Peak):
                Peak = Return [i][ii]
        
        for ii in range(0, int(AudioLengthSec / SliceDuration)):
            Return [i][ii] = Return [i][ii] / Peak
            
            
def PerSliceNorm(Sample):

    Return = [[0 for x in range(0, len(Sample))] for x in range(0, len(Sample[0]))] 

    # Find peak across a single column and normalize to peak
    for Row in range(0, len(Sample)):
        Peak = 0
        for Col in range(0, len(Sample[Row])):
            if (Return[Col][Row] > Peak):
                Peak = Return [Col][Row]
        
        for ii in range(0, len(Sample[Row])):
            Return [Col][Row] = Return [Col][Row] / Peak
            
            
def ChunkNorm(Sample):

    Return = [[0 for x in range(0, len(Sample))] for x in range(0, len(Sample[0]))] 

    # Find peak across a single column and normalize to peak
    for Row in range(0, int(len(Sample[0]) / 2)):
        Peak = 0
        for Col in range(0, len(Sample)):
            if (Return[Col][Row] > Peak):
                Peak = Return [Col][Row]
        
        for Col in range(0, len(Sample)):
            Return [Col][Row] = Return [Col][Row] / Peak
            
    # Find peak across a single row and normalize to peak
    for Col in range(int(len(Sample) / 2) + 1, len(Sample)):            
        Peak = 0
        for Row in range(0, len(Sample[Col])):
            if (Return[Col][Row] > Peak):
                Peak = Return [Col][Row]
        
        for Row in range(0, len(Sample[Col])):
            Return [Col][Row] = Return [Col][Row] / Peak

#Fully functional normalization by row
def Normal2(Filename):
    
    SampleFreq = 44100
    RawData = ReadWAV(Filename)
    RawAudio = RawData[1]
    Audio = RawAudio[:, 1] 
    AudioLengthSec = int(len(Audio) / SampleFreq)
    SliceDuration = 0.05
    
    # Calculate FFT
    Return = [[0 for x in range(0, int(AudioLengthSec / SliceDuration))] for x in range(0, 480)] 
    for i in range(0, int(AudioLengthSec / SliceDuration)):
        Slice = GetSlice(Audio, i * SliceDuration, SliceDuration, SampleFreq) 
        FFT = GetFFT(Slice, SampleFreq, SliceDuration)
        Normalized = FillFreqBins(FFT, len(FFT), 480)
        
        for ii in range(0, len(Normalized)):
            Return[ii][i] = Normalized[len(Normalized)-ii-1]
    
    
    

    # Find peak across rows and normalize to peak
    for i in range(0, 480):
        Peak = 0
        for ii in range(0, int(AudioLengthSec / SliceDuration)):
            if (Return[i][ii] > Peak):
                Peak = Return [i][ii]
        
        for ii in range(0, int(AudioLengthSec / SliceDuration)):
            Return [i][ii] = Return [i][ii] / Peak
    
#    # Find peak across rows and normalize to peak
#    for i in range(0, 480):
#        Peak = 0
#        for ii in range(0, int(AudioLengthSec / SliceDuration)):
#            if (Return[i][ii] > Peak):
#                Peak = Return [i][ii]
#        
#        for ii in range(0, int(AudioLengthSec / SliceDuration)):
#            Return [i][ii] = Return [i][ii] / Peak
        
    
    
#        Normalized = Normalize(FFT, len(FFT))
#        for ii in range(0, len(Normalized)):
#            Return[ii][i] = Normalized[len(Normalized) - ii - 1]
    
#    # Average all frequency bins
#    Baseline = np.linspace(1, 1, 480)
#    for i in range(480):
#        Average = 0
#        for ii in range(len(Return)):
#            Average = Average + Return[ii][i]
#        Baseline[i] = Baseline[i] / len(Return)
#
#    # Normalize to average frequency bins
#    for i in range(len(Return)):
#        for ii in range(len(Return[i])):
#            Return[i][ii] = Return[i][ii] - Baseline[i]
    
    return Return
        
        
def LoadNormilizationData(Filename):
    
    f = open(Filename, 'r')
    Return = np.linspace(1, 1, 480)
    for i in range(480):
        Line = f.readline()
        Return[i] = float(Line[:-1])
        
    f.close()
    return Return
    



def Breaked(Filename, Width, Height):
    
    SampleFreq = 44100
    RawData = ReadWAV(Filename)
    RawAudio = RawData[1]
    Audio = RawAudio[:, 1] 
    
    SliceLength = len(Audio) / Width
    FreqBinLength = (SampleFreq / 2) / Height
    
    print(SliceLength)    
    
    Return = [[0 for x in range(Width)] for x in range(Height)] 
    for Col in range(Width):
        Slice = GetSlice(Audio, Col * SliceLength, SliceLength, SampleFreq)
        FFT = GetFFT(Slice, SampleFreq, SliceLength)
        for Row in range(Height):
            Return[Col][Row] = FFT[range(Height) - Row - 1]
    
    # Average all frequency bins
    Baseline = np.linspace(1, 1, Height)
    for Row in range(Height):
        Average = 0
        for Col in range(Width):
            Average = Average + Return[Col][Row]
        Baseline[Row] = Baseline[Row] / Width

    # Normalize to average frequency bins
    for Col in range(Width):
        for Row in range(Height):
            Return[Col][Row] = Return[Col][Row] - Baseline[Row]
    
    return Return
    

    




SliceMap = Normal2('foo3.wav')
print('Slice Completed')

#f = open('NormTests.csv', 'w')
#for i in range(0, len(SliceMap)):
#    for ii in range(0, len(SliceMap[i])):
#        f.write(SliceMap[i][ii])
#        f,write(',')
#    f.write('\n')
#f.close()

WI.WriteToImage(SliceMap)
print('Finished')
        








     