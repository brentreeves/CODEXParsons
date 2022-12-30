def getAverageDropLowest(numList):
    lowest = numList[0]
    sum = 0
    for index in range(len(numList)):
        value = numList[index]
        if value < lowest:
            lowest = value
        sum = sum + value
    if len(numList) == 0:
        return 0
    return (sum - lowest) / (len(numList) - 1)
