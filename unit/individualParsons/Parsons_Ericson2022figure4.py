import sys
import M

# Brent Reeves
# Winter '22
#

# Ericson2022figure4.txt
# def alarm_clock(day, vacation):
# 	if vacation:
# 		if day == 0 or day == 6:
# 			return 'off'
# 		else:
# 			return '10:00'
# 	else:
# 		if day == 0 or day == 6:
# 			return '10:00'
# 		else:
# 			return '7:00'

class Parsons_Ericson2022figure4(M.Parsons):
    def __init__(self):
        super().__init__("Ericson2022figure4", "alarm_clock")
    
    def testit(self):
        return self.set_predicates_return([
            # ( "(0,True) :", self.mf( 0,True ), 'zzz'), # blink test
            ( "(0,True) :", self.mf( 0,True ), 'off'),
            ( "(1,True) :", self.mf( 1,True ), '10:00'),
            ( "(2,True) :", self.mf( 2,True ), '10:00'),
            ( "(3,True) :", self.mf( 3,True ), '10:00'),
            ( "(4,True) :", self.mf( 4,True ), '10:00'),
            ( "(5,True) :", self.mf( 5,True ), '10:00'),
            ( "(6,True) :", self.mf( 6,True ), 'off'),
            ( "(0,False) :", self.mf( 0,False ), '10:00'),
            ( "(1,False) :", self.mf( 1,False ), '7:00'),
            ( "(2,False) :", self.mf( 2,False ), '7:00'),
            ( "(3,False) :", self.mf( 3,False ), '7:00'),
            ( "(4,False) :", self.mf( 4,False ), '7:00'),
            ( "(5,False) :", self.mf( 5,False ), '7:00'),
            ( "(6,False) :", self.mf( 6,False ), '10:00'),
        ])


if __name__ == '__main__':
    p = Parsons_Ericson2022figure4()
    print( p.pp(sys.argv[1], int(sys.argv[2])) )
