import itertools

L = [2, 5, 4, 3, 7, 8, 9]
print(L)
# [2, 5, 4, 3, 7, 8, 9]

print('slice result from 0: ' + str(L[0::2]))
print('slice result from 1: ' + str(L[1::2]))

print('two number from the list adds up to a targeted number')

print('range practice:')
for i in range(10):
    print(i, end=" ")
print()

print('Range practice with given list:')

print('Practice iter:')

el = iter([1, 2, 3, 4])
first = next(el)
second = next(el)
print(first)
print(second)

print('...................')

for i in el:
    print(i)

from itertools import combinations

list_num = [1, 2 , 4, -3, 3, 5, 6, 7, 8]


def addingTargetNumber(target_num):
    for x, y in itertools.combinations(list_num, 2):
        if x + y == target_num:
            print ( x, y ) # Up to this give the answer of my problem
        #elif int(x+y) != int(target_num):
         #   print ('They doesnt equal: ' + str(x,y))
    #return

addingTargetNumber(11)

print('.................')


