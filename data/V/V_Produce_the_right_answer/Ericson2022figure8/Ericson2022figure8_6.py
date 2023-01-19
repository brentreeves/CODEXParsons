def getAverageDropLowest(numList):
    sum = 0
    lowest = numList[0]
    for value in numList:
        sum = sum + value
        if value < lowest:
            lowest = value
    return (sum - lowest) / (len(numList) - 1)
