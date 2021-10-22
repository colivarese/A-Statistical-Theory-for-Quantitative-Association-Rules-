import numpy as np
from utils import *

dataset = readFile('./dataset/hours_gad.csv')

dataset, avg, minDif = preprocess(dataset,0,1)
rules = Window(dataset, avg, minDif)
pass

