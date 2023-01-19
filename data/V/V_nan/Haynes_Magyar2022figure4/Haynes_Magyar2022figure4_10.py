count = 0
if current == target:
return count
count = count + 1
def countInRange(target, start, end, numList):
for index in range(start, end+1):
current = numList[index]
