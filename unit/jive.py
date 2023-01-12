Class Parsons:
    def blee:
        x = 1
        
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
                        happy = v2 == expect
                        return self.entry(happy, note, v2, expect, '')
                    except:
                        # print('stringOrFunction: v1 was NOT callable', file=sys.stderr)
                        ff = f'ERROR: Weinmann2021figure1 stringOrFunction 1  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
                        ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
                        self.errLog(ee)
                        return self.entry(False, note, str(sys.exc_info()[1]), expect, 'runtime error')
                    # return {"msg": note, "ok": False, "actual": v2}
                else:
                    if (type(v1) is str):
                        # print("stringOrFunction returning v1", file=sys.stderr)
                        happy = v1 == expect
                        return self.entry(happy, note, str(sys.exc_info()[1]), expect, '')
                    
                    return self.entry(False, note, v1, expect, '')
                
            except:
                ff = f'ERROR: Weinmann2021figure1 stringOrFunction 2  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
                ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
                self.errLog(ee)
                
                return self.entry(False, note, v1, expect, '')
        
