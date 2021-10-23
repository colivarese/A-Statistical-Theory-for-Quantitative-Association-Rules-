import numpy as np
from utils import *
from apriori import *
from utilsApriori import *
dataset = readFile('./dataset/categorical.csv', asArray=False)


cat_dataset = extractCategorical(dataset,asArray=True)
reversed_cat = [set(i) for i in cat_dataset]

dataset = dataset.to_numpy()
freq_itemset = aprioriFromFile('./dataset/categorical.csv',100,100)
n = len(freq_itemset[0])
keys = range(0,n)
freqs = {key: [] for key in keys}
for i in range(n):
    for its in freq_itemset[0][i]:
        freqs[i].append(set(its))


for freq in freqs[2]:
    indices = [i for i, x in enumerate(reversed_cat) if x == freq]
    tmp_sum = []
    for idx in indices:
        tmp_sum.append(dataset[idx][3])
    #print(freq, "==>", np.mean(tmp_sum))
print(freqs[1])