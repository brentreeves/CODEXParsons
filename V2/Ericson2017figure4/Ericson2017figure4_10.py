def avgValuesInRange(numList, start, end):
sum = 0
if (end - start + 1) >= 1:
for index in range(start,end-1):
value = numList[index]
sum = sum + value
return sum / (end - start + 1)
return 0
