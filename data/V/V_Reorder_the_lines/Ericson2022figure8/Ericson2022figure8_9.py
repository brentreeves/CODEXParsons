def getAverageDropLowest(numList):
if len(numList) == 0:
return 0
lowest = numList[0]
sum = numList[0]
for index in range(1, len(numList)):
value = numList[index]
sum = sum + value
if value < lowest:
lowest = value
return (sum - lowest) / (len(numList) - 1)
