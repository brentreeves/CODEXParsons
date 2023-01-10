def getAverageDropLowest(numList):
    if len(numList) == 0:
        return 0
    sum = 0
    lowest = numList[0]
    for index in range(len(numList)):
        value = numList[index]
        sum = sum + value
        if value < lowest:
            lowest = value
    return (sum - lowest) / (len(numList) - 1)

