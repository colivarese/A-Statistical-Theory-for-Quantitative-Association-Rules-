import pandas as pd
import numpy as np

def readFile(file):
    return pd.read_csv(file, index=False)

def sortOnIdndex(array):
    pass

def Window(array,dim, minDif):
    avg = np.mean(array[:,dim]) + minDif
    sorted(array, key=lambda a: a[dim])
    return sorted
