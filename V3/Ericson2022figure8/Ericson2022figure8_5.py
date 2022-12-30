def getAverageDropLowest(numList):
    sum = 0
    lowest = numList[0]
    if len(numList) == 0:
        return 0
    for index in range(len(numList)):
        value = numList[index]
        if value < lowest:
            lowest = value
        sum = sum + value
    return (sum - lowest) / (len(numList) - 1)
