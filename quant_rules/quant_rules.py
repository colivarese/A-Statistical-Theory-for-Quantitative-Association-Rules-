import numpy as np
from utils import *

dataset = readFile('./dataset/Hours_age.csv')

dataset = Window(dataset, 0, 1)
print(dataset)