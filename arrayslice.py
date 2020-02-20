from array import *
array_num = array('i', [1,3,5,7,8,9])
for i in array_num:
    print(i)
print('Access first three items individually')
for i in range(3):
    print(array_num[i])
print("Array num called by index: " + str(array_num[0]))


array_num.append(6)
print(array_num)

print('Python Slices practice')
L = range(10)
print(L)
#range(0, 10)
L[::2]
print(L)
#range(0, 10)

L = [2,5,4,3,7,8,9]
print(L)
#[2, 5, 4, 3, 7, 8, 9]

print('slice result: ' + str(L[::3]))
# slice result with [::2] : [2, 4, 7, 9]
# slice result with [::3] : [2, 3, 9]

print('reverse a list: ' + str(L[::-1]))

print( 'print the length of the array: '+ str(len(array_num)))

print('Length is bytes of one array item: ' + str(array_num.itemsize))

print('Current memory address and the length in elements of the buffer: ' + str(array_num.buffer_info()))

print(' The size of the memory buffer in bytes: ' + str(array_num.buffer_info()[1]* array_num.itemsize))

array_num.append(6)
print(array_num)
print('Number of the occurrences counting: ' + str(array_num.count(6)))

num_list = [1,2,6,-8]
print('Append array_num from the num_list')
array_num.fromlist(num_list)
print(array_num)
# output: array('i', [1, 3, 5, 7, 8, 9, 6, 6, 1, 2, 6, -8])
print('insert a new value 4 before 3 ' + str(array_num.insert(1,4)))
print(array_num)
print('remove an item from an array using index: ' + str(array_num.pop(2))) # removes third item from array
print(array_num)
print('Remove first occurrence of a specified item: ' + str(array_num.remove(6)))
print(array_num)
print('convert an array to an ordinary list with the same items:')
num_list1 = array_num.tolist()
print(num_list1)
print('find if an array contains duplicate value: ')
def test_duplicate(array_num):
    numset = set(array_num)
    return len(array_num) != len(numset)
print(test_duplicate([1,2,2,4,5]))
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,3,4,5]))

print('Find out first duplicate number:')
def find_first_duplicate(nums):
    num_set = set()
    no_duplicate= -1

    for i in range(len(nums)):
        if nums[i] in num_set:
            return nums[i]
        else: num_set.add(nums[i])
    return no_duplicate
print(find_first_duplicate([1,2,3,4,5]))
print(find_first_duplicate([1,2,2,3,4,5]))
print(find_first_duplicate([1,2,2,3,4,5,5]))





