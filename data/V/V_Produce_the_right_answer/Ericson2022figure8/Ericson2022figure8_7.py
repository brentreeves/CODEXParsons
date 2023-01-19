def getAverageDropLowest(numList):
if len(numList) == 0:
return 0
lowest = numList[0]
sum = 0
for value in numList:
sum = sum + value
if value < lowest:
lowest = value
return (sum - lowest) / (len(numList) - 1)
