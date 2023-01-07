# 0
def avgValuesInRange(numList, start, end):
    if (end - start + 1) >= 1:
        sum = 0
        for index in range(start,end+1):
            value = numList[index]
            sum = sum + value
        return sum / (end - start + 1)
    print("_1 returning 0", file=sys.stderr)
    return 0


# def avgValuesInRange(numList, start, end):
#     sum = 0
#     if (end - start + 1) >= 1:
#         for index in range(start,end+1):
#             value = numList[index]
#             sum = sum + value
#         return sum / (end - start + 1)
#     return 0

print ( avgValuesInRange([1,2,3], 0, 1) )
