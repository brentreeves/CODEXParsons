from importlib import import_module
import os
import inspect
import sys
import glob
import json
import inspect

# Brent Reeves
# Winter '22
#
class Parsons():
    me = ''             # Ericson2017figure1, i.e. subfolder name and problem name
    m = None            # holds imported module (i.e codex solution)
    mfname = 'yo'         # name of function in the solution, e.g. 'getSum'
    mf = None           # function definition
    folder = ''
    ff = []
    solutions = ""      # ~20 solution files
    predicates = None   # 'shoulda orta'
    failedtests = None  # dictionary of failed tests
    failcount = 0
    successcount = 0    # how many problems passed
    dafile = ''         # the current codex being tested
    xref = []           # problem name and function to call 

    fails = None
    wins = None
    loglevel = 0


    # will no longer get figure and function
    # instead, keep xref array
    #
    def __init__(self):
        # self.me = figurename
        # self.mfname = functionname
        self.setXref()
        self.fails = []
        self.wins = []


    def setUpFolder(self, folder):
        self.fails = []
        self.wins = []
        self.folder = folder
        dastring = f'./{self.folder}/{self.me}/{self.me}*.py'
        self.log(1, f'setUpFolder globs b4: {self.ff}  glob: {dastring}')
        self.ff = glob.glob(dastring)
        self.log(1, f'setUpFolder globs affa: {self.ff}  glob: {dastring}')
        # print(f'setUpClass globs: affa: {str(self.ff)}  glob: {dastring}')

        
    def Ericson2017figure1(self):
        return self.set_predicates_return([
            ("[] = 0", self.mf([]), 0),
            ("[0] = 0", self.mf([0]), 0),
            ("[0,0,0] = 0", self.mf([0,0,0]), 0 ),
            ("[-1] = -1", self.mf([-1]), -1 ),
            ("[1,0,-1,-1] = -1 ", self.mf([1, 0, -1, -1]), -1 ),
            ("[1,2,3,4] = 10 ", self.mf([1, 2, 3, 4]), 10),
            ("[-99,1,1,1,1,1] = 94 ", self.mf([-99, 1, 1, 1, 1, 1]), -94),
        ])

    def Ericson2018figure5(self):
        return self.set_predicates_return([
            # ("([1],0,0) = T", self.mf( [1],0,0 ), False),
            ("([1],0,0) = T", self.mf( [1],0,0 ), True),
            ("([1,1,1],0,0) =T", self.mf( [1,1,1],0,0)  , True),
            ("([1,1,99],0,0) =T", self.mf( [1,1,99],0,0)  , True),
            ("([1,1,1],0,1) =T", self.mf([1,1,1],0,1) , True),
            ("([1,1,99],0,1) =T", self.mf([1,1,99],0,1) , True),
            ("([1,1,99],0,2) =F", self.mf([1,1,99],0,2) , False),
            ("([1,1,9],0,2) =T", self.mf([1,1,9],0,2) , True),
            ("([1,1,1,9],0,2) =T", self.mf([1,1,1,9],0,2) , True),
            ("([1,1,1,1,9],0,2) =T", self.mf([1,1,1,1,9],0,2) , True),
            ("([1,1,1,1,9],0,3) =T", self.mf([1,1,1,1,9],0,3) , True),
            ("([1,1,1,1,9],0,4) =T", self.mf([1,1,1,1,9],0,4) , True),
            ("([1,1,1,1,10],0,4) =T", self.mf([1,1,1,1,10],0,4) , True),
            ("([1,1,1,1,11],0,4) =T", self.mf([1,1,1,1,11],0,4) , True),
            ("([1,1,1,1,12],0,4) =F", self.mf([1,1,1,1,12],0,4) , False),
            ("([1,1,1,1,-9],0,4) =T", self.mf([1,1,1,1,-9],0,4) , True),
            ("([1,1,1,1,-10],0,4) =F", self.mf([1,1,1,1,-10],0,4) , False),
            ("([0,3,6,9,12,15,18,21,24,27],0,1) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,1) , True),
            ("([0,3,6,9,12,15,18,21,24,27],0,2) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,2) , True),
            ("([0,3,6,9,12,15,18,21,24,27],0,3) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,3) , True),
            ("([0,3,6,9,12,15,18,21,24,27],0,4) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,4) , False),
            ("([0,3,6,9,12,15,18,21,24,27],1,5) :", self.mf([0,3,6,9,12,15,18,21,24,27],1,5) , False),
            ("([0,3,6,9,12,15,18,21,24,27],2.6) :", self.mf([0,3,6,9,12,15,18,21,24,27],2,6) , False),
            ("([0,3,6,9,12,15,18,21,24,27],2.6) :", self.mf([0,3,6,9,12,15,18,21,24,27],3,7) , False),
            ("([0,3,6,9,12,15,18,21,24,27],0,5) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,5) , False),
        ])        

    
    def setXref(self):
        self.xref = {}
        for x in [('Ericson2017figure1', self.Ericson2017figure1, 'getSum'),
                  ('Ericson2018figure5', self.Ericson2018figure5, 'isLevel')
                  ]:
            self.xref[x[0]] = (x[1], x[2])
            

    def entry(self, ok, note, actual, expected, errortype):
        yo = 1
        if ok:
            yo = 0
            
        return {"folder": self.folder,
                "figure": self.me,
                "file": self.dafile,
                "ok" : yo,
                "msg": note,
                "actual" : actual,
                "expected": expected,
                "errortype": errortype
                }

    
    def errLog(self, txt):
        print(txt, file=sys.stderr)

    def setLog(self, n):
        self.loglevel = n
        # print("self.loglevel is now: " + str(self.loglevel) + ' after receiving: ' + str(n))

    def log(self, lvl, msg):
        if (lvl < self.loglevel):
            print(msg)
    
    # self.predicates = list(map ( self.fixem, args ))
    def fixem(self, args):
        note, result, expected = args
        # print("fixem...")
        rc = False
        
        if ( (type(expected) is int ) or (type(expected) is float)):
            rc = abs(  abs(result) - abs(expected)) < 0.0001
        else:
            rc = result == expected

        errortype = ''
        if not rc:
            errortype = 'output incorrect'

        return self.entry(rc, note, result, expected, errortype)


    def set_predicates(self, alist):
        self.predicates = list(map ( self.fixem, alist ))

    def set_predicates_return(self, alist):
        self.set_predicates(alist)
        self.log(1,'set_predicates_return: ' + str(self.predicates))

        good = list(filter(lambda x: x["ok"] == True, self.predicates ))
        bad = list(filter(lambda x: x["ok"] == False, self.predicates ))
        self.log(1,'set_predicates_return good: ' + str(good))
        self.log(1,'set_predicates_return bad : ' + str(bad))
        return len(bad), good, bad

    
    # def expect(self, note, f, args, expect):
    #     rc = None
    #     try:
    #         rc = f(args)
    #     except:
    #         # print("expect caught exception of f(args)")
    #         return note, False, rc
    #     errortype = ''
    #     happy = rc == expect
    #     if not happy:
    #         errortype = 'output incorrect'
    #     return self.entry(happy, note, rc, expect, errortype)


    def expectN(self, note, f, args, expect):
        # print(f'expectN: {note} f: {f}  args: {args} expect: {expect}')
        actual = None
        errortype = ''

        try:    
            actual = f(args)
        except:
            ff = f'ERROR: M.py expectN  Folder: {self.folder} File: {self.dafile}\nNote: {note} args: {args} expect: {expect}'
            ee = {"error" : ff, "exception" : str(sys.exc_info()[1]) }
            self.errLog(ee)
            return self.entry(False, note, actual, expect, "runtime error")
            # return {"msg": note, "ok": False, "actual": actual, "expected": expect, "errortype": "runtime error"}

        withinlimit = abs(abs(actual) - abs(expect)) < 0.001
        if not withinlimit:
            errortype = 'output incorrect'

        # return {"msg": note, "ok":  withinlimit, "actual": actual, "errortype": errortype}
        return self.entry(withinlimit, note, actual, expect, errortype)


    def me(self):
        return ""
    
    def mfname(self):
        return "getSum"
    
    def testit(self, problem):
        self.log(2, f'\ntestit start: {problem}') 
        fn, fname = self.xref[problem]
        self.log(2, f'\ntestit: {fname} {fn} ') 

        rc = fn()
        self.log(2, f'\ntestit: rc {rc} ') 

        return rc

    #
    # test1('./V/V1', 'Ericson2018figure5', 'Ericson2018figure5_0')
    # folder = '../data/V/V1/'
    # problem = 'Ericson2017figure1'
    # afile   = 'Ericson2017figure1_1'

    #
    def test1(self, folder, problem, afile):
        self.folder = folder
        self.me = problem
        self.dafile = problem
        
        mpath = f'./{folder}/{problem}'

        seeking = f'{folder}/{problem}/{afile}'
        self.log(1, f'seeking: {seeking}')
        there = os.path.exists(seeking+".py")

        self.log(1, f'  seeking? {there}: {seeking}')
        f = os.path.abspath(seeking)

        fails = 0

        sys.path.insert(0, mpath)
                
        m, f = self.xref[problem]

        self.log(1,"\ntest1 start\n")
        # self.dafile = f'{problem}_{i}'
        try:
            self.log(2,f'\nimport trying: {afile}')
            self.m = __import__(afile)
            self.log(2,f'\nimport happy: {afile}')
            try:
                self.log(2,"source code: " + inspect.getsource(self.m))
            except:
                print("inspect not happy.")
                
            if (hasattr(self.m, f)):
                self.log(2,"attribute function happy " + f)
                self.mf = getattr(self.m, f)                            

            try: 
                self.log(1,"\ntest1 calling testit\n")

                nfail, good, bad = self.testit(problem)

                self.log(2,f'\n\ntestit()====================================\n fail: {nfail} \n  good: {good} \n  bad: {bad} ')
                if (nfail >0):
                    fails += 1

                self.fails = self.fails + bad
                self.wins = self.wins + good 

            except:
                ff = f'ERROR: error running File: {afile}'
                ee = {"error" : ff, "exception" :  str(sys.exc_info()[1]) }
                print(ee, file=sys.stderr)

                fails += 1
                bug = self.entry(False,
                                     "error running " + afile,
                                     str(sys.exc_info()[1]),
                                     'should run',
                                     'runtime error'
                                     )
                self.log(2,"   runtime issue " + str(bug))
                self.fails.append( bug )
    
        except:
            ff = f'ERROR: problem with import  File: {afile}'
            ee = {"error" : ff, "exception" :  str(sys.exc_info()[1]) }
            print(ee, file=sys.stderr)

            fails += 1

            self.fails.append(
                self.entry(False,
                           "error importing source code " + afile,
                           str(sys.exc_info()[1]),
                           'should import',
                           "import error"
                           )
            )

        try:
            del sys.modules[self.dafile]
            log(2, "we migh have just removed module: " + str(self.dafile))
        except:
            # oh well...
            pass

        # return fails
        return self.fails + self.wins

    def yloopit(self, dbg):
        # for each V in data folder
        #    for each parson item in xref
        #       for each _*.py file in the data folder
        #
        return true;
        
    #
    # check every predicate against every file
    #
    def zloopit(self, dbg):
        self.setLog(dbg)
        fails = 0
        mpath = f'./{self.folder}/{self.me}'

        self.log(1,"loopit enumerate..." + str(list(self.ff)))
        if ( len(self.ff) < 1) :
            # folder typo?
            ff = f'ERROR: no input files found for [{self.me}] folder: {self.ff}'
            self.errLog(ff)
            fails += 1
            self.log(2,"  fail no input files")
            self.fails.append(
                self.entry(False,
                           "error no input files found in folder " + str(self.ff),
                           "error",
                           "valid folder",
                           "empty folder"
                           )
                )

        # in preparation for import, add correct folder to path
        #
        # sys.modules.clear()
        self.log(1,f'\nloopit path b4: [{mpath}] folder: {self.folder} me: {self.me} \n\npath: {sys.path}')
        sys.path.insert(0, mpath)
        self.log(1,f'\nloopit path af: [{mpath}] folder: {self.folder} me: {self.me} \n\npath: {sys.path}')
                
        for i, f in enumerate(self.ff):
            self.log(1,"\nloopit enumerate start\n")
            self.dafile = f'{self.me}_{i}'
            self.log(1,"\nloopit enumerate dafile " + self.dafile + "\n")
            try:
                self.m = __import__(self.dafile)
                self.log(2,"\nimport happy " + self.dafile)
                try:
                    self.log(2,"source code: " + inspect.getsource(self.m))
                except:
                    print("inspect not happy.")
                if (hasattr(self.m, self.mfname)):
                    self.log(2,"attribute mfname happy " + self.mfname)
                    self.mf = getattr(self.m, self.mfname)                            

                try: 
                    self.log(1,"\nloopit calling testit\n")

                    nfail, good, bad = self.testit()

                    self.log(2,f'\n\ntestit()====================================\n fail: {nfail} \n  good: {good} \n  bad: {bad} ')
                    # print("nfail: ", nfail)
                    # print("bad: ", bad, file=sys.stderr)
                    if (nfail >0):
                        fails += 1

                    self.fails = self.fails + bad
                    self.wins = self.wins + good 

                except:
                    ff = f'ERROR: error running File: {self.dafile}'
                    ee = {"error" : ff, "exception" :  str(sys.exc_info()[1]) }
                    print(ee, file=sys.stderr)

                    fails += 1
                    bug = self.entry(False,
                                     "error running " + self.dafile,
                                     str(sys.exc_info()[1]),
                                     'should run',
                                     'runtime error'
                                     )
                    self.log(2,"   runtime issue " + str(bug))
                    self.fails.append( bug )
    
            except:
                ff = f'ERROR: problem with import  File: {self.dafile}'
                # ee = {"error" : ff, "exception" : str( sys.exc_info()[1] )  }
                # ee = {"error" : ff, "exception" :  sys.exc_info()[1]  }
                ee = {"error" : ff, "exception" :  str(sys.exc_info()[1]) }
                print(ee, file=sys.stderr)

                fails += 1
    # def entry(self, ok, note, actual, expected, errortype):
                self.fails.append( self.entry(False,
                                              "error importing source code " + self.dafile,
                                              str(sys.exc_info()[1]),
                                              'should import',
                                              "import error"
                                              )
                                  )
            #                         "issues" : [{"msg": "error importing source code " + self.dafile,
            #                                      "ok": False,
            #                                      "actual": str(sys.exc_info()),
            #                                      "errortype": "import error"
            #                                      }]} )
            try:
                del sys.modules[self.dafile]
                log(2, "we migh have just removed module: " + str(self.dafile))
            except:
                # oh well...
                pass

        # s = sys.modules
        # print(s)
        # # print("sys.path b4 remove: ", sys.path)
        # sys.path.remove(mpath)
        # print("sys.path affa remove: ", sys.path)
        # # sys.path.pop()
        return fails



    def ppjson(self):
        return json.dumps (self.fails + self.wins) 
        
    # def pp(self):
    #     for key, (n, good, bad) in self.fails.items():
    #         print(f'{key}: ({n})')

    # def pp2(self):
    #     for key, (n, good, bad) in self.fails.items():
    #         print(f'\n{key}: ({n})\nGood: {good}\nBad : {bad}')

    # def pp3(self):
    #     for key, (n, good, bad) in self.fails.items():
    #         print(f'\n{key}: ({n})\nGood: {good}\nBad : {bad}')

    def go(self, folder, dbg=0):
        self.setLog(dbg)
        self.setUpFolder(folder)
        rc = self.loopit(dbg)
        return self.fails + self.wins

    def pp(self, folder, dbg=0):
        x = self.go(folder, dbg)
        return json.dumps (x)

    def cmdfolder(self):
        n = len(sys.argv)
        folder = ''
        if (n>1):
            folder = sys.argv[1]
        # print("folder: ", folder)
        return folder
