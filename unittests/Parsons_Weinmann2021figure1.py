import sys
import O


# Brent Reeves
# Winter '22
#

class Parsons_Weinmann2021figure1(O.Parsons):

    def stringOrFunction(self, jive):
        # print("stringOrFunction: ", jive, file=sys.stderr)
        note, f, arg1, arg2, expect = jive
        v1 = None
        v2 = None
        try:
            v1 = f(arg1)
            # print('stringOrFunction: f(arg1)', file=sys.stderr)
            v2 = None
            # print('mf worked...:', v1)
            if (callable(v1)):
                try:
                    # print('stringOrFunction: v1 was callable', file=sys.stderr)
                    v2 = v1(arg2)
                    return {"msg": note, "ok": v2 == expect, "actual": v2}
                except:
                    # print('stringOrFunction: v1 was NOT callable', file=sys.stderr)
                    ff = f'ERROR: Weinmann2021figure1 stringOrFunction 1  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
                    ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
                    print(ee, file=sys.stderr)
                    return {"msg": note, "ok": False, "actual": v2}
            else:
                if (type(v1) is str):
                    # print("stringOrFunction returning v1", file=sys.stderr)
                    return {"msg": note, "ok": v1 == expect, "actual": v1}

            # print("stringOrFunction returning False v1", file=sys.stderr)
            return {"msg": note, "ok": False, "actual": v1}
            
        except:
            # print("safely caught exception")
            ff = f'ERROR: Weinmann2021figure1 stringOrFunction 2  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
            ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
            print(ee, file=sys.stderr)

            # print("stringOrFunction returning False v1 bottom ", file=sys.stderr)
            return {"msg": note, "ok": False, "actual": v1}

        # return {"msg": note, "ok": v1 == expect, "actual": v1}

# Weinmann2021figure1.txt
# def last_even_adder(li):
# 	for index in range (len(li)-1,-1,-1):
# # 		if(li(index)) % 2 == 0: # oops () vs []
# 		if(li[index]) % 2 == 0:
# 			return lambda x : x + li(index)
# 	return 'All odd'

    def testit(self):
        # print("Ericson2022figure4:testit: ", self.dafile)
        self.predicates = []
        args = [
            ( "[] = 'All odd'", self.mf, [], '', 'All odd' ),
            ( "[1] = 'All odd'", self.mf, [1], '', 'All odd' ),
            ( "[1,3] = 'All odd'", self.mf, [1,3], '', 'All odd' ),
            ( "[1,3,5] = 'All odd'", self.mf, [1,3,5], '', 'All odd' ),
            ( "[3,3,3,3] = 'All odd'", self.mf, [3,3,3,3], '', 'All odd' ),
            ( "[-3,-3,-3,-3] = 'All odd'", self.mf, [-3,-3,-3,-3], '', 'All odd' ),
            ( "[0] = 0", self.mf, [0], 3, 3 ),
            ( "[0, 0] = 0", self.mf, [0, 0], 4, 4 ),
            ( "[0, 0, 0] = 0", self.mf, [0, 0, 0], 5, 5 ),
            ( "[2, 0, 0] = 0", self.mf, [2, 0, 0], 5, 5 ),
            ( "[0, 2, 0] = 0", self.mf, [0, 2, 0], 5, 5 ),
            ( "[0, 0, 2] = 0", self.mf, [0, 0, 2], 5, 7 ),
            ( "[1, 0, 0] = 0", self.mf, [1, 0, 0], 5, 5 ),
            ( "[0, 1, 0] = 0", self.mf, [0, 1, 0], 5, 5 ),
            ( "[0, 0, 1] = 0", self.mf, [0, 0, 1], 5, 5 ),
            ( "[1, 2, 0] = 0", self.mf, [1, 2, 0], 5, 5 ),
            ( "[0, 1, 2] = 5 7", self.mf, [0, 1, 2], 5, 7 ),
            ( "[0, 2, 1] = 5 7", self.mf, [0, 2, 1], 5, 7 ),
            ( "[4, 1, 1] = 5 9", self.mf, [4, 1, 1], 5, 9 ),
            ( "[-4, 1, 1] = 5 1", self.mf, [-4, 1, 1], 5, 1 ),

        ]
        self.predicates = list(map ( self.stringOrFunction, args ))
        
        good = list(filter(lambda x:  x["ok"] == True, self.predicates ))
        bad = list(filter(lambda x:  x["ok"] == False, self.predicates ))

        return len(bad), good, bad


if __name__ == '__main__':
    p1 = Parsons_Weinmann2021figure1("Weinmann2021figure1", "last_even_adder")
    rc = p1.go()
