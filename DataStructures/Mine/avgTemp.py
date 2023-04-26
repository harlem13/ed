from array import *
import numpy as np

noDays = int(input("Days to enter for temperature calc"))
a = np.array([])
#a = array('i',[])
for i in range(1,noDays+1):
    temp = int(input(str(i)+"'day's temp : "))
    a = np.append(a,temp)
print(a)

aMean = a.mean()
print(aMean)
aboveAvg = 0
for i in a:
    if i > aMean:
        aboveAvg += 1
print(aboveAvg)