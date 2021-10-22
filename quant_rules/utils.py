import pandas as pd
import numpy as np

def readFile(file):
    df = pd.read_csv(file)
    return df.to_numpy()

def sortOnIndex(array, dim):
    return sorted(array, key=lambda a: a[dim])

def getDimension(array, dim):
    return [a[dim] for a in array]

def Window(array,dim, minDif):
    avg = np.mean(getDimension(array,dim)) + minDif
    sorted_arr = sortOnIndex(array,dim)
    return sorted_arr
