firstDict = {}
firstDict = {'one':{'hello':'uno'},'two':{'hola':'dos'}}
secondDict = firstDict
thirdDict = firstDict.copy()
print(secondDict)
newDict = {}.fromkeys([1,2,3],0)
print(newDict)
firstDict['three']={'Hallo':'tres'}
print(firstDict)
print(secondDict)
print(thirdDict)
print(thirdDict.get('two')) # or use setDefault() which works the same I think
print(firstDict.keys())
print(firstDict.values())
thirdDict.update(firstDict)
print(thirdDict)

simpleDict = {1:'Ed',2:'Mogol',3:'Bestos',4:'Beyzos',5:'Zuzu'}
print(simpleDict[1])
print(id(simpleDict))

#print(firstDict['one']['hello'])
#print(hash(firstDict['one']['hello']))
#firstDict.clear()