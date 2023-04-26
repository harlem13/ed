from array import *
import numpy as np

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
print(fruit_list3)
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

print(fruit_list1)
print(fruit_list2)
print(fruit_list3)
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
        print(sum)
    if ls[1] == 'Kiwi':
        sum += 20


print(sum)

a=[1,2,3,4,5,6,7,8,9]
print(a[3:0:-1])

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
print(arr[6])
for i in range(0, 6):
    print(arr[i], end = " ")

a=[1,2,3,4,5]
print(a.pop())

arr1 = array('i',[1,2,3,4,4,4,4,4,4,4,5])
print(arr1)
arr1.pop()
print(arr1)
print(arr1.index(2))
arr1.reverse()
print(arr1)
arr1.insert(5,19)
print(arr1.buffer_info())
print(arr1.count(4))
arr1.append(666)
print(arr1)

print(arr1[3:])
print(arr1[:4])

print("___Starting Numpy Array Examples_____________________________")

arrN = np.array([["adnan", "cem", "erman"], ["ezgi", "betul", "naz"], ["NL","IS","GR"]])
print(arrN)
print(arrN[1,2])
arrN = np.insert(arrN,1,[["hello","hola","hallo"]],axis=0)
print(arrN[1,2])
print('hola' in arrN)

list1 = ['ed',1, 25, 'istanbul', 'blue']
print(list1)

del list1[3:5]
print(list1)

#list1.remove('istanbul')
#print(list1)

#list1.pop(1)
#print(list1)


#list1.pop()
#print(list1)
print('...............')
list1 = list1*2
print(list1)
