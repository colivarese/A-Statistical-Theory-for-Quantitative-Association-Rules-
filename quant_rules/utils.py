import pandas as pd

def readFile(file):
    return pd.read_csv(file, index=False)
    print('hi')