# Put the blocks in order to define the function has22 to return True if there are at least two items in the list nums that are adjacent and both equal to 2, otherwise return False.  For example, return True for has22([1,2,2]) since there are two adjacent items equal to 2 (at index 1 and 2) and False for has22(2,1,2) since the 2's are not adjacent
def has22(nums):
	for i in range (len(numbs)-1):
		if nums[i] == 2 and num [i+1] == 2:
			return True
	return False
