import sys
import M

# Brent Reeves
# Winter '22
#
    
#Karavirta2012Figure3.txt
# def findmax(alist):
# 	if len(alist) > 0:
# 		curmax=alist[0]
# 		for item in alist:
# 			if item > curmax:
# 				curmax=item
# 	return curmax

class Parsons_Karavirta2012Figure3(M.Parsons):
    def __init__(self):
        super().__init__("Karavirta2012Figure3", "findmax")

    def testit(self):
        # print("Karavirta2012Figure3:testit: ", self.dafile)

        return self.set_predicates_return([
            # ( "[]", self.mf([]), 999999), # blink test
            ( "[]", self.mf([]), None),
            ( "[-9]", self.mf([-9]), -9),
            ( "[-9,-8]", self.mf([-9,-8]), -8),
            ( "[-9,-8,-10]", self.mf([-9,-8,-10]), -8),
            ( "[1,2,3]", self.mf([1,2,3]), 3),
            ( "[3,2,1]", self.mf([3,2,1]), 3),
            ( "[-9,-8,-7,3,2,1]", self.mf([-9,-8,-7,3,2,1]), 3),
            ( "[1,1,1,1,1,1,1]", self.mf([1,1,1,1,1,1,1]), 1),
            ( "[2,1,1,1,1,1,1]", self.mf([2,1,1,1,1,1,1]), 2),
            ( "[1,1,1,1,1,1,2]", self.mf([1,1,1,1,1,1,2]), 2),
            ( "[1,1,1,2,1,1,1]", self.mf([1,1,1,2,1,1,1]), 2),
        ])


if __name__ == '__main__':
    p = Parsons_Karavirta2012Figure3()
    print( p.pp(sys.argv[1], int(sys.argv[2])) )

