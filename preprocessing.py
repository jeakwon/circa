import os
import pyabf
import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt
import utils
import datetime

class Converter:

    def convert(self, abf):
        fs = abf.dataRate
        converted = []
        for data in abf.data:
            data = self.__high_pass_filter(data, fs)
            data = self.__root_mean_square(data, fs)
        return data

    @staticmethod
    def __high_pass_filter(x, fs, cutoff=1, order=5):
        fnyq = 0.5 * fs
        normal_cutoff = cutoff/fnyq
        b, a = butter(N=order, Wn=normal_cutoff, btype='high',analog=False)
        return filtfilt(b, a, x)

    @staticmethod
    def __root_mean_square(x, window):
        x = np.convolve(x**2, np.ones((window,))/window, mode='valid')
        return np.sqrt(x)

    @staticmethod
    def __integral_average(x, window):
        return np.convolve(abs(x), np.ones((window,))/window, mode='valid')


if __name__ == '__main__':
    converter = Converter()
    abf = pyabf.ABF('sample.abf')
    data = converter.convert(abf)
    import matplotlib.pyplot as plt
    # plt.plot(data)
    # plt.show()
    # print(data)
    print(abf.abfDateTime)
    df = pd.DataFrame(data)
    # datetime.timedelta(seconds=1/20)
    print(
        pd.date_range(start=abf.abfDateTime, periods=len(data))
    )
    print(abf.dataPointCount)
    print(len(pd.date_range(start="2018-4-1", periods=30)))
    # from pprint import pprint
    # for item in dir(abf):
    #     print(item, abf.__getattribute__(item))
    # print(abf.abfDateTime)
    # print(abf.adcNames)
    # # print(converter.convert(abf).shape)