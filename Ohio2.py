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


def FreqToBin(Sample, length, outLength = 480):

    Return = np.linspace(1, 1, outLength)        
    for i in range(0, outLength):
        Return[i] = 0
        for ii in range(int(i * (length / outLength)), int((i + 1) * (length / outLength))):
            if (Sample[ii] > Return[i]):
                Return[i] = Sample[ii]

    return Return
    


def NormalizeAvg(Matrix):

    Return = [[0 for x in range(0, len(Matrix[0]))] for x in range(0, len(Matrix))]
    # Average all frequency bins
    Baseline = np.linspace(1, 1, 480)
    for i in range(0, len(Matrix)):
        Average = 0
        for ii in range(0, len(Matrix[i])):
            Average = Average + Matrix[i][ii]
        Baseline[i] = Baseline[i] / len(Matrix[i])

    # Normalize to average frequency bins
    for i in range(0, len(Matrix)):
        for ii in range(0, len(Matrix[i])):
            Return[i][ii] = Matrix[i][ii] / Baseline[i]

    return Return

def NormalizeFreq(Matrix):

    print(len(Matrix))
    print(len(Matrix[0]))

    Return = [[0 for x in range(0, len(Matrix[0]))] for x in range(0, len(Matrix))]
    # Average across all slices
    for i in range(0, len(Matrix)):
        Peak = 0
        for ii in range(0, len(Matrix[i])):
            if (Peak < Matrix[i][ii]):
                Peak = Matrix[i][ii]

        #if (Peak != 0):
        for ii in range(0, len(Matrix[i])):
            Return[i][ii] = Matrix[i][ii] / Peak

    return Return

def NormalizeSlice(Matrix):

    Return = [[0 for x in range(0, len(Matrix[0]))] for x in range(0, len(Matrix))]
    # Average across all frequency bins
    for ii in range(0, len(Matrix[0])):
        Peak = 0
        for i in range(0, len(Matrix)):
            if (Peak < Matrix[i][ii]):
                Peak = Matrix[i][ii]

        #if (Peak != 0):
        for i in range(0, len(Matrix)):
            Return[i][ii] = Matrix[i][ii] / Peak

    return Return


def NormalizeLog(Matrix):

    Return = [[0 for x in range(0, len(Matrix[0]))] for x in range(0, len(Matrix))]
    # Average across all frequency bins
    for ii in range(0, len(Matrix[0])):
        Peak = 0
        for i in range(0, len(Matrix)):
            if (Peak < Matrix[i][ii]):
                Peak = Matrix[i][ii]

        #if (Peak != 0):
        for i in range(0, len(Matrix)):
            Return[i][ii] = np.log10(Matrix[i][ii] / Peak)

    return Return

def NormalizeTest(Matrix, multiplier = 20):

    Return = [[0 for x in range(0, len(Matrix[0]))] for x in range(0, len(Matrix))]
    # Average across all frequency bins
    for ii in range(0, len(Matrix[0])):
        Peak = 0
        for i in range(0, len(Matrix)):
            if (Peak < Matrix[i][ii]):
                Peak = Matrix[i][ii]

        #if (Peak != 0):
        for i in range(0, len(Matrix)):
            Return[i][ii] = multiplier * np.log10(Matrix[i][ii] / Peak)

        Min = 0
        for i in range(0, len(Matrix)):
            if (Min > Return[i][ii]):
                Min = Return[i][ii]

        for i in range(0, len(Matrix)):
            Return[i][ii] = abs(Return[i][ii] / Min)

    return Return

def NormalizePeaks(Matrix):

    Return = [[0 for x in range(0, len(Matrix[0]))] for x in range(0, len(Matrix))]
    # Average across all frequency bins
    for ii in range(0, len(Matrix[0])):

        for i in range(0, len(Matrix) - 1):
            Return[i][ii] = abs(Matrix[i][ii] - Matrix[i + 1][ii])

        Peak = 0
        for i in range(0, len(Matrix)):
            if (Peak < Matrix[i][ii]):
                Peak = Matrix[i][ii]

        for i in range(0, len(Matrix)):
            Return[i][ii] = Matrix[i][ii] / Peak

    return Return



def GetSliceMap(Filename):
    
    SampleFreq = 44100
    RawData = ReadWAV(Filename)
    RawAudio = RawData[1]
    Audio = RawAudio[:, 1] 
    AudioLengthSec = int(len(Audio) / SampleFreq)
    SliceDuration = 0.05
    
    # Calculate FFT
    Return = [[0 for x in range(int(AudioLengthSec / SliceDuration))] for x in range(480)] 
    for i in range(0, int(AudioLengthSec / SliceDuration)):
        Slice = GetSlice(Audio, i * SliceDuration, SliceDuration, SampleFreq) 
        FFT = GetFFT(Slice, SampleFreq, SliceDuration)
        BinData = FreqToBin(FFT, len(FFT))
        for ii in range(0, len(BinData)):
            Return[ii][i] = BinData[len(BinData) - ii - 1]

    return Return

def ToFile(Mat, Filename):
    f = open(Filename, 'w')
    for i in range(0, len(Mat)):
        for ii in range(0, len(Mat[i])):
            f.write(str(Mat[i][ii]))
            f.write(',')
        f.write('\n')
    f.close()



NotNorm = GetSliceMap('bone.wav')

#ToFile(NotNorm, 'You try so hard, and come so far, but in the end it doesnt even matter.csv')
#Norm1 = NormalizeFreq(NotNorm)

#
print('10%')
Norm1 = NormalizeAvg(NotNorm)
#ToFile(Norm1, 'n1.csv')
print('20%')
Norm2 = NormalizeFreq(NotNorm)
#ToFile(Norm2, 'n2.csv')
print('30%')
Norm3 = NormalizeSlice(NotNorm)
ToFile(Norm3, 'n3.csv')
print('40%')
Norm4 = NormalizeTest(NotNorm)
Norm3 = NormalizeFreq(Norm4);
#ToFile(Norm4, 'n4.csv')
print('50%')

print('Slice Completed')

#WI.WriteToImage(NotNorm)
print('60%')
#WI.WriteToImage(Norm1)
print('70%')
#WI.WriteToImage(Norm2)
print('80%')
WI.WriteToImage(Norm3)
print('90%')
WI.WriteToImage(Norm4)
print('100%')

print('Finished')









     