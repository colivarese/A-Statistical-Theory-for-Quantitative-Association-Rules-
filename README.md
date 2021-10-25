# A-Statistical-Theory-for-Quantitative-Association-Rules-
An algorithm to find association rules with quantitative values, based on the paper: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.92.4189&amp;rep=rep1&amp;type=pdf

Save datafile (.csv) on the dataset folder

To get Quantitative => Quantitative Rules

    On the quant_rules.py file use the function
    getQuantRules(dataFile='./dataset/YOUR_OWN_CSV',minDif_in=INT)


To get Categorical => Quantitatve Rules

    On the cat_rules.py file use the function
    getCatQuantRules(dataFile='./dataset/YOUR_OWN_CSV',support=INT)


There is no Hash-Tree implementation, this results in slower times.

Quantitative Performance

![Quant Performance](https://user-images.githubusercontent.com/80273045/138647541-eefdded6-991c-4f55-a128-0ee6307d9e15.png)

Categorical Performance 

![Categorical performance](https://user-images.githubusercontent.com/80273045/138647560-a1b90530-a827-4d24-b769-b9a77eaf20f6.png)
