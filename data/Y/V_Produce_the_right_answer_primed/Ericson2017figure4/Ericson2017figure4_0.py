def avgValuesInRange(numList, start, end):
for index in range(start,end+1):
value = numList[index]
sum = sum + value
if (end - start + 1) >= 1:
return sum / (end - start + 1)
sum = 0
return 0
