# write a function to return the average of values in a list, given a start and end index.  For example avgValuesInRange([1,2,3,4,5],0,2) is 2.0 and avgValuesInRange([1,2,3,4,5],2,4) is 4.0
def avgValuesInRange(numList, start, end):
	sum = 0
	for index in range(start,end+1):
		value = numList[index]
		sum = sum + value
	if (end - start + 1) >= 1:
		return sum / (end - start + 1)
	return 0
