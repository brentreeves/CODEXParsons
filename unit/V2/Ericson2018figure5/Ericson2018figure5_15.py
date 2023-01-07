def isLevel(elList, start, end):
    min = elList[start]
    max = elList[start]
    for index in range(start, end+1):
        value = elList[index]
        if value < min:
            min = value
        if value > max:
            max = value
    return (max-min) <= 10
