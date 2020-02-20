def increment(n):
    print(id(n))
    n += 1
    print(id(n))
    print(n)
b = 5
increment(b)
print(id(b))
''' Output:
140710500484896
140710500484928
6
140710500484896
'''

def increment1(n):
    print(id(n))
    n.append(3)
    print(id(n))
    print(n)
b = [1,2]
increment1(b)
print(id(b))
''' 
1929330094912
1929330094912
[1, 2, 3]
1929330094912
'''
