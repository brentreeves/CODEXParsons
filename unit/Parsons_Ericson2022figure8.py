import sys
import M

# Brent Reeves
# Winter '22
#

# Ericson2022figure8.txt
# def getAverageDropLowest(numList):
# 	if len(numList) == 0:
# 		return 0
# 	sum = 0
# 	lowest = numList[0]
# 	for index in range(len(numList)):
# 		value = numList[index]
# 		sum = sum + value
# 		if value < lowest:
# 			lowest = value
# 	return (sum - lowest) / (len(numList) - 1)

class Parsons_Ericson2022figure8(M.Parsons):
    def __init__(self):
        super().__init__("Ericson2022figure8", "getAverageDropLowest")
    
    def testit(self):
        # print("Ericson2022figure8:testit: ", self.dafile)

        self.predicates = [
            # self.expectN("[] = 0", self.mf, [], -1), # blink test
            self.expectN("[] = 0", self.mf, [], 0),
            self.expectN("[0,0] = 0.0", self.mf, [0,0], 0),
            self.expectN("[0,0,0] = 0.0", self.mf, [0,0,0], 0),
            self.expectN("[0,0,0,-1] = 0.0", self.mf, [0,0,0,-1], 0),
            self.expectN("[0,0,0,-3] = 0.0", self.mf, [0,0,0,-3], 0),
            self.expectN("[1,1,1,0] = 1.0", self.mf, [1,1,1,0], 1),
            self.expectN("[1,1,0,1] = 1.0", self.mf, [1,1,0,1], 1),
            self.expectN("[1,0,1,1] = 1.0", self.mf, [1,0,1,1], 1),
            self.expectN("[0,1,1,1] = 1.0", self.mf, [0,1,1,1], 1),
            
            self.expectN("[-9,-1,-3,-5] = -3", self.mf, [-9,-1,-3,-5], -3),
            self.expectN("[-1,-9,-3,-5] = -3", self.mf, [-1,-9,-3,-5], -3),
            self.expectN("[-1,-3,-9,-5] = -3", self.mf, [-1,-3,-9,-5], -3),
            self.expectN("[-1,-3,-5,-9] = -3", self.mf, [-1,-3,-5,-9], -3),
            
            self.expectN("[0,2,2,2] = 2", self.mf, [0,2,2,2], 2),
            self.expectN("[0,1,3,5] = 3", self.mf, [0,1,3,5], 3) 
         ]

        good = list(filter(lambda x:  x["ok"] == True, self.predicates ))
        bad = list(filter(lambda x:  x["ok"] == False, self.predicates ))

        return len(bad), good, bad


if __name__ == '__main__':
    p = Parsons_Ericson2022figure8()
    print( p.pp(sys.argv[1], int(sys.argv[2])) )
