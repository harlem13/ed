fruit = {}


def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1


addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))