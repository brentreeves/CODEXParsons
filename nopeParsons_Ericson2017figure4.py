import unittest
from importlib import import_module
import os
import sys
import glob 
import O

# Ericson2017figure4.txt
# def avgValuesInRange(numList, start, end):
# 	sum = 0
# 	for index in range(start,end-1):
# 		value = numList[index]
# 		sum = sum + value
# 	if (end - start + 1) >= 1:
# 		return sum / (end - start + 1)
# 	return 0

#
# ??
#

class Parsons_Ericson2017figure4(O.Parsons):

    def testit(self):
        # print("Ericson2017figure4:testit: ", self.dafile)
        return self.set_predicates_return([
            ("[1] 0 0 = 0", self.mf([1],0,0), 0),
            ("[1] 0 1 = 0",  self.mf([1],0,1), 0)
        ])


if __name__ == '__main__':
    p1 = Parsons_Ericson2017figure4("Ericson2017figure4", "avgValuesInRange")
    rc = p1.go()
