import numpy as np
from utils import *
import time
import matplotlib.pyplot as plt

def getQuantRules(dataFile, minDif_in):
    dataset = readFile(dataFile,asArray=True)

    #dataset = readFileCols_quant(dataFile,cols)

    data_to_work, avg, minDif = preprocess(dataset,0,minDif_in)
    rules = Window(data_to_work, avg, minDif)

    cols = getQuantHeaders(readFile(dataFile,asArray=False))
    print(cols[0], " ==> ",cols[1])
    createRules(rules,dataset,0) 

def getQuantPerformance(dataFile, low_minDif, high_minDif, step_minDif):
    x = []
    y = []
    for i in range(low_minDif,high_minDif,step_minDif):
        start_time = time.time()
        getQuantRules(dataFile=dataFile,minDif_in=i)
        x.append(i)
        y.append((time.time() - start_time))

    plt.plot(x, y, 'k-', marker='o',lw=1.5)
    plt.xlabel('Support threshold')
    plt.ylabel('Runtime (sec)')
    plt.grid(color='black', linestyle='-', linewidth=0.09)
    plt.title('Time against support threshold')
    plt.show()


#Guardar en la carpeta de dataset tus datos
#Para el cuantitativo SOLO debe haber columnas numericas
#getQuantRules(dataFile='./dataset/hours_gad.csv',minDif_in=3)


#getQuantPerformance(dataFile='./dataset/hours_gad.csv',low_minDif=1, high_minDif=6, step_minDif=1)

getQuantPerformance(dataFile='./dataset/hours_gad.csv', low_minDif=1, high_minDif=6, step_minDif=1)








