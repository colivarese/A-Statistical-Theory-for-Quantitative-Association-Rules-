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
![Quant Performance](https://user-images.githubusercontent.com/80273045/138647271-6b35932f-ecb8-4001-b5a9-e707ff384fc4.png)

Categorical Performance 
![Categorical performance](https://user-images.githubusercontent.com/80273045/138647305-dc9d4494-f6fc-4837-abff-58223a50ca4d.png)

