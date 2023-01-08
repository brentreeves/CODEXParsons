import sys
import M

# Brent Reeves
# Winter '22
#

# Ericson2022figure3.txt
# class Person:
#         def __init__(self, first, last):
#             self.first = first
#             self.last = last
#
#         def __str__(self):
#             return (self.first + " " + self.last)
#    
#         def initials(self):
# 	      return(self.first[0] + self.last[0])


class Parsons_Ericson2022figure3(M.Parsons):
    def __init__(self):
        super().__init__("Ericson2022figure3", "Person")

    def classy(self, jive):
        note, first, last, true_name, true_initials = jive
        # print('\nclassy: ', jive)
        daname = ''
        initials=''
        
        try:
            p1 = self.m.Person(first, last)
            errortype = ''
            
            initials = ''
            try:
                initials = p1.initials()
            except:
                self.errLog("ERROR initials()")
                actual = str(sys.exc_info()[1])
                return self.entry(False,
                                  "Error initials() not happy",
                                  actual,
                                  "initials method",
                                  'runtime error')

            if (initials != true_initials):
                return self.entry(False,
                                  note,
                                  initials,
                                  true_initials,
                                  'output incorrect')

            daname = ''
            try:
                daname = str(p1)
            except:
                print("ERROR __str__()", file=sys.stderr)
                return self.entry(False,
                                  "Error __str__ not happy",
                                  str(sys.exc_info()[1]),
                                  "__str__ should be defined"
                                  'runtime error')

            if (daname != true_name):
                return self.entry(False,
                                  note,
                                  daname,
                                  true_name,
                                  'output incorrect')
            
            return self.entry(True, note, daname, '', '')
        except:
            # print("safely caught exception")
            ff = f'ERROR: File: {self.dafile}'
            ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
            self.errLog(ee)

        return self.entry(False,
                          note,
                          "Could not make a Person",
                          "class Person:...",
                          'runtime error')

    
    def testit(self):
        # print("Ericson2022figure3:testit: ", self.dafile)

        args = [
            # ("a b = 'ab' 'a b'", 'a','b','a b', 'zz'), # blink test
            ("a b = 'ab' 'a b'", 'a','b','a b', 'ab'),
            ("aa bb = 'ab'",'aa','bb','aa bb', 'ab'),
            ("aaa bbb = ab", 'aaa','bbb','aaa bbb', 'ab'),
            ("' spacea',' spaceb' = [  ] ", ' spacea',' spaceb',' spacea  spaceb', '  '),
            ("' spacesa ',' spacesb ' = ...", ' spacesa ',' spacesb ',' spacesa   spacesb ', '  '),
            ("'a z','b z' = ab", 'a z','b z','a z b z', 'ab'),
        ]
        self.predicates = list(map ( self.classy, args ))

        good = list(filter(lambda x:  x["ok"] == True, self.predicates ))
        bad = list(filter(lambda x:  x["ok"] == False, self.predicates ))

        return len(bad), good, bad


if __name__ == '__main__':
    p = Parsons_Ericson2022figure3()
    print( p.pp(sys.argv[1], int(sys.argv[2])) )

