curmax=alist[0]
def findmax(alist):
for item in alist:
if len(alist) > 0:
return curmax
if item > curmax:
curmax=item
