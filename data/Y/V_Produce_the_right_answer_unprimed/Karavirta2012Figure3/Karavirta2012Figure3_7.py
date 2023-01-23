def findmax(alist):
curmax=alist[0]
for item in alist:
if item > curmax:
curmax=item
return curmax
