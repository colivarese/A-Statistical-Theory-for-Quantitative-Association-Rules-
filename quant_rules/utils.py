import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats import weightstats as stests
import itertools
import time
import matplotlib.pyplot as plt

def readFile(file, asArray):
    df = pd.read_csv(file)
    if asArray:
        return df.to_numpy()
    else:
        return df


def sortOnIndex(array, dim):
    return sorted(array, key=lambda a: a[dim])

def getDimension(array, dim):
    return [a[dim] for a in array]

def getAverage(A,B):
    return np.mean(A+B)

def preprocess(array,dim,minDif):
    #TODO ponemos la dimension sobre la cual ordenas y el otro es el entrada al window
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

def createRules(rules,array,dim):
    prev = None
    sorted_arr = sortOnIndex(array,dim)
    for r in rules:
        if r[1]==len(array):
            break
        else:
            if prev is None:
                print("[ None, ",sorted_arr[r[1]][0],"]", " ==> " , round(np.mean(r[0])))
            else:
                print("[",sorted_arr[prev][0], "," ,sorted_arr[r[1]][0], "] ==> " , round(np.mean(r[0])))
        prev = r[1]

    

# --- CATEGORICAL-----

def extractCategorical(dataset, asArray):
    if asArray:
        return dataset.select_dtypes(['object']).to_numpy()
    else:
        return dataset.select_dtypes(['object'])

def extractNumerical(dataset, asArray):
    if asArray:
        return dataset.select_dtypes(['int64']).to_numpy()
    else:
        return dataset.select_dtypes(['int64'])

def getCategoricalHeaeders(dataset):
    categorical_headers = [key for key in dict(dataset.dtypes) if dict(dataset.dtypes)[key] in ['object']]
    categorical_headers = list(combinations(categorical_headers))
    return [header for header in categorical_headers if len(header) > 0]

def getQuantHeaders(dataset):
    return [key for key in dict(dataset.dtypes) if dict(dataset.dtypes)[key] in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']]

def combinations(items):
    return ( set(itertools.compress(items,mask)) for mask in itertools.product(*[[0,1]]*len(items)) )
    # alternative:  