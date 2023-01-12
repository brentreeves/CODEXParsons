import sys
import M

# Ericson2017figure4.txt
# def avgValuesInRange(numList, start, end):
# 	sum = 0
# 	for index in range(start,end+1):
# 		value = numList[index]
# 		sum = sum + value
# 	if (end - start + 1) >= 1:
# 		return sum / (end - start + 1)
# 	return 0

class Parsons_Ericson2017figure4(M.Parsons):
    def __init__(self):
        super().__init__("Ericson2017figure4", "avgValuesInRange")

    def testit(self):
        # print("Ericson2017figure4:testit: ", self.dafile)
        return self.set_predicates_return([
            ( "[1],0,0 = 1.0 == ", avgValuesInRange([1],0,0), 1.0),
            ( "[1,1],0,0 = 1.0 == ", avgValuesInRange([1,1],0,0), 1.0),
            ( "[1,1,1],0,0 = 1.0 == ", avgValuesInRange([1,1,1],0,0), 1.0),
            ( "[1,1,1,1],0,0 = 1.0 == ", avgValuesInRange([1,1,1,1],0,0), 1.0),

            ( "[1,1],0,1 = 1.0 == ", avgValuesInRange([1,1],0,1), 1.0),
            ( "[1,1,1],0,2 = 1.0 == ", avgValuesInRange([1,1,1],0,2), 1.0),
            ( "[1,1,1,1],0,3 = 1.0 == ", avgValuesInRange([1,1,1,1],0,3), 1.0),

            ( "[1,3],0,1 = 2.0 == ", avgValuesInRange([1,3],0,1), 2.0),
            ( "[1,4,1],0,2 = 2.0 == ", avgValuesInRange([1,4,1],0,2), 2.0),
            ( "[1,2,3,4],0,3 = 2.5 == ", avgValuesInRange([1,2,3,4],0,3), 2.5),
            ( "[1,2,3,4,5],0,2 = 2 == ", avgValuesInRange([1,2,3,4,5],0,2), 2.0),
            ( "[1,2,3,4,5],2,4 = 3 == ", avgValuesInRange([1,2,3,4,5],2,4), 4.0),
            
            ( "[1],0,0 = 1.0 == ", avgValuesInRange([1],0,0), 1.0),
            ( "[2],0,0 = 2.0 == ", avgValuesInRange([2],0,0), 2.0)
        ])


if __name__ == '__main__':
    p = Parsons_Ericson2017figure4()
    print( p.pp(sys.argv[1], int(sys.argv[2])) )


