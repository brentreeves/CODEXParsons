def isLevel(elList, start, end):
	max = elList[start]
	min = max
	for index in range(start, end+1):
		value = elList[index]
		if value > max:
			max = value
		if value < min:
			min = value
	return (max-min) <= 10