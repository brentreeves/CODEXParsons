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
        super().__init__("Ericson2017figure1", "getSum")

    def testit(self):
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
    p = Ericson2017figure1()
    print ( p.go(sys.argv[1], int(sys.argv[2])) )
