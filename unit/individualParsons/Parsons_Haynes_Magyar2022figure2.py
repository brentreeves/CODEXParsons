import sys
import M

# Brent Reeves
# Winter '22
#

# Haynes-Magyar2022figure2.txt
# def has22(nums):
# 	for i in range (len(numbs)-1):
# 		if nums[i] == 2 and num [i+1] == 2:
# 			return True
# 	return False

class Parsons_Haynes_Magyar2022figure2(M.Parsons):
    def __init__(self):
        super().__init__("Haynes_Magyar2022figure2", "has22")

    def testit(self):
        return self.set_predicates_return([
            # ( " [1] = False", self.mf([1]), True), # blink test
            ( " [1] = False", self.mf([1]), False),
            ( " [1,1] = False", self.mf([1,1]), False),
            ( " [1,1,1] = False", self.mf([1,1,1]), False),
            ( " [1,2,3,4] = False", self.mf([1,2,3,4]), False),
            ( " [1,2,1,2,1,2,1] = False", self.mf([1,2,1,2,1,2,1]), False),
            ( " [1,2,2,1,2,1] = True", self.mf([1,2,2,1,2,1]), True),
            ( " [2,2] = True", self.mf([2,2]), True),
            ( " [1,2,1,2,1,2,2] = True", self.mf([1,2,1,2,1,2,2]), True),
        ])


if __name__ == '__main__':
    p = Parsons_Haynes_Magyar2022figure2()
    print( p.pp(sys.argv[1], int(sys.argv[2])) )
