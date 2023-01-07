import M

# Brent Reeves
# Winter '22
#

# Ericson2017figure1.txt
# def getSum(numlist):
#         sum = 0
#         for num in numList:
#                 sum = sum + num
#                 return sum

class Ericson2017figure1(M.Parsons):

    def __init__(self):
        print("2017figure1... b4")
        super().__init__("Ericson2017figure1", "getSum")
        print("2017figure1... affa")

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
