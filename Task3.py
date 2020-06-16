import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance 
from operator import itemgetter

sensores = pd.read_csv('sensors.txt', sep = ' ', names = ['sx','sy'])
centrais = pd.read_csv('centrais.txt', sep = ',', names = ['centrais','cx','cy'])

plt.scatter(sensores.sx, sensores.sy)
plt.show()

plt.scatter(centrais.cx, centrais.cy)
plt.show()

final = dict()
for index, rowz in sensores.iterrows():
  s = (rowz['sx'], rowz['sy'])
  vet = []
  for index, rowc in centrais.iterrows():
    c = (rowc['cx'], rowc['cy'])
    cName = rowc['centrais']
    dst = distance.euclidean(s, c)
    if(dst <= 0.25):
     vet.append(cName)
  final.setdefault(s, vet)

countEmpty = 0;
countMore = 0;
countOne = 0;
string = []
for index, rowz in sensores.iterrows():
  s = (rowz['sx'], rowz['sy'])
  if (len(final.get(s)) == 0 ):
    countEmpty += 1
  if(len(final.get(s)) > 1 ):
    countMore += 1
  if(len(final.get(s)) == 1 ): 
    countOne += 1
    string.append(final.get(s))

dc = dict()
for index, row in centrais.iterrows():
  cName = row['centrais']
  count = string.count([cName])
  dc.setdefault(cName, count)
ordered = dict(sorted(dc.items(), key=itemgetter(1)))

print("Sensores e centrais alcançadas:")
print(final)
print("Sensores que não possuem centrais alcançadas:",countEmpty)
print("Sensores que possuem mais de duas centrais alcançadas:",countMore)
print("Sensores que possuem apenas uma central alcançada:",countOne)
print("Estações por ordem crescente de quantidade de sensores atendidos:")
print(ordered)
