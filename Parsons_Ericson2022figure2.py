import O

# Brent Reeves
# Winter '22
#

# Ericson2022figure2.txt
# def check_guess(guess,target):
# 	if guess < target:
# 		return 'too low'
# 	elif guess == target:
# 		return 'correct'
# 	else:
# 		return 'too high'

# Ericson2022figure2_2 not indented
# Ericson2022figure2_11 not indented

class Parsons_Ericson2022figure2(O.Parsons):
    
    def testit(self):
        # print("Ericson2022figure2:testit: ", self.dafile)

        return self.set_predicates_return([
            # ( "(0,0) :", self.mf( 0,0 ) , 'too low', ), # blink test
            ( "(0,0) :", self.mf( 0,0 ) , 'correct', ),
            ( "(-1,-1) :", self.mf( -1,-1 ) , 'correct', ),
            ( "(-2,-2) :", self.mf( -2,-2 ) , 'correct', ),
            ( "(1,1) :", self.mf( 1,1 ) , 'correct', ),
            ( "(2,2) :", self.mf( 2,2 ) , 'correct', ),
            ( "(0,1) :", self.mf( 0,1 ) , 'too low', ),
            ( "(0.0,1.0) :", self.mf( 0.0,1.0 ) , 'too low', ),
            ( "(0,2) :", self.mf( 0,2 ) , 'too low', ),
            ( "(0,999) :", self.mf( 0,999 ) , 'too low', ),
            ( "(-1,0) :", self.mf( -1,0) , 'too low', ),
            ( "(-2,-1) :", self.mf( -2,-1 ) , 'too low', ),
            ( "(1,0) :", self.mf( 1,0 ) , 'too high', ),
            ( "(2,0) :", self.mf( 2,0 ) , 'too high', ),
            ( "(999,0) :", self.mf( 999,0 ) , 'too high', ),
            ( "(0,-1) :", self.mf( 0,-1) , 'too high', ),
            ( "(-1,-2) :", self.mf( -1,-2 ) , 'too high', ),
        ])


if __name__ == '__main__':
    p1 = Parsons_Ericson2022figure2("Ericson2022figure2", "check_guess")
    rc = p1.go()
