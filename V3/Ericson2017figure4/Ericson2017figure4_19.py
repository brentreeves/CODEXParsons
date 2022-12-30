def avgValuesInRange(numList, start, end):
if (end - start + 1) >= 1:
sum = 0
for index in range(start,end-1):
value = numList[index]
sum = sum + value
return sum / (end - start + 1)
return 0
