#!python3
import json
import os
import MM as m
dir(m)
# n = m.Parsons('Ericson2018figure5', 'isLevel')
n = m.Parsons()
n.setLog(0)
# print ( dir(n) )
# n.go('../data/V', 0)
folder = '../data/V/V1'
problem = 'Ericson2017figure1'
afile   = 'Ericson2017figure1_1'
fname = f'{folder}/{problem}/{afile}'
print ( os.path.exists(fname+".py") )
print (os.path.basename(fname))
print (os.path.abspath(fname))
# False
# Ericson2017figure1_1
# /Users/bnr01a/Documents/data/projects_current/CODEXParsons/data/V/V1/Ericson2017figure1/Ericson2017figure1_1

print ( json.dumps (n.test1(folder, problem, afile) ))
