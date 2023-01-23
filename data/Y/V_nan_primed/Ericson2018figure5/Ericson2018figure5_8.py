for index in range(start, end+1):
if value < min:
value = elList[index]
if value > max:
min = max
max = value
def isLevel(elList, start, end):
min = value
max = elList[start]
return (max-min) <= 10
