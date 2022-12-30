import O

# Brent Reeves
# Winter '22
#

class Parsons_Hou2022figure2(O.Parsons):
    
# Hou2022figure2.txt
    # def filter_strings(str_list):
    # 	new_list = []
    # 	for word in str_list:
    # 		if len(word) > 3:
    # 			new_list.append(word)
    # 	return new_list

    def testit(self):
        # print("Hou2022figure2:testit: ", self.dafile)

        return self.set_predicates_return([
            # ( "[] = []", self.mf([]), ['a'] ), # blink test
            ( "[] = []", self.mf([]), [] ),
	    ( "[''] = [] ", self.mf(['']), []),
            ( "['a'] = [] ", self.mf(['a']), []),
            ( "['a', 'b'] = [] ", self.mf(['a', 'b']), []),
            ( "['aaa'] = [] ", self.mf(['aaa']), []),
            ( "['aaaa'] = ['aaaa'] ", self.mf(['aaaa']), ['aaaa']),
            ( "['aaaa', ''] = ['aaaa'] ",  self.mf(['aaaa', '']), ['aaaa']),
            ( "['aaaa', 'b'] = ['aaaa'] ",  self.mf(['aaaa', 'b']), ['aaaa']),
            ( "['aaaa', 'bbbb'] = ['aaaa', 'bbbb'] ", self.mf(['aaaa', 'bbbb']), ['aaaa', 'bbbb']),
            ( "['1','12','123','1234','12345','123456'] = ['1234','12345','123456'] ", self.mf(['1','12','123','1234','12345','123456']), ['1234','12345','123456']),
            ( "['123456','12345','1234','123','12','1'] = ['123456','12345','1234'] ", self.mf(['123456','12345','1234','123','12','1']), ['123456','12345','1234']),
        ])


if __name__ == '__main__':
    p1 = Parsons_Hou2022figure2("Hou2022figure2", "filter_strings")
    rc = p1.go()
    # class Parsons_Hou2022figure2(O.Parsons):
