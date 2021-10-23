import numpy as np
from utils import *

dataset = readFile('./dataset/hours_gad.csv',asArray=True)

data_to_work, avg, minDif = preprocess(dataset,0,1)
rules = Window(data_to_work, avg, minDif)

createRules(rules,dataset,0)

