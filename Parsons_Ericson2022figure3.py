import O

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


class Parsons_Ericson2022figure3(O.Parsons):

    def classy(self, jive):
        note, first, last, true_name, true_initials = jive
        # print('\nclassy: ', jive)
        daname = ''
        initials=''

        try:
            p1 = self.m.Person(first, last)

            initials = ''
            try:
                initials = p1.initials()
            except:
                print("ERROR initials()", file=sys.stderr)
                return {"msg": "Error initials() not happy", "ok": False, "actual": str(sys.exc_info()[1]) }

            if (initials != true_initials):
                return {"msg": note, "ok": False, "actual": initials, "expected": true_initials}

            daname = ''
            try:
                daname = str(p1)
            except:
                print("ERROR __str__()", file=sys.stderr)
                return {"msg": "Error __str__ not happy", "ok": False, "actual": str(sys.exc_info()[1]) }

            if (daname != true_name):
                return {"msg": note, "ok": False, "actual": daname, "expected": true_name}

            return {"msg": note, "ok": True, "actual": daname }
            
        except:
            # print("safely caught exception")
            ff = f'ERROR: File: {self.dafile}'
            ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
            print(ee, file=sys.stderr)

        return {"msg": note, "ok": False, "actual": "Could not make a Person", "expected": "class Person:..."}

    
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
        # print("preds: ", self.predicates)

        good = list(filter(lambda x:  x["ok"] == True, self.predicates ))
        bad = list(filter(lambda x:  x["ok"] == False, self.predicates ))

        return len(bad), good, bad


if __name__ == '__main__':
    p1 = Parsons_Ericson2022figure3("Ericson2022figure3", "Person")
    rc = p1.go()
