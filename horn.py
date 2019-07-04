#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Horn detection Get Instensities per second
from scipy.io import wavfile as wav
import numpy as np
import scipy
from progress import printProgressBar
import os
import sys

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def convert_to_hhmmss(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h,24)
    return "%02d:%02d:%02d" % (h, m, s)

def date_time(text,i):
    import re
    var = re.findall(r'\d+',text.split('/')[-1])
    seconds = get_sec(var[3]+':'+var[4]+':'+var[5]) + i
    return var[1]+'/'+var[2]+'/'+var[0]+' '+convert_to_hhmmss(seconds)

def convert_to_mono(x):
    return x.astype(float).sum(axis=1) / 2

def band_pass(x,sr,fL,fU):
    x = list(np.array(x))           #converting array to list
    i = 1
    out = []
    while i*sr<len(x):      #sampling rate X time actually i is the time to reach all the samples
        x_ = x[(i-1)*sr:i*sr]   #considering the values of the currently working i only its equal to sr actually
        fft_out = np.fft.fft(x_)        #fast fourier transformation taking from time domain to frequency domain
        fft_out[0:fL] = 0           #FL is the lowest index from which we will start counting the freq
        fft_out[fU:-1] = 0             #FU is highest freaq we will consider for the horn
        wave = np.fft.ifft(fft_out)     #For the portion we wont consider we make it 0 to cut off noise
        out += list(wave.real)            #fft sometimes gives complex number we must only consider the real part
        i += 1
    return np.array(out).astype(np.int16)       #converting list to np array of integer

def write_audio(x,sr,filename = 'work.wav'):
    scipy.io.wavfile.write(filename,sr,x)

def read_audio(filename):
    sr, x = wav.read(filename)          #sr->sampling rate  
                                        #x->data (numpy array)
    return sr,x

def dbfft(x, fs, win=None, ref=32768):
    """
    Calculate spectrum in dB scale
    Args:
        x: input signal
        fs: sampling frequency
        win: vector containing window samples (same length as x).
             If not provided, then rectangular window is used by default.
        ref: reference value used for dBFS scale. 32768 for int16 and 1 for float
        #######-----------------------------------------------##################
        db is decibel scale it is a comperative score not absolute 10 db means 10times louder than another sound
        dbFS is full scale decibel it is absolute measure of the maximum sound allowed to be saved on a disk

        0 dbFS is the maximum sound that can be stored so actually -10 dbFS is much greater than 10 db 
        it is digital modulation. so to save we must  convert db to dbFS
        ---------------------------------------------------------------
    Returns:
        freq: frequency vector
        s_db: spectrum in dB scale
    """

    N = len(x)  # Length of input sequence

    if win is None:
        win = np.ones(N)       #making win np array of 1 
    if len(x) != len(win):
            raise ValueError('Signal and window must be of the same length')
    x = x * win         #conversion

    # Calculate real FFT and frequency vector
    sp = np.fft.rfft(x)                 #calculate the fft and give real valued data only calculated in real domain
    freq = np.arange((N / 2) + 1) / (float(N) / fs) #arange function returns a ndarray of evenly spaced integers i the given range by default
    #produces the fft spectrum

    '''
    the fft spectrum is symmetric about an axis line so we consider upper half only

    but due to parsing the amp also becomes half so double it to maintain the actual value
    '''
    # Scale the magnitude of FFT by window and factor of 2,
    # because we are using half of FFT spectrum.
    s_mag = np.abs(sp) * 2 / np.sum(win)    #scaling the magnitude

    # Convert to dBFS
    s_dbfs = 20 * np.log10(s_mag/ref)

    # Scale from dBFS to dB
    K = 120
    s_db = s_dbfs + K
    return freq, s_db

    #returns the sampling freq and the new numpy array having scale of dbFS

def main():
    filename ='new_data'

    files=os.listdir(filename)
    files.sort()
    folder = "sound_f"
    if os.path.exists("sound_f"):
    	os.system("rm -r sound_f")
    os.mkdir("sound_f")
    ext="/Sound"
    count=0
    for i in files:
        count+=1
        name=filename+"/"+i+ext
        file=os.listdir(name)
        name_f=name+"/"+file[0]
        sr, x = read_audio(name_f)
    # print(x.shape)
        if len(x.shape) == 2: # if channael is stereo then convert it to mono
                        #if wavefile is stereofile the data is returned in the form of multi dimensional
                      #array,if we need to convert the stereo to mono
                        # we need to add up the two values of the list of the index as 1 as float data
            x = convert_to_mono(x)
        X = band_pass(x, sr, 2000, 5001)#we consider between 2000 & 5001
        i = 1
        pwd = os.getcwd()       #get the current working directory
        os.chdir(folder)        #folder variable actually contains the output directoy changing to it
        f= open("processed_"+os.path.basename(name_f)[:-4]+"_0"+str(count)+".txt","w+")       #newfile in output dir to write as text
        while i*sr<len(X):      #sampling rate X time actually i is the time to reach all the samples
            x_ = X[(i-1)*sr:i*sr]     #considering the values of the currently working i only its equal to sr actually      
       # Take slice
            N = 8000
            win = np.hamming(N)      #https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.hamming.html
                                #we want the array final to have 8000 value.hamming(m):m->int->number of points in the output window
                                #if zero empty array is returned.The output is a normalized numpy array of 8000 values
            freq, s_db = dbfft(x_, sr, win)
            t=date_time(name_f,i)
            date,time=t.split(" ")

            f.write( date+','+time+","+str(np.max(s_db))+'\n')# logging data timewise and the value
            i += 1
            printProgressBar(i*sr,len(X))        #print the progress of operation for each sound file
        f.close()
       # write_audio(X,sr,os.path.basename(name_f)[:-4]+'_filtered.wav') #saving the sounds with the honks only
        os.chdir(pwd)

if __name__== "__main__":
  main()
