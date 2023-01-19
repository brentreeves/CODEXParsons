count = 0
current = numList[index]
def countInRange(target, start, end, numList):
for index in range(start, end+1):
if current == target:
count = count + 1
return count
