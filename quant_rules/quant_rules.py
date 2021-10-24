from os import PathLike
import numpy as np
from utils import *

dataset = readFile('./dataset/hours_gad.csv',asArray=True)

data_to_work, avg, minDif = preprocess(dataset,0,5)
rules = Window(data_to_work, avg, minDif)

cols = getQuantHeaders(readFile('./dataset/hours_gad.csv',asArray=False))
print(cols[0], " ==> ",cols[1])
createRules(rules,dataset,0) 





