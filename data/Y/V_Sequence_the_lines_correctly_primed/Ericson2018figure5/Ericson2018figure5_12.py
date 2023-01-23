def isLevel(elList, start, end):
min = max = elList[start]
for index in range(start, end+1):
value = elList[index]
if value > max:
max = value
if value < min:
min = value
return (max-min) <= 10
