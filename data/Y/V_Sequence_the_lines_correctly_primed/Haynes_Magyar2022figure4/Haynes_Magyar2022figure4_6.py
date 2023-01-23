count = 0
for index in range(start, end+1):
current = numList[index]
if current == target:
count = count + 1
def countInRange(target, start, end, numList):
return count
