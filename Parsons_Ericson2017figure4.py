import O

# Ericson2017figure4.txt
# def avgValuesInRange(numList, start, end):
# 	sum = 0
# 	for index in range(start,end-1):
# 		value = numList[index]
# 		sum = sum + value
# 	if (end - start + 1) >= 1:
# 		return sum / (end - start + 1)
# 	return 0

#
# don't understand this... :-) but here are the results...
#

class Parsons_Ericson2017figure4(O.Parsons):

    def testit(self):
        # print("Ericson2017figure4:testit: ", self.dafile)
        return self.set_predicates_return([
            ( "[1],0,1) = 0.0", self.mf([1],0,1),  0.0),
            ( "[1],0,2) = 0.333", self.mf([1],0,2),  0.33333),
            ( "[1],1,1) = 0.0 ", self.mf([1],1,1),  0.0 ),
            ( "[1],1,2) = 0.0 ", self.mf([1],1,2),  0.0 ),
            ( "[1,1],0,0) = 0.0 ", self.mf([1,1],0,0),  0.0 ),
            ( "[1,1],0,1) = 0.0 ", self.mf([1,1],0,1),  0.0 ),
            ( "[1,1],0,2) = 0.333 ", self.mf([1,1],0,2),  0.33333 ),
            ( "[1,1],1,1) = 0.0 ", self.mf([1,1],1,1),  0.0 ),
            ( "[1,1],1,2) = 0.0 ", self.mf([1,1],1,2),  0.0 ),
            ( "[1,1],1,3) = 0.333 ", self.mf([1,1],1,3),  0.33333 ),
            ( "[1,2,3],0,0) = 0.0 ", self.mf([1,2,3],0,0),  0.0 ),
            ( "[1,2,3],0,1) = 0.0 ", self.mf([1,2,3],0,1),  0.0 ),
            ( "[1,2,3],0,2) = 0.333 ", self.mf([1,2,3],0,2),  0.33333 ),
            ( "[1,2,3],0,3) = 0.75 ", self.mf([1,2,3],0,3),  0.75 ),
            ( "[1,2,3],0,4) = 1.2 ", self.mf([1,2,3],0,4),  1.2 ),
            ( "[-1,-2,-3,-4,-5],0,0) = 0.0 ", self.mf([-1,-2,-3,-4,-5],0,0),  0.0 ),
            ( "[-1,-2,-3,-4,-5],0,1) = 0.0 ", self.mf([-1,-2,-3,-4,-5],0,1),  0.0 ),
            ( "[-1,-2,-3,-4,-5],0,2) = -0.333 ", self.mf([-1,-2,-3,-4,-5],0,2),  -0.33333 ),
            ( "[-1,-2,-3,-4,-5],0,3) = -0.75 ", self.mf([-1,-2,-3,-4,-5],0,3),  -0.75 ),
            ( "[-1,-2,-3,-4,-5],0,4) = -1.2 ", self.mf([-1,-2,-3,-4,-5],0,4),  -1.2 ),
        ])


if __name__ == '__main__':
    p1 = Parsons_Ericson2017figure4("Ericson2017figure4", "avgValuesInRange")
    rc = p1.go()
