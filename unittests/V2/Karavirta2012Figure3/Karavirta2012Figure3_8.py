def findmax(alist):
    curmax=alist[0]
    for item in alist:
        if item > curmax:
            curmax=item
    if len(alist) > 0:
        return curmax
