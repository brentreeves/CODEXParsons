for index in range(start, end+1):
def isLevel(elList, start, end):
min = value
max = elList[start]
if value < min:
min = max
if value > max:
value = elList[index]
max = value
return (max-min) <= 10
