def isLevel(elList, start, end):
for index in range(start, end+1):
value = elList[index]
min = value
max = elList[start]
if value < min:
min = max
if value > max:
max = value
return (max-min) <= 10
