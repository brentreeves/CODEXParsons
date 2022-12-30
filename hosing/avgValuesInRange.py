# Ericson2017figure4.txt
def avgValuesInRange(numList, start, end):
    sum = 0
    for index in range(start,end-1):
        value = numList[index]
        sum = sum + value
    if (end - start + 1) >= 1:
        return sum / (end - start + 1)
    return 0


print(10)
print( "1],0,0 = 0.0", avgValuesInRange([1],0,0))
print( "[1],0,1) = 0.0", avgValuesInRange([1],0,1))
print( "[1],0,2) = 0.333", avgValuesInRange([1],0,2))
print( "[1],1,1) = 0.0 ", avgValuesInRange([1],1,1))
print( "[1],1,2) = 0.0 ", avgValuesInRange([1],1,2))

print(20)
print( "[1,1],0,0) = 0.0 ", avgValuesInRange([1,1],0,0))
print( "[1,1],0,1) = 0.0 ", avgValuesInRange([1,1],0,1))
print( "[1,1],0,2) = 0.333 ", avgValuesInRange([1,1],0,2))

print(30)
print( "[1,1],1,1) = 0.0 ", avgValuesInRange([1,1],1,1))
print( "[1,1],1,2) = 0.0 ", avgValuesInRange([1,1],1,2))
print( "[1,1],1,3) = 0.333 ", avgValuesInRange([1,1],1,3))

print(40)
print( "[1,2,3],0,0) = 0.0 ", avgValuesInRange([1,2,3],0,0))
print( "[1,2,3],0,1) = 0.0 ", avgValuesInRange([1,2,3],0,1))
print( "[1,2,3],0,2) = 0.333 ", avgValuesInRange([1,2,3],0,2))
print( "[1,2,3],0,3) = 0.75 ", avgValuesInRange([1,2,3],0,3))
print( "[1,2,3],0,4) = 1.2 ", avgValuesInRange([1,2,3],0,4))

print(50)
print( "[-1,-2,-3,-4,-5],0,0) = 0.0 ", avgValuesInRange([-1,-2,-3,-4,-5],0,0))
print( "[-1,-2,-3,-4,-5],0,1) = 0.0 ", avgValuesInRange([-1,-2,-3,-4,-5],0,1))
print( "[-1,-2,-3,-4,-5],0,2) = -0.333 ", avgValuesInRange([-1,-2,-3,-4,-5],0,2))
print( "[-1,-2,-3,-4,-5],0,3) = -0.75 ", avgValuesInRange([-1,-2,-3,-4,-5],0,3))
print( "[-1,-2,-3,-4,-5],0,4) = -1.2 ", avgValuesInRange([-1,-2,-3,-4,-5],0,4))



print( "[1],0,3) = ", avgValuesInRange([1],0,3))

