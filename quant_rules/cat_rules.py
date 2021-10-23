import numpy as np
from utils import *
from apriori import *
from utilsApriori import *
dataset = readFile('./dataset/categorical.csv', asArray=False)

cat_dataset = extractCategorical(dataset,asArray=True)
reversed_cat = list([list(reversed(i)) for i in cat_dataset])

freq_itemset = aprioriFromFile('./dataset/categorical.csv',400,100)
n = len(freq_itemset[0])
keys = range(0,n)
freqs = {key: [] for key in keys}
for i in range(n):
    for its in freq_itemset[0][i]:
        freqs[i].append(list(its))

print(freqs[2][0] in reversed_cat)
print(freqs[2][0])
print(reversed_cat[10])