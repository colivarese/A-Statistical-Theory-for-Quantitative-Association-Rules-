import numpy as np
from utils import *
from apriori import *
from utilsApriori import *
dataset = readFile('./dataset/categorical.csv', asArray=False)

cat_dataset = extractCategorical(dataset)

freq_itemset = aprioriFromFile('./dataset/categorical.csv',600,100)
n = len(freq_itemset[0])
keys = range(0,n)
freqs = {key: [] for key in keys}
for i in range(n):
    for its in freq_itemset[0][i]:
        freqs[i].append(list(its))

print(len(freq_itemset[0]))
freq_itemset = (freq_itemset[0][2])
freq = [list(x) for x in freq_itemset]
#print(freq)
