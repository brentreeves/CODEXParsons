def isLevel(elList, start, end):
for index in range(start, end+1):
value = elList[index]
max = value
min = max
if value < min:
min = value
if value > max:
max = value
return (max-min) <= 10
