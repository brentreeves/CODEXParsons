count = 0
def countInRange(target, start, end, numList):
for index in range(start, end+1):
current = numList[index]
if current == target:
count = count + 1
return count
