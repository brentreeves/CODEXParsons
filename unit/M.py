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

    fails = None
    loglevel = 0


    def __init__(self, figurename, functionname):
        self.me = figurename
        self.mfname = functionname

    def setUpFolder(self, folder):
        self.fails = []
        self.folder = folder
        dastring = f'./{self.folder}/{self.me}/{self.me}*.py'
        self.log(1, f'setUpFolder globs b4: {self.ff}  glob: {dastring}')
        self.ff = glob.glob(dastring)
        self.log(1, f'setUpFolder globs affa: {self.ff}  glob: {dastring}')
        # print(f'setUpClass globs: affa: {str(self.ff)}  glob: {dastring}')
    
    def setLog(self, n):
        self.loglevel = n
        print("self.loglevel is now: " + str(self.loglevel) + ' after receiving: ' + str(n))

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
            
        return {"msg": note,
                "ok" : rc,
                "actual" : result,
                "expected": expected,
                "errortype": errortype
                }


    def set_predicates(self, alist):
        self.predicates = list(map ( self.fixem, alist ))

    def set_predicates_return(self, alist):
        self.set_predicates(alist)
        good = list(filter(lambda x: x["ok"] == True, self.predicates ))
        bad = list(filter(lambda x: x["ok"] == False, self.predicates ))
        return len(bad), good, bad

    
    def expect(self, note, f, args, expect):
        rc = None
        try:
            rc = f(args)
        except:
            # print("expect caught exception of f(args)")
            return note, False, rc

        errortype = ''
        happy = rc == expect
        if not happy:
            errortype = 'output incorrect'

        return {"msg": note, "ok" : happy, "actual": rc, "errortype": errortype}


    def expectN(self, note, f, args, expect):
        # print(f'expectN: {note} f: {f}  args: {args} expect: {expect}')
        rc = None
        errortype = ''

        try:    
            rc = f(args)
        except:
            ff = f'ERROR: 0.py expectN  Folder: {self.folder} File: {self.dafile}\nNote: {note} args: {args} expect: {expect}'
            ee = {"error" : ff, "exception" : str(sys.exc_info()[1]) }
            print(ee, file=sys.stderr)
            return {"msg": note, "ok": False, "actual": rc, "expected": expect, "errortype": "runtime error"}

        withinlimit = abs(abs(rc) - abs(expect)) < 0.001
        if not withinlimit:
            errortype = 'output incorrect'

        return {"msg": note, "ok":  withinlimit, "actual": rc, "errortype": errortype}


    def me(self):
        return ''
    
    def mfname(self):
        return 'getSum'
    

    def ppjson(self, allfails):
        # if (allfails > 0):
        print ( json.dumps( {"folder": self.folder, "problem": self.me, "fails" : allfails, "tests" : self.fails} ) + ", " )

    def pp(self):
        for key, (n, good, bad) in self.fails.items():
            print(f'{key}: ({n})')

    def pp2(self):
        for key, (n, good, bad) in self.fails.items():
            print(f'\n{key}: ({n})\nGood: {good}\nBad : {bad}')

    def pp3(self):
        for key, (n, good, bad) in self.fails.items():
            print(f'\n{key}: ({n})\nGood: {good}\nBad : {bad}')

    def testit(self, dafile):
        # best overide with trixy things
        print("Parsons:testit")
        return [],[],0

    def loopit(self, dbg):
        self.setLog(dbg)
        fails = 0
        mpath = f'./{self.folder}/{self.me}'

        self.log(1,"loopit enumerate..." + str(list(self.ff)))
        if ( len(self.ff) < 1) :
            # folder typo?
            ff = f'ERROR: no input files found for [{self.me}] folder: {self.ff}'
            print(ff, file=sys.stderr)
            fails += 1
            self.fails.append(
                {"figure" : self.dafile,
                 "bad" : 1,
                 "issues" : [{"msg": "error no input files found in folder " + str(self.ff),
                              "ok": False,
                              "actual": "error",
                              "errortype": "empty folder"}]} )

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
                    self.log(2,f'\ntestit() fail: {nfail} good: {good} bad: {bad} ')
                    # print("nfail: ", nfail)
                    # print("bad: ", bad, file=sys.stderr)
                    if (nfail >0):
                        fails += 1

                    if (len(bad) > 0):
                        self.fails.append( {"figure" : self.dafile,
                                            "bad" : len(bad),
                                            "issues" : bad})
                    # else:
                    #     self.fails.append( {"figure" : self.dafile,
                    #                         "bad" : 0,
                    #                         "issues" : ""})

                except:
                    ff = f'ERROR: error running File: {self.dafile}'
                    ee = {"error" : ff, "exception" :  sys.exc_info() }
                    print(ee, file=sys.stderr)

                    fails += 1
                    self.fails.append( {"figure" : self.dafile,
                                    "bad" : 1,
                                    "issues" : [{"msg": "error running " + self.dafile,
                                                 "ok": False,
                                                 "actual": str(sys.exc_info()),
                                                 "errortype": "runtime error"
                                                 }]} )                    
            except:
                ff = f'ERROR: problem with import  File: {self.dafile}'
                # ee = {"error" : ff, "exception" : str( sys.exc_info()[1] )  }
                # ee = {"error" : ff, "exception" :  sys.exc_info()[1]  }
                ee = {"error" : ff, "exception" :  sys.exc_info() }
                print(ee, file=sys.stderr)

                fails += 1
                self.fails.append( {"figure" : self.dafile,
                                    "bad" : 1,
                                    "issues" : [{"msg": "error importing source code " + self.dafile,
                                                 "ok": False,
                                                 "actual": str(sys.exc_info()),
                                                 "errortype": "import error"
                                                 }]} )
            try:
                del sys.modules[self.dafile]
                log(2, "we migh have just removed module: " + str(self.dafile))
            except:
                # oh well...
                pass

        s = sys.modules
        print(s)
        # print("sys.path b4 remove: ", sys.path)
        # sys.path.remove(mpath)
        # print("sys.path affa remove: ", sys.path)
        # # sys.path.pop()
        return fails


    def go(self, folder, dbg=0):
        self.setLog(dbg)
        self.setUpFolder(folder)
        rc = self.loopit(dbg)
        return self.ppjson(rc)

    def cmdfolder(self):
        n = len(sys.argv)
        folder = ''
        if (n>1):
            folder = sys.argv[1]
        # print("folder: ", folder)
        return folder


# if __name__ == '__main__':
#     p1 = Parsons("BNR", "yo")
#     p1.go()
