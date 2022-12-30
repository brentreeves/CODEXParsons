def findmax(alist):
    curmax=alist[0]
    for item in alist:
        if len(alist) > 0:
            if item > curmax:
                curmax=item
    return curmax

