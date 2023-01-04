import O

# Brent Reeves
# Winter '22
#

# Ericson2017figure1.txt
# def getSum(numlist):
#         sum = 0
#         for num in numList:
#                 sum = sum + num
#                 return sum

class Parsons_Ericson2017figure1(O.Parsons):

    def testit(self):
        # print("Ericson2017figure1:testit: ", self.dafile)
        
        return self.set_predicates_return([
            ("[] = 0", self.mf([]), 0),
            ("[0] = 0", self.mf([0]), 0),
            ("[0,0,0] = 0", self.mf([0,0,0]), 0 ),
            ("[-1] = -1", self.mf([-1]), -1 ),
            ("[1,0,-1,-1] = -1 ", self.mf([1, 0, -1, -1]), -1 ),
            ("[1,2,3,4] = 10 ", self.mf([1, 2, 3, 4]), 10),
            ("[-99,1,1,1,1,1] = 94 ", self.mf([-99, 1, 1, 1, 1, 1]), -94),
        ])


if __name__ == '__main__':
    p1 = Parsons_Ericson2017figure1("Ericson2017figure1", "getSum")
    p1.log(1, "Ericson2017figure1:testit: " + p1.dafile)
    rc = p1.go()
