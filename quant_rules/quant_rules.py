import numpy as np
from utils import *

def getQuantRules(dataFile, minDif_in):
    dataset = readFile(dataFile,asArray=True)

    data_to_work, avg, minDif = preprocess(dataset,0,minDif_in)
    rules = Window(data_to_work, avg, minDif)

    cols = getQuantHeaders(readFile(dataFile,asArray=False))
    print(cols[0], " ==> ",cols[1])
    createRules(rules,dataset,0) 


#Guardar en la carpeta de dataset tus datos
#Para el cuantitativo SOLO debe haber columnas numericas
getQuantRules(dataFile='./dataset/hours_gad.csv',minDif_in=5)








