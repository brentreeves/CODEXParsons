for index in range(start, end+1):
def isLevel(elList, start, end):
value = elList[index]
min = value
max = value
min = max
if value > max:
return (max-min) <= 10
max = elList[start]
if value < min:
