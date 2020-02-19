a = lambda x,y : x+y

print(a(2,5))
print(a(x= int(input("Enter a number")), y= int(input("Enter another number"))))

def lamultiplier(n):
    return lambda x : x*n

mydoubler= lamultiplier(2)
mytripler= lamultiplier(3)

print(mydoubler(11))
print(mytripler(11))