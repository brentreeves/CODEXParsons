def isLevel(elList, start, end):
min = elList[start]
max = elList[start]
for index in range(start, end+1):
if elList[index] < min:
min = elList[index]
if elList[index] > max:
max = elList[index]
return (max-min) <= 10
