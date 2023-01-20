# Finish the function to define countInRange that returns a count of the number of tines that a target value appears in a list between the start and end indices (inclusive). For example, countInRange(1,2,4,[1,2,1,1,1,1]) should return 3 since there are three 1s between index 2 and 4 inclusive.
def countInRange(target, start, end, numList):
	count = 0
	for index in range(start, end+1):
		current = numList[index]
		if current == target:
			count = count + 1
	return count
