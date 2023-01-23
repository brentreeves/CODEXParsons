count = 0
current = numList[index]
for index in range(start, end+1):
if current == target:
count = count + 1
def countInRange(target, start, end, numList):
return count
