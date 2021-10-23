import numpy as np
from utils import *
from apriori import *
from utilsApriori import *
dataset = readFile('./dataset/categorical.csv', asArray=False)


cat_dataset = extractCategorical(dataset,asArray=True)
reversed_cat = [set(i) for i in cat_dataset]
pd.DataFrame(reversed_cat).to_csv('./dataset/categorical_only.csv')
quant_dataset = extractNumerical(dataset,asArray=True)

#freq_itemset = aprioriFromFile('./dataset/categorical.csv',400,100)
freq_itemset = aprioriFromFile('./dataset/categorical_only.csv',700,100)
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
        tmp_sum.append(quant_dataset[idx]) #SOLO AGREGA LA SIGUIENTE DIMENSION CAMBIAR A QUE AGREGE TODAS LAS NUMERICAS
    print(freq, "==>", np.mean(tmp_sum,axis=0))
