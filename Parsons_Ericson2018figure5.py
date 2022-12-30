import O

# Brent Reeves
# Winter '22
#

# Ericson2018figure5.txt
# def isLevel(elList, start, end):
# 	max = elList[start]
# 	min = max
# 	for index in range(start, end+1):
# 		value = elList[index]
# 		if value > max:
# 			max = value
# 		if value < min:
# 			min = value
# 	return (max-min) <= 10

class Parsons_Ericson2018figure5(O.Parsons):
    
    def testit(self):

        # print("Ericson2018figure5:testit: ", self.dafile)
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


if __name__ == '__main__':
    p1 = Parsons_Ericson2018figure5("Ericson2018figure5", "isLevel")
    rc = p1.go()
