import numpy as np
from utils import *
from apriori import *
from utilsApriori import *
import os
import itertools
dataset = readFile('./dataset/categorical_two.csv', asArray=False)

categoricalHead = getCategoricalHeaeders(dataset)
quantHead = getQuantHeaders(dataset)

for head in categoricalHead:
    print(head, ' ==> ', quantHead)
    cat_dataset = extractCategorical(dataset[head],asArray=True)
    reversed_cat = [set(i) for i in cat_dataset]
    pd.DataFrame(reversed_cat).to_csv('./dataset/categorical_only.csv')
    quant_dataset = extractNumerical(dataset,asArray=True)

    #freq_itemset = aprioriFromFile('./dataset/categorical.csv',400,100)
    freq_itemset = aprioriFromFile('./dataset/categorical_only.csv',400,100)
    n = len(freq_itemset[0])
    keys = range(0,n)
    freqs = {key: [] for key in keys}
    for i in range(n):
        for its in freq_itemset[0][i]:
            freqs[i].append(set(its))

    for freq in freqs[len(freqs)-1]:
        indices = [i for i, x in enumerate(reversed_cat) if x == freq]
        tmp_sum = []
        for idx in indices:
            tmp_sum.append(quant_dataset[idx]) 
        print(freq, "==>", np.mean(tmp_sum,axis=0))
    os.remove('./dataset/categorical_only.csv')
    print(" ============== \n \n")
