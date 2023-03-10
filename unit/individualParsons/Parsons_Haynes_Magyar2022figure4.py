import sys
import M

# Brent Reeves
# Winter '22
#

# Haynes-Magyar2022figure4.txt
# def countInRange(target, start, end, numList):
# 	count = 0
# 	for index in range(start, end+1):
# 		current = numList[index]
# 		if current == target:
# 			count = count + 1
# 	return count

class Parsons_Haynes_Magyar2022figure4(M.Parsons):
    def __init__(self):
        super().__init__("Haynes_Magyar2022figure4", "countInRange")
    
    def testit(self):
        self.log(1, "Haynes_Magyar2022figure4:testit: " + self.dafile)

        return self.set_predicates_return([
            # ( '0,0,0,[0]=1', self.mf( 0,0,0,[0] ), 9), # blink test
            ( '0,0,0,[0]=1', self.mf( 0,0,0,[0] ), 1),
            ( '1,0,0,[0]=0', self.mf( 1,0,0,[0] ), 0),
            ( '0,0,1,[0,0]=2', self.mf( 0,0,1,[0,0] ), 2),
            ( '0,0,1,[0,0,0]=2', self.mf( 0,0,1,[0,0,0] ), 2),
            ( '0,0,1,[0,0,0,0]=2', self.mf( 0,0,1,[0,0,0,0] ), 2),
            ( '0,0,2,[0,0,0,0]=3', self.mf( 0,0,2,[0,0,0,0] ), 3),
            ( '0,0,3,[0,0,0,0]=4', self.mf( 0,0,3,[0,0,0,0] ), 4),
            ( '3,0,3,[1,2,3,1,2,3,1,2,3]=1', self.mf( 3,0,3,[1,2,3,1,2,3,1,2,3] ), 1),
            ( '3,0,6,[1,2,3,1,2,3,1,2,3]=2', self.mf( 3,0,6,[1,2,3,1,2,3,1,2,3] ), 2),
            ( '3,0,7,[1,2,3,1,2,3,1,2,3]=2', self.mf( 3,0,7,[1,2,3,1,2,3,1,2,3] ), 2),
            ( '3,0,8,[1,2,3,1,2,3,1,2,3]=3', self.mf( 3,0,8,[1,2,3,1,2,3,1,2,3] ), 3),
            ( '2,0,8,[1,2,3,1,2,3,1,2,3]=3', self.mf( 2,0,8,[1,2,3,1,2,3,1,2,3] ), 3),
            ( '1,0,8,[1,2,3,1,2,3,1,2,3]=3', self.mf( 1,0,8,[1,2,3,1,2,3,1,2,3] ), 3),
            ( '9,0,0,[9,9,9,9,9,9,9,9,9]=1', self.mf( 9,0,0,[9,9,9,9,9,9,9,9,9] ), 1),
            ( '9,0,1,[9,9,9,9,9,9,9,9,9]=2', self.mf( 9,0,1,[9,9,9,9,9,9,9,9,9] ), 2),
            ( '9,0,2,[9,9,9,9,9,9,9,9,9]=3', self.mf( 9,0,2,[9,9,9,9,9,9,9,9,9] ), 3),
            ( '9,0,3,[9,9,9,9,9,9,9,9,9]=4', self.mf( 9,0,3,[9,9,9,9,9,9,9,9,9] ), 4),
            ( '9,0,8,[9,9,9,9,9,9,9,9,9]=9', self.mf( 9,0,8,[9,9,9,9,9,9,9,9,9] ), 9),
            ( '9,8,8,[9,9,9,9,9,9,9,9,9]=1', self.mf( 9,8,8,[9,9,9,9,9,9,9,9,9] ), 1),
            ( '9,7,8,[9,9,9,9,9,9,9,9,9]=2', self.mf( 9,7,8,[9,9,9,9,9,9,9,9,9] ), 2),
            ( '9,4,5,[9,9,9,9,9,9,9,9,9]=2', self.mf( 9,4,5,[9,9,9,9,9,9,9,9,9] ), 2),
        ])

if __name__ == '__main__':
    p = Parsons_Haynes_Magyar2022figure4()
    print( p.pp(sys.argv[1], int(sys.argv[2])) )
