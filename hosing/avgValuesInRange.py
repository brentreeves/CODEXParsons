# Ericson2017figure4.txt
def avgValuesInRange(numList, start, end):
    sum = 0
    for index in range(start,end+1):
        value = numList[index]
        sum = sum + value
    if (end - start + 1) >= 1:
        return sum / (end - start + 1)
    return 0


print(10)
print( "[1],0,0 = 1.0 == ", avgValuesInRange([1],0,0))
print( "[1,1],0,0 = 1.0 == ", avgValuesInRange([1,1],0,0))
print( "[1,1,1],0,0 = 1.0 == ", avgValuesInRange([1,1,1],0,0))
print( "[1,1,1,1],0,0 = 1.0 == ", avgValuesInRange([1,1,1,1],0,0))

print(20)
print( "[1,1],0,1 = 1.0 == ", avgValuesInRange([1,1],0,1))
print( "[1,1,1],0,2 = 1.0 == ", avgValuesInRange([1,1,1],0,2))
print( "[1,1,1,1],0,3 = 1.0 == ", avgValuesInRange([1,1,1,1],0,3))

print(30)
print( "[1,3],0,1 = 2.0 == ", avgValuesInRange([1,3],0,1))
print( "[1,4,1],0,2 = 2.0 == ", avgValuesInRange([1,4,1],0,2))
print( "[1,2,3,4],0,3 = 2.5 == ", avgValuesInRange([1,2,3,4],0,3))
print( "[1,2,3,4,5],0,2 = 2 == ", avgValuesInRange([1,2,3,4,5],0,2))
print( "[1,2,3,4,5],2,4 = 3 == ", avgValuesInRange([1,2,3,4,5],2,4))

print(40)
print( "[1],0,0 = 1.0 == ", avgValuesInRange([1],0,0))
print( "[2],0,0 = 2.0 == ", avgValuesInRange([2],0,0))

