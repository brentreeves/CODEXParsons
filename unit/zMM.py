    # -------------------------------------------------------------------------------------------------------
    # check every predicate against every file
    #
    #
    def zloopit(self, dbg):
        self.setLog(dbg)
        fails = 0
        mpath = f'{self.folder}/{self.me}'

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



    
