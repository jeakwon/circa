import os
import pyabf
import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt
import utils
class Converter:
    def convert(self, abf):
        fs = abf.dataRate
        converted = []
        for data in abf.data:
            data = self.__high_pass_filter(data, fs)
            data = abs(data)
            data = self.__down_sampling(data, fs)
        return data

    def absolutize(self, abf):
        return 

    @staticmethod
    def __high_pass_filter(x, fs, cutoff=1, order=5):
        fnyq = 0.5 * fs
        normal_cutoff = cutoff/fnyq
        b, a = butter(N=order, Wn=normal_cutoff, btype='high',analog=False)
        return filtfilt(b, a, x)

    @staticmethod
    def __down_sampling(x, factor):
        M = factor
        N = int(np.ceil(len(x)/factor))
        
        X = np.copy(x)
        X.reshape(-1, M)
        Y = np.mean(X,1)
        
        return Y


if __name__ == '__main__':
    converter = Converter()
    abf = pyabf.ABF('sample.abf') 
    print(converter.convert(abf).shape)