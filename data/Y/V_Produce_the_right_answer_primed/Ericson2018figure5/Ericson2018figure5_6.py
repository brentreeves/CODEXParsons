for index in range(start, end+1):
value = elList[index]
min = value
max = value
if value > max:
max = value
if value < min:
min = value
return (max-min) <= 10
