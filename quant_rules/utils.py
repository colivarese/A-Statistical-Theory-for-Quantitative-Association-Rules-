import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats import weightstats as stests


def readFile(file):
    df = pd.read_csv(file)
    return df.to_numpy()

def sortOnIndex(array, dim):
    return sorted(array, key=lambda a: a[dim])

def getDimension(array, dim):
    return [a[dim] for a in array]

def getAverage(A,B):
    return np.mean(A+B)

def preprocess(array,dim,minDif):
    avg = np.mean(getDimension(array,1)) + minDif
    sorted_arr = sortOnIndex(array,dim)
    array = [a[1] for a in sorted_arr]
    return array, avg, minDif

def nextAboveAvg(arr,avg,current):
    for idx in range(current, len(arr)):
        if arr[idx] >= avg:
            return idx

def Window(array,avg,minDif):
    R = []
    avg += minDif
    current = 0
    end_of_array = len(array)

    while current < end_of_array:
        current = nextAboveAvg(array,avg,current)
        A,B = [],[]
        A.append(array[current])
        while (getAverage)(A,B) >= avg:
            B.append(array[current])
            current += 1
            if current == end_of_array:
                break
            if getAverage(B,[]) > avg:
                A += B
                B = []
        _ ,pval = stests.ztest(A, x2=None, value=np.mean(A))
        if pval > 0.05:
            R.append((A,current))
        #    Window(A, getAverage(A,[]),minDif)
        current += 1
    return R

    

