def findmax(alist):
    if len(alist) > 0:
        curmax = alist[0]
        for item in alist:
            if item > curmax:
                curmax = item
        return curmax

